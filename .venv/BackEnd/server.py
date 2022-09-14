from ast import arguments
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from authentification import *

app = Flask(__name__)
api = Api(app)
CORS(app)

class Login_Authenticate(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        response = login(username, password)
        return response

class Register_Authenticate(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        response = register(username, password)
        return response

api.add_resource(Login_Authenticate, "/login")
api.add_resource(Register_Authenticate, "/register")

if __name__ == "__main__":
    app.run(debug=True)
