def create_from_list():
    import pandas as pd
    try:
        n = int(input("Enter number of records: "))
        data = []

        for i in range(n):
            row = input(f"Enter values for row {i+1} (name age marks): ").split()
            if len(row) != 3:
                print("Invalid input. Enter exactly 3 values.")
                return
            name, age, marks = row
            data.append([name, int(age), float(marks)])

        df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
        print("\nDataFrame from List:\n", df)

    except ValueError:
        print("Invalid input.")


def create_from_dict():
    import pandas as pd
    try:
        names = input("Enter names: ").split()
        ages = list(map(int, input("Enter ages: ").split()))
        marks = list(map(float, input("Enter marks: ").split()))

        if not (len(names) == len(ages) == len(marks)):
            print("All lists must be of same length.")
            return

        data = {
            "Name": names,
            "Age": ages,
            "Marks": marks
        }

        df = pd.DataFrame(data)
        print("\nDataFrame from Dictionary:\n", df)

    except ValueError:
        print("Invalid input.")


def create_from_csv():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nDataFrame from CSV:\n", df.head())

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


def main_menu():
    while True:
        print("\n===== DATAFRAME CREATION MENU =====")
        print("1. From List")
        print("2. From Dictionary")
        print("3. From CSV")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_from_list()
        elif choice == "2":
            create_from_dict()
        elif choice == "3":
            create_from_csv()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()