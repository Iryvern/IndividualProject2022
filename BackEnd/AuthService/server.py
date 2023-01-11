from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from authentification import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from waitress import serve
from database import *
import os

white = ["*"]

app = Flask(__name__)
# Whitelist
CORS(app, resources={r"/*": {"origins": white, "send_wildcard": "False"}})
api = Api(app)
#app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"
jwt = JWTManager(app)


@app.route("/test", methods=["GET"])
def test():
    return "Test"


class Login_Auth(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json .get("password")
        response = login(username, password, collection)
        if response == True:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return response


class Register_Auth(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        email = request.json.get("email")
        response = register(username, password, email, collection)
        return response


class ChangeUsername_Auth(Resource):
    @jwt_required()
    def post(self):
        n_username = request.json.get("username")
        o_username = request.json.get("o_username")
        response = change_username(o_username, n_username, collection)
        return response


class ChangeEmail_Auth(Resource):
    @jwt_required()
    def post(self):
        username = request.json.get("username")
        email = request.json.get("email")
        response = change_email(username, email, collection)
        return response


class ChangePassword_Auth(Resource):
    @jwt_required()
    def post(self):
        username = request.json.get("username")
        o_password = request.json.get("opassword")
        n_password = request.json.get("password")
        response = change_password(
            username, o_password, n_password, collection)
        return response


api.add_resource(Login_Auth, "/login")
api.add_resource(Register_Auth, "/register")
api.add_resource(ChangeUsername_Auth, "/change/username")
api.add_resource(ChangeEmail_Auth, "/change/email")
api.add_resource(ChangePassword_Auth, "/change/password")

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True, port=8080)
