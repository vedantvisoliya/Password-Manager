from cryptography.fernet import Fernet
from key_function import load_key

master_key = input("Enter the master key: ")

def view(master_key: str):
    key = load_key(master_key)
    cipher = Fernet(key)
    with open("passwords.txt", 'r') as pass_file:
        passwords = pass_file.readlines()
    for info in passwords:
        acc_name, passw = info.split('|')
        passw = cipher.decrypt(passw).decode()
        print(f"Account Name: {acc_name} , Password: {passw}")
    print()

def add(master_key: str):
    key = load_key(master_key)
    cipher = Fernet(key)
    account_name = input("Enter Account Name: ")
    password = input("Enter the Password: ")
    with open("passwords.txt", "a") as pass_file:
        pass_file.write(account_name + "|" + cipher.encrypt(password.encode()).decode() + "\n")
    print()


while True:
    mode = input("Which mode do you want?\n1. view (type view)\n2. add (type add)\n3. quit (press q)\n: ").lower()
    if mode == 'q':
        break

    if mode == "view":
        view(master_key)
    elif mode == "add":
        add(master_key)