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
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LinearRegression
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

        pipeline = Pipeline([
            (
                "scaler",
                StandardScaler()
            ),
            (
                "model",
                LinearRegression()
            )
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

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

        print("\n===== MODEL TRAINED =====")

        print(f"\nMAE : {round(mae, 3)}")
        print(f"MSE : {round(mse, 3)}")
        print(f"RMSE: {round(rmse, 3)}")
        print(f"R²  : {round(r2, 3)}")

        print("\nActual | Predicted")

        for actual, pred in zip(y_test, predictions):
            print(f"{actual} | {round(pred, 2)}")

        return pipeline

    except Exception as e:
        print("Error:", e)
        return None


def predict_price(model):

    try:
        import pandas as pd

        if model is None:
            print("Train model first.")
            return

        area = float(input("Enter area: "))
        bedrooms = int(input("Enter bedrooms: "))
        bathrooms = int(input("Enter bathrooms: "))
        floors = int(input("Enter floors: "))
        parking = int(input("Enter parking spaces: "))

        custom_df = pd.DataFrame([
            {
                "Area": area,
                "Bedrooms": bedrooms,
                "Bathrooms": bathrooms,
                "Floors": floors,
                "Parking": parking
            }
        ])

        prediction = model.predict(custom_df)[0]

        print("\n===== HOUSE PRICE PREDICTION =====")

        print(f"Predicted Price: {round(prediction, 2)}")

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    model = None

    while True:

        print("\n===== HOUSE PRICE PREDICTION MENU =====")
        print("1. View Dataset Info")
        print("2. Train Regression Model")
        print("3. Predict House Price")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            model = train_model(df)

        elif choice == "3":

            predict_price(model)

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()