import uuid
from modules.file_io import load_data, save_data

STUDENT_FILE = "data/students.json"

class Student:
    def __init__(self, student_id, name, age, gender, room=None):
        self.id = student_id
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

    @staticmethod
    def from_dict(data):
        return Student(
            student_id=data["id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            room=data.get("room")
        )

class StudentManager:
    def __init__(self):
        self.students = [Student.from_dict(s) for s in load_data(STUDENT_FILE)]

    def save(self):
        save_data(STUDENT_FILE, [s.to_dict() for s in self.students])

    def add_student(self, name, age, gender):
        student_id = str(uuid.uuid4())[:8]
        student = Student(student_id, name, age, gender)
        self.students.append(student)
        self.save()
        print(f"Student {name} added with ID: {student_id}")

    def view_all_students(self):
        if not self.students:
            print("No students found.")
            return

        for s in self.students:
            room_info = s.room if s.room else "Unassigned"
            print(f"{s.id} - {s.name} ({s.gender}, {s.age}) | Room: {room_info}")

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                self.save()
                print(f"Student {student.name} deleted.")
                return
        print("Student not found.")

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
