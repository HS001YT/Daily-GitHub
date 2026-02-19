# ✅ Combined Task – Student Record Management System
# 🔹 Objective
# Create a Student Record System using:
# OOP
# Lists
# Dictionaries
# String operations
# File handling

# 🔹 Part 1 – Class Design (OOP)
# Create a class named Student.
# Constructor should take:
# name
# roll_number
# marks (list of 3 subjects)
# Store them as instance variables.
# Add Methods:
# 1️⃣ calculate_total()
# Return total marks
# 2️⃣ calculate_average()
# Return average
# 3️⃣ get_grade()
# Average ≥ 75 → Grade A
# Average ≥ 50 → Grade B
# Else → Grade C
# 4️⃣ to_dict()
# Return student data in dictionary format

# 🔹 Part 2 – Data Storage (Lists + Dict)
# Maintain a list to store multiple Student objects
# Convert each object to dictionary using to_dict()
# Store all dictionaries in a list

# 🔹 Part 3 – String Operations
# Name should be formatted properly (capitalize)
# Remove extra spaces
# Display formatted output

# 🔹 Part 4– File Handling
# Save Data:
# Store all student records in a .txt file
# Each student in one line
# Retrieve Data:
# Read the file
# Display all student records properly

# 🔹 Part 5 – Search Feature (Dict Practice)
# Ask user for roll number
# Search student from stored records
# Print full details

# 🔥 Rules
# No global variables
# Use at least one loop
# Use at least one dictionary
# Use at least one list
# Proper class structure
# Handle file-not-found error

class Student:
    def __init__(self, name, roll_number, marks):
        # String Operations
        self.name = name.strip().title()   # remove extra spaces + capitalize
        self.roll_number = roll_number
        self.marks = [int(i) for i in marks.split()]

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 75:
            return "Grade A"
        elif avg >= 50:
            return "Grade B"
        else:
            return "Grade C"

    def to_dict(self):
        return {
            "Name": self.name,
            "Roll No": self.roll_number,
            "Marks": self.marks,
            "Total": self.calculate_total(),
            "Average": round(self.calculate_average(), 2),
            "Grade": self.get_grade()
        }


def main():
    students_objects = []   # list of objects
    students_records = []   # list of dictionaries

    n = int(input("Enter number of students: "))

    for i in range(1, n + 1):
        name = input(f"\nEnter Student name[{i}]: ")
        roll_number = int(input("Enter roll number: "))
        marks = input("Enter marks (space separated, 3 subjects): ")

        student = Student(name, roll_number, marks)
        students_objects.append(student)
        students_records.append(student.to_dict())

    # Display formatted output
    print("\n===== Student Records =====")
    for record in students_records:
        print(f"""
Name       : {record['Name']}
Roll No    : {record['Roll No']}
Marks      : {record['Marks']}
Total      : {record['Total']}
Average    : {record['Average']}
Grade      : {record['Grade']}
-----------------------------
""")

    # 🔹 Save to file
    try:
        with open("students.txt", "w") as file:
            for record in students_records:
                line = f"{record['Name']},{record['Roll No']},{record['Marks']},{record['Total']},{record['Average']},{record['Grade']}\n"
                file.write(line)
        print("Data saved to students.txt successfully.")
    except Exception as e:
        print("Error while writing file:", e)

    # 🔹 Read from file
    try:
        print("\n===== Reading From File =====")
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")

    # 🔹 Search Feature
    search_roll = int(input("\nEnter roll number to search: "))
    found = False

    for record in students_records:
        if record["Roll No"] == search_roll:
            print("\nStudent Found:")
            print(record)
            found = True
            break

    if not found:
        print("Student not found.")


if __name__ == "__main__":
    main()
