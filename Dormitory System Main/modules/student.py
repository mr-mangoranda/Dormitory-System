import json
import os

class Student:
    def __init__(self, id, name, age, gender, room=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.room = room

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "room": self.room
        }

class StudentManager:
    def __init__(self, filename="data/students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    return [Student(**d) for d in data]
            else:
                return []
        except json.JSONDecodeError:
            print("Error: Invalid data in students.json. Starting with an empty list.")
            return []
        except Exception as e:
            print(f"Unexpected error loading students: {e}")
            return []

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([s.to_dict() for s in self.students], f, indent=4)
        except Exception as e:
            print(f"Error saving student data: {e}")

    def add_student(self, name, age, gender):
        try:
            student_id = input("Enter student ID: ").strip()
            if not student_id:
                raise ValueError("Student ID cannot be empty.")
            if any(s.id == student_id for s in self.students):
                print("Error: A student with that ID already exists.")
                return

            new_student = Student(student_id, name, age, gender)
            self.students.append(new_student)
            self.save_data()
            print(f"Student {name} added successfully with ID {student_id}.")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Unexpected error adding student: {e}")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
            return

        for s in self.students:
            room_info = s.room if s.room else "Unassigned"
            print(f"{s.id} - {s.name} ({s.gender}, {s.age}) | Room: {room_info}")

    def delete_student(self, student_id):
        try:
            student = next((s for s in self.students if s.id == student_id), None)
            if student:
                self.students.remove(student)
                self.save_data()
                print(f"Student {student_id} deleted successfully.")
            else:
                print("Student not found.")
        except Exception as e:
            print(f"Error deleting student: {e}")

    def search_student(self, query):
        try:
            results = []
            query = query.lower()

            for student in self.students:
                if query in student.name.lower() or query == student.id:
                    results.append(student)

            if not results:
                print("No matching students found.")
                return

            for s in results:
                room_info = s.room if s.room else "Unassigned"
                print(f"{s.id} - {s.name} ({s.gender}, {s.age}) | Room: {room_info}")
        except Exception as e:
            print(f"Error searching students: {e}")
