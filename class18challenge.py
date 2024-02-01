#!/usr/bin/env python3
# Script: Ops 401 
# Class 18 challenge
# Authur: Will B. with the help of ChatGPT
# Date: 1/31/2024
# Resources Google, Bard, ChatGPT

# Automated Brute Force Wordlist Attack Tool Part 3 of 3
    # Goal to brute force a PW protected zip document 
# Install zip and unzip command: sudo apt-get install zip unzip -y
# create test file then password protect it
# command is: zip --encrypt "ziped file name" "original file name"

# Import libraries needed
import time
from zipfile import ZipFile  # Install with sudo apt-get install zip unzip -y

# Function to unzip a file with a provided password
def unzip_zip_file(zipped_file, password):
    try:
        with ZipFile(zipped_file, 'r') as zf:
            zf.extractall(pwd=bytes(password, 'utf-8'))
        print(f'The file {zipped_file} has been successfully unzipped!')
        return True
    except Exception as e:
        print(f"Failed to unzip with password '{password}': {e}")
        return False

# Function to perform password breaking using a word list
def pw_break(zipped_file):
    # Open the specified word list file (rockyou.txt)
    with open('rockyou.txt', 'r', errors='ignore') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading/trailing whitespaces and assign the word to a variable
            word = line.strip()
            # Add a delay between words to mimic an iterator
            time.sleep(1)

            # Attempt to unzip the file with the current password
            if unzip_zip_file(zipped_file, word):
                # If successful, break out of the loop
                print(f'Password found: {word}')
                break

# Main function
def main():
    # Prompt the user for the zipped file name
    zipped_file = input("Enter the name of the zipped file: ") or "ru.zip"
    # Call the password breaking function with the specified zipped file
    pw_break(zipped_file)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()