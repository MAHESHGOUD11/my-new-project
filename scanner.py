import os

hostname = "127.0.0.1"

print(f"Checking network connection for {hostname}...")
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(f"Success: {hostname} is online!")
else:
    print(f"Error: Connection to {hostname} failed.")
