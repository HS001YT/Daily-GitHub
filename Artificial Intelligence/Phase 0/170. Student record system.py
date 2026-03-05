# ================= BASE CLASS =================

class Person:
    def __init__(self, person_id, name, age):
        self._id = person_id
        self._name = name
        self._age = age

    def get_id(self):
        return self._id

    def display_basic_info(self):
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")


# ================= STUDENT CLASS =================

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

    # Method Overriding (Polymorphism)
    def display_info(self):
        self.display_basic_info()
        print(f"Course: {self._course}")
        print(f"Marks: {self._marks}")
        print(f"Grade: {self.calculate_grade()}")


# ================= EMPLOYEE CLASS =================

class Employee(Person):
    def __init__(self, person_id, name, age, department, salary):
        super().__init__(person_id, name, age)
        self._department = department
        self._salary = salary

    def annual_salary(self):
        return self._salary * 12

    # Method Overriding (Polymorphism)
    def display_info(self):
        self.display_basic_info()
        print(f"Department: {self._department}")
        print(f"Monthly Salary: {self._salary}")
        print(f"Annual Salary: {self.annual_salary()}")


# ================= RECORD MANAGER =================

class RecordManager:
    def __init__(self):
        self._records = {}  # In-memory storage

    def add_record(self, record):
        if record.get_id() in self._records:
            print("Record with this ID already exists.")
            return
        self._records[record.get_id()] = record
        print("Record added successfully.")

    def display_all(self):
        if not self._records:
            print("No records available.")
            return

        for record in self._records.values():
            print("\n------------------------")
            record.display_info()   # Polymorphism in action

    def search_record(self, record_id):
        record = self._records.get(record_id)
        if record:
            print("\nRecord Found:")
            record.display_info()
        else:
            print("Record not found.")

    def delete_record(self, record_id):
        if record_id in self._records:
            del self._records[record_id]
            print("Record deleted successfully.")
        else:
            print("Record not found.")


# ================= MAIN MENU =================

def main():
    manager = RecordManager()

    while True:
        print("\n====== RECORD SYSTEM (Day 170) ======")
        print("1. Add Student")
        print("2. Add Employee")
        print("3. Display All Records")
        print("4. Search Record")
        print("5. Delete Record")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            student = Student(sid, name, age, course, marks)
            manager.add_record(student)

        elif choice == 2:
            eid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            dept = input("Enter Department: ")
            salary = float(input("Enter Monthly Salary: "))

            employee = Employee(eid, name, age, dept, salary)
            manager.add_record(employee)

        elif choice == 3:
            manager.display_all()

        elif choice == 4:
            rid = input("Enter Record ID: ")
            manager.search_record(rid)

        elif choice == 5:
            rid = input("Enter Record ID: ")
            manager.delete_record(rid)

        elif choice == 6:
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()