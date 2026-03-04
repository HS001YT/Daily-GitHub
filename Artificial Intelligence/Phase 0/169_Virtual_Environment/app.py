# Work flow-

# cd project-folder
# python -m venv myenv                          to create a virtual environment
# myenv\Scripts\activate                activate it
# pip install requests                                  install required libraries (these can onlY BE ACCESSED in this virtual environemt)
# python your_script.py                 run your py file
# deactivate                                                turn off the virtual environment



import logging
import requests
import json
import os
from datetime import datetime


# ================= LOGGING SETUP =================

def setup_logger():
    logging.basicConfig(
        filename="error_log.txt",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


# ================= NETWORK CHECK =================

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error while accessing {url}: {e}")
        print("Failed to access website.")
        return None
    else:
        print(f"Website reachable. Status code: {response.status_code}")
        return response.status_code


# ================= FILE READER =================

def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        print("File not found.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        print("Invalid JSON format.")
        return None
    else:
        print("File loaded successfully.")
        return data


# ================= SAFE DIVISION =================

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Division by zero: {e}")
        print("Cannot divide by zero.")
        return None


# ================= SYSTEM INFO =================

def show_environment_info():
    print("\n--- Environment Info ---")
    print("Current Working Directory:", os.getcwd())
    print("Python Executable:", os.sys.executable)
    print("Current Time:", datetime.now())


# ================= MAIN MENU =================

def main():

    setup_logger()

    while True:
        print("\n====== DEBUG & ENVIRONMENT APP ======")
        print("1. Check Website")
        print("2. Read JSON File")
        print("3. Perform Safe Division")
        print("4. Show Environment Info")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            url = input("Enter website URL (with https://): ")
            check_website(url)

        elif choice == 2:
            filename = input("Enter JSON file name: ")
            read_json_file(filename)

        elif choice == 3:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = safe_division(a, b)
                if result is not None:
                    print("Result:", result)
            except ValueError:
                print("Invalid numeric input.")

        elif choice == 4:
            show_environment_info()

        elif choice == 5:
            print("Exiting safely...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()