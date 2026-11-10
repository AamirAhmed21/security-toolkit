from ceaser_cipher import ceasercipher
from ceaser_cracker import ceasercracker
from vigenere_cipher import vigenerecipher
def main():
    while True:
        print("\n1. Caesar encrypt")
        print("2. Caesar decrypt")
        print("3. Crack Caesar (no key needed)")
        print("4. Vigenère encrypt")
        print("5. Vigenère decrypt")
        print("6. Quit")
        try:
            choice = int(input("Choose a number "))
        except ValueError:
            print("Enter a valid Number 1, 2, or 3")
            continue
        if choice == 1:
            message = input("enter a message:")
            key = int(input('enter a key:'))
            cipher = ceasercipher(key)
            print("The encrypted message is ", cipher.encrypt(message))
        elif choice == 2:
            message = input("enter a message: ")
            key = int(input('enter a key:'))
            cipher = ceasercipher(key)
            print("The decrypted message is ", cipher.decrypt(message))
        elif choice == 3:
            message = input("Enter the secret message: ")
            cracker = ceasercracker()
            key, text = cracker.crack(message)
            print(f"Likely key: {key}")
            print(f"Decrypted message: {text}")
        elif choice == 4:
            message = input("Enter a message: ")
            key = input("Enter a key word: ")
            cipher = vigenerecipher(key)
            print("The encrypted message is", cipher.encrypt(message))
        elif choice == 5:
            message = input("Enter a message: ")
            key = input("Enter a key word: ")
            cipher = vigenerecipher(key)
            print("The decrypted message is", cipher.decrypt(message))
        elif choice == 6:
            print("Goodbay!")
            break
        else:
            print("Invalid option, please choose 1 to 6 option.")


if __name__ == "__main__":
    main()
