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


def standardize_column(df):
    try:
        import numpy as np

        col = input("Enter column to standardize: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        data = df[col]

        if not data.dtype.kind in "biufc":
            print("Column must be numeric.")
            return

        mean = data.mean()
        std = data.std()

        if std == 0:
            print("Cannot standardize: standard deviation is zero.")
            return

        df[col + "_zscore"] = (data - mean) / std

        print("\nStandardized Column Added:\n", df[[col, col + "_zscore"]].head())

    except Exception as e:
        print("Error:", e)


def standardize_multiple_columns(df):
    try:
        cols = input("Enter columns to standardize (space-separated): ").split()

        for col in cols:
            if col not in df.columns:
                print(f"Invalid column: {col}")
                return

            data = df[col]

            if not data.dtype.kind in "biufc":
                print(f"Column {col} must be numeric.")
                return

            mean = data.mean()
            std = data.std()

            if std == 0:
                print(f"Skipping {col}: std = 0.")
                continue

            df[col + "_zscore"] = (data - mean) / std

        print("\nStandardized Columns Added:\n", df.head())

    except Exception as e:
        print("Error:", e)


def show_dataset(df):
    print("\nCurrent Dataset:\n", df.head())


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== STANDARDIZATION MENU =====")
        print("1. Standardize Single Column")
        print("2. Standardize Multiple Columns")
        print("3. Show Dataset")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            standardize_column(df)
        elif choice == "2":
            standardize_multiple_columns(df)
        elif choice == "3":
            show_dataset(df)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()