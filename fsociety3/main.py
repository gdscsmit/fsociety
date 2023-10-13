import os
import time
import subprocess
from scripts import distro,requirements,nmap,android

def run():
    print("1. Install Dependencies")
    print("2. Nmap")
    print("3. SQLMap")
    print("4. Android tools")
    print("9. Go Back To Main Menu")
    choice = int(input("fsociety# "))
    if choice == 1:
        dist = distro.get_distro()
        requirements.install_requirements(distro)
    elif choice == 2:
        options = nmap.get_nmap_options()
        host = nmap.get_host()
        command = ['nmap'] + options + [host]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    elif choice == 4:
        print("1. Bypass 4 digit lockscreen")
        print("2. Bypass 6 digit lockscreen")
        choice = int(input("fsociety# "))
        if choice == 1:
            android.bypass(4)
        else:
            android.bypass(6)
