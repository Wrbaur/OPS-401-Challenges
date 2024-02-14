#!/usr/bin/env python3
# Script: Ops 401 
# Class 27 Challenge
# Authur: Will B. with the help of ChatGPT
# Date: 2/13/2024
# Resources Google, Gemini, ChatGPT, 
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/,

# Add steamhandler ans file handler, also can distinguish between types, also add emailing for error and warnings

import logging
from logging.handlers import RotatingFileHandler
import paramiko
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

file_handler = RotatingFileHandler('my_logs.log', maxBytes=1024, backupCount=3)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

email_from = "r.ruab630@gmail.com"
email_to = "r.ruab630@gmail.com"
email_subject = "Error or Warning Logged"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your_smtp_username"
smtp_password = "your_smtp_password"

def send_email(receiver_email, subject, body):
    # Specify the Gmail account for sending emails
    sender_email = "r.ruab630@gmail.com"
    sender_password = "rsnk pfec jdxs kujl"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

class EmailLoggingHandler(logging.Handler):
    def emit(self, record):
        if record.levelno >= logging.ERROR:
            send_email(email_to, "Error Logged", f"{record.levelname}: {record.msg}")
        elif record.levelno >= logging.WARNING:
            send_email(email_to, "Warning Logged", f"{record.levelname}: {record.msg}")
email_handler = EmailLoggingHandler()
email_handler.setLevel(logging.WARNING)
email_handler.setFormatter(formatter)
logger.addHandler(email_handler)

def unzip_zip_file(zipped_file, password):
    print(f"Trying to unzip {zipped_file} with password: {password}")
    logging.info(f"Trying to unzip {zipped_file} with password: {password}")

def get_credentials():
    host = input('Enter the target SSH host (default "192.168.50.30"): ') or "192.168.50.30"
    logging.info(f"Target SSH host: {host}")
    user = input('Enter the SSH username (default "will"): ') or "will"
    logging.info(f"SSH username: {user}")
    return host, user, get_password(host, user)

def get_password(host, user):
    password = input(f'Enter the SSH password for {user}@{host} (default "passwo1234"): ') or "passwo1234"
    logging.info("Entered SSH password.")
    return password

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

def main():
    mode = input("Select mode:\n1. Offensive; Dictionary Iterator\n2. Defensive; Password Recognized\n3. SSH Authentication\nEnter mode (1, 2, or 3): ")
    if mode not in ['1', '2', '3']:
        logging.error("Invalid mode selection.")
        print("Invalid mode. Exiting.")
        return
    
    mode = int(mode)

    if mode == 1:
        pass
    elif mode == 2:
        pass
    elif mode == 3:
        ssh_client()

if __name__ == "__main__":
    main()
