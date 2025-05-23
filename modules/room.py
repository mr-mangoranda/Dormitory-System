import json
import os

class Room:
    def __init__(self, number, capacity, occupants=None):
        self.number = number
        self.capacity = capacity
        self.occupants = occupants if occupants is not None else []

    def to_dict(self):
        return {
            "number": self.number,
            "capacity": self.capacity,
            "occupants": self.occupants
        }

class RoomManager:
    def __init__(self, filename="data/rooms.json"):
        self.filename = filename
        self.rooms = self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    return [Room(**d) for d in data]
            else:
                return []
        except json.JSONDecodeError:
            print("Error: Invalid data in rooms.json. Starting with an empty list.")
            return []
        except Exception as e:
            print(f"Unexpected error loading rooms: {e}")
            return []

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([r.to_dict() for r in self.rooms], f, indent=4)
        except Exception as e:
            print(f"Error saving room data: {e}")

    def add_room(self, number, capacity):
        try:
            if any(r.number == number for r in self.rooms):
                print("Error: Room number already exists.")
                return

            if capacity <= 0:
                print("Error: Capacity must be greater than 0.")
                return

            new_room = Room(number, capacity)
            self.rooms.append(new_room)
            self.save_data()
            print(f"Room {number} added with capacity {capacity}.")
        except Exception as e:
            print(f"Unexpected error adding room: {e}")

    def view_all_rooms(self):
        if not self.rooms:
            print("No rooms available.")
            return

        for r in self.rooms:
            status = "Available" if len(r.occupants) < r.capacity else "Full"
            print(f"{r.number} - Capacity: {r.capacity}, Occupants: {len(r.occupants)} ({status})")

    def view_available_rooms(self):
        available = [r for r in self.rooms if len(r.occupants) < r.capacity]
        if not available:
            print("No available rooms.")
            return

        for r in available:
            print(f"{r.number} - Capacity: {r.capacity}, Occupants: {len(r.occupants)}")

    def delete_room(self, number):
        try:
            room = next((r for r in self.rooms if r.number == number), None)
            if room:
                self.rooms.remove(room)
                self.save_data()
                print(f"Room {number} deleted.")
            else:
                print("Room not found.")
        except Exception as e:
            print(f"Error deleting room: {e}")

    def assign_room_to_student(self, student_id, room_number):
        try:
            room = next((r for r in self.rooms if r.number == room_number), None)
            if not room:
                print("Room not found.")
                return

            if student_id in room.occupants:
                print("Student is already assigned to this room.")
                return

            if len(room.occupants) >= room.capacity:
                print("Room is already full.")
                return

            room.occupants.append(student_id)
            self.save_data()
            print(f"Student {student_id} assigned to room {room_number}.")
        except Exception as e:
            print(f"Error assigning student to room: {e}")

    def unassign_student_from_room(self, student_id):
        try:
            for room in self.rooms:
                if student_id in room.occupants:
                    room.occupants.remove(student_id)
                    self.save_data()
                    print(f"Student {student_id} unassigned from room {room.number}.")
                    return
            print("Student not found in any room.")
        except Exception as e:
            print(f"Error unassigning student from room: {e}")

    def search_room(self, room_number):
        try:
            for room in self.rooms:
                if room.number == room_number:
                    print(f"Room {room.number} - Capacity: {room.capacity}")
                    print(f"Occupants ({len(room.occupants)}): {', '.join(room.occupants) if room.occupants else 'None'}")
                    return
            print("Room not found.")
        except Exception as e:
            print(f"Error searching for room: {e}")
