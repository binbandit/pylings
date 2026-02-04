"""
Concept: collections.Counter

What:
`Counter` is a specialized dictionary for counting hashable objects.
It takes an iterable and returns a dictionary where keys are elements
and values are their counts.

Why:
- Counting frequency is an extremely common operation
- Manual counting with loops is verbose and error-prone
- Counter is optimized and provides useful methods like `.most_common()`
- Essential for many interview questions and data analysis tasks

How:
    from collections import Counter

    # Count characters in a string
    counts = Counter("hello")
    # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

    # Count items in a list
    votes = Counter(["yes", "no", "yes", "yes", "no"])
    # Counter({'yes': 3, 'no': 2})

    # Access counts like a dict
    print(counts['l'])           # 2
    print(counts['z'])           # 0 (not KeyError!)

    # Get most common items
    counts.most_common(2)        # [('l', 2), ('h', 1)]

    # Arithmetic operations
    Counter("aab") + Counter("bcc")  # Counter({'b': 2, 'a': 2, 'c': 2})

Task:
Use Counter to count the frequency of each character in "abracadabra".
Assign the result to `counts`.
"""

from collections import Counter


def main():
    text = "abracadabra"

    # TODO: Use Counter to count characters
    counts = None

    # Verification
    if counts is None:
        raise Exception("counts is None! Use Counter(text) to count characters.")

    if not isinstance(counts, Counter):
        raise Exception(
            f"counts should be a Counter, got {type(counts).__name__}\n"
            "Use: Counter(text)"
        )

    if counts["a"] != 5:
        raise Exception(f"Expected 5 'a's in 'abracadabra', got {counts['a']}")

    if counts["b"] != 2:
        raise Exception(f"Expected 2 'b's in 'abracadabra', got {counts['b']}")

    if counts["r"] != 2:
        raise Exception(f"Expected 2 'r's in 'abracadabra', got {counts['r']}")

    print(f"Character counts: {dict(counts)}")
    print("Counter exercise completed!")


if __name__ == "__main__":
    main()
