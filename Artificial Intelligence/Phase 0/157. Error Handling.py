# 🔹 Task 1 – Handle Division Errors
# Requirement:
# Take two numbers from user
# Divide them
# Handle:
# Division by zero
# Invalid numeric input

def div_by_zero():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = a/ b
        print("a/ b =", c)
    except ZeroDivisionError:
        print("Denomenator is zero.")
    except ValueError:
        print("Enter numbers only.")



# 🔹 Task 2 – Handle File Not Found
# Requirement:
# Ask user for file name
# Try to open it
# Handle file-not-found error

def open_file():
    import os

    file_name = input("Enter file name with extension: ")
    if not (file_name.endswith(".txt") or file_name.endswith(".csv")):
        print("Only text or csv file.")
        return
    
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "other_files")
    files = os.listdir(file_path)
    print("Looking inside:", file_path)


    file_address = os.path.join(file_path, file_name)

    try:
        with open(file_address, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Files in the directory: {", end="")
        print(", ".join(os.listdir(file_path)), end="")
        print("}")

        print("No %s file in the directory." % {file_name})

    finally:
        print("Execution Completed")
            
def main_menu():
    choice = int(input("""Enter your choice: 
    1. Divide two numbers.
    2. Read a file.
    3. Exit.\n:-> """))

    if (choice == 1):
        div_by_zero()
    elif (choice == 2):
        open_file()
    elif (choice == 3):
        exit()
    else:
        print('Invalid Choice')

main_menu()