def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/house_price.csv): "
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

        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def compare_tree_depths(df):

    try:
        import math
        import pandas as pd
        import matplotlib.pyplot as plt

        from sklearn.model_selection import train_test_split

        from sklearn.pipeline import Pipeline

        from sklearn.preprocessing import StandardScaler

        from sklearn.tree import DecisionTreeRegressor

        from sklearn.metrics import (
            mean_absolute_error,
            mean_squared_error,
            r2_score
        )

        features = [
            "Area",
            "Bedrooms",
            "Bathrooms",
            "Floors",
            "Parking"
        ]

        target = "Price"

        X = df[features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        depths = [
            1,
            3,
            5,
            None
        ]

        depth_labels = []
        r2_scores = []

        print("\n===== DEPTH COMPARISON =====")

        for depth in depths:

            pipeline = Pipeline([
                (
                    "scaler",
                    StandardScaler()
                ),
                (
                    "model",
                    DecisionTreeRegressor(
                        max_depth=depth,
                        random_state=42
                    )
                )
            ])

            pipeline.fit(X_train, y_train)

            predictions = pipeline.predict(X_test)

            train_score = pipeline.score(
                X_train,
                y_train
            )

            test_score = pipeline.score(
                X_test,
                y_test
            )

            mae = mean_absolute_error(
                y_test,
                predictions
            )

            mse = mean_squared_error(
                y_test,
                predictions
            )

            rmse = math.sqrt(mse)

            r2 = r2_score(
                y_test,
                predictions
            )

            depth_name = (
                str(depth)
                if depth is not None
                else "None"
            )

            depth_labels.append(depth_name)

            r2_scores.append(r2)

            print(f"\n===== MAX DEPTH: {depth_name} =====")

            print(f"Train Score : {round(train_score, 3)}")
            print(f"Test Score  : {round(test_score, 3)}")
            print(f"MAE         : {round(mae, 3)}")
            print(f"RMSE        : {round(rmse, 3)}")
            print(f"R² Score    : {round(r2, 3)}")

        plt.figure(figsize=(8, 5))

        plt.plot(
            depth_labels,
            r2_scores,
            marker="o"
        )

        plt.title(
            "Decision Tree Depth vs R² Score"
        )

        plt.xlabel("Max Depth")

        plt.ylabel("R² Score")

        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== OVERFITTING CONTROL MENU =====")
        print("1. View Dataset Info")
        print("2. Compare Tree Depths")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            compare_tree_depths(df)

        elif choice == "3":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()