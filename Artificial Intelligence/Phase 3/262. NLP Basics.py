def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/text_dataset.csv): "
        ).strip()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file)

        df = pd.read_csv(full_path)

        print("\nDataset Loaded Successfully.\n")
        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def preprocess_text(text):

    import re

    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    # Lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    words = word_tokenize(text)

    # Stopwords
    stop_words = set(stopwords.words("english"))

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    # Stemming
    stemmer = PorterStemmer()

    words = [
        stemmer.stem(word)
        for word in words
    ]

    return " ".join(words)


def show_dataset_info(df):

    print("\n===== DATASET INFO =====")

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nNull Values:")
    print(df.isnull().sum())


def process_dataset(df):

    try:

        df = df.copy()

        df["Cleaned_Text"] = (
            df["Text"]
            .apply(preprocess_text)
        )

        print(
            "\n===== CLEANED DATASET ====="
        )

        print(df)

        return df

    except Exception as e:

        print("Error:", e)
        return None


def save_cleaned_dataset(df):

    try:

        if df is None:
            print("No processed dataset found.")
            return

        output_file = (
            "cleaned_text_dataset.csv"
        )

        df.to_csv(
            output_file,
            index=False
        )

        print(
            f"\nSaved as: {output_file}"
        )

    except Exception as e:

        print("Error:", e)


def main_menu():

    import nltk

    nltk.download("punkt")
    nltk.download("stopwords")

    df = load_dataset()

    if df is None:
        return

    processed_df = None

    while True:

        print(
            "\n===== NLP PREPROCESSING MENU ====="
        )

        print("1. View Dataset Info")
        print("2. Process Text")
        print("3. Save Cleaned Dataset")
        print("4. Exit")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            processed_df = process_dataset(df)

        elif choice == "3":

            save_cleaned_dataset(
                processed_df
            )

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()