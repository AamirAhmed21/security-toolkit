from ceaser_cipher import ceasercipher

def brute_force_crack(secrets):
    result = []
    for key in range(26):
        cipher = ceasercipher(key)
        decrypted = cipher.decrypt(secrets)
        result.append((key, decrypted))
    return result


if __name__ == "__main__":
    cipher = ceasercipher(17)
    secret = cipher.encrypt("The meeting is at midnight near the old bridge")
    print("Intercepted:", secret)
    for key, text in brute_force_crack(secret):
        print(f"Key: {key}, Text: {text}")
