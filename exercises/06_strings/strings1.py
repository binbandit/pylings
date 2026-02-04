"""
strings1.py - String Concatenation

Strings can be combined (concatenated) using the `+` operator:

    first = "Hello"
    second = "World"
    combined = first + second  # "HelloWorld"

    # To add a space between:
    combined = first + " " + second  # "Hello World"

Your task: Combine `part1` and `part2` with a space between them to create
"Hello World".
"""


def main():
    part1 = "Hello"
    part2 = "World"

    # TODO: Concatenate part1 and part2 with a space between them
    result = part1 + part2  # This gives "HelloWorld" - needs a space!

    if result != "Hello World":
        raise Exception(f"Expected 'Hello World', got '{result}'. Add a space between!")

    print(result)
    print("String concatenation works!")


if __name__ == "__main__":
    main()
