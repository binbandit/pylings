"""
Concept: Cosine Similarity for RAG (Retrieval Augmented Generation)

RAG is a technique that enhances LLM responses by retrieving relevant documents
from a knowledge base. The key to retrieval is finding documents that are
semantically similar to the user's query.

Documents and queries are converted to vectors (embeddings) using models like
OpenAI's text-embedding-ada-002 or open-source alternatives. To find similar
documents, we calculate the similarity between vectors.

Cosine Similarity measures the angle between two vectors:
- Value of 1.0: Vectors point in the same direction (identical meaning)
- Value of 0.0: Vectors are perpendicular (unrelated)
- Value of -1.0: Vectors point in opposite directions

The formula is:
    cosine_similarity(A, B) = (A . B) / (||A|| * ||B||)

Where:
- A . B is the dot product: sum of element-wise multiplication
- ||A|| is the norm (magnitude): sqrt(sum of squares)

In NumPy:
- Dot product: np.dot(a, b)
- Norm: np.linalg.norm(a)

Task: Implement the cosine_similarity function using the formula above.
"""

import numpy as np


def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors.

    Args:
        vec1: First vector (numpy array)
        vec2: Second vector (numpy array)

    Returns:
        float: Cosine similarity between -1 and 1
    """
    # TODO: Calculate the dot product of vec1 and vec2
    dot_product = 0  # FIX ME: Use np.dot()

    # TODO: Calculate the norm (magnitude) of each vector
    norm1 = 1  # FIX ME: Use np.linalg.norm()
    norm2 = 1  # FIX ME: Use np.linalg.norm()

    # TODO: Return dot_product / (norm1 * norm2)
    return 0.0  # FIX ME: Calculate and return the cosine similarity


def main():
    # Test 1: Identical vectors should have similarity of 1.0
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([1.0, 0.0, 0.0])

    sim = cosine_similarity(v1, v2)
    if not np.isclose(sim, 1.0):
        raise Exception(
            f"Test 1 Failed: Identical vectors should have similarity 1.0\n"
            f"Expected: 1.0, Got: {sim}\n"
            f"Hint: When vectors are identical, the angle is 0, so cos(0) = 1"
        )
    print(f"Test 1 passed: identical vectors -> {sim:.2f}")

    # Test 2: Orthogonal (perpendicular) vectors should have similarity of 0.0
    v3 = np.array([1.0, 0.0, 0.0])
    v4 = np.array([0.0, 1.0, 0.0])

    sim = cosine_similarity(v3, v4)
    if not np.isclose(sim, 0.0):
        raise Exception(
            f"Test 2 Failed: Orthogonal vectors should have similarity 0.0\n"
            f"Expected: 0.0, Got: {sim}\n"
            f"Hint: Perpendicular vectors have a 90-degree angle, cos(90) = 0"
        )
    print(f"Test 2 passed: orthogonal vectors -> {sim:.2f}")

    # Test 3: Similar vectors should have high similarity
    v5 = np.array([1.0, 2.0, 3.0])
    v6 = np.array([1.0, 2.0, 3.5])  # Slightly different

    sim = cosine_similarity(v5, v6)
    if sim < 0.95:
        raise Exception(
            f"Test 3 Failed: Similar vectors should have high similarity\n"
            f"Expected: > 0.95, Got: {sim}\n"
            f"Hint: These vectors are almost parallel"
        )
    print(f"Test 3 passed: similar vectors -> {sim:.2f}")

    print("\nAll tests passed! You've implemented cosine similarity correctly.")
    print("This is the foundation of semantic search in RAG systems.")


if __name__ == "__main__":
    main()
