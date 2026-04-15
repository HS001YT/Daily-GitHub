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


def normalize_column(df):
    try:
        col = input("Enter column to normalize: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        data = df[col]

        if not data.dtype.kind in "biufc":
            print("Column must be numeric.")
            return

        min_val = data.min()
        max_val = data.max()

        if max_val == min_val:
            print("Cannot normalize: max and min are equal.")
            return

        df[col + "_norm"] = (data - min_val) / (max_val - min_val)

        print("\nNormalized Column Added:\n", df[[col, col + "_norm"]].head())

    except Exception as e:
        print("Error:", e)


def normalize_multiple_columns(df):
    try:
        cols = input("Enter columns to normalize (space-separated): ").split()

        for col in cols:
            if col not in df.columns:
                print(f"Invalid column: {col}")
                return

            data = df[col]

            if not data.dtype.kind in "biufc":
                print(f"Column {col} must be numeric.")
                return

            min_val = data.min()
            max_val = data.max()

            if max_val == min_val:
                print(f"Skipping {col}: max = min.")
                continue

            df[col + "_norm"] = (data - min_val) / (max_val - min_val)

        print("\nNormalized Columns Added:\n", df.head())

    except Exception as e:
        print("Error:", e)


def show_dataset(df):
    print("\nCurrent Dataset:\n", df.head())


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== NORMALIZATION MENU =====")
        print("1. Normalize Single Column")
        print("2. Normalize Multiple Columns")
        print("3. Show Dataset")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            normalize_column(df)
        elif choice == "2":
            normalize_multiple_columns(df)
        elif choice == "3":
            show_dataset(df)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()