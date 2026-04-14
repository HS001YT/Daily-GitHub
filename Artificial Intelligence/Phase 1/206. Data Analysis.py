def load_dataset():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nDataset Loaded:\n", df.head())
        return df
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def compute_correlation(df):
    try:
        corr = df.corr(numeric_only=True)
        print("\nCorrelation Matrix:\n", corr)
        return corr
    except Exception as e:
        print("Error:", e)
        return None


def plot_heatmap(corr):
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt

        plt.figure()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    except Exception as e:
        print("Error:", e)


def extract_insights(corr):
    try:
        print("\n--- Correlation Insights ---")
        threshold = 0.7

        for col in corr.columns:
            for row in corr.index:
                if col != row:
                    value = corr.loc[row, col]

                    if value >= threshold:
                        print(f"Strong Positive: {row} ↔ {col} = {value:.2f}")
                    elif value <= -threshold:
                        print(f"Strong Negative: {row} ↔ {col} = {value:.2f}")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    corr = None

    while True:
        print("\n===== CORRELATION MENU =====")
        print("1. Compute Correlation Matrix")
        print("2. Show Heatmap")
        print("3. Show Insights")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            corr = compute_correlation(df)

        elif choice == "2":
            if corr is not None:
                plot_heatmap(corr)
            else:
                print("Compute correlation first.")

        elif choice == "3":
            if corr is not None:
                extract_insights(corr)
            else:
                print("Compute correlation first.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()