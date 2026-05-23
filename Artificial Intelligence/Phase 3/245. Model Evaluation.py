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


def compare_models(df):

    try:
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler

        from sklearn.linear_model import LinearRegression

        from sklearn.tree import DecisionTreeRegressor

        from sklearn.ensemble import RandomForestRegressor

        from sklearn.metrics import (
            mean_absolute_error,
            mean_squared_error,
            r2_score
        )

        import math

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

        models = {

            "Linear Regression":
            Pipeline([
                (
                    "scaler",
                    StandardScaler()
                ),
                (
                    "model",
                    LinearRegression()
                )
            ]),

            "Decision Tree":
            Pipeline([
                (
                    "scaler",
                    StandardScaler()
                ),
                (
                    "model",
                    DecisionTreeRegressor(
                        random_state=42
                    )
                )
            ]),

            "Random Forest":
            Pipeline([
                (
                    "scaler",
                    StandardScaler()
                ),
                (
                    "model",
                    RandomForestRegressor(
                        random_state=42,
                        n_estimators=100
                    )
                )
            ])
        }

        results = {}

        print("\n===== MODEL COMPARISON =====")

        for name, model in models.items():

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

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

            results[name] = r2

            print(f"\n{name}")

            print(f"MAE : {round(mae, 3)}")
            print(f"RMSE: {round(rmse, 3)}")
            print(f"R²  : {round(r2, 3)}")

        best_model = max(
            results,
            key=results.get
        )

        print("\n===== BEST MODEL =====")

        print(f"{best_model}")
        print(f"Best R² Score: {round(results[best_model], 3)}")

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== MODEL EVALUATION MENU =====")
        print("1. View Dataset Info")
        print("2. Compare Regression Models")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            compare_models(df)

        elif choice == "3":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()