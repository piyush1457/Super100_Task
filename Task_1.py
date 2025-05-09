users = [
    {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
    {"id": 2, "name": "Bob", "email": "bob@gmail.com"}
]

def create_user(users):
    user_id = int(input("Enter user ID: "))
    for user in users:
        if user['id'] == user_id:
            print("User ID already exists!")
            return
    name = input("Enter name: ")
    email = input("Enter email: ")
    users.append({"id": user_id, "name": name, "email": email})
    print("User added.")

def read_users(users):
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

def update_user(users):
    user_id = int(input("Enter user ID to update: "))
    for user in users:
        if user['id'] == user_id:
            user['name'] = input("Enter new name: ")
            user['email'] = input("Enter new email: ")
            print("User updated.")
            return
    print("User not found.")

def delete_user(users):
    user_id = int(input("Enter user ID to delete: "))
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(i)
            print("User deleted.")
            return
    print("User not found.")

while True:
    print("\n1. Create User\n2. Read Users\n3. Update User\n4. Delete User\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        create_user(users)
    elif choice == '2':
        read_users(users)
    elif choice == '3':
        update_user(users)
    elif choice == '4':
        delete_user(users)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
