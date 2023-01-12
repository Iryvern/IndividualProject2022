from multiprocessing import current_process
import uuid
from datetime import datetime


def get_all_communities(db):
    result = list(db.find()).limit(100)
    if result is not None:
        return result
    else:
        return False


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


def delete_community(community, db):
    result = db.find_one({"community": community})
    if result is not None:
        db.delete_one({"community": community})
        return True
    else:
        return False


def join_community(username, community, db):
    result = db.find_one({"community": community})
    if result is not None:
        if username not in result["bans"]:
            current_members = result["members"]
            if username in current_members:
                print("user is already a member")
                return False
            else:
                new_memebers = current_members+[username]
                db.update_one({"community": community}, {
                    "$set": {"members": new_memebers}})
                return new_memebers
        else:
            print("user is banned")
            return False
    else:
        print("community doesn't exist")
        return False


# Make that the creator can't leave the community or if all people are gone, delete the community
def leave_community(username, community, db):
    result = db.find_one({"community": community})
    if result is not None:
        current_members = result["members"]
        if username in current_members:
            current_members.remove(username)
            db.update_one({"community": community}, {
                "$set": {"members": current_members}})
            return True
        else:
            return False
    else:
        return False


def make_post_in_community(username, post_title, content, community, db):
    unique_id = str(uuid.uuid4())
    new_post = {"_id": unique_id, "creator": username, "content": content, "title": post_title, "likes": 0, "liked_by": [],
                "n_comments": 0, "comments": [], "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    db.update_one({"community": community}, {
        "$push": {"posts": new_post}})
    return True


def show_community_with_posts(community, db):
    result = db.find_one({"community": community})
    if result is not None:
        return result
    else:
        return False


def delete_post(post_id, db):
    result = db.find_one({"posts._id": post_id})
    if result is not None:
        db.delete_one({"posts._id": post_id})
        return True
    else:
        return False

# Rules must be a list of strings


def set_community_rules(username, community, rules, db):
    result = db.find_one({"community": community})
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
    result = db.find_one({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            current_members = result["members"]
            if target in current_members:
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
    else:
        return False


def like_post(post_id, community, username, db):
    result = db.find_one({"community": community})
    if result is not None:
        posts = result["posts"]
        for index in range(len(posts)):
            post = posts[index]
            if post["_id"] == post_id:
                liked_by = posts[index]["liked_by"]
                if username in liked_by:
                    posts[index]["likes"] -= 1
                    posts[index]["liked_by"].remove(username)
                else:
                    posts[index]["likes"] += 1
                    posts[index]["liked_by"] += [username]
                break
            else:
                return False
        db.update_one({"community": community}, {
            "$set": {"posts": posts}})
        return True
    else:
        return False


def get_post(post_id, db):
    result = db.find_one({"posts._id": post_id})
    if result is not None:
        posts = result["posts"]
        for index in range(len(posts)):
            post = posts[index]
            if post["_id"] == post_id:
                return post
    else:
        return False


def comment_on_post(post_id, community, username, content, db):
    result = db.find_one({"community": community})
    if result is not None:
        posts = result["posts"]
        for index in range(len(posts)):
            post = posts[index]
            if post["_id"] == post_id:
                unique_id = str(uuid.uuid4())
                comment = {"_id": unique_id, "username": username, "content": content,
                           "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                posts[index]["comments"] += [comment]
            else:
                return False
        db.update_one({"community": community}, {
            "$set": {"posts": posts}})
        return unique_id
    else:
        return False


def show_community_memebrs(community, db):
    result = db.find_one({"community": community})
    if result is not None:
        return result["members"]
    else:
        return False


def delete_comment(username, community, post_id, comment_id, db):
    result = db.find_one({"community": community})
    if result is not None:
        mods = result["mods"]
        if username in mods:
            posts = result["posts"]
            for index in range(len(posts)):
                post = posts[index]
                if post["_id"] == post_id:
                    comments = posts[index]["comments"]
                    for index in range(len(comments)):
                        comment = comments[index]
                        if comment["_id"] == comment_id:
                            del comments[index]
                            break
                else:
                    return False
            db.update_one({"community": community}, {
                "$set": {"posts": posts}})
            return True
        else:
            return False
    else:
        return False


def upgrade_to_mod(username, community, db):
    result = db.find_one({"community": community})
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
    result = db.find_one({"community": community})
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
