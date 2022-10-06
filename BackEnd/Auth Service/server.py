from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from authentification import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"  # Hide this!
jwt = JWTManager(app)


@app.route("/test", methods=["POST"])
@jwt_required()
def test():
    print("Test")
    return "Test"


class Login_Auth(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        response = login(username, password)
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
        response = register(username, password, email)
        return response


class ChangeUsername_Auth(Resource):
    @jwt_required()
    def post(self):
        n_username = request.json.get("username")
        o_username = request.json.get("o_username")
        response = change_username(o_username, n_username)
        return response


class ChangeEmail_Auth(Resource):
    @jwt_required()
    def post(self):
        username = request.json.get("username")
        email = request.json.get("email")
        response = change_email(username, email)
        return response


class ChangePassword_Auth(Resource):
    @jwt_required()
    def post(self):
        username = request.json.get("username")
        o_password = request.json.get("opassword")
        n_password = request.json.get("password")
        response = change_password(username, o_password, n_password)
        return response


api.add_resource(Login_Auth, "/login")
api.add_resource(Register_Auth, "/register")
api.add_resource(ChangeUsername_Auth, "/change/username")
api.add_resource(ChangeEmail_Auth, "/change/email")
api.add_resource(ChangePassword_Auth, "/change/password")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
