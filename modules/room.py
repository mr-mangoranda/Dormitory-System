from modules.file_io import load_data, save_data

ROOM_FILE = 'data/rooms.json'
STUDENT_FILE = 'data/students.json'

def assign_room_to_student():
    print("\n=== Assign Room to Student ===")

    students = load_data(STUDENT_FILE)
    rooms = load_data(ROOM_FILE)

    # Get unassigned students
    unassigned_students = [s for s in students if not s['room']]
    if not unassigned_students:
        print("All students are already assigned to rooms.")
        return

    print("\nUnassigned Students:")
    for s in unassigned_students:
        print(f"{s['id']}: {s['name']} ({s['gender']})")

    student_id = input("Enter Student ID to assign: ").strip()
    student = next((s for s in students if s['id'] == student_id and not s['room']), None)

    if not student:
        print("Invalid or already assigned student.")
        return

    # Get rooms with space
    available_rooms = [r for r in rooms if len(r['occupants']) < r['capacity']]
    if not available_rooms:
        print("No available rooms.")
        return

    print("\nAvailable Rooms:")
    for r in available_rooms:
        space_left = r['capacity'] - len(r['occupants'])
        print(f"{r['number']} - Capacity: {r['capacity']} | Occupied: {len(r['occupants'])} | Space Left: {space_left}")

    room_number = input("Enter Room Number to assign: ").strip().upper()
    room = next((r for r in rooms if r['number'] == room_number and len(r['occupants']) < r['capacity']), None)

    if not room:
        print("Invalid room or room is full.")
        return

    # Update room and student
    room['occupants'].append(student['id'])
    student['room'] = room['number']

    # Save changes
    save_data(STUDENT_FILE, students)
    save_data(ROOM_FILE, rooms)

    print(f"{student['name']} assigned to Room {room['number']}.")

    # modules/room.py (continued)

def view_all_rooms():
    print("\n=== All Rooms ===")

    rooms = load_data(ROOM_FILE)
    students = load_data(STUDENT_FILE)

    if not rooms:
        print("No rooms found.")
        return

    for room in rooms:
        print(f"\nRoom Number: {room['number']}")
        print(f"Capacity: {room['capacity']}")
        print(f"Occupants ({len(room['occupants'])}/{room['capacity']}):")

        if room["occupants"]:
            for student_id in room["occupants"]:
                student = next((s for s in students if s["id"] == student_id), None)
                if student:
                    print(f" - {student['name']} ({student['id']})")
                else:
                    print(f" - Unknown student ID: {student_id}")
        else:
            print(" - None")

# modules/room.py (continued)

def delete_room():
    print("\n=== Delete Room ===")

    rooms = load_data(ROOM_FILE)

    if not rooms:
        print("No rooms found.")
        return

    room_number = input("Enter Room Number to delete: ").strip().upper()
    room = next((r for r in rooms if r["number"] == room_number), None)

    if not room:
        print("Room not found.")
        return

    if room["occupants"]:
        print("Cannot delete room. It has occupants.")
        return

    confirm = input(f"Are you sure you want to delete Room {room_number} (Y/N)? ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return

    rooms = [r for r in rooms if r["number"] != room_number]
    save_data(ROOM_FILE, rooms)

    print(f"Room {room_number} deleted.")

def unassign_student_from_room():
    print("\n=== Unassign Student from Room ===")

    students = load_data(STUDENT_FILE)
    rooms = load_data(ROOM_FILE)

    student_id = input("Enter Student ID to unassign: ").strip()
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        print("Student not found.")
        return

    if not student["room"]:
        print("ℹStudent is not assigned to any room.")
        return

    # Remove student from room's occupant list
    for room in rooms:
        if room["number"] == student["room"]:
            room["occupants"] = [id for id in room["occupants"] if id != student_id]
            break

    student["room"] = None  # Unassign room in student record

    # Save changes
    save_data(STUDENT_FILE, students)
    save_data(ROOM_FILE, rooms)

    print(f"Student {student['name']} has been unassigned from the room.")

def view_available_rooms():
    print("\n=== Available Rooms ===")

    rooms = load_data(ROOM_FILE)

    available = [room for room in rooms if len(room["occupants"]) < room["capacity"]]

    if not available:
        print("No available rooms found.")
        return

    for room in available:
        remaining = room["capacity"] - len(room["occupants"])
        print(f"Room {room['number']} - {remaining} slot(s) available")
