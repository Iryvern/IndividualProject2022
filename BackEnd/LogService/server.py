from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from waitress import serve
from logservice import *

white = ["*"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": white, "send_wildcard": "False"}})
api = Api(app)
# Hide this in an environemnt in github.
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"
jwt = JWTManager(app)


class LoginFail(Resource):
    def post(self):
        username = request.json.get("username")
        response = save_fail(username)
        return response


api.add_resource(LoginFail, "/loginfail")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5002)
