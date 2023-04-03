# pSCAN
pSCAN scans for open ports on a specified IP address, showing a progress bar and the most common 1000 ports used in the industry. A great and simple OSINT tool.

## How the script works?

pSCAN is designed to scan for open ports on a specified IP address. It uses the socket module to create a new socket object and connect to each port specified in the pSCAN-ports.txt file. If a connection is successful, the script adds the port to a list of open ports and displays the status. The script also uses the tqdm module to display a progress bar while scanning the ports.

## Breakdown of the script:

- Imports the necessary modules: os, socket, and tqdm.
- Prints out an ASCII art of the word "SCAN".
- Defines the version of the script.
- Gets the user input for the IP address to scan.
- Defines the path to the port file and read in the list of ports from the file.
- Converts the list of port strings to a list of integers.
- Initializes an empty list to store the open ports.
- Loops over each port in the list and attempt to connect to it.
- If the connection is successful, it adds the port to the list of open ports and displays the status.
- Closes the socket after each connection attempt.
- Uses the tqdm module to display a progress bar while scanning the ports.
- Prints out the list of open ports found.

Overall, this script can be useful for OSINT network administrators or security professionals who want to check for any open ports on a given IP address. However, it is important to note that scanning ports without permission may be illegal and should only be performed on systems that you have explicit permission.

## Preparation

The following Python modules must be installed:
```bash
pip3 socket, tqdm
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x pSCAN.py
```

## Usage
```bash
sudo python3 pSCAN.py

Enter an IP address to scan for open ports:
```

## Sample script
```python
import os
import socket
from tqdm import tqdm

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
```

## Sample output
```
sudo python3 pSCAN.py

▒█▀▄░▄▀▀░▄▀▀▒▄▀▄░█▄░█
░█▀▒▒▄██░▀▄▄░█▀█░█▒▀█


Enter an IP address to scan for open ports: 10.211.55.3
Scanning port 125: █████▋                                                                                                                          Port 135 is open
Scanning port 135: █████▊                                                                                                                          Port 139 is open
Scanning port 444: █████████▋                                                                                                                      Port 445 is open
Scanning port 65389: ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

OPEN PORTS FOUND:

135
139
445
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
