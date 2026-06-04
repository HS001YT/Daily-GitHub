def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/stock_prices.csv): "
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


def analyze_trend(df):

    try:
        import matplotlib.pyplot as plt
        import pandas as pd

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df["Price"],
            marker="o"
        )

        plt.title(
            "Stock Price Trend"
        )

        plt.xlabel("Date")

        plt.ylabel("Price")

        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


def moving_average_analysis(df):

    try:
        import matplotlib.pyplot as plt
        import pandas as pd

        df["Date"] = pd.to_datetime(
            df["Date"]
        )

        df["MovingAverage"] = (
            df["Price"]
            .rolling(window=3)
            .mean()
        )

        print(
            "\n===== MOVING AVERAGE ====="
        )

        print(
            df[
                [
                    "Date",
                    "Price",
                    "MovingAverage"
                ]
            ]
        )

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df["Price"],
            label="Price"
        )

        plt.plot(
            df["Date"],
            df["MovingAverage"],
            label="3-Day Moving Average"
        )

        plt.title(
            "Price vs Moving Average"
        )

        plt.xlabel("Date")

        plt.ylabel("Price")

        plt.legend()

        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


def predict_next_price(df):

    try:
        changes = (
            df["Price"]
            .diff()
            .dropna()
        )

        avg_change = changes.mean()

        last_price = (
            df["Price"]
            .iloc[-1]
        )

        predicted_price = (
            last_price
            + avg_change
        )

        print(
            "\n===== SIMPLE FORECAST ====="
        )

        print(
            f"Last Price: {last_price}"
        )

        print(
            f"Average Change: "
            f"{avg_change:.2f}"
        )

        print(
            f"Predicted Next Price: "
            f"{predicted_price:.2f}"
        )

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    while True:

        print("\n===== TIME SERIES MENU =====")

        print("1. View Dataset Info")
        print("2. Analyze Trend")
        print("3. Moving Average Analysis")
        print("4. Predict Next Price")
        print("5. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            analyze_trend(df)

        elif choice == "3":

            moving_average_analysis(df)

        elif choice == "4":

            predict_next_price(df)

        elif choice == "5":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()