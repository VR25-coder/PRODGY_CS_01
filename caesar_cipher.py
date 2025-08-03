def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Encryption/Decryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'E':
        encrypted = encrypt(text, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'D':
        decrypted = decrypt(text, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please select 'E' or 'D'.")


if __name__ == "__main__":
    main()
