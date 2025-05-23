from modules.student import add_student, view_students, add_room, delete_student
from modules.room import assign_room_to_student, view_all_rooms, delete_room


def main_menu():
    while True:
        print("\n===== Dormitory Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add New Rroom")
        print("4. Assign Room to Student")
        print("5. View All Rooms")
        print("6. Delete Student")
        print("7. Delete Room")

        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == '3':
            add_room()
        elif choice == "4":
            assign_room_to_student()
        elif choice == "5":
            view_all_rooms()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            delete_room()
        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main_menu()

