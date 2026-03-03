import os
import csv

def get_base_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "other_files")

def show_files():
    file_path = get_base_path()

    if not os.path.exists(file_path):
        print("Folder does not exist.")
        return

    files = os.listdir(file_path)

    for file in files:
        if file.endswith(".txt"):
            print(file)

def get_file(create=False):
    file_name = input("Enter the file name with extension: ")

    if not file_name.endswith(".txt"):
        print("Only .txt files are allowed.")
        return None

    file_address = os.path.join(get_base_path(), file_name)

    if not create and not os.path.exists(file_address):
        print("File does not exist in directory.")
        return None

    return file_address

def read_file(file_name):
    while True:
        choice = int(input("""Read options:
    1. Read full content
    2. Read one line
    3. Read all lines as list
    4. Back
 :-> """))

        if choice == 4:
            break

        with open(file_name, "r") as file:
            if choice == 1:
                print(file.read())
            elif choice == 2:
                print(file.readline())
            elif choice == 3:
                for line in file.readlines():
                    print(line.strip())
            else:
                print("Invalid choice")

def write_file(file_name):
    while True:
        choice = int(input("""Write options:
    1. Overwrite single line
    2. Overwrite multiple lines
    3. Append multiple lines
    4. Back
 :-> """))

        if choice == 4:
            break

        elif choice == 1:
            sentence = input("Enter the line: ")
            with open(file_name, "w") as file:
                file.write(sentence + "\n")

        elif choice == 2:
            with open(file_name, "w") as file:
                print("Enter lines (type STOP to finish):")
                while True:
                    line = input(":-> ")
                    if line == "STOP":
                        break
                    file.write(line + "\n")

        elif choice == 3:
            with open(file_name, "a") as file:
                print("Enter lines to append (type STOP to finish):")
                while True:
                    line = input(":-> ")
                    if line == "STOP":
                        break
                    file.write(line + "\n")

        else:
            print("Invalid choice")

def rename_file():
    old_file = get_file()
    if not old_file:
        return

    new_name = input("Enter new file name with extension: ")

    if not new_name.endswith(".txt"):
        print("Only .txt files allowed.")
        return

    new_path = os.path.join(get_base_path(), new_name)

    os.rename(old_file, new_path)
    print("File renamed successfully.")

def delete_file():
    file_name = get_file()
    if not file_name:
        return

    confirm = input("Are you sure you want to delete? (yes/no): ")

    if confirm.lower() == "yes":
        os.remove(file_name)
        print("File deleted successfully.")
    else:
        print("Deletion cancelled.")

def txt_file():
    while True:
        choice = int(input("""\nText File Menu:
    1. Show all files
    2. Read file
    3. Create/Write file
    4. Rename file
    5. Delete file
    6. Back
 :-> """))

        if choice == 1:
            show_files()

        elif choice == 2:
            file_name = get_file()
            if file_name:
                read_file(file_name)

        elif choice == 3:
            file_name = get_file(create=True)
            if file_name:
                write_file(file_name)

        elif choice == 4:
            rename_file()

        elif choice == 5:
            delete_file()

        elif choice == 6:
            break

        else:
            print("Invalid choice")




def show_csv_files():
    path = get_base_path()

    files = os.listdir(path)

    for file in files:
        if file.endswith(".csv"):
            print(file)

def get_csv_file(create=False):
    file_name = input("Enter CSV file name with extension: ")

    if not file_name.endswith(".csv"):
        print("Only .csv files allowed.")
        return None

    file_path = os.path.join(get_base_path(), file_name)

    if not create and not os.path.exists(file_path):
        print("File does not exist.")
        return None

    return file_path

def read_csv(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

def calculate_total(file_name):
    column_name = input("Enter column name to calculate total: ")

    total = 0

    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                total += float(row[column_name])
            except:
                pass

    print("Total =", total)

def append_row(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader)

    print("Enter values for each column:")
    row_data = []

    for header in headers:
        value = input(f"{header}: ")
        row_data.append(value)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row_data)

    print("Row added successfully.")

def create_csv(file_name):
    headers = input("Enter column names separated by comma: ")
    headers = headers.split(",")

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

    print("CSV file created successfully.")

def csv_file():
    while True:
        choice = int(input("""\nCSV Menu:
    1. Show CSV files
    2. Read CSV file
    3. Calculate total of numeric column
    4. Append new row
    5. Create new CSV
    6. Back
 :-> """))

        if choice == 1:
            show_csv_files()

        elif choice == 2:
            file_name = get_csv_file()
            if file_name:
                read_csv(file_name)

        elif choice == 3:
            file_name = get_csv_file()
            if file_name:
                calculate_total(file_name)

        elif choice == 4:
            file_name = get_csv_file()
            if file_name:
                append_row(file_name)

        elif choice == 5:
            file_name = get_csv_file(create=True)
            if file_name:
                create_csv(file_name)

        elif choice == 6:
            break

        else:
            print("Invalid choice.")

def main_menu():
    while True:
        choice = int(input("""\nMain Menu:
    1. Text file operations
    2. CSV file operations
    3. Exit
 :-> """))

        if choice == 1:
            txt_file()
        elif choice == 2:
            csv_file()
        elif choice == 3:
            break
        else:
            print("Invalid Input.")

main_menu()