def install_requirements(distro):
    if distro == "arch":
        os.system('sudo pacman -S nmap yay')
        os.system('yay -S android-sdk-platform-tools')
    if distro == "ubuntu" or distro == "debian":
        os.system('sudo apt-get install nmap android-platform-tools')