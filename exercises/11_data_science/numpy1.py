"""
Concept: NumPy Arrays and Element-wise Operations

NumPy is the fundamental package for numerical computing in Python. Its main
object is the ndarray (N-dimensional array), which is much faster than Python
lists for numerical operations.

Key concepts:
- `np.array([1, 2, 3])` - Create an array from a Python list
- Arrays support element-wise operations (no loops needed!)
- `arr * 2` multiplies every element by 2
- `arr + 10` adds 10 to every element
- `arr ** 2` squares every element

Why NumPy over lists?
    # With lists (slow, verbose):
    result = [x * 2 for x in my_list]

    # With NumPy (fast, clean):
    result = my_array * 2

Example:
    import numpy as np
    prices = np.array([10.0, 20.0, 30.0])
    discounted = prices * 0.9  # 10% off: [9.0, 18.0, 27.0]

Task:
    1. Create a NumPy array containing [1, 2, 3]
    2. Multiply every element by 2 to get [2, 4, 6]
"""

import numpy as np


def main():
    # TODO: Create a numpy array with values [1, 2, 3]
    # Hint: Use np.array() with a list
    arr = None

    # Verification for array creation
    if arr is None:
        raise Exception("arr is None! Create an array using np.array([1, 2, 3])")

    if not isinstance(arr, np.ndarray):
        raise Exception(
            f"arr should be a numpy.ndarray, got {type(arr).__name__}\n"
            "Use np.array() to create it!"
        )

    if arr.tolist() != [1, 2, 3]:
        raise Exception(f"Array should contain [1, 2, 3], got {arr.tolist()}")

    # TODO: Multiply every element in arr by 2
    # Hint: NumPy allows element-wise operations: arr * 2
    doubled = None

    # Verification for element-wise multiplication
    if doubled is None:
        raise Exception("doubled is None! Use arr * 2 for element-wise multiplication")

    if not isinstance(doubled, np.ndarray):
        raise Exception(
            f"doubled should be a numpy.ndarray, got {type(doubled).__name__}"
        )

    if doubled.tolist() != [2, 4, 6]:
        raise Exception(
            f"Expected [2, 4, 6] after doubling, got {doubled.tolist()}\n"
            "Did you multiply by 2?"
        )

    print("NumPy arrays verified!")
    print(f"Original array: {arr}")
    print(f"Doubled array:  {doubled}")
    print(f"Sum of doubled: {doubled.sum()}")


if __name__ == "__main__":
    main()
