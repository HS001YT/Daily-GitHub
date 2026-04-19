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


def validate_columns(df, cols):
    for col in cols:
        if col not in df.columns:
            print(f"Invalid column: {col}")
            return False
    return True


def line_chart(df):
    import matplotlib.pyplot as plt
    try:
        x_col = input("Enter X column: ")
        y_col = input("Enter Y column: ")

        if not validate_columns(df, [x_col, y_col]):
            return

        plt.figure()
        plt.plot(df[x_col], df[y_col])
        plt.title("Line Chart")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid()
        plt.show()

    except Exception as e:
        print("Error:", e)


def bar_chart(df):
    import matplotlib.pyplot as plt
    try:
        x_col = input("Enter X column: ")
        y_col = input("Enter Y column: ")

        if not validate_columns(df, [x_col, y_col]):
            return

        plt.figure()
        plt.bar(df[x_col], df[y_col])
        plt.title("Bar Chart")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()

    except Exception as e:
        print("Error:", e)


def histogram(df):
    import matplotlib.pyplot as plt
    try:
        col = input("Enter column: ")

        if not validate_columns(df, [col]):
            return

        plt.figure()
        plt.hist(df[col].dropna())
        plt.title("Histogram")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()

    except Exception as e:
        print("Error:", e)


def scatter_plot(df):
    import matplotlib.pyplot as plt
    try:
        x_col = input("Enter X column: ")
        y_col = input("Enter Y column: ")

        if not validate_columns(df, [x_col, y_col]):
            return

        plt.figure()
        plt.scatter(df[x_col], df[y_col])
        plt.title("Scatter Plot")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid()
        plt.show()

    except Exception as e:
        print("Error:", e)


def boxplot(df):
    import matplotlib.pyplot as plt
    try:
        col = input("Enter column: ")

        if not validate_columns(df, [col]):
            return

        plt.figure()
        plt.boxplot(df[col].dropna())
        plt.title("Boxplot")
        plt.show()

    except Exception as e:
        print("Error:", e)


def heatmap(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    try:
        corr = df.corr(numeric_only=True)

        plt.figure()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    except Exception as e:
        print("Error:", e)


def main_menu():
    df = load_dataset()
    if df is None:
        return

    while True:
        print("\n===== VISUALIZATION DASHBOARD =====")
        print("1. Line Chart")
        print("2. Bar Chart")
        print("3. Histogram")
        print("4. Scatter Plot")
        print("5. Boxplot")
        print("6. Heatmap")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            line_chart(df)
        elif choice == "2":
            bar_chart(df)
        elif choice == "3":
            histogram(df)
        elif choice == "4":
            scatter_plot(df)
        elif choice == "5":
            boxplot(df)
        elif choice == "6":
            heatmap(df)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()