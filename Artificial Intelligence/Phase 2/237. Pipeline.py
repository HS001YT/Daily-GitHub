def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/ml_pipeline.csv): ").strip()

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


def train_pipeline(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score

        X = df[["Hours", "Attendance"]]
        y = df["Pass"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", MinMaxScaler()),
            ("model", LogisticRegression())
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\nPipeline Trained Successfully.")
        print(f"Accuracy: {round(accuracy, 3)}")

        print("\n--- Actual vs Predicted ---")
        print("Actual | Predicted")

        for actual, pred in zip(y_test, predictions):
            print(f"{actual} | {pred}")

        return pipeline

    except Exception as e:
        print("Error:", e)
        return None


def predict_custom(pipeline):
    try:
        import pandas as pd

        if pipeline is None:
            print("Train pipeline first.")
            return

        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance: "))

        custom_df = pd.DataFrame(
            [[hours, attendance]],
            columns=["Hours", "Attendance"]
        )

        prediction = pipeline.predict(custom_df)

        print(f"\nPredicted Class (Pass=1 / Fail=0): {prediction[0]}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    pipeline = None

    while True:
        print("\n===== FULL ML PIPELINE MENU =====")
        print("1. Train Pipeline")
        print("2. Predict Custom Input")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            pipeline = train_pipeline(df)

        elif choice == "2":
            predict_custom(pipeline)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()