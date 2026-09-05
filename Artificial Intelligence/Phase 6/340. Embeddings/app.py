from embedding import generate_embedding
from similarity import (
    cosine_similarity,
    similarity_percentage
)


def get_documents():
    documents = []

    print()
    print("=" * 60)
    print("SEMANTIC DOCUMENT SIMILARITY")
    print("=" * 60)

    print()
    print("Enter documents one by one.")
    print("Type 'done' when finished.")
    print()

    while True:
        text = input(
            f"Document {len(documents) + 1} > "
        ).strip()

        if text.lower() == "done":
            break

        if not text:
            print(
                "Document cannot be empty."
            )
            continue

        documents.append(text)

    return documents


def generate_document_embeddings(documents):
    embeddings = []

    print()
    print("Generating embeddings...")
    print()

    for index, document in enumerate(
        documents,
        start=1
    ):
        try:
            print(
                f"Processing document {index}..."
            )

            embedding = generate_embedding(
                document
            )

            embeddings.append(
                embedding
            )

            print(
                f"Document {index} completed."
            )

        except Exception as error:
            print(
                f"Error processing document "
                f"{index}: {error}"
            )

            embeddings.append(None)

    return embeddings


def calculate_similarity_matrix(
    documents,
    embeddings
):
    results = []

    for i in range(len(documents)):

        if embeddings[i] is None:
            continue

        for j in range(
            i + 1,
            len(documents)
        ):

            if embeddings[j] is None:
                continue

            score = cosine_similarity(
                embeddings[i],
                embeddings[j]
            )

            percentage = similarity_percentage(
                score
            )

            results.append({
                "document_a": i + 1,
                "document_b": j + 1,
                "score": score,
                "percentage": percentage
            })

    return results


def display_results(
    documents,
    results
):
    print()
    print("=" * 60)
    print("SIMILARITY RESULTS")
    print("=" * 60)

    if not results:
        print(
            "Not enough valid documents to compare."
        )
        return

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    for result in results:

        a = result["document_a"]
        b = result["document_b"]

        score = result["score"]
        percentage = result["percentage"]

        print()
        print(
            f"Document {a} ↔ Document {b}"
        )

        print(
            f"Cosine similarity: "
            f"{score:.4f}"
        )

        print(
            f"Similarity percentage: "
            f"{percentage:.2f}%"
        )

        print(
            f"Document {a}: "
            f"{documents[a - 1]}"
        )

        print(
            f"Document {b}: "
            f"{documents[b - 1]}"
        )


def main():
    documents = get_documents()

    if len(documents) < 2:
        print()
        print(
            "At least two documents are required."
        )
        return

    embeddings = generate_document_embeddings(
        documents
    )

    results = calculate_similarity_matrix(
        documents,
        embeddings
    )

    display_results(
        documents,
        results
    )


if __name__ == "__main__":
    main()