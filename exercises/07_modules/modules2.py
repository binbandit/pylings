"""
Concept: Importing Specific Items from Modules (from ... import ...)

Instead of importing an entire module, you can import specific functions,
classes, or variables directly using:
    from module_name import item_name

This lets you use the item directly without the module prefix:
    from math import sqrt
    result = sqrt(16)  # No need for math.sqrt()

You can also import multiple items:
    from math import sqrt, pi, ceil

Or rename imports with `as`:
    from math import sqrt as square_root

Task:
Import the `say_hello` function from the `my_lib` module (located in the same
directory as this file).

The my_lib module contains a function called `say_hello` that returns a greeting.
"""

# TODO: Import the say_hello function from my_lib
# Hint: from ??? import ???


def main():
    # Call the imported function
    message = say_hello()

    expected = "Hello from my_lib!"
    if message != expected:
        raise AssertionError(f"Expected '{expected}', but got '{message}'")

    print(message)
    print("Successfully imported from a local module!")


if __name__ == "__main__":
    main()
