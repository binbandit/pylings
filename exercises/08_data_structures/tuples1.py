"""
Concept: Tuples

What:
Tuples are ordered collections of items, similar to lists.
The KEY difference: tuples are **immutable** - once created, they cannot be changed.
Tuples are created using parentheses `()` or just commas.

Why:
- Use tuples for data that shouldn't change (coordinates, RGB colors, database records)
- Tuples are slightly faster and use less memory than lists
- Tuples can be used as dictionary keys (lists cannot!)
- They signal intent: "this data is fixed"

How:
    # Creating tuples
    point = (10, 20)
    colors = ("red", "green", "blue")
    single = (42,)          # Note the comma for single-item tuple!
    also_tuple = 1, 2, 3    # Parentheses are optional

    # Accessing elements (same as lists)
    x = point[0]            # 10
    color = colors[1]       # "green"

    # Unpacking (very useful!)
    x, y = point            # x=10, y=20

    # Cannot modify!
    point[0] = 5            # TypeError: tuples don't support item assignment

Task:
1. Create a tuple named `my_tuple` containing "apple", "banana", and "cherry"
2. Access the second element (index 1) and assign it to variable `item`
"""


def main():
    # TODO: Create a tuple with "apple", "banana", "cherry"
    my_tuple = None

    # TODO: Get the second element (index 1) from my_tuple
    item = None

    # Verification
    if my_tuple is None:
        raise Exception(
            "my_tuple is None! Create a tuple: ('apple', 'banana', 'cherry')"
        )

    if not isinstance(my_tuple, tuple):
        raise Exception(
            f"my_tuple should be a tuple, but got {type(my_tuple).__name__}.\n"
            "Use parentheses: (item1, item2, item3)"
        )

    if len(my_tuple) != 3:
        raise Exception(f"my_tuple should have 3 elements, got {len(my_tuple)}")

    if item is None:
        raise Exception("item is None! Access the tuple: my_tuple[1]")

    if item != "banana":
        raise Exception(f"Expected item to be 'banana', got '{item}'")

    # Demonstrate immutability (this should fail)
    try:
        my_tuple[0] = "orange"
        raise Exception("Tuples should be immutable, but modification succeeded!")
    except TypeError:
        pass  # This is expected - tuples can't be modified

    print("Tuple exercise completed successfully!")


if __name__ == "__main__":
    main()
