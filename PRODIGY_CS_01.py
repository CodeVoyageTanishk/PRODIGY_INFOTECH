def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text
def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Please enter a valid choice (encrypt/decrypt)")
            continue
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        if choice == 'encrypt':
            encrypted_text = encrypt(text, shift)
            print("Encrypted message:", encrypted_text)
        else:
            decrypted_text = decrypt(text, shift)
            print("Decrypted message:", decrypted_text)
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
