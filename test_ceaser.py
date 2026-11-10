from ceaser_cipher import ceasercipher
from ceaser_cracker import ceasercracker
from vigenere_cipher import vigenerecipher
import pytest

MESSAGE = "The meeting is at midnight near the old bridge"
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
@pytest.mark.parametrize("key", [1, 5, 13, 17, 25])
def test_cracker(key):
    secret =ceasercipher(key).encrypt(MESSAGE)
    cracker = ceasercracker()
    assert cracker.crack(secret) == (key, MESSAGE)
def test_score():
    cracker = ceasercracker()
    assert cracker.score("The cat") == 5
    assert cracker.score("Vjg ecv") == 1
@pytest.mark.parametrize("text, key,expected",[
    ("HELLO", "KEY", "RIJVS"),
    ("hello world", "hello", "oiwwc dscwr"),
    ("Hello, World!", "hello", "Oiwwc, Dscwr!"),
])
def test_vigenere_cipher(text, key, expected):
    cipher = vigenerecipher(key)
    assert cipher.encrypt(text) == expected
    assert cipher.decrypt(expected) == text
