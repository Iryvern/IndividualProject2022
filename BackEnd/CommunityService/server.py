from operator import truediv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from database import *


app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})
api = Api(app)
app.config["JWT_SECRET_KEY"] = "ZOl9P^8Ag9K6O2JCmjc&"  # Hide this!
jwt = JWTManager(app)


class Test_Community(Resource):
    def post(self):
        result = collection.find_one({"username": "test"})
        if result != None:
            return True
        else:
            return False


api.add_resource(Test_Community, "/test")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
