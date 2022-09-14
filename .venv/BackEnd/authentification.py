from database import *
from encryption import *
import uuid


def register(username, password):
    result = collection.find_one({"username": username})
    if result == None:
        unique_id = str(uuid.uuid4())
        e_password = encrypt_data(password)
        json_data = {"_id": unique_id,
                     "username": username, "password": e_password}
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
