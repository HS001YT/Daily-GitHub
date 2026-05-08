def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/knn_students.csv): ").strip()

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


def tune_knn(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score

        X = df[["Hours", "Attendance"]]
        y = df["Pass"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42
        )

        best_k = None
        best_accuracy = 0

        print("\n===== K VALUE COMPARISON =====")

        for k in [1, 3, 5, 7]:

            model = KNeighborsClassifier(n_neighbors=k)

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)

            print(f"\nK = {k}")
            print("Actual | Predicted")

            for actual, pred in zip(y_test, predictions):
                print(f"{actual} | {pred}")

            print(f"Accuracy: {round(accuracy, 3)}")

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k

        print("\n===== BEST RESULT =====")
        print(f"Best K Value: {best_k}")
        print(f"Best Accuracy: {round(best_accuracy, 3)}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    while True:
        print("\n===== KNN TUNING MENU =====")
        print("1. Run KNN Tuning")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            tune_knn(df)

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()