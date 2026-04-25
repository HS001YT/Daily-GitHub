def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/students_ml.csv): ").strip()

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


def split_data(df):
    try:
        from sklearn.model_selection import train_test_split

        # Features and Target
        X = df[["Hours", "Marks"]]
        y = df["Pass"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        print("\n--- TRAIN DATA ---")
        print("X_train:\n", X_train)
        print("y_train:\n", y_train)

        print("\n--- TEST DATA ---")
        print("X_test:\n", X_test)
        print("y_test:\n", y_test)

        print("\n--- SHAPES ---")
        print("X_train:", X_train.shape)
        print("X_test:", X_test.shape)
        print("y_train:", y_train.shape)
        print("y_test:", y_test.shape)

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== TRAIN-TEST SPLIT MENU =====")
        print("1. Perform Train-Test Split")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            split_data(df)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()