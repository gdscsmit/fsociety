

def generate_md5_hash(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

def crack_md5_hash(hashed_value, password_list):
    for password in password_list:
        if hashlib.md5(password.encode()).hexdigest() == hashed_value:
            return password
    return None
