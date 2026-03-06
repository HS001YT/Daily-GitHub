import json
import os

# ================= BASE CLASS =================

class Person:
    def __init__(self, person_id, name, age):
        self._id = person_id
        self._name = name
        self._age = age

    def get_id(self):
        return self._id

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "age": self._age
        }

    def display_basic_info(self):
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")


# ================= STUDENT =================

class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)
        self._course = course
        self._marks = marks

    def calculate_grade(self):
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        elif self._marks >= 60:
            return "C"
        else:
            return "D"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Student",
            "course": self._course,
            "marks": self._marks
        })
        return data

    def display_info(self):
        self.display_basic_info()
        print(f"Course: {self._course}")
        print(f"Marks: {self._marks}")
        print(f"Grade: {self.calculate_grade()}")


# ================= EMPLOYEE =================

class Employee(Person):
    def __init__(self, person_id, name, age, department, salary):
        super().__init__(person_id, name, age)
        self._department = department
        self._salary = salary

    def annual_salary(self):
        return self._salary * 12

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Employee",
            "department": self._department,
            "salary": self._salary
        })
        return data

    def display_info(self):
        self.display_basic_info()
        print(f"Department: {self._department}")
        print(f"Monthly Salary: {self._salary}")
        print(f"Annual Salary: {self.annual_salary()}")


# ================= RECORD MANAGER =================

class RecordManager:
    def __init__(self):
        # Get current file directory
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Build path to other_files/records.json
        self._filename = os.path.join(base_dir, "other_files", "171.json")

        self._records = {}
        self.load_from_file()

    def add_record(self, record):
        if record.get_id() in self._records:
            print("Record already exists.")
            return
        self._records[record.get_id()] = record
        print("Record added.")

    def display_all(self):
        if not self._records:
            print("No records available.")
            return
        for record in self._records.values():
            print("\n--------------------")
            record.display_info()

    def search_record(self, record_id):
        record = self._records.get(record_id)
        if record:
            record.display_info()
        else:
            print("Record not found.")

    def delete_record(self, record_id):
        if record_id in self._records:
            del self._records[record_id]
            print("Record deleted.")
        else:
            print("Record not found.")

    # ================= FILE STORAGE =================

    def save_to_file(self):
        data = [record.to_dict() for record in self._records.values()]
        with open(self._filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Records saved to file.")

    def load_from_file(self):
        try:
            with open(self._filename, "r") as file:
                data_list = json.load(file)

            for item in data_list:
                if item["type"] == "Student":
                    obj = Student(
                        item["id"],
                        item["name"],
                        item["age"],
                        item["course"],
                        item["marks"]
                    )
                elif item["type"] == "Employee":
                    obj = Employee(
                        item["id"],
                        item["name"],
                        item["age"],
                        item["department"],
                        item["salary"]
                    )
                self._records[obj.get_id()] = obj

        except FileNotFoundError:
            pass  # First run — file does not exist


# ================= MAIN MENU =================

def main():
    manager = RecordManager()

    while True:
        print("\n====== RECORD SYSTEM (Day 171) ======")
        print("1. Add Student")
        print("2. Add Employee")
        print("3. Display All")
        print("4. Search Record")
        print("5. Delete Record")
        print("6. Save & Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            sid = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            marks = float(input("Marks: "))
            manager.add_record(Student(sid, name, age, course, marks))

        elif choice == 2:
            eid = input("Employee ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = float(input("Salary: "))
            manager.add_record(Employee(eid, name, age, dept, salary))

        elif choice == 3:
            manager.display_all()

        elif choice == 4:
            rid = input("Enter ID: ")
            manager.search_record(rid)

        elif choice == 5:
            rid = input("Enter ID: ")
            manager.delete_record(rid)

        elif choice == 6:
            manager.save_to_file()
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()