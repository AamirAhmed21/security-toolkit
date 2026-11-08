from unittest.main import main


class ceasercipher:
    def __init__(self, key) -> None:
        self.key = key % 26
        self.encrypt_map = {}
        self.decrypt_map = {}
        # for upper case letter handle it key - original letter and value is shifted letter
        for i in range(26):
            original = chr(65 + i)
            shifted = chr(65 + (i+self.key)%26)
            self.encrypt_map[original] = shifted
            self.decrypt_map[shifted] = original
         # for lower case letter handle it key - original letter and value is shifted letter
        for i in range(26):
            original = chr(97 + i)
            shifted = chr(97 + (i+self.key)%26)
            self.encrypt_map[original] = shifted
            self.decrypt_map[shifted] = original

    def encrypt(self, text):
        result = ""
        for ch in text:
           result += self.encrypt_map.get(ch,ch)
        return result
    def decrypt(self,text):
        result = ""
        for ch in text:
           result += self.decrypt_map.get(ch,ch)
        return result

# cipher = ceasercipher(29)
# encrp = cipher.encrypt("Hello, World! 123")
# print(encrp)
# print(cipher.decrypt(encrp))
