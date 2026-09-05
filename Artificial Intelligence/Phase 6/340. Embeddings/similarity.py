import numpy as np


def cosine_similarity(vector_a, vector_b):
    a = np.array(
        vector_a,
        dtype=float
    )

    b = np.array(
        vector_b,
        dtype=float
    )

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    similarity = np.dot(
        a,
        b
    ) / (
        magnitude_a * magnitude_b
    )

    return float(similarity)


def similarity_percentage(score):
    score = max(
        -1.0,
        min(1.0, score)
    )

    return ((score + 1) / 2) * 100