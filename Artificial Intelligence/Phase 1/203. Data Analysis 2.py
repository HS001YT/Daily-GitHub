def load_dataset():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nDataset Loaded:\n", df.head())
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def create_arithmetic_feature(df):
    try:
        print("\n--- Arithmetic Feature ---")
        col1 = input("Enter first column: ")
        col2 = input("Enter second column: ")
        new_col = input("Enter new column name: ")

        if col1 not in df.columns or col2 not in df.columns:
            print("Invalid column name.")
            return

        df[new_col] = df[col1] + df[col2]
        print("\nUpdated Data:\n", df.head())

    except Exception as e:
        print("Error:", e)


def create_percentage(df):
    try:
        print("\n--- Percentage Feature ---")
        marks_col = input("Enter marks column: ")
        total_col = input("Enter total marks column: ")

        if marks_col not in df.columns or total_col not in df.columns:
            print("Invalid column name.")
            return

        df["Percentage"] = (df[marks_col] / df[total_col]) * 100
        print("\nUpdated Data:\n", df.head())

    except Exception as e:
        print("Error:", e)


def create_grade(df):
    try:
        print("\n--- Grade Feature ---")
        col = input("Enter column for grading: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        def grade(x):
            try:
                if x >= 90:
                    return "A"
                elif x >= 75:
                    return "B"
                elif x >= 50:
                    return "C"
                else:
                    return "Fail"
            except:
                return "Invalid"

        df["Grade"] = df[col].apply(grade)
        print("\nUpdated Data:\n", df.head())

    except Exception as e:
        print("Error:", e)


def create_pass_fail(df):
    try:
        print("\n--- Pass/Fail Feature ---")
        col = input("Enter column: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        df["Pass"] = df[col].apply(lambda x: "Yes" if x >= 50 else "No")
        print("\nUpdated Data:\n", df.head())

    except Exception as e:
        print("Error:", e)


def show_dataset(df):
    print("\nCurrent Dataset:\n", df)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== FEATURE CREATION MENU =====")
        print("1. Arithmetic Feature")
        print("2. Percentage Feature")
        print("3. Grade Feature")
        print("4. Pass/Fail Feature")
        print("5. Show Dataset")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_arithmetic_feature(df)
        elif choice == "2":
            create_percentage(df)
        elif choice == "3":
            create_grade(df)
        elif choice == "4":
            create_pass_fail(df)
        elif choice == "5":
            show_dataset(df)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()