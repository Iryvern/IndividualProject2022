from encryption import *
from authentification import *


class TestEncryption:
    def test_encrypt(self):
        var = "Test"
        e_var = encrypt_data(var)
        result = compare_e_data(var, e_var)
        assert result == True


class TestAuthentification:
    def test_register(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        email = "test@gmail.com"
        result = register(username, password, email, collection)
        assert result == True
