#!/usr/bin/env python3
# Script: Ops 401 
# Class 17 challenge
# Authur: Will B. with the help of ChatGPT
# Date: 1/30/2024
# Resources Google, Bard, ChatGPT

# Automated Brute Force Wordlist Attack Tool Part 2 of 3
    # Create 2 Modes Offensive and defensive
import time
import paramiko  # Import the Paramiko library for SSH
import os  # Import the os library for system information

def get_host():
    # Prompt the user for an SSH client to connect to or use the default
    host = input('Enter an SSH client to connect to or press Enter for default "192.168.50.30": ') or "192.168.50.30"
    return host

def get_user():
    # Prompt the user for a username or use the default
    user = input('Enter user name or press Enter for default:"will" ') or "will"
    return user

def get_password():
    # Prompt the user for a password or use the default
    password = input('Enter password or press Enter for default: ') or "password1234"
    return password

def ssh_client():
    # Set the SSH port
    port = 22

    # Create an SSH client instance
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server using user-provided or default values
        ssh.connect(get_host(), port, get_user(), get_password())
        print("Successfully connected via SSH.")
        
        # Execute commands on the remote system
        execute_remote_commands(ssh)

        # Dump user credential hashes
        dump_hashes(ssh)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

def execute_remote_commands(ssh):
    # List of commands to execute on the remote system
    commands = ["whoami", "pwd", "uptime"]

    # Iterate through commands and print output
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        time.sleep(3)
        output = stdout.read()
        print("-" * 50)
        print(f"Output of command '{command}':")
        print(output.decode())

def dump_hashes(ssh):
    # Dump user credential hashes using the passwd file
    passwd_file = "/etc/passwd"
    command = f"sudo cat {passwd_file}"

    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(3)
    output = stdout.read()

    print("-" * 50)
    print(f"User Credential Hashes (from {passwd_file}):")
    print(output.decode())

def print_system_information():
    # Use various Linux commands to print system information
    print("-" * 50)
    os.system("uname -a")
    os.system("lsb_release -a")
    os.system("hostnamectl")
    os.system("inxi -F")
    print("-" * 50)

def main():
    # Prompt the user to select a mode
    mode = int(input("Select mode:\n1. Authenticate to SSH Server\nEnter mode (1): "))

    if mode == 1:
        # Mode 1: Authenticate to SSH Server
        ssh_client()
        print_system_information()
    else:
        print("Invalid mode. Exiting.")

if __name__ == "__main__":
    main()