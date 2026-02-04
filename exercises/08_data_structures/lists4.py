"""
Concept: List Slicing

What:
Slicing extracts a portion of a list using the syntax `list[start:end]`.
- `start` is the index where the slice begins (inclusive)
- `end` is the index where the slice ends (exclusive)

Why:
Slicing is a powerful Pythonic feature for extracting sublists without
modifying the original. It's used for pagination, getting recent items,
splitting data, and much more.

How:
    numbers = [10, 20, 30, 40, 50]
    #          0   1   2   3   4   <- indices

    numbers[1:4]   # [20, 30, 40]  - index 1, 2, 3 (not 4!)
    numbers[:3]    # [10, 20, 30]  - from start to index 3
    numbers[2:]    # [30, 40, 50]  - from index 2 to end
    numbers[-2:]   # [40, 50]      - last 2 items
    numbers[::2]   # [10, 30, 50]  - every 2nd item (step=2)
    numbers[::-1]  # [50, 40, 30, 20, 10]  - reversed!

Task:
Use slicing to extract the middle three elements [20, 30, 40] from the list.
Assign the result to the variable `middle`.
"""


def main():
    numbers = [10, 20, 30, 40, 50]
    #          0   1   2   3   4   <- use these indices!

    # TODO: Use slicing to get [20, 30, 40]
    # Hint: What index does 20 start at? What index comes AFTER 40?
    middle = []

    # Verification
    if middle == []:
        raise Exception("middle is empty! Use slicing: numbers[start:end]")

    if middle != [20, 30, 40]:
        raise Exception(f"Expected [20, 30, 40], got {middle}")

    print("Slicing successful!")


if __name__ == "__main__":
    main()
