import json
import os

ROOMS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "rooms.json")

def load_rooms():
    if not os.path.exists(ROOMS_FILE):
        return []
    with open(ROOMS_FILE, "r") as f:
        return json.load(f)

def save_rooms(rooms):
    with open(ROOMS_FILE, "w") as f:
        json.dump(rooms, f, indent=4)

def add_room(room):
    rooms = load_rooms()
    rooms.append(room)
    save_rooms(rooms)

def get_room_by_id(room_id):
    rooms = load_rooms()
    return next((r for r in rooms if r["id"] == room_id), None)

def update_room(room_id, updated_data):
    rooms = load_rooms()
    for room in rooms:
        if room["id"] == room_id:
            room.update(updated_data)
            break
    save_rooms(rooms)

def delete_room(room_id):
    rooms = load_rooms()
    rooms = [r for r in rooms if r["id"] != room_id]
    save_rooms(rooms)