"""
variables1.py - Variables

Variables are containers for storing data values. In Python, you create
a variable by assigning a value to a name using the `=` operator:

    my_variable = 42
    greeting = "Hello"

Variable names:
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Are case-sensitive (name and Name are different)
- Cannot be Python keywords (like if, for, while, etc.)

Your task: Create a variable named `x` and assign it the value 5.
"""


def main():
    # TODO: Create a variable named `x` and assign it the value 5

    print(f"The value of x is: {x}")

    if x != 5:
        raise Exception(f"x should be 5, but got {x}")

    print("You've created your first variable!")


if __name__ == "__main__":
    main()
