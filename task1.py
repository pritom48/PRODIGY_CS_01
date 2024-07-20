def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # For other characters, don't change
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        print("Encrypted message: ", encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted message: ", decrypt(text, shift))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
