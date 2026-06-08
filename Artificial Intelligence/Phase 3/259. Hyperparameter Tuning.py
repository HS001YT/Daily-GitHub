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

    print("\n===== DATASET INFO =====")

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nNull Values:")
    print(df.isnull().sum())


def tune_model(df):

    try:
        from sklearn.model_selection import (
            train_test_split,
            GridSearchCV,
            RandomizedSearchCV
        )

        from sklearn.tree import (
            DecisionTreeClassifier
        )

        from sklearn.metrics import (
            accuracy_score
        )

        from sklearn.preprocessing import (
            LabelEncoder
        )

        df = df.copy()

        df["Age"] = (
            df["Age"]
            .fillna(
                df["Age"].median()
            )
        )

        df["Sex"] = (
            LabelEncoder()
            .fit_transform(df["Sex"])
        )

        X = df[
            [
                "Pclass",
                "Sex",
                "Age",
                "Fare"
            ]
        ]

        y = df["Survived"]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        # ---------------- BASE MODEL ----------------

        baseline = DecisionTreeClassifier(
            random_state=42
        )

        baseline.fit(
            X_train,
            y_train
        )

        baseline_pred = baseline.predict(
            X_test
        )

        baseline_acc = accuracy_score(
            y_test,
            baseline_pred
        )

        print(
            "\nBaseline Accuracy:",
            round(baseline_acc, 3)
        )

        # ---------------- GRID SEARCH ----------------

        param_grid = {

            "max_depth":
            [2, 3, 4, 5, 6],

            "min_samples_split":
            [2, 5, 10],

            "criterion":
            ["gini", "entropy"]
        }

        grid = GridSearchCV(

            estimator=
            DecisionTreeClassifier(
                random_state=42
            ),

            param_grid=
            param_grid,

            cv=5,

            scoring=
            "accuracy"
        )

        grid.fit(
            X_train,
            y_train
        )

        print(
            "\n===== GRID SEARCH ====="
        )

        print(
            "Best Parameters:",
            grid.best_params_
        )

        print(
            "Best CV Score:",
            round(
                grid.best_score_,
                3
            )
        )

        grid_pred = (
            grid.best_estimator_
            .predict(X_test)
        )

        grid_acc = accuracy_score(
            y_test,
            grid_pred
        )

        print(
            "Test Accuracy:",
            round(grid_acc, 3)
        )

        # ---------------- RANDOM SEARCH ----------------

        random_search = RandomizedSearchCV(

            estimator=
            DecisionTreeClassifier(
                random_state=42
            ),

            param_distributions=
            param_grid,

            n_iter=5,

            cv=5,

            random_state=42,

            scoring=
            "accuracy"
        )

        random_search.fit(
            X_train,
            y_train
        )

        print(
            "\n===== RANDOM SEARCH ====="
        )

        print(
            "Best Parameters:",
            random_search.best_params_
        )

        print(
            "Best CV Score:",
            round(
                random_search.best_score_,
                3
            )
        )

        random_pred = (
            random_search
            .best_estimator_
            .predict(X_test)
        )

        random_acc = accuracy_score(
            y_test,
            random_pred
        )

        print(
            "Test Accuracy:",
            round(random_acc, 3)
        )

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print(
            "\n===== HYPERPARAMETER TUNING MENU ====="
        )

        print("1. View Dataset Info")
        print("2. Run Hyperparameter Tuning")
        print("3. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":
            show_dataset_info(df)

        elif choice == "2":
            tune_model(df)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()