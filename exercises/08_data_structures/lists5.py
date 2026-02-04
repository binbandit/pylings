"""
Concept: List Comprehensions (Introduction)

What:
List comprehensions are a concise, "Pythonic" way to create lists from
existing iterables. They combine a for-loop and list creation into one line.

Why:
- More readable than multi-line loops for simple transformations
- Often faster than equivalent for-loops with .append()
- Considered a Pythonic best practice for list creation

How:
Basic syntax: `[expression for item in iterable]`
With filter:  `[expression for item in iterable if condition]`

Examples:
    # Double each number
    [x * 2 for x in [1, 2, 3]]          # [2, 4, 6]

    # Square of even numbers only
    [x**2 for x in range(6) if x % 2 == 0]  # [0, 4, 16]

    # Equivalent long form:
    result = []
    for x in range(6):
        if x % 2 == 0:
            result.append(x**2)

Task:
Create a list comprehension that generates squares of EVEN numbers from `nums`.
- Use `x**2` for squaring
- Use `x % 2 == 0` to check if a number is even
"""


def main():
    nums = [1, 2, 3, 4, 5]

    # TODO: Create a list with squares of even numbers using list comprehension
    # Format: [expression for x in nums if condition]
    squares = []

    # Verification
    expected = [4, 16]  # 2**2=4, 4**4=16 (only 2 and 4 are even)

    if squares == []:
        raise Exception("squares is empty! Use a list comprehension.")

    if squares != expected:
        raise Exception(
            f"Expected {expected}, got {squares}\n"
            "Hint: [x**2 for x in nums if x is even]"
        )

    print("List comprehension successful!")


if __name__ == "__main__":
    main()
