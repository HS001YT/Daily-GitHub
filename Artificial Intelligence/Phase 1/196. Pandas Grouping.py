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


def groupby_single(df):
    try:
        print("\n--- GroupBy (Single Column) ---")
        col = input("Enter column to group by: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        grouped = df.groupby(col).mean(numeric_only=True)
        print("\nGrouped Data (Mean):\n", grouped)

    except Exception as e:
        print("Error:", e)


def groupby_multiple(df):
    try:
        print("\n--- GroupBy (Multiple Columns) ---")
        cols = input("Enter columns to group by (space-separated): ").split()

        for c in cols:
            if c not in df.columns:
                print(f"Invalid column: {c}")
                return

        grouped = df.groupby(cols).sum(numeric_only=True)
        print("\nGrouped Data (Sum):\n", grouped)

    except Exception as e:
        print("Error:", e)


def custom_aggregation(df):
    try:
        print("\n--- Custom Aggregation ---")
        group_col = input("Enter column to group by: ")
        target_col = input("Enter column to aggregate: ")

        if group_col not in df.columns or target_col not in df.columns:
            print("Invalid column.")
            return

        grouped = df.groupby(group_col)[target_col].agg(["sum", "mean", "min", "max"])
        print("\nCustom Aggregation:\n", grouped)

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataframe()
    if df is None:
        return

    while True:
        print("\n===== GROUPBY MENU =====")
        print("1. GroupBy Single Column (Mean)")
        print("2. GroupBy Multiple Columns (Sum)")
        print("3. Custom Aggregation")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            groupby_single(df)
        elif choice == "2":
            groupby_multiple(df)
        elif choice == "3":
            custom_aggregation(df)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()