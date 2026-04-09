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


def basic_info(df):
    try:
        print("\n--- BASIC INFO ---")
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print("Data Types:\n", df.dtypes)
        print("\nSummary Statistics:\n", df.describe())

    except Exception as e:
        print("Error:", e)


def data_quality(df):
    try:
        print("\n--- DATA QUALITY ---")
        print("Missing Values:\n", df.isnull().sum())
        print("Duplicate Rows:", df.duplicated().sum())

    except Exception as e:
        print("Error:", e)


def value_counts(df):
    try:
        col = input("Enter column for value counts: ")
        if col not in df.columns:
            print("Invalid column.")
            return

        print("\nValue Counts:\n", df[col].value_counts())

    except Exception as e:
        print("Error:", e)


def correlation_heatmap(df):
    try:
        import seaborn as sns
        import matplotlib.pyplot as plt

        corr = df.corr(numeric_only=True)

        plt.figure()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")

        plt.show()

    except Exception as e:
        print("Error:", e)


def histogram(df):
    try:
        import matplotlib.pyplot as plt

        col = input("Enter column for histogram: ")
        if col not in df.columns:
            print("Invalid column.")
            return

        plt.figure()
        plt.hist(df[col].dropna())
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        plt.show()

    except Exception as e:
        print("Error:", e)


def boxplot(df):
    try:
        import matplotlib.pyplot as plt

        col = input("Enter column for boxplot: ")
        if col not in df.columns:
            print("Invalid column.")
            return

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

    while True:
        print("\n===== EDA MENU =====")
        print("1. Basic Info")
        print("2. Data Quality Check")
        print("3. Value Counts")
        print("4. Histogram")
        print("5. Boxplot")
        print("6. Correlation Heatmap")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            basic_info(df)
        elif choice == "2":
            data_quality(df)
        elif choice == "3":
            value_counts(df)
        elif choice == "4":
            histogram(df)
        elif choice == "5":
            boxplot(df)
        elif choice == "6":
            correlation_heatmap(df)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()