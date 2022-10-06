from encryption import *


class TestEncryption:
    def test_encrypt(self):
        var = "Test"
        e_var = encrypt_data(var)
        result = compare_e_data(var, e_var)
        assert result == True
