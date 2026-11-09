from ceaser_cipher import ceasercipher
class ceasercracker:

    def __init__(self,common="etaoinshrdlu"):
        self.common = common

    def brute_force_crack(self,secrets):
        result = []
        for key in range(26):
            cipher = ceasercipher(key)
            decrypted = cipher.decrypt(secrets)
            result.append((key, decrypted))
        return result

    def score(self, text):
        counter = 0
        for ch in text.lower():
            if ch in self.common:
                counter += 1
        return counter

    def crack(self, text):
        results = self.brute_force_crack(text)
        best_score = -1
        best_result = None
        for key, text in results:
            s = self.score(text)
            if s > best_score:
                best_score = s
                best_result = (key, text)
        return best_result



if __name__ == "__main__":
    cipher = ceasercipher(17)
    secret = cipher.encrypt("The meeting is at midnight near the old bridge")
    cracker = ceasercracker()
    print(cracker.crack(secret))
    # print("Intercepted:", secret)
    # for key, text in brute_force_crack(secret):
    #     print(f"Key: {key}, Text: {text}")
