def get_distro():
    id_like = None

    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('ID_LIKE'):
                id_like = line.split('=')[1].strip()

    return id_like