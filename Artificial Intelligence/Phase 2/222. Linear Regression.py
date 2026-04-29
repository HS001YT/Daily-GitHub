def load_dataset():
    import pandas as pd
    import os

    try:
        file = input("Enter CSV file path (e.g., other_files/students_ml.csv): ").strip()
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


def train_model(df):
    try:
        from sklearn.linear_model import LinearRegression

        X = df[["Hours"]]
        y = df["Marks"]

        model = LinearRegression()
        model.fit(X, y)

        print("\nModel Trained Successfully.")
        return model, X, y

    except Exception as e:
        print("Error:", e)
        return None, None, None


def plot_regression(model, X, y):
    import matplotlib.pyplot as plt
    try:
        if model is None:
            print("Train model first.")
            return

        predictions = model.predict(X)

        plt.figure()
        plt.scatter(X, y)
        plt.plot(X, predictions)
        plt.title("Linear Regression Line")
        plt.xlabel("Hours")
        plt.ylabel("Marks")
        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    model = None
    X = None
    y = None

    while True:
        print("\n===== REGRESSION VISUALIZATION MENU =====")
        print("1. Train Model")
        print("2. Plot Regression Line")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            model, X, y = train_model(df)
        elif choice == "2":
            plot_regression(model, X, y)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()