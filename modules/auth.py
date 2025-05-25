import json
import os
import hashlib
import pwinput

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
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        users = self.load_users()
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = pwinput.pwinput(prompt="Password: ").strip()
        hashed_password = self.hash_password(password)

        for user in users:
            if user["username"] == username and user["password"] == hashed_password:
                self.logged_in_user = User(username, user["role"])
                print(f"Login successful. Welcome, {username} ({user['role']})!")
                return self.logged_in_user

        print("Invalid username or password.")
        return None
    
    def register_user(self):
        print("\n=== REGISTER NEW USER ===")

        users = self.load_users()

        username = input("Enter new username: ").strip()
        if any(user['username'] == username for user in users):
            print("Username already exists.")
            return

        password = pwinput.pwinput(prompt="Enter password: ").strip()
        hashed_password = self.hash_password(password)

        role = input("Enter role (admin/staff): ").strip().lower()

        if role not in ["admin", "staff"]:
            print("Invalid role. Must be 'admin' or 'staff'.")
            return

        new_user = {
            "username": username,
            "password": hashed_password,
            "role": role
        }

        users.append(new_user)

        try:
            with open(self.users_file, "w") as f:
                json.dump(users, f, indent=4)
            print(f"User '{username}' registered successfully as {role}.")
        except Exception as e:
            print(f"Failed to register user: {e}")

    