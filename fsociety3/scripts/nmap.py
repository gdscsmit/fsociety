
import os
import subprocess  # Import the subprocess module here


def get_nmap_options():
    print("Select an option:")
    print("1. Stealth Scan")
    print("2. Normal Scan")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        return ['-sS']
    elif option == '2':
        return []
    elif option == '3':
        return None
    else:
        print("Invalid option, please try again.")
        return get_nmap_options()

def get_host():
    return input("Enter the host: ")

