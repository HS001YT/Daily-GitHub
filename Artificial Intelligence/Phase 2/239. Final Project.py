def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/final_ml_project.csv): "
        ).strip()

        base_dir = os.path.dirname(os.path.abspath(__file__))

        full_path = os.path.join(base_dir, file)

        df = pd.read_csv(full_path)

        print("\nDataset Loaded Successfully.\n")

        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def show_dataset_info(df):
    try:
        print("\n===== DATASET INFO =====")

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def train_model(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.linear_model import LogisticRegression

        X = df[["Hours", "Attendance", "Assignment"]]
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

        print("\nModel Trained Successfully.")

        return pipeline, X_test, y_test

    except Exception as e:
        print("Error:", e)
        return None, None, None


def evaluate_model(model, X_test, y_test):
    try:
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import confusion_matrix

        if model is None:
            print("Train model first.")
            return

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        cm = confusion_matrix(y_test, predictions)

        print("\n===== MODEL EVALUATION =====")

        print(f"Accuracy: {round(accuracy, 3)}")

        print("\nConfusion Matrix:")
        print(cm)

        print("\nActual | Predicted")

        for actual, pred in zip(y_test, predictions):
            print(f"{actual} | {pred}")

    except Exception as e:
        print("Error:", e)


def predict_student(model):
    try:
        import pandas as pd

        if model is None:
            print("Train model first.")
            return

        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance: "))
        assignment = float(input("Enter assignment score: "))

        custom_df = pd.DataFrame(
            [[hours, attendance, assignment]],
            columns=["Hours", "Attendance", "Assignment"]
        )

        prediction = model.predict(custom_df)[0]

        probability = model.predict_proba(custom_df)[0]

        print("\n===== PREDICTION RESULT =====")

        if prediction == 1:
            print("Prediction: PASS")
        else:
            print("Prediction: FAIL")

        print(f"Pass Probability: {round(probability[1], 3)}")
        print(f"Fail Probability: {round(probability[0], 3)}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    model = None
    X_test = None
    y_test = None

    while True:
        print("\n===== FINAL ML PROJECT MENU =====")
        print("1. View Dataset Info")
        print("2. Train Model")
        print("3. Evaluate Model")
        print("4. Predict Student Result")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_dataset_info(df)

        elif choice == "2":
            model, X_test, y_test = train_model(df)

        elif choice == "3":
            evaluate_model(model, X_test, y_test)

        elif choice == "4":
            predict_student(model)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()