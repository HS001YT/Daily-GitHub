def load_dataframe():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        return pd.read_csv(file)
    except:
        print("Error loading file.")
        return None


def using_loc(df):
    try:
        print("\nUsing loc (label-based)")
        row = int(input("Enter row index: "))
        col = input("Enter column name: ")
        print(df.loc[row, col])
    except Exception as e:
        print("Error:", e)


def using_iloc(df):
    try:
        print("\nUsing iloc (position-based)")
        row = int(input("Enter row position: "))
        col = int(input("Enter column position: "))
        print(df.iloc[row, col])
    except Exception as e:
        print("Error:", e)


def filtering(df):
    try:
        col = input("Enter column for filtering: ")
        val = float(input("Enter threshold value: "))

        filtered = df[df[col] > val]
        print("\nFiltered Data:\n", filtered)

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataframe()
    if df is None:
        return

    while True:
        print("\n===== INDEXING MENU =====")
        print("1. Using loc")
        print("2. Using iloc")
        print("3. Filtering")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            using_loc(df)
        elif choice == "2":
            using_iloc(df)
        elif choice == "3":
            filtering(df)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()