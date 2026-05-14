def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/scaling_data.csv): ").strip()

        base_dir = os.path.dirname(os.path.abspath(__file__))
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


def normalize_data(df):
    try:
        import pandas as pd
        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler()

        scaled_values = scaler.fit_transform(df)

        scaled_df = pd.DataFrame(
            scaled_values,
            columns=df.columns
        )

        print("\n--- Original Dataset ---")
        print(df)

        print("\n--- Normalized Dataset ---")
        print(scaled_df)

        return scaler

    except Exception as e:
        print("Error:", e)
        return None


def normalize_custom_input(scaler):
    try:
        import pandas as pd

        if scaler is None:
            print("Normalize dataset first.")
            return

        hours = float(input("Enter Hours: "))
        attendance = float(input("Enter Attendance: "))
        marks = float(input("Enter Marks: "))

        custom_df = pd.DataFrame(
            [[hours, attendance, marks]],
            columns=["Hours", "Attendance", "Marks"]
        )

        scaled = scaler.transform(custom_df)

        print("\n--- Normalized Custom Input ---")
        print(scaled)

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    scaler = None

    while True:
        print("\n===== NORMALIZATION MENU =====")
        print("1. Normalize Dataset")
        print("2. Normalize Custom Input")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            scaler = normalize_data(df)

        elif choice == "2":
            normalize_custom_input(scaler)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()