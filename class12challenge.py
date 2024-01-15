#!/usr/bin/env python3
# Script: Ops 401 
# Class 12 challenge 
# Authur: Will B. with the help of ChatGPT
# Date: 1/15/2024
# Resources Google, Bard, ChatGPT, 

# A network Security tool using Scapy part 2 of 3

# Import the necessary modules from Scapy
from scapy.all import IP, TCP, sr1, ICMP

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

# Function to perform an ICMP ping sweep on a given network
def icmp_ping_sweep(network_address):
    # Create a list to store online hosts
    online_hosts = []

    # Generate a list of IP addresses from the given network (excluding network and broadcast addresses)
    ip_list = [str(ip) for ip in IP(network_address).hosts()]

    # Loop through each IP address and perform ICMP ping
    for ip in ip_list:
        # Create an IP packet with the target IP
        ip_packet = IP(dst=ip)

        # Create an ICMP packet (ping request)
        icmp_packet = ICMP()

        # Combine the IP and ICMP packets
        packet = ip_packet / icmp_packet

        # Send the packet and capture the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if a response was received
        if response:
            # Check the ICMP type and code in the response
            if response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                # ICMP type 3, codes 1, 2, 3, 9, 10, 13 indicate blocking
                print(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                # Host is responding
                print(f"Host {ip} is responding.")
                online_hosts.append(ip)
        else:
            # No response - host is down or unresponsive
            print(f"Host {ip} is down or unresponsive.")

    # Count and inform the user about the number of online hosts
    print(f"\nNumber of online hosts: {len(online_hosts)}")

# Main function
def main():
    # Prompt the user to choose between TCP Port Range Scanner and ICMP Ping Sweep
    choice = input("Choose mode:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\nEnter choice (1 or 2): ")

    if choice == "1":
        # Get user input for TCP Port Range Scanner
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        tcp_port_scanner(target_ip, start_port, end_port)
    elif choice == "2":
        # Get user input for ICMP Ping Sweep
        network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()