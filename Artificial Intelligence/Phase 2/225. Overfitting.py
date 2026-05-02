def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/students_large.csv): ").strip()
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


def train_and_evaluate(df, label):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error

        X = df[["Hours"]]
        y = df["Marks"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)

        train_error = mean_squared_error(y_train, train_pred)
        test_error = mean_squared_error(y_test, test_pred)

        print(f"\n--- {label} ---")
        print(f"Training Error (MSE): {round(train_error,2)}")
        print(f"Testing Error (MSE): {round(test_error,2)}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== OVERFITTING MENU =====")
        print("1. Test Small Dataset")
        print("2. Test Full Dataset")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            small_df = df.head(5)  # small data
            train_and_evaluate(small_df, "Small Dataset")
        elif choice == "2":
            train_and_evaluate(df, "Full Dataset")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()