from modules.student import StudentManager
from modules.room import RoomManager
from modules.report import ReportGenerator
from modules.auth import AuthSystem


# Create manager instances
student_manager = StudentManager()
room_manager = RoomManager()
report_generator = ReportGenerator(student_manager, room_manager)


def student_menu():
    while True:
        print("\nStudent Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            if user.role != "admin":
                print("Access denied. Only admin can add students.")
            else:
                name = input("Enter name: ")
                age = input("Enter age: ")
                gender = input("Enter gender (M/F): ")
                student_manager.add_student(name, age, gender)
        elif choice == '2':
            student_manager.view_all_students()
        elif choice == '3':
            if user.role != "admin":
                print("Access denied. Only admin can delete students.")
            else:
                student_id = input("Enter student ID to delete: ")
                student_manager.delete_student(student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def room_menu():
    while True:
        print("\nRoom Management")
        print("1. Add Room")
        print("2. View All Rooms")
        print("3. View Available Rooms")
        print("4. Delete Room")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            if user.role != "admin":
                print("Access denied. Only admin can add rooms.")
            else:
                number = input("Enter room number: ")
                capacity = int(input("Enter room capacity: "))
                room_manager.add_room(number, capacity)
        elif choice == '2':
            room_manager.view_all_rooms()
        elif choice == '3':
            room_manager.view_available_rooms()
        elif choice == '4':
            if user.role != "admin":
                print("Access denied. Only admin can delete rooms.")
            else:
                number = input("Enter room number to delete: ")
                room_manager.delete_room(number)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def assignment_menu():
    while True:
        print("\nRoom Assignment")
        print("1. Assign Room to Student")
        print("2. Unassign Student from Room")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            if user.role != "admin":
                print("Access denied. Only admin can assign rooms.")
            else:
                student_id = input("Enter student ID: ")
                room_number = input("Enter room number: ")
                room_manager.assign_room_to_student(student_id, room_number)
        elif choice == '2':
            if user.role != "admin":
                print("Access denied. Only admin can unassign rooms.")
            else:
                student_id = input("Enter student ID: ")
                room_manager.unassign_student_from_room(student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def search_menu():
    while True:
        print("\nSearch Menu")
        print("1. Search Student by Name or ID")
        print("2. Search Room by Room Number")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            query = input("Enter student name or ID to search: ")
            student_manager.search_student(query)
        elif choice == '2':
            room_number = input("Enter room number to search: ")
            room_manager.search_room(room_number)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def report_menu():
    while True:
        print("\n--- REPORT MENU ---")
        print("1. Generate Student Report")
        print("2. Generate Room Report")
        print("3. Back to Main Menu")

        choice = input("Select an option: ").strip()
        if choice == "1":
            if user.role != "admin":
                print("Access denied. Only admin can generate reports.")
            else:
                report_generator.generate_student_report()
        elif choice == "2":
            if user.role != "admin":
                print("Access denied. Only admin can generate reports.")
            else:
                report_generator.generate_room_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Generate Reports")
        print("2. Register New User")
        print("3. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            report_menu()
        elif choice == "2":
            auth.register_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def main_menu():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Room Assignment")
        print("4. Change Password")
        print("5. Search")
        
        if user.role == "admin":
            print("9. Admin Menu")
            print("0. Logout / Exit")
        else:
            print("0. Logout / Exit")


        choice = input("Select an option: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            room_menu()
        elif choice == "3":
            assignment_menu()
        elif choice == "4":
            auth.change_password()
        elif choice == "5":
            search_menu()
        elif choice == "9" and user.role == "admin":
            admin_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Start program
if __name__ == "__main__":
    auth = AuthSystem()
    user = auth.login()

    if user:
        main_menu()
    else:
        print("Access denied. Exiting system.")