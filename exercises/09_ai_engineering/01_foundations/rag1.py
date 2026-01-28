"""
Concept: RAG (Cosine Similarity)
Retrieval Augmented Generation relies on finding similar text vectors. Cosine similarity measures the angle between two vectors (closer to 1 means more similar).

Task: Calculate the cosine similarity using `dot(a, b) / (norm(a) * norm(b))`.
"""

import numpy as np

def cosine_similarity(v1, v2):
    # FIX ME: Implement dot product / (norm(v1) * norm(v2))
    # return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return 0.0

def main():
    v1 = np.array([1, 0, 0])
    v2 = np.array([1, 0, 0])
    
    sim = cosine_similarity(v1, v2)
    
    if not np.isclose(sim, 1.0):
        raise Exception(f"Identical vectors should have similarity 1.0, got {sim}")
        
    v3 = np.array([0, 1, 0])
    sim = cosine_similarity(v1, v3)
    
    if not np.isclose(sim, 0.0):
        raise Exception(f"Orthogonal vectors should have similarity 0.0, got {sim}")

if __name__ == "__main__":
    main()
