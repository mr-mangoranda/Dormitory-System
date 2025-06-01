import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/students.json')


def load_students():
    try:
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(DATA_PATH, 'w') as f:
        json.dump(students, f, indent=4)

def add_student(student_data):
    students = load_students()
    students.append(student_data)
    save_students(students)
    return student_data

def get_student_by_id(student_id):
    students = load_students()
    for student in students:
        if student.get("id") == student_id:
            return student
    return None

def update_student(student_id, new_data):
    students = load_students()
    for i, student in enumerate(students):
        if student.get("id") == student_id:
            students[i].update(new_data)
            save_students(students)
            return students[i]
    return None

def delete_student(student_id):
    students = load_students()
    students = [s for s in students if s.get("id") != student_id]
    save_students(students)
    return True
