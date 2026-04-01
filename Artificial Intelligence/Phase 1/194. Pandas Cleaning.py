def load_dataframe():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        return pd.read_csv(file)
    except:
        print("Error loading file.")
        return None


def show_missing(df):
    print("\nMissing Values:\n", df.isnull().sum())


def drop_missing(df):
    try:
        new_df = df.dropna()
        print("\nAfter dropna():\n", new_df)
    except Exception as e:
        print("Error:", e)


def fill_missing(df):
    try:
        col = input("Enter column to fill: ")
        value = input("Enter value to fill: ")

        if col not in df.columns:
            print("Invalid column.")
            return

        df[col] = df[col].fillna(value)
        print("\nAfter fillna():\n", df)

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataframe()
    if df is None:
        return

    while True:
        print("\n===== DATA CLEANING MENU =====")
        print("1. Show Missing Data")
        print("2. Drop Missing Data")
        print("3. Fill Missing Data")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_missing(df)
        elif choice == "2":
            drop_missing(df)
        elif choice == "3":
            fill_missing(df)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()