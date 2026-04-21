def create_dataset():
    import pandas as pd
    try:
        data = {
            "Name": ["A", "B", "C", "D", "E"],
            "Department": ["IT", "HR", "IT", "Finance", "HR"],
            "Salary": [50000, 40000, 60000, 55000, 45000],
            "Experience": [1, 3, 5, 7, 2]
        }
        df = pd.DataFrame(data)
        print("\nDataset Created:\n", df)
        return df
    except Exception as e:
        print("Error:", e)
        return None


def transform_data(df):
    try:
        df["Bonus"] = df["Salary"] * 0.10
        df["Updated_Salary"] = df["Salary"] + df["Bonus"]

        def categorize(exp):
            if exp <= 2:
                return "Junior"
            elif exp <= 5:
                return "Mid"
            else:
                return "Senior"

        df["Level"] = df["Experience"].apply(categorize)

        print("\nTransformed Data:\n", df)

    except Exception as e:
        print("Error:", e)


def aggregation(df):
    try:
        print("\n--- Aggregation ---")
        print("Average Salary:\n", df.groupby("Department")["Salary"].mean())
        print("\nTotal Salary:\n", df.groupby("Department")["Salary"].sum())
        print("\nEmployee Count:\n", df.groupby("Department")["Name"].count())

    except Exception as e:
        print("Error:", e)


def normalize_salary(df):
    try:
        min_val = df["Salary"].min()
        max_val = df["Salary"].max()

        if max_val != min_val:
            df["Salary_norm"] = (df["Salary"] - min_val) / (max_val - min_val)

        print("\nNormalized Salary:\n", df[["Salary", "Salary_norm"]])

    except Exception as e:
        print("Error:", e)


def filtering(df):
    try:
        avg_salary = df["Salary"].mean()

        print("\nAbove Average Salary:\n", df[df["Salary"] > avg_salary])
        print("\nSenior Employees:\n", df[df["Level"] == "Senior"])

    except Exception as e:
        print("Error:", e)


def sorting(df):
    try:
        sorted_df = df.sort_values(by="Updated_Salary", ascending=False)
        print("\nSorted Data:\n", sorted_df)

    except Exception as e:
        print("Error:", e)


def show_dataset(df):
    print("\nCurrent Dataset:\n", df)


def main_menu():
    df = create_dataset()
    if df is None:
        return

    while True:
        print("\n===== DATA TRANSFORMATION MENU =====")
        print("1. Transform Data")
        print("2. Aggregation")
        print("3. Normalize Salary")
        print("4. Filtering")
        print("5. Sorting")
        print("6. Show Dataset")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            transform_data(df)
        elif choice == "2":
            aggregation(df)
        elif choice == "3":
            normalize_salary(df)
        elif choice == "4":
            filtering(df)
        elif choice == "5":
            sorting(df)
        elif choice == "6":
            show_dataset(df)
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()