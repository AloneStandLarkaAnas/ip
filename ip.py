import os
import subprocess
import time

def install_tor():
    print("Installing Tor...")
    subprocess.run(["apt-get", "update"], check=True)
    subprocess.run(["apt-get", "install", "-y", "tor"], check=True)
    print("Tor installation complete.")

def start_tor_service():
    print("Starting Tor service...")
    subprocess.run(["service", "tor", "start"], check=True)
    print("Tor service started.")

def change_ip(interval):
    while True:
        print(f"Changing IP address every {interval} seconds...")
        subprocess.run(["tor", "--hash-password", "my_password"], check=True)
        time.sleep(interval)

def main():
    try:
        interval = int(input("Enter the time in seconds for changing IP address: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Check if Tor is installed
    try:
        subprocess.run(["tor", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Tor is already installed.")
    except subprocess.CalledProcessError:
        install_tor()

    start_tor_service()
    change_ip(interval)

if __name__ == "__main__":
    main()
