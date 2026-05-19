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


def create_features(df):
    try:
        import pandas as pd

        # FamilySize
        df["FamilySize"] = (
            df["SibSp"] +
            df["Parch"] + 1
        )

        # IsAlone
        df["IsAlone"] = (
            df["FamilySize"] == 1
        ).astype(int)

        # Title Extraction
        df["Title"] = df["Name"].str.extract(
            r",\s*([^\.]+)\."
        )

        # Age Group
        def age_group(age):

            if pd.isnull(age):
                return "Unknown"

            if age < 13:
                return "Child"

            elif age < 20:
                return "Teen"

            elif age < 60:
                return "Adult"

            else:
                return "Senior"

        df["AgeGroup"] = df["Age"].apply(age_group)

        print("\nFeature Engineering Completed.\n")

        return df

    except Exception as e:
        print("Error:", e)
        return df


def show_engineered_features(df):
    try:
        columns = [
            "Name",
            "Age",
            "SibSp",
            "Parch",
            "FamilySize",
            "IsAlone",
            "Title",
            "AgeGroup"
        ]

        print("\n===== ENGINEERED FEATURES =====")
        print(df[columns].head(10))

    except Exception as e:
        print("Error:", e)


def compare_models(df):
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import (
            OneHotEncoder,
            StandardScaler
        )
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score

        # ---------------- BEFORE FEATURE ENGINEERING ----------------

        base_features = [
            "Pclass",
            "Sex",
            "Age",
            "Fare"
        ]

        X_base = df[base_features]
        y = df["Survived"]

        numeric_base = [
            "Age",
            "Fare"
        ]

        categorical_base = [
            "Sex"
        ]

        base_preprocessor = ColumnTransformer([
            (
                "num",
                Pipeline([
                    (
                        "imputer",
                        SimpleImputer(strategy="mean")
                    ),
                    (
                        "scaler",
                        StandardScaler()
                    )
                ]),
                numeric_base
            ),
            (
                "cat",
                Pipeline([
                    (
                        "imputer",
                        SimpleImputer(strategy="most_frequent")
                    ),
                    (
                        "encoder",
                        OneHotEncoder(handle_unknown="ignore")
                    )
                ]),
                categorical_base
            )
        ],
        remainder="passthrough")

        base_pipeline = Pipeline([
            (
                "preprocessor",
                base_preprocessor
            ),
            (
                "model",
                LogisticRegression(max_iter=1000)
            )
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X_base,
            y,
            test_size=0.2,
            random_state=42
        )

        base_pipeline.fit(X_train, y_train)

        base_predictions = base_pipeline.predict(X_test)

        base_accuracy = accuracy_score(
            y_test,
            base_predictions
        )

        # ---------------- AFTER FEATURE ENGINEERING ----------------

        engineered_features = [
            "Pclass",
            "Sex",
            "Age",
            "Fare",
            "FamilySize",
            "IsAlone",
            "Title",
            "AgeGroup"
        ]

        X_eng = df[engineered_features]

        numeric_eng = [
            "Age",
            "Fare",
            "FamilySize"
        ]

        categorical_eng = [
            "Sex",
            "Title",
            "AgeGroup"
        ]

        eng_preprocessor = ColumnTransformer([
            (
                "num",
                Pipeline([
                    (
                        "imputer",
                        SimpleImputer(strategy="mean")
                    ),
                    (
                        "scaler",
                        StandardScaler()
                    )
                ]),
                numeric_eng
            ),
            (
                "cat",
                Pipeline([
                    (
                        "imputer",
                        SimpleImputer(strategy="most_frequent")
                    ),
                    (
                        "encoder",
                        OneHotEncoder(handle_unknown="ignore")
                    )
                ]),
                categorical_eng
            )
        ],
        remainder="passthrough")

        eng_pipeline = Pipeline([
            (
                "preprocessor",
                eng_preprocessor
            ),
            (
                "model",
                LogisticRegression(max_iter=1000)
            )
        ])

        X_train2, X_test2, y_train2, y_test2 = train_test_split(
            X_eng,
            y,
            test_size=0.2,
            random_state=42
        )

        eng_pipeline.fit(X_train2, y_train2)

        eng_predictions = eng_pipeline.predict(X_test2)

        eng_accuracy = accuracy_score(
            y_test2,
            eng_predictions
        )

        print("\n===== MODEL COMPARISON =====")

        print(
            f"\nAccuracy Before Feature Engineering: "
            f"{round(base_accuracy, 3)}"
        )

        print(
            f"Accuracy After Feature Engineering: "
            f"{round(eng_accuracy, 3)}"
        )

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    engineered_df = None

    while True:

        print("\n===== FEATURE ENGINEERING MENU =====")
        print("1. Create Features")
        print("2. Show Engineered Features")
        print("3. Compare Model Accuracy")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            engineered_df = create_features(df)

        elif choice == "2":

            if engineered_df is None:
                print("Create features first.")
            else:
                show_engineered_features(engineered_df)

        elif choice == "3":

            if engineered_df is None:
                print("Create features first.")
            else:
                compare_models(engineered_df)

        elif choice == "4":

            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()