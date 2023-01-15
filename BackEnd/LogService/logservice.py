import uuid
from database import *


def save_login_fail(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "Too Many Login Attempts"}
    collection.insert_one(json_data)
    return True


def save_ban(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "User Has Been Banned"}
    collection.insert_one(json_data)
    return True


def save_save_unusual_login_location(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "User Has Logged In From An Unusual Location"}
    collection.insert_one(json_data)
    return True


def save_high_user_activity():
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "warning": "Spike in user activity, may need more resources"}
    collection.insert_one(json_data)
    return True


def save_syste_down():
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "warning": "One or more nodes have turned off"}
    collection.insert_one(json_data)
    return True


def save_potential_bot(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "User may be a bot"}
    collection.insert_one(json_data)
    return True


def save_admin_login(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "High Level Account Has Logged In"}
    collection.insert_one(json_data)
    return True
