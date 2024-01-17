#!/usr/bin/env python3
# Script: Ops 401 
# Class 7 challenge 
# Authur: Will B. with the help of ChatGPT
# Date: 1/16/2024
# Resources Google, Bard, ChatGPT, https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python, https://pypi.org/project/cryptography/


# Create a file encryption script part 2 of 3
# Install cyptography with the command "pip install cryptography"

# Import necessary modules from the cryptography library
from cryptography.fernet import Fernet
import os

# Function to generate a key for encryption and decryption
def generate_key():
    """
    Generate a key for encryption and decryption.
    """
    return Fernet.generate_key()

# Function to save the encryption/decryption key to a file
def save_key(key, key_file='secret.key'):
    """
    Save the encryption/decryption key to a file.
    """
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

# Function to load the encryption/decryption key from a file
def load_key(key_file='secret.key'):
    """
    Load the encryption/decryption key from a file.
    """
    return open(key_file, 'rb').read()

# Function to encrypt a target file or folder and replace it with the encrypted version
def encrypt_file_or_folder(path, key):
    """
    Encrypt a target file or folder and replace it with the encrypted version.
    """
    fernet = Fernet(key)

    if os.path.isdir(path):
        # If it's a directory, encrypt its contents recursively
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)
        print(f"Folder '{path}' and its contents encrypted successfully.")
    else:
        encrypt_file(path, key)
        print(f"File '{path}' encrypted successfully.")

# Function to decrypt a target file or folder and replace it with the decrypted version
def decrypt_file_or_folder(path, key):
    """
    Decrypt a target file or folder and replace it with the decrypted version.
    """
    fernet = Fernet(key)

    if os.path.isdir(path):
        # If it's a directory, decrypt its contents recursively
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
        print(f"Folder '{path}' and its contents decrypted successfully.")
    else:
        decrypt_file(path, key)
        print(f"File '{path}' decrypted successfully.")

# Function to encrypt a target file and replace it with the encrypted version
def encrypt_file(file_path, key):
    """
    Encrypt a target file and replace it with the encrypted version.
    """
    fernet = Fernet(key)

    # Check if the file doesn't exist
    if not os.path.exists(file_path):
        # Prompt the user to create the file
        create_file = input(f"The file '{file_path}' doesn't exist. Do you want to create it? (yes/no): ")
        
        # Check if the user's response is affirmative
        if create_file.lower() in ['yes', 'y']:
            # Create an empty file
            open(file_path, 'w').close()
            print(f"File '{file_path}' created.")
        else:
            print("Encryption aborted.")
            return

    # Read the contents of the target file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(data)

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' encrypted successfully.")

# Function to decrypt a target file and replace it with the decrypted version
def decrypt_file(file_path, key):
    """
    Decrypt a target file and replace it with the decrypted version.
    """
    fernet = Fernet(key)

    # Check if the file doesn't exist
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' doesn't exist.")
        return

    # Read the contents of the encrypted file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"File '{file_path}' decrypted successfully.")

# Function to encrypt a cleartext string and print the ciphertext
def encrypt_string(cleartext, key):
    """
    Encrypt a cleartext string and print the ciphertext.
    """
    fernet = Fernet(key)

    # Encrypt the cleartext string
    ciphertext = fernet.encrypt(cleartext.encode())

    # Print the ciphertext
    print("Ciphertext:", ciphertext.decode())

# Function to decrypt a ciphertext string and print the cleartext
def decrypt_string(ciphertext, key):
    """
    Decrypt a ciphertext string and print the cleartext.
    """
    fernet = Fernet(key)

    # Decrypt the ciphertext string
    cleartext = fernet.decrypt(ciphertext.encode())

    # Print the cleartext
    print("Cleartext:", cleartext.decode())

# Main function
def main():
    # Prompt the user to select a mode
    mode = int(input("Select mode:\n1. Encrypt a file or folder\n2. Decrypt a file or folder\n3. Encrypt a message\n4. Decrypt a message\nEnter mode (1, 2, 3, or 4): "))

    # Generate or load the key
    if not os.path.exists('secret.key'):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    if mode == 1 or mode == 2:
        # Prompt the user to provide a filepath to a target file or folder
        file_or_folder_path = input("Enter the filepath to the target file or folder: ")
        if mode == 1:
            encrypt_file_or_folder(file_or_folder_path, key)
        elif mode == 2:
            decrypt_file_or_folder(file_or_folder_path, key)
    elif mode == 3 or mode == 4:
        # Prompt the user to provide a cleartext string
        cleartext = input("Enter the cleartext string: ")
        if mode == 3:
            encrypt_string(cleartext, key)
        elif mode == 4:
            decrypt_string(cleartext, key)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()