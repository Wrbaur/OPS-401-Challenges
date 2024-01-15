#!/usr/bin/env python3
# Script: Ops 401 
# Class 11 challenge 
# Authur: Will B. with the help of ChatGPT
# Date: 1/15/2024
# Resources Google, Bard, ChatGPT, 

# A network Security tool using Scapy part 1 of 3

# Import the necessary modules from Scapy
from scapy.all import IP, TCP, sr1

# Function to perform a TCP port scan on a given host and port range
def tcp_port_scanner(target_ip, start_port, end_port):
    # Loop through each port in the specified range
    for port in range(start_port, end_port + 1):
        # Create an IP packet with the target IP
        ip_packet = IP(dst=target_ip)

        # Create a TCP packet with the current port as the destination port
        tcp_packet = TCP(dport=port, flags="S")  # "S" flag indicates a SYN packet

        # Combine the IP and TCP packets
        packet = ip_packet / tcp_packet

        # Send the packet and capture the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if a response was received
        if response:
            # Check the TCP flags in the response
            if response.haslayer(TCP) and response[TCP].flags == 0x12:
                # 0x12 means "SYN-ACK" - port is open
                print(f"Port {port} is open.")
            elif response.haslayer(TCP) and response[TCP].flags == 0x14:
                # 0x14 means "RST-ACK" - port is closed
                print(f"Port {port} is closed.")
            else:
                # No specific flag received - port is filtered
                print(f"Port {port} is filtered (silent drop).")

# Get user input for target IP and port range
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Call the function to perform the TCP port scan
tcp_port_scanner(target_ip, start_port, end_port)