# Image Steganography using Steganography Module

This Python program implements image steganography, a technique used to hide secret messages within images. It utilizes the Steganography module along with other libraries for image manipulation and encryption.

## Libraries Used
- Steganography: For encoding and decoding hidden messages within images.
- PIL (Python Imaging Library): For opening, manipulating, and saving many different image file formats.
- Cryptography: For encrypting and decrypting text using the Fernet symmetric encryption algorithm.
- Colorama: For adding colored text output in the console.
- OS: For interacting with the operating system, specifically for handling file operations.

## Flow of the Program

### 1. Main Function
The `main()` function presents a menu to the user, allowing them to choose between encoding, decoding, or exiting the program.

### 2. Handle Options Function
This function (`handle_options(opt)`) processes the user's choice and executes the corresponding functionality.

- **Encode (Option 1):** Prompts the user to enter the data and select an image. It then encodes the data into the image and saves the resulting image as "output.png".
- **Decode (Option 2):** Prompts the user to enter the encryption key and select an image containing hidden data. It then decodes the hidden data and prints it to the console.
- **Exit (Option 3):** Exits the program.

### 3. Encryption Functions
- `generate_fernet_key()`: Generates a Fernet key for symmetric encryption.
- `encrypt_text(text, key)`: Encrypts the given text using the Fernet key.
- `decrypt_text(text, key)`: Decrypts the encrypted text using the Fernet key.

### 4. Image Encoding and Decoding
- `encode(text, image_path, output_image_path)`: Encodes the given text into the specified image using the Steganography module.
- `decode(image_path, key)`: Decodes the hidden text from the specified image using the Steganography module.

## Output
The program provides a user-friendly interface for encoding secret messages into images and decoding hidden messages from images, enabling secure communication through steganography.
