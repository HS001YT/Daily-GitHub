import numpy as np
import faiss


class VectorStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(
            dimension
        )

    def add_embeddings(self, embeddings):
        vectors = np.array(
            embeddings,
            dtype="float32"
        )

        faiss.normalize_L2(vectors)

        self.index.add(vectors)

    def search(self, query_embedding, top_k=3):
        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        faiss.normalize_L2(query_vector)

        scores, indices = self.index.search(
            query_vector,
            top_k
        )

        return scores[0], indices[0]

    def total_vectors(self):
        return self.index.ntotal