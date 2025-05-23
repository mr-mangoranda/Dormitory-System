from modules.file_io import load_data, save_data
from modules.student import StudentManager

ROOM_FILE = "data/rooms.json"

class Room:
    def __init__(self, number, capacity, occupants=None):
        self.number = number
        self.capacity = capacity
        self.occupants = occupants if occupants else []

    def to_dict(self):
        return {
            "number": self.number,
            "capacity": self.capacity,
            "occupants": self.occupants
        }

    @staticmethod
    def from_dict(data):
        return Room(
            number=data["number"],
            capacity=data["capacity"],
            occupants=data.get("occupants", [])
        )

class RoomManager:
    def __init__(self):
        self.rooms = [Room.from_dict(r) for r in load_data(ROOM_FILE)]
        self.student_manager = StudentManager()

    def save(self):
        save_data(ROOM_FILE, [r.to_dict() for r in self.rooms])
        self.student_manager.save()

    def add_room(self, number, capacity):
        if any(r.number == number for r in self.rooms):
            print("Room already exists.")
            return
        self.rooms.append(Room(number, capacity))
        self.save()
        print(f"Room {number} added.")

    def view_all_rooms(self):
        if not self.rooms:
            print("No rooms found.")
            return
        for r in self.rooms:
            print(f"Room {r.number} - {len(r.occupants)}/{r.capacity} occupants")

    def delete_room(self, number):
        for room in self.rooms:
            if room.number == number:
                if room.occupants:
                    print("Cannot delete room with assigned students.")
                    return
                self.rooms.remove(room)
                self.save()
                print(f"Room {number} deleted.")
                return
        print("Room not found.")

    def view_available_rooms(self):
        available = [r for r in self.rooms if len(r.occupants) < r.capacity]
        if not available:
            print("No available rooms.")
            return
        for r in available:
            print(f"Room {r.number} - {r.capacity - len(r.occupants)} slots available")

    def assign_room_to_student(self, student_id, room_number):
        student = self.student_manager.get_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        for room in self.rooms:
            if room.number == room_number:
                if len(room.occupants) >= room.capacity:
                    print("Room is full.")
                    return
                if student.room:
                    print("Student already assigned to a room.")
                    return
                room.occupants.append(student_id)
                student.room = room.number
                self.save()
                print(f"Assigned Room {room.number} to {student.name}")
                return
        print("Room not found.")

    def unassign_student_from_room(self, student_id):
        student = self.student_manager.get_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        if not student.room:
            print("Student is not assigned to any room.")
            return

        for room in self.rooms:
            if room.number == student.room:
                if student_id in room.occupants:
                    room.occupants.remove(student_id)
                    break

        student.room = None
        self.save()
        print(f"Student {student.name} unassigned from room.")
