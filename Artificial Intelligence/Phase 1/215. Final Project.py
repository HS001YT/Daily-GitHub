def load_dataset():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nDataset Loaded:\n", df.head())
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        return df
    except Exception as e:
        print("Error:", e)
        return None


def understand_data(df):
    try:
        print("\n--- DATA UNDERSTANDING ---")
        print("Data Types:\n", df.dtypes)
        print("\nSummary:\n", df.describe())
        print("\nUnique Values:")
        for col in df.columns:
            print(f"{col}: {df[col].nunique()}")
    except Exception as e:
        print("Error:", e)


def clean_data(df):
    import numpy as np
    try:
        # Missing values
        for col in df.columns:
            if df[col].dtype.kind in "biufc":
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Remove outliers (IQR)
        num_cols = df.select_dtypes(include=['number']).columns
        for col in num_cols:
            Q1 = np.percentile(df[col], 25)
            Q3 = np.percentile(df[col], 75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower) & (df[col] <= upper)]

        print("Data cleaned.")
        return df

    except Exception as e:
        print("Error:", e)
        return df


def transform_data(df):
    try:
        num_cols = df.select_dtypes(include=['number']).columns
        for col in num_cols:
            mean = df[col].mean()
            std = df[col].std()
            if std != 0:
                df[col] = (df[col] - mean) / std

        print("Data standardized.")
        return df

    except Exception as e:
        print("Error:", e)
        return df


def analyze_data(df):
    try:
        print("\n--- ANALYSIS ---")
        print("Correlation:\n", df.corr(numeric_only=True))

        if "Category" in df.columns:
            print("\nGroupBy Category:\n", df.groupby("Category").mean(numeric_only=True))

    except Exception as e:
        print("Error:", e)


def visualize_data(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    try:
        num_cols = df.select_dtypes(include=['number']).columns

        for col in num_cols:
            plt.figure()
            plt.hist(df[col])
            plt.title(f"Histogram of {col}")
            plt.show()

            plt.figure()
            plt.boxplot(df[col])
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
        with open("final_report.txt", "w") as f:
            f.write("FINAL EDA REPORT\n\n")
            f.write(f"Shape: {df.shape}\n")
            f.write(f"Columns: {df.columns.tolist()}\n\n")
            f.write(str(df.describe()) + "\n")

        df.to_csv("cleaned_dataset.csv", index=False)
        print("Report and cleaned dataset saved.")

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== FINAL EDA MENU =====")
        print("1. Understand Data")
        print("2. Clean Data")
        print("3. Transform Data")
        print("4. Analyze Data")
        print("5. Visualize Data")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            understand_data(df)
        elif choice == "2":
            df = clean_data(df)
        elif choice == "3":
            df = transform_data(df)
        elif choice == "4":
            analyze_data(df)
        elif choice == "5":
            visualize_data(df)
        elif choice == "6":
            generate_report(df)
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()