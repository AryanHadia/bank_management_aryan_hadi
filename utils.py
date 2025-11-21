import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def check_password(hashed_password, plain_password):
    if hashed_password == hash_password(plain_password):
        return True
    else:
        return False
    
