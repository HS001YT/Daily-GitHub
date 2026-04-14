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


def select_column(df):
    col = input("Enter numeric column: ")
    if col not in df.columns:
        print("Invalid column.")
        return None
    return col


def detect_outliers_iqr(df, col):
    import numpy as np
    try:
        data = df[col].dropna()

        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = data[(data < lower) | (data > upper)]

        print("\n--- IQR Method ---")
        print("Lower Bound:", lower)
        print("Upper Bound:", upper)
        print("Outliers:\n", outliers)
        print("Total Outliers:", len(outliers))

    except Exception as e:
        print("Error:", e)


def detect_outliers_zscore(df, col):
    import numpy as np
    try:
        data = df[col].dropna()

        mean = np.mean(data)
        std = np.std(data)

        z_scores = (data - mean) / std
        outliers = data[np.abs(z_scores) > 3]

        print("\n--- Z-Score Method ---")
        print("Mean:", mean)
        print("Std Dev:", std)
        print("Outliers:\n", outliers)
        print("Total Outliers:", len(outliers))

    except Exception as e:
        print("Error:", e)


def plot_boxplot(df, col):
    import matplotlib.pyplot as plt
    try:
        plt.figure()
        plt.boxplot(df[col].dropna())
        plt.title(f"Boxplot of {col}")
        plt.show()
    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    col = select_column(df)
    if col is None:
        return

    while True:
        print("\n===== OUTLIER DETECTION MENU =====")
        print("1. IQR Method")
        print("2. Z-Score Method")
        print("3. Boxplot")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            detect_outliers_iqr(df, col)
        elif choice == "2":
            detect_outliers_zscore(df, col)
        elif choice == "3":
            plot_boxplot(df, col)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()