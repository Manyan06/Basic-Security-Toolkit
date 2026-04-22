from PIL import Image
import numpy as np
import random

# ---------------------------
# Encryption
# ---------------------------
def encrypt_image(input_path, output_path, key, seed=42):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    # Step 1: Pixel value transformation
    encrypted_pixels = (pixels.astype(np.int16) + key) % 256

    # Step 2: Shuffle pixels (optional but stronger)
    h, w, c = encrypted_pixels.shape
    flat_pixels = encrypted_pixels.reshape(-1, 3)

    random.seed(seed)
    indices = list(range(len(flat_pixels)))
    random.shuffle(indices)

    shuffled_pixels = flat_pixels[indices]
    shuffled_pixels = shuffled_pixels.reshape(h, w, 3)

    encrypted_img = Image.fromarray(np.uint8(shuffled_pixels))
    encrypted_img.save(output_path)

    print("Encryption complete:", output_path)


# ---------------------------
# Decryption
# ---------------------------
def decrypt_image(input_path, output_path, key, seed=42):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    h, w, c = pixels.shape
    flat_pixels = pixels.reshape(-1, 3)

    # Reverse shuffle
    random.seed(seed)
    indices = list(range(len(flat_pixels)))
    random.shuffle(indices)

    unshuffled = np.zeros_like(flat_pixels)
    for i, j in enumerate(indices):
        unshuffled[j] = flat_pixels[i]

    unshuffled = unshuffled.reshape(h, w, 3)

    # Reverse pixel transformation
    decrypted_pixels = (unshuffled.astype(np.int16) - key) % 2561

    decrypted_img = Image.fromarray(np.uint8(decrypted_pixels))
    decrypted_img.save(output_path)

    print("Decryption complete:", output_path)


# ---------------------------
# Main Menu
# ---------------------------
if __name__ == "__main__":
    print("=== Image Encryption Tool ===")
    
    choice = input("1. Encrypt\n2. Decrypt\nChoose: ")
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter key (0-255): "))

    if choice == '1':
        encrypt_image(input_path, output_path, key)

    elif choice == '2':
        decrypt_image(input_path, output_path, key)

    else:
        print("Invalid choice")

# Output:

# #Encryption
# === Image Encryption Tool ===
# 1. Encrypt
# 2. Decrypt
# Choose: 1
# Enter input image path: C:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot 2026-04-18 234820.png  
# Enter output image path: C:\Users\hp\Downloads\removed_bg.png  
# Enter key (0-255): 200
# Encryption complete: C:\Users\hp\Downloads\removed_bg.png


# #Decryption
# === Image Encryption Tool ===
# 1. Encrypt
# 2. Decrypt
# Choose: 2
# Enter input image path: C:\Users\hp\Downloads\removed_bg.png  
# Enter output image path: C:\Users\hp\Downloads\Eid.png  
# Enter key (0-255): 200
# Decryption complete: C:\Users\hp\Downloads\Eid.png