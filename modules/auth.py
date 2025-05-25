import json
import os

USERS_FILE = "data/users.json"

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class AuthSystem:
    def __init__(self, users_file=USERS_FILE):
        self.users_file = users_file
        self.logged_in_user = None

    def load_users(self):
        if not os.path.exists(self.users_file):
            return []
        with open(self.users_file, "r") as f:
            return json.load(f)

    def login(self):
        users = self.load_users()
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for user in users:
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = User(username, user["role"])
                print(f"Login successful. Welcome, {username} ({user['role']})!")
                return self.logged_in_user

        print("Invalid username or password.")
        return None
    
