from cryptography.fernet import Fernet

def generate_key(master_key: str):
    key = Fernet.generate_key() + master_key.encode()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(master_key: str):
    with open("key.key", "rb") as key_file:
        key = key_file.read().decode()
    real_key = (key.split('='))[1]
    if (real_key == master_key):
        return key
    else:
        raise ValueError("Invalid Master Key")


# run single time to create a unique key
if (__name__ == "__main__"):
    master_key = input("Create a master key: ")
    generate_key(master_key)