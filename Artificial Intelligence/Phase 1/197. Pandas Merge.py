def load_dataframe(prompt_msg):
    import pandas as pd
    try:
        file = input(prompt_msg).strip()
        df = pd.read_csv(file)
        print("\nLoaded Data:\n", df.head())
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def merge_dataframes(df1, df2):
    try:
        print("\n--- MERGE OPERATION ---")
        key = input("Enter common column name: ").strip()

        if key not in df1.columns or key not in df2.columns:
            print("Column not found in both DataFrames.")
            return

        print("Merge Types: inner / left / right / outer")
        how_type = input("Enter merge type: ").strip().lower()

        if how_type not in ["inner", "left", "right", "outer"]:
            print("Invalid merge type.")
            return

        import pandas as pd
        merged = pd.merge(df1, df2, on=key, how=how_type)

        print("\nMerged DataFrame:\n", merged.head())

    except Exception as e:
        print("Error:", e)


def join_dataframes(df1, df2):
    try:
        print("\n--- JOIN OPERATION ---")
        print("Join Types: left / right / outer / inner")
        how_type = input("Enter join type: ").strip().lower()

        if how_type not in ["left", "right", "outer", "inner"]:
            print("Invalid join type.")
            return

        # Setting index for join
        key = input("Enter column to set as index: ").strip()

        if key not in df1.columns or key not in df2.columns:
            print("Column not found in both DataFrames.")
            return

        df1_indexed = df1.set_index(key)
        df2_indexed = df2.set_index(key)

        joined = df1_indexed.join(df2_indexed, how=how_type, lsuffix='_left', rsuffix='_right')

        print("\nJoined DataFrame:\n", joined.head())

    except Exception as e:
        print("Error:", e)


def concat_dataframes(df1, df2):
    try:
        print("\n--- CONCAT OPERATION ---")
        print("Axis: 0 (rows) / 1 (columns)")
        axis = int(input("Enter axis: "))

        if axis not in [0, 1]:
            print("Invalid axis.")
            return

        import pandas as pd
        concatenated = pd.concat([df1, df2], axis=axis)

        print("\nConcatenated DataFrame:\n", concatenated.head())

    except Exception as e:
        print("Error:", e)


def main_menu():
    df1 = load_dataframe("Enter first CSV file path: ")
    if df1 is None:
        return

    df2 = load_dataframe("Enter second CSV file path: ")
    if df2 is None:
        return

    while True:
        print("\n===== DATA COMBINATION MENU =====")
        print("1. Merge DataFrames")
        print("2. Join DataFrames")
        print("3. Concat DataFrames")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            merge_dataframes(df1, df2)
        elif choice == "2":
            join_dataframes(df1, df2)
        elif choice == "3":
            concat_dataframes(df1, df2)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()