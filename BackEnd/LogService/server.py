from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from waitress import serve
import database
from logservice import *
import os

white = ["*"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": white, "send_wildcard": "False"}})
api = Api(app)
app.config["JWT_SECRET_KEY"] = database.key()
jwt = JWTManager(app)


class LoginFail(Resource):
    def post(self):
        username = request.json.get("username")
        response = save_fail(username)
        return response


class Visit(Resource):
    def get(self):
        return "Hello Logging Service"


api.add_resource(Visit, "/")
api.add_resource(LoginFail, "/loginfail")

if __name__ == "__main__":
    serve(app, port=8083)
