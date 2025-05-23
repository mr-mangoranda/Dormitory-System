from modules.student import add_student, view_students, add_room, delete_student
from modules.room import assign_room_to_student, view_all_rooms, delete_room, unassign_student_from_room, view_available_rooms

def main_menu():
    while True:
        print("\n===== Dormitory Management System =====")
        print(" 1. Student Management")
        print(" 2. Room Management")
        print(" 3. Room Assignment")
        print(" 0. Exit")

def student_menu():
    while True:
        print("\nStudent Management")
        print(" 1. Add Student")
        print(" 2. View All Students")
        print(" 3. Delete Student")
        print(" 0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def room_menu():
    while True:
        print("\nRoom Management")
        print(" 1. Add Room")
        print(" 2. View All Rooms")
        print(" 3. View Available Rooms")
        print(" 4. Delete Room")
        print(" 0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_room()
        elif choice == '2':
            view_all_rooms()
        elif choice == '3':
            view_available_rooms()
        elif choice == '4':
            delete_room()
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
            assign_room_to_student()
        elif choice == '2':
            unassign_student_from_room()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")



        choice = input("Enter your choice: ")

        if choice == '1':
            student_menu()
        elif choice == '2':
            room_menu()
        elif choice == '3':
            assignment_menu()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        
if __name__ == "__main__":
    main_menu()

