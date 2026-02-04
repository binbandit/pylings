"""
Concept: List Comprehensions (Advanced)

What:
List comprehensions create new lists by applying an expression to each item
in an iterable, optionally filtering with a condition.

Syntax: `[expression for item in iterable if condition]`

Why:
- Cleaner and more readable than multi-line for-loops
- Often faster due to Python's internal optimizations
- A Pythonic best practice - experienced Python devs use them constantly

How:
    # Basic: transform each item
    doubled = [x * 2 for x in range(5)]        # [0, 2, 4, 6, 8]

    # With condition: filter items
    evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

    # Combined: transform AND filter
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    # [0, 4, 16, 36, 64]

    # Nested comprehensions (less common)
    matrix = [[1, 2], [3, 4]]
    flat = [num for row in matrix for num in row]  # [1, 2, 3, 4]

Task:
Create a list called `squares` that contains the square (x**2) of every
EVEN number from 0 to 9.

Even numbers: 0, 2, 4, 6, 8
Their squares: 0, 4, 16, 36, 64
"""


def main():
    # TODO: Create a list comprehension for squares of even numbers 0-9
    # [x**2 for x in range(10) if <condition for even>]
    squares = []

    expected = [0, 4, 16, 36, 64]  # 0^2, 2^2, 4^2, 6^2, 8^2

    # Verification
    if squares == []:
        raise Exception(
            "squares is empty! Use a list comprehension:\n"
            "[expression for x in range(10) if condition]"
        )

    if squares != expected:
        raise Exception(
            f"Expected {expected}, got {squares}\n"
            "Check: x**2 for squaring, x % 2 == 0 for even check"
        )

    print("List comprehension mastered!")


if __name__ == "__main__":
    main()
