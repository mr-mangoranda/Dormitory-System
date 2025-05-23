# modules/room.py

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
        print("❌ Invalid or already assigned student.")
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