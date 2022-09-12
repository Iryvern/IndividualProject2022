from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from authentification import *

app = Flask(__name__)
api = Api(app)
CORS(app)

login_args = reqparse.RequestParser()
login_args.add_argument(
    "username", type=str, help="Username Required", required=True)
login_args.add_argument(
    "password", type=str, help="Password Required", required=True)


class Login_Authenticate(Resource):
    def get(self):
        args = login_args.parse_args()
        username = args["username"]
        password = args["password"]
        response = login(username, password)
        return response


class Register_Authenticate(Resource):
    def post(self):
        args = login_args.parse_args()
        username = args["username"]
        password = args["password"]
        response = register(username, password)
        return response


api.add_resource(Login_Authenticate, "/login")
api.add_resource(Register_Authenticate, "/register")

if __name__ == "__main__":
    app.run(debug=True)
