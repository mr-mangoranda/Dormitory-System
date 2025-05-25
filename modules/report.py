import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, student_manager, room_manager, output_dir="reports"):
        self.student_manager = student_manager
        self.room_manager = room_manager
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_student_report(self):
        filename = f"{self.output_dir}/students_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, "w") as f:
                f.write("==== STUDENT REPORT ====\n\n")
                if not self.student_manager.students:
                    f.write("No students available.\n")
                else:
                    for s in self.student_manager.students:
                        room_info = s.room if s.room else "Unassigned"
                        f.write(f"ID: {s.id}\nName: {s.name}\nAge: {s.age}\nGender: {s.gender}\nRoom: {room_info}\n\n")

            print(f"Student report generated: {filename}")
        except Exception as e:
            print(f"Error generating student report: {e}")

    def generate_room_report(self):
        filename = f"{self.output_dir}/rooms_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, "w") as f:
                f.write("==== ROOM REPORT ====\n\n")
                if not self.room_manager.rooms:
                    f.write("No rooms available.\n")
                else:
                    for r in self.room_manager.rooms:
                        f.write(f"Room Number: {r.number}\nCapacity: {r.capacity}\nOccupants ({len(r.occupants)}):\n")
                        if r.occupants:
                            for occ in r.occupants:
                                f.write(f" - {occ}\n")
                        else:
                            f.write(" - None\n")
                        f.write("\n")

            print(f"Room report generated: {filename}")
        except Exception as e:
            print(f"Error generating room report: {e}")
