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


def analyze_dataset(df):
    try:
        print("\n--- BASIC INFO ---")
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print("Data Types:\n", df.dtypes)

        print("\n--- SUMMARY STATISTICS ---")
        print(df.describe())

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


def visualize_data(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    try:
        col = input("Enter numeric column for histogram & boxplot: ")
        if col not in df.columns:
            print("Invalid column.")
            return

        plt.figure()
        plt.hist(df[col].dropna())
        plt.title(f"Histogram of {col}")
        plt.show()

        plt.figure()
        plt.boxplot(df[col].dropna())
        plt.title(f"Boxplot of {col}")
        plt.show()

        corr = df.corr(numeric_only=True)

        plt.figure()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    except Exception as e:
        print("Error:", e)


def generate_report(df):
    try:
        with open("eda_report.txt", "w") as f:
            f.write("===== DATASET REPORT =====\n\n")

            f.write(f"Shape: {df.shape}\n\n")
            f.write(f"Columns: {df.columns.tolist()}\n\n")

            f.write("Data Types:\n")
            f.write(str(df.dtypes) + "\n\n")

            f.write("Summary Statistics:\n")
            f.write(str(df.describe()) + "\n\n")

            f.write("Missing Values:\n")
            f.write(str(df.isnull().sum()) + "\n\n")

            f.write(f"Duplicate Rows: {df.duplicated().sum()}\n")

        print("\nReport saved as 'eda_report.txt'")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== MINI PROJECT MENU =====")
        print("1. Run Full Analysis")
        print("2. Value Counts")
        print("3. Visualizations")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            analyze_dataset(df)
        elif choice == "2":
            value_counts(df)
        elif choice == "3":
            visualize_data(df)
        elif choice == "4":
            generate_report(df)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()