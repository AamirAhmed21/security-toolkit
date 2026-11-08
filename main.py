from ceaser_cipher import ceasercipher

def main():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
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
            print("Goodbay!")
            break
        else:
            print("Invalid option, please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
