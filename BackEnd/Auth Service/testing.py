import unittest
from encryption import *

# Testing


class TestEncryption(unittest.TestCase):
    def test_encrypt(self):
        var = "Test"
        e_var = encrypt_data(var)
        result = compare_e_data(var, e_var)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
