from modules.student import add_student, view_students, add_room


def main_menu():
    while True:
        print("\n===== Dormitory Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add New Rroom")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == '3':
            add_room()
        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main_menu()

