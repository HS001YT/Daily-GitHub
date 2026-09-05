from documents import DOCUMENTS
from embedding import generate_embedding
from vector_store import VectorStore


def build_vector_store():
    print()
    print("Creating document embeddings...")
    print()

    texts = [
        document["text"]
        for document in DOCUMENTS
    ]

    embeddings = []

    for index, text in enumerate(
        texts,
        start=1
    ):
        print(
            f"Embedding document {index}/"
            f"{len(texts)}..."
        )

        embedding = generate_embedding(
            text
        )

        embeddings.append(embedding)

    dimension = len(
        embeddings[0]
    )

    store = VectorStore(
        dimension
    )

    store.add_embeddings(
        embeddings
    )

    print()
    print(
        f"Vector store created with "
        f"{store.total_vectors()} documents."
    )

    return store


def search_documents(
    store,
    query,
    top_k=3
):
    query_embedding = generate_embedding(
        query
    )

    scores, indices = store.search(
        query_embedding,
        top_k
    )

    results = []

    for score, index in zip(
        scores,
        indices
    ):
        if index < 0:
            continue

        document = DOCUMENTS[index]

        results.append({
            "document": document,
            "score": float(score)
        })

    return results


def display_results(
    query,
    results
):
    print()
    print("=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    print()
    print(f"Query: {query}")

    if not results:
        print()
        print("No results found.")
        return

    for rank, result in enumerate(
        results,
        start=1
    ):
        document = result["document"]
        score = result["score"]

        print()
        print(
            f"{rank}. {document['title']}"
        )

        print(
            f"Similarity: {score:.4f}"
        )

        print(
            f"Content: {document['text']}"
        )


def main():
    print()
    print("=" * 60)
    print("SEMANTIC SEARCH ENGINE")
    print("=" * 60)

    try:
        store = build_vector_store()

    except Exception as error:
        print()
        print(
            f"Failed to build vector store: {error}"
        )
        return

    print()
    print(
        "Enter a question or search phrase."
    )
    print(
        "Type 'exit' to close."
    )

    while True:
        print()

        query = input(
            "Search > "
        ).strip()

        if query.lower() == "exit":
            print()
            print("Application closed.")
            break

        if not query:
            print(
                "Search query cannot be empty."
            )
            continue

        try:
            results = search_documents(
                store,
                query,
                top_k=3
            )

            display_results(
                query,
                results
            )

        except Exception as error:
            print()
            print(
                f"Search error: {error}"
            )


if __name__ == "__main__":
    main()