"""
loop6.py - Enumerate and Zip

Two helpful functions for looping:

enumerate(sequence) - gives you both index and item:
    names = ["Alice", "Bob"]
    for i, name in enumerate(names):
        print(f"{i}: {name}")  # 0: Alice, 1: Bob

zip(seq1, seq2) - pairs elements from multiple sequences:
    names = ["Alice", "Bob"]
    ages = [25, 30]
    for name, age in zip(names, ages):
        print(f"{name} is {age}")  # Alice is 25, Bob is 30

Your task:
1. Use enumerate() to build a list of (index, name) tuples
2. Use zip() to build a list of (name, age) tuples
"""


def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [24, 50, 18]

    # TODO: Use enumerate to create [(0, "Alice"), (1, "Bob"), (2, "Charlie")]
    indexed_names = []

    # TODO: Use zip to create [("Alice", 24), ("Bob", 50), ("Charlie", 18)]
    paired_data = []

    # Verification
    expected_indexed = [(0, "Alice"), (1, "Bob"), (2, "Charlie")]
    if indexed_names != expected_indexed:
        raise Exception(
            f"indexed_names should be {expected_indexed}, got {indexed_names}"
        )

    expected_paired = [("Alice", 24), ("Bob", 50), ("Charlie", 18)]
    if paired_data != expected_paired:
        raise Exception(f"paired_data should be {expected_paired}, got {paired_data}")

    print(f"Indexed: {indexed_names}")
    print(f"Paired: {paired_data}")
    print("Enumerate and zip work!")


if __name__ == "__main__":
    main()
