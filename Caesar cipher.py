def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine ASCII offset
            offset = ord('A') if char.isupper() else ord('a')
            
            # Apply shift
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += encrypted_char
        else:
            # Keep non-alphabet characters unchanged
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# User Input
if __name__ == "__main__":
    print("=== Caesar Cipher ===")
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    print("\n1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose option (1/2): ")

    if choice == '1':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted)

    elif choice == '2':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted)

    else:
        print("Invalid choice!")


# Output :
# === Caesar Cipher ===
# Enter your message: Hey
# Enter shift value: 7

# 1. Encrypt
# 2. Decrypt
# Choose option (1/2): 1
# Encrypted Message: Olf