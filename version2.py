import stepic
from PIL import Image
from cryptography.fernet import Fernet
from colorama import Fore
import os

# Define a global variable to store the encryption key
encryption_key = None

def main():
    print(Fore.WHITE)
    opt = input('''Select option
1. Encode
2. Decode
3. Exit
Option: ''')
    handle_options(opt)

def handle_options(opt):
    if opt == '1':
        print(Fore.GREEN + "*====================ENCODER=================*" + Fore.WHITE)
        text = input("Data: ")
        file = input("Photo: ")
        output_file = "output.png"
        encode(text, file, output_file)
        print(Fore.GREEN + "*====================SUCCESSFUL=================*" + Fore.WHITE)
        return True
    elif opt == '2':
        print(Fore.GREEN + "*====================DECODER=================*" + Fore.WHITE)
        key = input("Key: ")
        file = input("Photo: ")
        decoded_text = decode(file, key)
        print('Data: ' + decoded_text)
        print(Fore.GREEN + "*====================SUCCESSFUL=================*" + Fore.WHITE)
    elif opt == '3':
        exit()
    else:
        exit("Please select a valid option")

def generate_fernet_key():
    global encryption_key
    if encryption_key is None:
        encryption_key = Fernet.generate_key()
    print(encryption_key)
    return encryption_key

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def encode(text, image_path, output_image_path):
    key = generate_fernet_key()
    text_encrypted = encrypt_text(text, key)

    img = Image.open(image_path)
    img_encoded = stepic.encode(img, text_encrypted)
    img_encoded.save(output_image_path)

def decrypt_text(text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(text).decode()
    return decrypted_text

def decode(image_path, key):
    img = Image.open(image_path)
    decoded = stepic.decode(img)
    text_decrypted = decrypt_text(decoded.encode(), key)
    print(text_decrypted)
    return text_decrypted

if __name__ == "__main__":
    main()
