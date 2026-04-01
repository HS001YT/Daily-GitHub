def load_dataframe():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nData Loaded Successfully:\n", df.head())
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def create_new_column(df):
    try:
        print("\n--- Create New Column ---")
        col1 = input("Enter first column name: ")
        col2 = input("Enter second column name: ")
        new_col = input("Enter new column name: ")

        if col1 not in df.columns or col2 not in df.columns:
            print("Invalid column name.")
            return

        df[new_col] = df[col1] + df[col2]
        print("\nNew column added:\n", df.head())

    except Exception as e:
        print("Error:", e)


def apply_function(df):
    try:
        print("\n--- Apply Function ---")
        col = input("Enter column name: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        def grade(x):
            if x >= 90:
                return "A"
            elif x >= 75:
                return "B"
            elif x >= 50:
                return "C"
            else:
                return "Fail"

        df["Grade"] = df[col].apply(grade)
        print("\nAfter applying function:\n", df.head())

    except Exception as e:
        print("Error:", e)


def show_dataframe(df):
    print("\nCurrent DataFrame:\n", df)


def main_menu():
    df = load_dataframe()
    if df is None:
        return

    while True:
        print("\n===== COLUMN OPERATIONS MENU =====")
        print("1. Create New Column")
        print("2. Apply Function (Grade)")
        print("3. Show DataFrame")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_new_column(df)
        elif choice == "2":
            apply_function(df)
        elif choice == "3":
            show_dataframe(df)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()