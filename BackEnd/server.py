from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from authentification import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
CORS(app)
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"  # Hide this!
jwt = JWTManager(app)


class Login_Authenticate(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        response = login(username, password)
        if response == True:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return response


class Test(Resource):
    @jwt_required()
    def post(self):
        print("Test")
        return "Test"


class Register_Authenticate(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        response = register(username, password)
        return response


api.add_resource(Test, "/test")
api.add_resource(Login_Authenticate, "/login")
api.add_resource(Register_Authenticate, "/register")

if __name__ == "__main__":
    app.run(debug=True)
