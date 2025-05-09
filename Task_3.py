import hashlib

users = {}

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def register():
    u = input("Username: ")
    p = input("Password: ")
    users[u] = hash_pwd(p)
    print("Registered!")

def login():
    u = input("Username: ")
    p = input("Password: ")
    if u in users and users[u] == hash_pwd(p):
        print("Login successful!")
    else:
        print("Invalid credentials.")

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    ch = input("Choice: ")
    if ch == '1':
        register()
    elif ch == '2':
        login()
    elif ch == '3':
        break
    else:
        print("Invalid option.")
