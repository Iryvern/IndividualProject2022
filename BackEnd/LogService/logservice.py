import uuid
from database import *


def save_fail(username):
    unique_id = str(uuid.uuid4())
    json_data = {"_id": unique_id,
                 "username": username, "warning": "Too Many Login Attempts"}
    collection.insert_one(json_data)
    return True
