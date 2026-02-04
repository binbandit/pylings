"""
Concept: Creating Your Own Modules

A module is simply a Python file (.py) containing definitions (functions,
classes, variables) that you can import into other files.

Why create modules?
- Organize code into logical units
- Reuse code across multiple files
- Keep files manageable in size
- Share code with others

How it works:
1. Create a file like `my_utils.py` with functions
2. Import it in another file: `from my_utils import my_function`
3. Use the imported function normally

The `my_lib.py` file in this directory is a module you can import from.

Task:
This exercise has TWO parts:

Part 1: Edit the `my_lib.py` file in this same directory.
        Add a function called `calculate_area(length, width)` that returns
        the product of length and width (length * width).

Part 2: In THIS file, import the `calculate_area` function from `my_lib`
        and use it to calculate the area.

Hint: You'll need to edit TWO files to complete this exercise!
"""

# TODO: Import calculate_area from my_lib


def main():
    # TODO: Use the calculate_area function to compute the area
    # The function should multiply length by width
    length = 5
    width = 10

    area = None  # TODO: Replace None with a call to calculate_area(length, width)

    expected = 50
    if area != expected:
        raise AssertionError(
            f"Expected area to be {expected}, but got {area}.\n"
            "Did you:\n"
            "  1. Define calculate_area(length, width) in my_lib.py?\n"
            "  2. Import calculate_area from my_lib in this file?\n"
            "  3. Call calculate_area(length, width) and assign it to 'area'?"
        )

    print(f"Area of {length}x{width} rectangle = {area}")
    print("Successfully created and used a custom module!")


if __name__ == "__main__":
    main()
