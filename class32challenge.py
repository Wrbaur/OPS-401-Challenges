#!/usr/bin/env python3
# Script: Ops 401 
# Class 32 Challenge
# Authur: Will B. with the help of ChatGPT
# Date: 2/20/2024
# Resources Google, Gemini, ChatGPT,

# Signature based malware detection 2 of 3 
# Find or generate hashes of files using the hashlib library 

import hashlib  # Importing the hashlib module for hashing
import os  # Importing the os module for interacting with the operating system
import logging  # Importing the logging module for logging

# Configuring the logging module
logging.basicConfig(filename='malware_detection.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to hash a file given its filename
def hash_file(filename):
    h = hashlib.sha1()  # Creating a SHA-1 hash object
    with open(filename, 'rb') as file:  # Opening the file in binary mode for reading
        chunk = 0
        while chunk != b'':  # Reading the file in chunks of 1024 bytes
            chunk = file.read(1024)
            h.update(chunk)  # Updating the hash object with each chunk
    return h.hexdigest()  # Returning the hexadecimal digest of the hash

# Function to search for a file in a directory
def search_file(filename, directory):
    found_files = []  # List to store found file paths
    for root, dirs, files in os.walk(directory):  # Walking through the directory recursively
        if filename in files:  # Checking if the filename is in the current directory's files
            found_files.append(os.path.join(root, filename))  # Adding the full path of the found file to the list
    return found_files  # Returning the list of found file paths

# Getting user input for the file name and directory to search in
filename = input("Enter the file name to search for: ")
directory = input("Enter the directory to search in: ")

# Executing system-specific commands to search for the file
if os.name == 'posix':  # If the OS is Linux
    command = f"find {directory} -name {filename}"  # Using the 'find' command to search for the file
    os.system(command)  # Executing the command
elif os.name == 'nt':  # If the OS is Windows
    command = f"dir {directory} /s /b | findstr {filename}"  # Using the 'dir' and 'findstr' commands to search
    os.system(command)  # Executing the command

# Logging information about each found file, including its path and hash
for found_file in search_file(filename, directory):
    file_hash = hash_file(found_file)  # Hashing the found file
    logging.info(f"File found: {found_file}, Hash: {file_hash}")  # Logging the file path and hash