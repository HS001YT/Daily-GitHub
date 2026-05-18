def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/train.csv): "
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

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def train_model(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.compose import ColumnTransformer
        from sklearn.pipeline import Pipeline
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import confusion_matrix

        features = [
            "Pclass",
            "Sex",
            "Age",
            "Fare",
            "Embarked"
        ]

        target = "Survived"

        X = df[features]
        y = df[target]

        numerical_cols = [
            "Age",
            "Fare"
        ]

        categorical_cols = [
            "Sex",
            "Embarked"
        ]

        numerical_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="mean")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ])

        categorical_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore")
            )
        ])

        preprocessor = ColumnTransformer([
            (
                "num",
                numerical_pipeline,
                numerical_cols
            ),
            (
                "cat",
                categorical_pipeline,
                categorical_cols
            )
        ],
        remainder="passthrough")

        model_pipeline = Pipeline([
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                LogisticRegression()
            )
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model_pipeline.fit(X_train, y_train)

        predictions = model_pipeline.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        print("\nModel Trained Successfully.")

        print(f"\nAccuracy: {round(accuracy, 3)}")

        print("\nConfusion Matrix:")
        print(cm)

        return model_pipeline

    except Exception as e:
        print("Error:", e)
        return None


def predict_custom(model):
    try:
        import pandas as pd

        if model is None:
            print("Train model first.")
            return

        pclass = int(input("Enter passenger class: "))
        sex = input("Enter sex (male/female): ").strip().lower()
        age = float(input("Enter age: "))
        fare = float(input("Enter fare: "))
        embarked = input("Enter embarked port (C/Q/S): ").strip().upper()

        custom_df = pd.DataFrame([
            {
                "Pclass": pclass,
                "Sex": sex,
                "Age": age,
                "Fare": fare,
                "Embarked": embarked
            }
        ])

        prediction = model.predict(custom_df)[0]

        probability = model.predict_proba(custom_df)[0]

        print("\n===== PREDICTION RESULT =====")

        if prediction == 1:
            print("Prediction: Survived")
        else:
            print("Prediction: Not Survived")

        print(f"Survival Probability: {round(probability[1], 3)}")
        print(f"Non-Survival Probability: {round(probability[0], 3)}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()

    if df is None:
        return

    model = None

    while True:
        print("\n===== TITANIC ML WORKFLOW =====")
        print("1. View Dataset Info")
        print("2. Train Model")
        print("3. Predict Passenger Survival")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_dataset_info(df)

        elif choice == "2":
            model = train_model(df)

        elif choice == "3":
            predict_custom(model)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()