"""
Concept: Lists (Creation)

What:
Lists are ordered, mutable collections of items in Python. They can hold any type
of data (strings, numbers, other lists, etc.) and allow duplicates.

Why:
Lists are the most commonly used data structure in Python. They're essential for
storing collections of related items, like a shopping list, a list of scores,
or a sequence of user inputs.

How:
You create a list using square brackets `[]` with items separated by commas:

    my_list = ["item1", "item2", "item3"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]

You can access items by index (0-based):
    first_item = my_list[0]   # "item1"
    second_item = my_list[1]  # "item2"

Task:
Create a list named `fruits` containing exactly three strings:
"apple", "banana", and "cherry" (in that order).
"""


def main():
    # TODO: Create a list of fruits with "apple", "banana", "cherry"
    fruits = []

    # Verification
    if len(fruits) == 0:
        raise Exception("The list is empty! Add the three fruits to it.")

    if len(fruits) != 3:
        raise Exception(
            f"Expected 3 items, but got {len(fruits)}. Add exactly three fruits."
        )

    if fruits[0] != "apple":
        raise Exception(f"First fruit should be 'apple', got '{fruits[0]}'")

    if fruits[1] != "banana":
        raise Exception(f"Second fruit should be 'banana', got '{fruits[1]}'")

    if fruits[2] != "cherry":
        raise Exception(f"Third fruit should be 'cherry', got '{fruits[2]}'")

    print("Fruit list created successfully!")


if __name__ == "__main__":
    main()
