"""
Concept: Dictionary Comprehensions

What:
Just like list comprehensions, you can create dictionaries in a single line
using the `{key: value for item in iterable}` syntax.

Why:
- Transform data into lookup tables efficiently
- Swap keys and values
- Filter or transform dictionary entries
- Create mappings from lists or other data

How:
    # Basic: create a mapping
    squares = {x: x**2 for x in range(5)}
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # From a list of items
    names = ["Alice", "Bob", "Charlie"]
    name_lengths = {name: len(name) for name in names}
    # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

    # With condition
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

    # Swapping keys and values
    original = {"a": 1, "b": 2}
    swapped = {v: k for k, v in original.items()}
    # {1: "a", 2: "b"}

Task:
Create a dictionary called `cubes` where:
- Keys are numbers from 0 to 4
- Values are the cube of each number (x**3)

Expected: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
"""


def main():
    # TODO: Create a dict comprehension: {x: x**3 for x in range(5)}
    cubes = {}

    expected = {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

    # Verification
    if cubes == {}:
        raise Exception(
            "cubes is empty! Use a dict comprehension:\n"
            "{key_expr: value_expr for x in range(5)}"
        )

    if cubes != expected:
        raise Exception(
            f"Expected {expected}, got {cubes}\nUse x as key and x**3 as value"
        )

    print("Dictionary comprehension mastered!")


if __name__ == "__main__":
    main()
