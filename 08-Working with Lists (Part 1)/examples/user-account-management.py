#This Python script manages User Accounts in DevOps Environment

import json
import os

# File to store user accounts
USER_FILE = 'user_accounts.json'

# Load existing user accounts from a file
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    return []

# Save user accounts to a file
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Add a user
def add_user(username, email):
    users = load_users()
    if any(user['username'] == username for user in users):
        print(f"User '{username}' already exists.")
    else:
        users.append({'username': username, 'email': email})
        save_users(users)
        print(f"User '{username}' added successfully.")

# Remove a user
def remove_user(username):
    users = load_users()
    users = [user for user in users if user['username'] != username]
    save_users(users)
    print(f"User '{username}' removed successfully.")

# List all users
def list_users():
    users = load_users()
    if users:
        print("User Accounts:")
        for user in users:
            print(f"Username: {user['username']}, Email: {user['email']}")
    else:
        print("No users found.")

# Main function to demonstrate usage
def main():
    while True:
        print("\nUser Account Management")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            add_user(username, email)
        elif choice == '2':
            username = input("Enter username to remove: ")
            remove_user(username)
        elif choice == '3':
            list_users()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
