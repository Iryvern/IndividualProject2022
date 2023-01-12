from encryption import *
import uuid
# L2


def register(username, password, email, db):
    result = db.find_one({"username": username})
    if result is None:
        unique_id = str(uuid.uuid4())
        e_password = encrypt_data(password)
        e_email = encrypt_data(email)
        json_data = {"_id": unique_id,
                     "username": username, "password": e_password, "email": e_email}
        db.insert_one(json_data)
        return True
    else:
        return False


def login(username, password, db):
    result = db.find_one({"username": username})
    if result is not None:
        try:
            response = compare_e_data(password, result["password"])
            if response is True:
                return True
            else:
                return False

        except ValueError as e:
            return False
    else:
        return False


def change_username(o_username, n_username, db):
    result = db.find_one({"username": o_username})
    if result is not None:
        db.update_one({"username": o_username}, {
            "$set": {"username": n_username}})
        return True
    else:
        return False


def change_email(username, email, db):
    result = db.find_one({"username": username})
    print(result)
    print(username)
    if result is not None:
        db.update_one({"username": username}, {
            "$set": {"email": email}})
        return True
    else:
        return False


def change_password(username, o_password, n_password, db):
    result = db.find_one({"username": username})
    if result is not None:
        response = compare_e_data(o_password, result["password"])
        if response is True:
            e_password = encrypt_data(n_password)
            db.update_one({"username": username}, {
                "$set": {"password": e_password}})
            return True
    else:
        return False
