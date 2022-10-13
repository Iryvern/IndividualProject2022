from encryption import *
from authentification import *
import mongomock


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

    def test_register2(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        email = "test@gmail.com"
        register(username, password, email, collection)
        result = register(username, password, email, collection)
        assert result == False

    def test_login(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        result = login(username, password, collection)
        assert result == False

    def test_login2(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        email = "test@gmail.com"
        register(username, password, email, collection)
        result = login(username, password, collection)
        assert result == True

    def test_change_username(self):
        collection = mongomock.MongoClient().db.collection
        o_username = "Test"
        n_username = "Test_P"
        result = change_username(o_username, n_username, collection)
        assert result == False

    def test_change_username2(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        n_username = "Test_2"
        email = "test@gmail.com"
        result = register(username, password, email, collection)
        result = change_username(username, n_username, collection)
        assert result == True

    def test_change_email(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        email = "Test@gmail.com"
        result = change_email(username, email, collection)
        assert result == False

    def test_change_email2(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        email = "Test@gmail.com"
        password = "Test_P"
        new_email = "test@gmail.com"
        register(username, password, email, collection)
        result = change_email(username, new_email, collection)
        assert result == True

    def test_change_password(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        password = "Test_P"
        n_password = "test@gmail.com"
        result = change_password(username, password, n_password, collection)
        assert result == False

    def test_change_password2(self):
        collection = mongomock.MongoClient().db.collection
        username = "Test"
        email = "Test@gmail.com"
        password = "Test_P"
        n_password = "test@gmail.com"
        register(username, password, email, collection)
        result = change_password(username, password, n_password, collection)
        assert result == True
