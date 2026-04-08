def create_sample_data():
    try:
        import pandas as pd
        import numpy as np

        data = {
            "Math": np.random.randint(50, 100, 10),
            "Science": np.random.randint(50, 100, 10),
            "English": np.random.randint(50, 100, 10),
            "Computer": np.random.randint(50, 100, 10)
        }

        df = pd.DataFrame(data)
        return df

    except Exception as e:
        print("Error creating data:", e)
        return None


def plot_heatmap(df):
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt

        corr = df.corr()

        plt.figure()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")

        plt.show()

    except Exception as e:
        print("Error:", e)


def plot_pairplot(df):
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt

        sns.pairplot(df)
        plt.suptitle("Pairplot Visualization", y=1.02)

        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = create_sample_data()

    if df is None:
        print("Failed to create dataset.")
        return

    print("\nSample Dataset:\n", df)

    while True:
        print("\n===== SEABORN MENU =====")
        print("1. Heatmap")
        print("2. Pairplot")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            plot_heatmap(df)

        elif choice == "2":
            plot_pairplot(df)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()