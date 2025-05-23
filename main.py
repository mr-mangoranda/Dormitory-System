from modules.student import StudentManager
from modules.room import RoomManager

# Create manager instances
student_manager = StudentManager()
room_manager = RoomManager()

def student_menu():
    while True:
        print("\nStudent Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender (M/F): ")
            student_manager.add_student(name, age, gender)
        elif choice == '2':
            student_manager.view_all_students()
        elif choice == '3':
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
            number = input("Enter room number: ")
            capacity = int(input("Enter room capacity: "))
            room_manager.add_room(number, capacity)
        elif choice == '2':
            room_manager.view_all_rooms()
        elif choice == '3':
            room_manager.view_available_rooms()
        elif choice == '4':
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
            student_id = input("Enter student ID: ")
            room_number = input("Enter room number: ")
            room_manager.assign_room_to_student(student_id, room_number)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            room_manager.unassign_student_from_room(student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n===== Dormitory Management System =====")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Room Assignment")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_menu()
        elif choice == '2':
            room_menu()
        elif choice == '3':
            assignment_menu()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

# Start program
if __name__ == "__main__":
    main_menu()
