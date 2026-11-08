from ceaser_cipher import ceasercipher
import pytest

@pytest.mark.parametrize("text,key,expected",[
    ("abc", 3, "def"),
    ("xyz", 3, "abc"),
    ("HELLO", 3, "KHOOR"),
    ("Hello, World!", 3, "Khoor, Zruog!"),
    ("abc", 29, "def"),
    ("abc", 0, "abc")
])
def test_encrypt_decrypt(text,key, expected):
    cipher = ceasercipher(key)
    assert cipher.decrypt(cipher.encrypt(text)) == text
