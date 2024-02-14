#!/usr/bin/env python3
# Script: Ops 401 
# Class 27 Challenge
# Authur: Will B. with the help of ChatGPT
# Date: 2/13/2024
# Resources Google, Gemini, ChatGPT, 
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/,

# Adding logging functionallity to a previous scrip now having them rotate based on size 



import logging
import os
import paramiko
import time

# Create the "challenge_log" folder if it doesn't exist
log_folder = "challenge_log"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Set up logging
logging.basicConfig(filename=os.path.join(log_folder, 'chall17.log'), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Placeholder function for unzip_zip_file
def unzip_zip_file(zipped_file, password):
    # This is a placeholder. You should replace it with your actual unzip logic.
    logging.info(f"Trying to unzip {zipped_file} with password: {password}")

# Function to get the target SSH host, SSH username, and SSH password
def get_credentials():
    host = input('Enter the target SSH host to connect to (press Enter for default "192.168.50.30"): ') or "192.168.50.30"
    logging.info(f"Target SSH host: {host}")  # Log the entered target SSH host IP
    user = input('Enter the SSH username (press Enter for default "will"): ') or "will"
    logging.info(f"SSH username: {user}")  # Log the entered SSH username
    return host, user, get_password(host, user)

# Function to get the SSH password
def get_password(host, user):
    # Prompt the user for the SSH password
    password = input(f'Enter the SSH password for {user}@{host} (press Enter for default "password"): ') or "passwo1234"
    logging.info(f"Entered SSH password: {password}")  # Log the entered SSH password
    return password

# Function to perform SSH authentication and execute commands
def ssh_client():
    host, user, password = get_credentials()
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port, user, password)
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read()
        print("-" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("pwd")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(3)
        output = stdout.read()
        print(output)
        print("-" * 50)
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        ssh.close()

# Main function
def main():
    mode = input("Select mode:\n1. Offensive; Dictionary Iterator\n2. Defensive; Password Recognized\n3. SSH Authentication\nEnter mode (1, 2, or 3): ")
    if mode not in ['1', '2', '3']:
        logging.error("Invalid mode selection.")  # Log when an invalid mode selection is made
        print("Invalid mode. Exiting.")
        return
    
    mode = int(mode)

    if mode == 1:
        # Offensive mode: Dictionary Iterator
        # ... (your existing offensive mode code)
        pass
    elif mode == 2:
        # Defensive mode: Password Recognized
        # ... (your existing defensive mode code)
        pass
    elif mode == 3:
        # SSH Authentication mode
        ssh_client()

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()