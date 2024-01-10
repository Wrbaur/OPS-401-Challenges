#!/usr/bin/env python3
# Script: Ops 401 
# Class 2 challenge 
# Authur: Will B. with the help of ChatGPT
# Date: 1/09/2024
# Resources Google, Bard, ChatGPT, https://docs.python.org/3/library/subprocess.html

# Create uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down

# The script must:

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.

# Stretch Goals (Optional Objectives)
# In Python, add the below features to your uptime sensor tool.

# The script must:

# Save the output to a text file as a log of events.
# Accept user input for target IP address.

# import libraries 
import subprocess
import time
from datetime import datetime  # Import the datetime class from the datetime module

def ping_host(target_ip):
    try:
        # Use the subprocess module to run the ping command
        subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=1)
        return True  # Return True if the ping is successful
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False  # Return False if there's an error or timeout
    
def log_event(status, target_ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp in the specified format
    print(f"{timestamp} {'Active' if status else 'Inactive'} to {target_ip}")  # Print the log entry

def main():
    target_ip = input("Enter target IP address: ")
    while True:
        status = ping_host(target_ip)  # Check the status of the host
        log_event(status, target_ip)  # Log the event
        time.sleep(2)  # Pause for 2 seconds

if __name__ == "__main__":
    main()  # Call the main function when the script is executed