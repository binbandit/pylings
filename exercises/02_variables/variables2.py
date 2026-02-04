"""
variables2.py - Variable Reassignment

Variables can be reassigned to new values at any time. Python doesn't
require you to declare types - a variable can even change types:

    x = 10      # x is an integer
    x = 20      # x is still an integer, but now 20
    x = "hello" # x is now a string (this is allowed!)

Type hints are optional annotations that help document your code:
    x: int = 10  # Tells readers x should be an integer

Your task: The variable `x` has a type hint saying it should be an int.
Assign the value 10 to `x` to make the program pass.
"""


def main():
    # TODO: Assign the value 10 to x
    x: int

    if x != 10:
        raise Exception(f"x should be 10, got {x}")

    print(f"x is {x}")
    print("Variable assignment complete!")


if __name__ == "__main__":
    main()
