from ceaser_cipher import __version__
from ceaser_cipher.cipher import encrypt, decrypt, break_cipher, is_english


def test_version():
    assert __version__ == '0.1.0'

"""
Test cases:
    1. encrypt a string with a given shift
    2. decrypt a previously encrypted string with the same shift
    3. encryption should handle upper and lower case letters
    4. encryption should allow non-alpha characters but ignore them, including white space
    5. decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
"""

def test_cipher_encrypt():
    assert encrypt("abc", 10) == "klm"

def test_cipher_decrypt():
    assert decrypt("klm", 10) == "abc"

def test_cipher_encrypt_upper():
    assert encrypt("ABC", 10) == "klm"

def test_cipher_encrypt_non_alpha():
    assert encrypt("A B C $", 10) == "k l m $"

def test_cipher_break():
    assert break_cipher(encrypt("It was the best of times, it was the worst of times", 28)) == "it was the best of times, it was the worst of times"


