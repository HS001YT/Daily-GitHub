def load_dataset():
    import pandas as pd
    import os

    try:
        file = input(
            "Enter CSV file path (e.g., other_files/movies.csv): "
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


def show_dataset_info(df):

    try:
        print("\n===== DATASET INFO =====")

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nShape:")
        print(df.shape)

        print("\nNull Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)


def build_recommender(df):

    try:
        from sklearn.feature_extraction.text import (
            TfidfVectorizer
        )

        from sklearn.metrics.pairwise import (
            cosine_similarity
        )

        tfidf = TfidfVectorizer()

        tfidf_matrix = tfidf.fit_transform(
            df["Genre"]
        )

        similarity_matrix = cosine_similarity(
            tfidf_matrix
        )

        print(
            "\nRecommendation System Built Successfully."
        )

        return similarity_matrix

    except Exception as e:
        print("Error:", e)
        return None


def recommend_movies(df, similarity_matrix):

    try:
        if similarity_matrix is None:
            print("Build recommender first.")
            return

        movie_name = input(
            "Enter movie name: "
        ).strip()

        if movie_name not in df["Movie"].values:
            print("Movie not found.")
            return

        movie_index = df[
            df["Movie"] == movie_name
        ].index[0]

        similarity_scores = list(
            enumerate(
                similarity_matrix[movie_index]
            )
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        print(
            f"\nTop Recommendations for {movie_name}:"
        )

        count = 0

        for idx, score in similarity_scores:

            if idx == movie_index:
                continue

            print(
                f"{count+1}. "
                f"{df.iloc[idx]['Movie']} "
                f"(Similarity: {round(score,3)})"
            )

            count += 1

            if count == 3:
                break

    except Exception as e:
        print("Error:", e)


def main_menu():

    df = load_dataset()

    if df is None:
        return

    similarity_matrix = None

    while True:

        print("\n===== MOVIE RECOMMENDER MENU =====")
        print("1. View Dataset Info")
        print("2. Build Recommendation System")
        print("3. Get Recommendations")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_dataset_info(df)

        elif choice == "2":

            similarity_matrix = build_recommender(df)

        elif choice == "3":

            recommend_movies(
                df,
                similarity_matrix
            )

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main_menu()