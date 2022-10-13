import nacl.pwhash
import mongomock


def encrypt_data(string):
    string_b = bytes(string, encoding='utf-8')
    e_string = nacl.pwhash.scrypt.str(string_b)
    return e_string


def compare_e_data(string, h_string):
    string_b = bytes(string, encoding='utf-8')
    res_u = nacl.pwhash.verify(h_string, string_b)
    return res_u
