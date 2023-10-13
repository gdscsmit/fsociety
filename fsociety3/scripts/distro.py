def get_distro():
    id_like = None

    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('ID_LIKE'):
                    id_like = line.split('=')[1].strip()
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return id_like
