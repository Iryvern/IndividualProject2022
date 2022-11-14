from operator import truediv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from community import *
from database import *

white = ["localhost:3000"]

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
CORS(app, resources={r"/*": {"origins": white, "send_wildcard": "False"}})
api = Api(app)
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"  # Hide this!
jwt = JWTManager(app)


class Create_Community(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        result = create_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Delete_Community(Resource):
    def post(self):
        community = request.json.get("community")
        result = delete_community(community, collection)
        if result != None:
            return True
        else:
            return False


class Join_Community(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        result = join_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Leave_Community(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        result = leave_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Post_In_Community(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        post_title = request.json.get("post_title")
        result = make_post_in_community(
            username, post_title, community, collection)
        if result != None:
            return True
        else:
            return False


class Get_Community(Resource):
    def post(self):
        community = request.json.get("community")
        result = show_community_with_posts(community, collection)
        if result != None:
            return True
        else:
            return False


class Delete_Post(Resource):
    def post(self):
        post_id = request.json.get("post_id")
        result = delete_post(post_id, collection)
        if result != None:
            return True
        else:
            return False


class Community_Rules(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        rules = request.json.get("rules")
        result = set_community_rules(username, community, rules, collection)
        if result != None:
            return True
        else:
            return False


class Ban_In_Community(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        target = request.json.get("target")
        reason = request.json.get("reason")
        result = ban_in_community(
            username, target, community, reason, collection)
        if result != None:
            return True
        else:
            return False


class Like_Post(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        post_id = request.json.get("post_id")
        result = like_post(post_id, community, username, collection)
        if result != None:
            return True
        else:
            return False


class Comment_Post(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        post_id = request.json.get("post_id")
        content = request.json.get("content")
        result = comment_on_post(
            post_id, community, username, content, collection)
        if result != None:
            return True
        else:
            return False


class Community_Members(Resource):
    def post(self):
        community = request.json.get("community")
        result = show_community_memebrs(community, collection)
        if result != None:
            return True
        else:
            return False


class Delete_Comment(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        post_id = request.json.get("post_id")
        comment_id = request.json.get("comment_id")
        result = delete_comment(username, community,
                                post_id, comment_id, collection)
        if result != None:
            return True
        else:
            return False


class Upgrade_User_To_Mod(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        result = upgrade_to_mod(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Downgrade_To_User(Resource):
    def post(self):
        username = request.json.get("username")
        community = request.json.get("community")
        result = downgrade_to_user(username, community, collection)
        if result != None:
            return True
        else:
            return False


api.add_resource(Create_Community, "/c-create")
api.add_resource(Delete_Community, "/c-delete")
api.add_resource(Join_Community, "/c-join")
api.add_resource(Leave_Community, "/c-leave")
api.add_resource(Post_In_Community, "/c-post")
api.add_resource(Get_Community, "/community")
api.add_resource(Delete_Post, "/p-delete")
api.add_resource(Community_Rules, "/c-rules")
api.add_resource(Ban_In_Community, "/c-ban")
api.add_resource(Like_Post, "/p-like")
api.add_resource(Comment_Post, "/p-comment")
api.add_resource(Community_Members, "/c-members")
api.add_resource(Delete_Comment, "/co-delete")
api.add_resource(Upgrade_User_To_Mod, "/u-upgrade")
api.add_resource(Downgrade_To_User, "/u-dowgrade")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
