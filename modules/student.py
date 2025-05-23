from modules.file_io import load_data, save_data

STUDENT_FILE = 'data/students.json'
ROOM_FILE = 'data/rooms.json'


def add_student():
    print("\n=== Add New Student ===")

    # Get user input 
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    gender = input("Enter Gender (Male/Female): ")

    # Create a student dictionary
    student = {
        "id": student_id,
        "name": name,
        "gender": gender,
        "room": None # Not assigned yet
    }

    # load current students
    students = load_data(STUDENT_FILE)

    # Add new student 
    students.append(student)

    # save back to file 
    save_data(STUDENT_FILE, students)

    print(f"Student '{name}' added successfully!")

def view_students():
    print("\n======================== All Students =======================\n")

    students = load_data(STUDENT_FILE)

    if not students:
        print("No students found.")
        return
    
    # Print table header
    print(f"{'ID':<10} {'Name':<25} {"Gender":<10} {'Room':<10}")
    print("-" * 60)

    for student in students:
        room = student['room'] if student['room'] else "Not Assigned"
        print(f"{student['id']:<10} {student['name']:<25} {student['gender']:<10} {room:<10}")

def add_room():
    print("\n=== Add New Room ===")

    room_number = input("Enter Room Number: ").strip().upper()
    try:
        capacity = int(input("Enter Room Capacity: "))
    except ValueError:
        print("Capacity must be a number.")
        return

    # Load existing rooms
    rooms = load_data(ROOM_FILE)

    # Check for duplicate room number
    for room in rooms:
        if room["number"] == room_number:
            print("Room already exists.")
            return

    # Create new room dictionary
    new_room = {
        "number": room_number,
        "capacity": capacity,
        "occupants": []
    }

    # Add and save
    rooms.append(new_room)
    save_data(ROOM_FILE, rooms)

    print(f"Room {room_number} added with capacity {capacity}")

