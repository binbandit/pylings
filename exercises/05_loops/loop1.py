"""
loop1.py - For Loops

The `for` loop iterates over items in a sequence (list, string, etc.):

    for item in sequence:
        # do something with item

Example:
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

This prints each fruit on its own line.

Your task: Write a for loop that iterates over the `colors` list and
adds each color to the `result` list.
"""


def main():
    colors = ["red", "green", "blue"]
    result = []

    # TODO: Write a for loop that appends each color to result

    if len(result) == 0:
        raise Exception("result is empty! Write a for loop to add colors to it.")

    if result != colors:
        raise Exception(f"result should be {colors}, got {result}")

    print(f"Colors: {result}")
    print("For loops work!")


if __name__ == "__main__":
    main()
