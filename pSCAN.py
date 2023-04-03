import os
import socket
from tqdm import tqdm

# Print ASCII art
print("""
▒█▀▄░▄▀▀░▄▀▀▒▄▀▄░█▄░█
░█▀▒▒▄██░▀▄▄░█▀█░█▒▀█
""")

VERSION = "0.1"

print()

# Get input from the user for the IP address
ip_address = input("Enter an IP address to scan for open ports: ")

# Define the path to the port file
port_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pSCAN-ports.txt")

# Read in the list of ports from the file
with open(port_file, 'r') as f:
    port_list = f.read().strip().split(',')

# Convert the list of strings to a list of integers
ports = [int(port) for port in port_list]

# Initialize an empty list to store the open ports
open_ports = []

# Loop over each port in the list and check if it's open
with tqdm(total=len(ports), ncols=80, bar_format='{desc}\033[31m{bar}\033[0m', dynamic_ncols=True) as pbar:
    for port in ports:
        try:
            # Create a new socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout to avoid hanging indefinitely on unresponsive ports
            s.settimeout(0.1)
            # Attempt to connect to the IP address and port
            result = s.connect_ex((ip_address, port))
            # If the connection was successful, add the port to the list of open ports and display the status
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            # Close the socket
            s.close()
        except:
            # If there was an error, skip to the next port
            pass
        pbar.update(1)
        pbar.set_description(f"Scanning port {port}")

print()
print('\033[1;41m OPEN PORTS FOUND: \033[m')
print()

# Print out the open ports, one at a time, one above the other
for port in open_ports:
    print(port)
