#!/usr/bin/env python3
# Script: Ops 401 
# Class 3 challenge 
# Authur: Will B. with the help of ChatGPT
# Date: 1/10/2024
# Resources Google, Bard, ChatGPT
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-03/challenges/ops_challenge_2.py

# Create uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down
# Email to send notifications to 

# Imports
import subprocess # Import the subprocess module from the subprocess module https://docs.python.org/3/library
import time # Import the time module from the time module https://docs.python.org/3/library
from datetime import datetime # Import the datetime class from the datetime module https://docs.python.org/3
import smtplib # Import the smtplib module from the smtplib module https://docs.python.org/3/library
from email.mime.text import MIMEText # Import the MIMEText class from the MIMEText module https://docs.python.org/3
from email.mime.multipart import MIMEMultipart # Import the MIMEMultipart class from the MIMEMultipart module https://docs.python.org/3
from os import environ # Import the os module from the os module https://docs.python.org/3/library

# Function to check host status using ping
def ping_host(target_ip):
    try:
        subprocess.run(["ping", "-c", "1", target_ip], timeout=1, check=True)
        return True  # Ping successful
    except subprocess.TimeoutExpired:
        return "Timeout"  # Ping timed out
    except subprocess.CalledProcessError:
        return False  # Ping failed

def log_event(status, target_ip, log_file="event_log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if status == "Timeout":
        message = f"{timestamp} Ping to {target_ip} timed out\n"
    else:
        message = f"{timestamp} {'Active' if status else 'Inactive'} to {target_ip}\n"

    print(message)

    # Append the log entry to the file
    with open(log_file, "a") as log:
        log.write(message)

# Function to send email notifications
def send_email(sender_email, sender_password, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Main function
def main():
    target_ip = input("Enter target IP address: ")

    # Check for environment variables first
    sender_email = "XXXXXX630@gmail.com"
    sender_password = "xxxx xxxx xxxx xxxx"
    receiver_email = input("Enter the administrator's email address: ")

    previous_status = None
    while True:
        status = ping_host(target_ip)
        log_event(status, target_ip)

        if status != previous_status:
            subject = "Host Status Change"
            body = f"Host status changed from {'Active' if previous_status else 'Inactive'} to {'Active' if status else 'Inactive'}"
            send_email(sender_email, sender_password, receiver_email, subject, body)

        previous_status = status
        time.sleep(2)

if __name__ == "__main__":
    main()