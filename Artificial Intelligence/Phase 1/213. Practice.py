def create_dataset():
    import pandas as pd
    try:
        data = {
            "Name": ["A", "B", "C", "D", "E"],
            "Marks1": [78, 85, 62, 90, 55],
            "Marks2": [80, 88, 60, 92, 58],
            "Marks3": [75, 84, 65, 89, 50]
        }
        df = pd.DataFrame(data)
        print("\nDataset Created:\n", df)
        return df
    except Exception as e:
        print("Error:", e)
        return None


def numpy_operations(df):
    import numpy as np
    try:
        marks_array = df[["Marks1", "Marks2", "Marks3"]].values

        total = np.sum(marks_array, axis=1)
        mean = np.mean(marks_array, axis=1)
        std = np.std(marks_array, axis=1)

        print("\n--- NumPy Operations ---")
        print("Total Marks:", total)
        print("Mean Marks:", mean)
        print("Std Dev:", std)

    except Exception as e:
        print("Error:", e)


def create_features(df):
    try:
        df["Total"] = df[["Marks1", "Marks2", "Marks3"]].sum(axis=1)
        df["Average"] = df["Total"] / 3

        def grade(x):
            if x >= 90:
                return "A"
            elif x >= 75:
                return "B"
            elif x >= 50:
                return "C"
            else:
                return "Fail"

        df["Grade"] = df["Average"].apply(grade)

        print("\nFeatures Added:\n", df)

    except Exception as e:
        print("Error:", e)


def filtering(df):
    try:
        print("\nStudents with Average > 75:\n", df[df["Average"] > 75])
        print("\nFailed Students:\n", df[df["Grade"] == "Fail"])
    except Exception as e:
        print("Error:", e)


def grouping(df):
    try:
        print("\nStudents per Grade:\n", df["Grade"].value_counts())
    except Exception as e:
        print("Error:", e)


def sorting(df):
    try:
        sorted_df = df.sort_values(by="Average", ascending=False)
        print("\nSorted Dataset:\n", sorted_df)
    except Exception as e:
        print("Error:", e)


def visualization(df):
    import matplotlib.pyplot as plt
    try:
        plt.figure()
        plt.bar(df["Name"], df["Total"])
        plt.title("Total Marks")
        plt.xlabel("Name")
        plt.ylabel("Marks")
        plt.show()

        plt.figure()
        plt.hist(df["Average"])
        plt.title("Average Marks Distribution")
        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = create_dataset()
    if df is None:
        return

    while True:
        print("\n===== MIXED PRACTICE MENU =====")
        print("1. NumPy Operations")
        print("2. Feature Creation")
        print("3. Filtering")
        print("4. Grouping")
        print("5. Sorting")
        print("6. Visualization")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            numpy_operations(df)
        elif choice == "2":
            create_features(df)
        elif choice == "3":
            filtering(df)
        elif choice == "4":
            grouping(df)
        elif choice == "5":
            sorting(df)
        elif choice == "6":
            visualization(df)
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()