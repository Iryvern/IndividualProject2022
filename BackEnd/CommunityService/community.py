from multiprocessing import current_process
import uuid
from datetime import datetime


def create_community(username, community, db):
    result = db.find_one({"community": community})
    if result is None:
        unique_id = str(uuid.uuid4())
        json_data = {"_id": unique_id,
                     "creator": username, "community": community, "members": [username], "mods": [username], "posts": [], "rules": [], "bans": []}
        db.insert_one(json_data)
        return True
    else:
        return False


# Make it so it blocks all users except admins to see the community
def delete_community(community, db):
    result = db.find_one({"community": community})
    if result is None:
        return False
    else:
        return False


def show_community_with_posts(community, db):
    result = db.find_one({"community": community})
    if result is not None:
        return result
    else:
        return False


def join_community(username, community, db):
    result = db.find_one({"community": community})
    if result is not None:
        if username not in result["bans"]:
            current_members = result["members"]
            if username in current_members:
                return False
            else:
                new_memebers = current_members+[username]
                db.update_one({"community": community}, {
                    "$set": {"members": new_memebers}})
                return True
        else:
            return False
    else:
        return False


def leave_community(username, community, db):
    result = db.find_one({"community": community})
    if result is not None:
        current_members = result["members"]
        if username in current_members:
            new_memebers = current_members.remove(username)
            db.update_one({"community": community}, {
                "$set": {"members": new_memebers}})
            return True
        else:
            return False
    else:
        return False


def make_post_in_community(username, post_title, community, db):
    result = db.find_one({"community": community})
    if result is not None:
        current_posts = result["posts"]
        unique_id = str(uuid.uuid4())
        new_post = {"_id": unique_id, "creator": username, "title": post_title, "likes": 0, "liked_by": [],
                    "n_comments": 0, "comments": [], "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        updated_posts = current_posts + [new_post]
        db.update_one({"community": community}, {
            "$set": {"posts": updated_posts}})
        return True
    else:
        return False


def like_post(post_id, username, db):
    result = db.find({"_id": post_id})
    if result is not None:
        liked_by = result["liked_by"]
        if username in liked_by:
            new_likes = result["likes"]-1
            new_liked_by = liked_by.remove(username)
        else:
            new_likes = result["likes"]+1
            new_liked_by = liked_by+[username]
        db.update_one({"_id": post_id}, {
            "$set": [{"likes": new_likes}, {"liked_by": new_liked_by}]})
        return True
    else:
        return False


def comment_on_post(post_id, username, content, db):
    result = db.find({"_id": post_id})
    if result is not None:
        unique_id = str(uuid.uuid4())
        current_comments = result["comments"]
        comment = {"_id": unique_id, "username": username, "content": content,
                   "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        new_comments = current_comments+[comment]
        db.update_one({"_id": post_id}, {
            "$set": {"comments": new_comments}, })
        return True
    else:
        return False


def show_community_memebrs(community, db):
    result = db.find({"community": community})
    if result is not None:
        return result["members"]
    else:
        return False


# Rules must be a list of strings
def set_community_rules(username, community, rules, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            db.update_one({"community": community}, {
                "$set": {"rules": rules}})
            return True
        else:
            return False
    else:
        return False


def ban_in_community(username, target, community, reason, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            current_members = result["members"]
            new_memebers = current_members.remove(target)
            db.update_one({"community": community}, {
                "$set": {"members": new_memebers}})
            current_mods = result["mods"]
            if target in current_mods:
                new_mods = current_mods.remove(target)
                db.update_one({"community": community}, {
                    "$set": {"mods": new_mods}})
            bans = result["bans"]
            ban = {"username": username,
                   "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "reason": reason}
            new_bans = bans+[ban]
            db.update_one({"community": community}, {
                "$set": {"bans": new_bans}})
            return True
        else:
            return False
    else:
        return False


def delete_post(username, community, post_id, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            db.delete_one({"_id": post_id})
            return True
        else:
            return False
    else:
        return False


def delete_comment(username, community, comment_id, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            db.delete_one({"_id": comment_id})
            return True
        else:
            return False
    else:
        return False


def upgrade_to_mod(username, community, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username not in mods:
            new_mods = mods+[username]
            db.update_one({"community": community}, {
                "$set": {"mods": new_mods}})
            return True
        else:
            return False
    else:
        return False


def downgrade_to_user(username, community, db):
    result = db.find({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            new_mods = mods.remove(username)
            db.update_one({"community": community}, {
                "$set": {"mods": new_mods}})
            return True
        else:
            return False
    else:
        return False
