def load_dataset():
    import pandas as pd
    try:
        file = input("Enter CSV file path: ").strip()
        df = pd.read_csv(file)
        print("\nDataset Loaded:\n", df.head())
        return df
    except Exception as e:
        print("Error:", e)
        return None


def inspect_data(df):
    print("\n--- DATA INSPECTION ---")
    print("Shape:", df.shape)
    print("Missing Values:\n", df.isnull().sum())
    print("Duplicate Rows:", df.duplicated().sum())


def remove_duplicates(df):
    df.drop_duplicates(inplace=True)
    print("Duplicates removed.")
    return df


def handle_missing(df):
    try:
        for col in df.columns:
            if df[col].dtype.kind in "biufc":
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

        print("Missing values handled.")
        return df

    except Exception as e:
        print("Error:", e)
        return df


def remove_outliers(df):
    import numpy as np
    try:
        numeric_cols = df.select_dtypes(include=['number']).columns

        for col in numeric_cols:
            Q1 = np.percentile(df[col], 25)
            Q3 = np.percentile(df[col], 75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            df = df[(df[col] >= lower) & (df[col] <= upper)]

        print("Outliers removed.")
        return df

    except Exception as e:
        print("Error:", e)
        return df


def scale_data(df):
    try:
        choice = input("Choose scaling (1: Min-Max, 2: Z-score): ")

        numeric_cols = df.select_dtypes(include=['number']).columns

        if choice == "1":
            for col in numeric_cols:
                min_val = df[col].min()
                max_val = df[col].max()

                if max_val != min_val:
                    df[col] = (df[col] - min_val) / (max_val - min_val)

        elif choice == "2":
            for col in numeric_cols:
                mean = df[col].mean()
                std = df[col].std()

                if std != 0:
                    df[col] = (df[col] - mean) / std

        else:
            print("Invalid choice.")

        print("Scaling applied.")
        return df

    except Exception as e:
        print("Error:", e)
        return df


def save_dataset(df):
    try:
        file = input("Enter output file name: ").strip()
        df.to_csv(file, index=False)
        print(f"Dataset saved as {file}")
    except Exception as e:
        print("Error:", e)


def run_pipeline(df):
    inspect_data(df)
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = remove_outliers(df)
    df = scale_data(df)

    print("\n--- CLEANED DATA ---\n", df.head())
    return df


def main_menu():
    df = load_dataset()
    if df is None:
        return

    cleaned_df = None

    while True:
        print("\n===== DATA CLEANING PIPELINE =====")
        print("1. Run Full Pipeline")
        print("2. Show Cleaned Data")
        print("3. Save Cleaned Data")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            cleaned_df = run_pipeline(df.copy())

        elif choice == "2":
            if cleaned_df is not None:
                print(cleaned_df.head())
            else:
                print("Run pipeline first.")

        elif choice == "3":
            if cleaned_df is not None:
                save_dataset(cleaned_df)
            else:
                print("Run pipeline first.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()