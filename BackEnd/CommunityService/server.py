from operator import truediv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from waitress import serve
from community import *
from database import *
import database
import os


white = ["*"]

app = Flask(__name__)
# Whitelist
CORS(app, resources={r"/*": {"origins": white, "send_wildcard": "False"}})
api = Api(app)
app.config["JWT_SECRET_KEY"] = database.key()
jwt = JWTManager(app)


class Get_Communities(Resource):
    def get(self):
        result = get_all_communities(collection)
        if result != None:
            return result
        else:
            return False


class Create_Community(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        result = create_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Delete_Community(Resource):
    @jwt_required()
    def post(self):
        community = request.args.get("community")
        result = delete_community(community, collection)
        if result != None:
            return True
        else:
            return False


class Join_Community(Resource):
    @jwt_required()
    def get(self):
        username = request.args.get("username")
        community = request.args.get("community")
        result = join_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Leave_Community(Resource):
    @jwt_required()
    def get(self):
        username = request.args.get("username")
        community = request.args.get("community")
        result = leave_community(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Post_In_Community(Resource):
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        post_title = request.args.get("post_title")
        content = request.args.get("content")
        result = make_post_in_community(
            username, post_title, content, community, collection)
        if result != None:
            return True
        else:
            return False


class Get_Post(Resource):
    def get(self):
        post_id = request.args.get("post_id")
        result = get_post(post_id, collection)
        if result != None:
            return result
        else:
            return False


class Get_Community(Resource):
    def get(self):
        community = request.args.get("c")
        print(community)
        result = show_community_with_posts(community, collection)
        if result != None:
            return result
        else:
            return False


class Delete_Post(Resource):
    @jwt_required()
    def post(self):
        post_id = request.args.get("post_id")
        result = delete_post(post_id, collection)
        if result != None:
            return True
        else:
            return False


class Community_Rules(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        rules = request.args.get("rules")
        result = set_community_rules(username, community, rules, collection)
        if result != None:
            return True
        else:
            return False


class Ban_In_Community(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        target = request.args.get("target")
        reason = request.args.get("reason")
        result = ban_in_community(
            username, target, community, reason, collection)
        if result != None:
            return True
        else:
            return False


class Like_Post(Resource):
    def get(self):
        username = request.args.get("username")
        community = request.args.get("community")
        post_id = request.args.get("post_id")
        print(username, community, post_id)
        result = like_post(post_id, community, username, collection)
        if result != None:
            return True
        else:
            return False


class Comment_Post(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        post_id = request.args.get("post_id")
        content = request.args.get("content")
        result = comment_on_post(
            post_id, community, username, content, collection)
        if result != None:
            return True
        else:
            return False


class Community_Members(Resource):
    def post(self):
        community = request.args.get("community")
        result = show_community_memebrs(community, collection)
        if result != None:
            return True
        else:
            return False


class Delete_Comment(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        post_id = request.args.get("post_id")
        comment_id = request.args.get("comment_id")
        result = delete_comment(username, community,
                                post_id, comment_id, collection)
        if result != None:
            return True
        else:
            return False


class Upgrade_User_To_Mod(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        result = upgrade_to_mod(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Downgrade_To_User(Resource):
    @jwt_required()
    def post(self):
        username = request.args.get("username")
        community = request.args.get("community")
        result = downgrade_to_user(username, community, collection)
        if result != None:
            return True
        else:
            return False


class Visit(Resource):
    def get(self):
        return "Hello Community"


class Test(Resource):
    def post(self):
        test(collection)
        return "Hello Community"


api.add_resource(Visit, "/")
api.add_resource(Test, "/test")
api.add_resource(Get_Communities, "/a-communities")
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
api.add_resource(Get_Post, "/p-get")

if __name__ == "__main__":
    serve(app, port=8081)
    #app.run(debug=True, port=8081)
