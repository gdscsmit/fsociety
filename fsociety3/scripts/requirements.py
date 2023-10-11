def install_requirements(distro):
    if distro == "arch":
        os.system('sudo pacman -S nmap')