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

def delete(line_number: int):
    with open("passwords.txt", 'r') as pass_file:
        account_info = pass_file.readlines()
    try:
        del account_info[line_number-1]
    except Exception as e:
        raise e
    
    account_info = ''.join(account_info)

    with open("passwords.txt", 'w') as pass_file:
        pass_file.write(account_info)
 
while True:
    mode = input("Which mode do you want?\n1. view (type view)\n2. add (type add)\n3. delete (type del)\n4. quit (press q)\n: ").lower()
    print()

    if mode == 'q':
        break

    if mode == "view":
        view(master_key)
    elif mode == "add": 
        add(master_key)
    elif mode == "del":
        line_no = int(input("Which line number do you want to delete: "))
        print()
        delete(line_no)