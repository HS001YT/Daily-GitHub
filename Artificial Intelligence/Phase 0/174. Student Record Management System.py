import json
import os


# ================= STUDENT CLASS =================

class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    @staticmethod
    def from_dict(data):
        return Student(data["id"], data["name"], data["age"], data["course"])


# ================= STUDENT MANAGER =================

class StudentManager:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        folder_path = os.path.join(base_dir, "other_files")
        os.makedirs(folder_path, exist_ok=True)

        self.file_path = os.path.join(folder_path, "students.json")

        self.students = {}
        self.load_data()

    # ---------- Add Student ----------

    def add_student(self):

        sid = input("Enter Student ID: ")

        if sid in self.students:
            print("Student already exists.")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)

        self.students[sid] = student

        print("Student added successfully.")

    # ---------- View Students ----------

    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print("\n---------------------")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Course:", student.course)

    # ---------- Search Student ----------

    def search_student(self):

        sid = input("Enter Student ID: ")

        student = self.students.get(sid)

        if student:
            print("\nStudent Found")
            print("Name:", student.name)
            print("Age:", student.age)
            print("Course:", student.course)
        else:
            print("Student not found.")

    # ---------- Update Student ----------

    def update_student(self):

        sid = input("Enter Student ID to update: ")

        student = self.students.get(sid)

        if not student:
            print("Student not found.")
            return

        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        student.name = name
        student.age = age
        student.course = course

        print("Student updated successfully.")

    # ---------- Delete Student ----------

    def delete_student(self):

        sid = input("Enter Student ID to delete: ")

        if sid in self.students:
            del self.students[sid]
            print("Student deleted.")
        else:
            print("Student not found.")

    # ---------- Save Data ----------

    def save_data(self):

        data = [student.to_dict() for student in self.students.values()]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully.")

    # ---------- Load Data ----------

    def load_data(self):

        try:
            with open(self.file_path, "r") as file:

                data_list = json.load(file)

                for data in data_list:
                    student = Student.from_dict(data)
                    self.students[student.student_id] = student

        except FileNotFoundError:
            pass


# ================= MENU SYSTEM =================

def main_menu():

    manager = StudentManager()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.update_student()

        elif choice == "5":
            manager.delete_student()

        elif choice == "6":
            manager.save_data()
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()