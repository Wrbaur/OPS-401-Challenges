#!/usr/bin/env python3
# Script: Ops 401 
# Class 36 Challenge
# Authur: Will B. with the help of ChatGPT
# Date: 2/26/2024
# Resources Google, Gemini, ChatGPT


# Create a Banner grabbing/service fingerprinting script
# Install what web with sudo apt install whatweb, next command which whatweb, chmod +x /usr/bin/whatweb
# Install curl, sudo apt install curl, next command which curl, chmod +x /urs/bin/curl


import subprocess
import telnetlib

def get_user_input():
    while True:
        try:
            url_or_ip = input("Enter a URL or IP address: ")
            port = int(input("Enter a port number: "))
            return url_or_ip, port
        except ValueError:
            print("Invalid input. Please enter a valid URL or IP address and a valid port number.")

url_or_ip, port = get_user_input()

# Run netcat to grab the banner
try:
    print(f"Running netcat command for {url_or_ip}:{port}...")
    result = subprocess.run(['nc', '-v', '-n', '-z', '-w', '1', url_or_ip, str(port)], capture_output=True, text=True)
    print("Banner Grabbing Results (Netcat):")
    print(result.stdout)
    print(result.stderr)  # Add this line to print stderr for debugging
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# Run WhatWeb for banner grabbing
whatweb_path = "/usr/bin/whatweb"
try:
    whatweb_result = subprocess.run([whatweb_path, '--no-errors', f'http://{url_or_ip}:{port}'], capture_output=True, text=True)
    print("\nBanner Grabbing Results (WhatWeb):")
    print(whatweb_result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# Run cURL for banner grabbing
curl_path = "/usr/bin/curl"
try:
    curl_result = subprocess.run([curl_path, f'http://{url_or_ip}:{port}'], capture_output=True, text=True)
    print("\nBanner Grabbing Results (cURL):")
    print(curl_result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# Perform telnet-like operation for banner grabbing
try:
    tn = telnetlib.Telnet(url_or_ip, port, timeout=5)  # Increase timeout to 5 seconds
    print("\nBanner Grabbing Results (Telnet):")
    print(tn.read_all().decode('ascii'))
    tn.close()
except Exception as e:
    print(f"Error: {e}")