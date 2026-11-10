class vigenerecipher:
    def __init__(self, key) -> None:
        self.key = key
        self.shift = []
        for letter in self.key.upper():
            self.shift.append(ord(letter) - ord('A'))

    def encrypt(self,text):
        encrypted = ""
        key_index = 0
        for i in range(len(text)):
            if text[i].isupper():
                if text[i].isalpha():
                    position = (ord(text[i]) - ord('A') + self.shift[key_index % len(self.shift)]) % 26
                    encrypted += chr(position + ord('A'))
                    key_index += 1
                else:
                    encrypted += text[i]
            else:
                if text[i].isalpha():
                    position = (ord(text[i]) - ord('a') + self.shift[key_index % len(self.shift)]) % 26
                    encrypted += chr(position + ord('a'))
                    key_index += 1
                else:
                    encrypted += text[i]
        return encrypted
    def decrypt(self,text):
        decrypted = ""
        key_index = 0
        for i in range(len(text)):
            if text[i].isupper():
                if text[i].isalpha():
                    position = (ord(text[i]) - ord('A') - self.shift[key_index % len(self.shift)]) % 26
                    decrypted += chr(position + ord('A'))
                    key_index += 1
                else:
                    decrypted += text[i]
            else:
                if text[i].isalpha():
                    position = (ord(text[i]) - ord('a') - self.shift[key_index % len(self.shift)]) % 26
                    decrypted += chr(position + ord('a'))
                    key_index += 1
                else:
                    decrypted += text[i]
        return decrypted
if __name__ == "__main__":
    vigenere = vigenerecipher('hello')
    print(vigenere.shift)
    secret = vigenere.encrypt("Hello world")
    print(secret)
    print(vigenere.decrypt(secret))
