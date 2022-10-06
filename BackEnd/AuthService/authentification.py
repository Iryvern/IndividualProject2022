from database import *
from encryption import *
import uuid


def register(username, password, email):
    result = collection.find_one({"username": username})
    if result == None:
        unique_id = str(uuid.uuid4())
        e_password = encrypt_data(password)
        json_data = {"_id": unique_id,
                     "username": username, "password": e_password, "email": email}
        add_data(json_data)
        return True
    else:
        return False


def login(username, password):
    result = collection.find_one({"username": username})
    if result != None:
        try:
            response = compare_e_data(password, result["password"])
            if response == True:
                return True
            else:
                return False

        except:
            return False
    else:
        return False


def change_username(o_username, n_username):
    result = collection.find_one({"username": o_username})
    if result != None:
        collection.update_one({"username": o_username}, {
            "$set": {"username": n_username}})
    else:
        return False


def change_email(username, email):
    result = collection.find_one({"username": username})
    print(result)
    print(username)
    if result != None:
        collection.update_one({"username": username}, {
            "$set": {"email": email}})
    else:
        return False


def change_password(username, o_password, n_password):
    result = collection.find_one({"username": username})
    if result != None:
        response = compare_e_data(o_password, result["password"])
        if response == True:
            e_password = encrypt_data(n_password)
            collection.update_one({"username": username}, {
                "$set": {"password": e_password}})
    else:
        return False
