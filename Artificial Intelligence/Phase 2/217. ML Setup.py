def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/students.csv): ").strip()

        # Get current script directory
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Create full path
        full_path = os.path.join(base_dir, file)

        df = pd.read_csv(full_path)
        print("\nDataset Loaded Successfully.\n")
        return df

    except FileNotFoundError:
        print("File not found. Check the path.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def show_head_tail(df):
    try:
        print("\n--- First 5 Rows ---")
        print(df.head())
        print("\n--- Last 5 Rows ---")
        print(df.tail())
    except Exception as e:
        print("Error:", e)


def show_structure(df):
    try:
        print("\nShape:", df.shape)
        print("\nColumns:", df.columns.tolist())
        print("\nData Types:\n", df.dtypes)
    except Exception as e:
        print("Error:", e)


def dataset_info(df):
    try:
        print("\n--- Dataset Info ---")
        print(df.info())
    except Exception as e:
        print("Error:", e)


def statistical_summary(df):
    try:
        print("\n--- Statistical Summary ---")
        print(df.describe())
    except Exception as e:
        print("Error:", e)


def select_columns(df):
    try:
        col = input("Enter column name: ").strip()
        if col in df.columns:
            print("\nSelected Column:\n", df[col])
        else:
            print("Invalid column name.")

        cols = input("\nEnter multiple columns (space-separated): ").split()
        if all(c in df.columns for c in cols):
            print("\nSelected Columns:\n", df[cols])
        else:
            print("One or more invalid column names.")

    except Exception as e:
        print("Error:", e)


def check_missing(df):
    try:
        print("\nMissing Values:\n", df.isnull().sum())
    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== DATASET MENU =====")
        print("1. Show Head & Tail")
        print("2. Show Structure")
        print("3. Dataset Info")
        print("4. Statistical Summary")
        print("5. Select Columns")
        print("6. Check Missing Values")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_head_tail(df)
        elif choice == "2":
            show_structure(df)
        elif choice == "3":
            dataset_info(df)
        elif choice == "4":
            statistical_summary(df)
        elif choice == "5":
            select_columns(df)
        elif choice == "6":
            check_missing(df)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()