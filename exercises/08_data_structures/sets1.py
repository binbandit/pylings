"""
Concept: Sets

What:
Sets are unordered collections of **unique** elements.
They automatically remove duplicates and don't maintain insertion order.
Sets are created using curly braces `{}` or the `set()` function.

Why:
- Automatically remove duplicates from data
- VERY fast membership testing: `if x in my_set` is O(1) vs O(n) for lists
- Mathematical set operations: union, intersection, difference
- Great for finding unique items or comparing collections

How:
    # Creating sets
    my_set = {1, 2, 3}
    from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3} - duplicates removed!
    empty_set = set()                  # Note: {} creates an empty DICT!

    # Adding elements
    my_set.add(4)                      # {1, 2, 3, 4}
    my_set.add(2)                      # {1, 2, 3, 4} - no change, 2 exists

    # Set operations
    a = {1, 2, 3}
    b = {2, 3, 4}
    a | b   # Union: {1, 2, 3, 4}
    a & b   # Intersection: {2, 3}
    a - b   # Difference: {1}

Task:
1. Create a set named `my_set` from `initial_list` (notice how duplicates vanish!)
2. Add the number 4 to the set using `.add()`
"""


def main():
    initial_list = [1, 2, 2, 3, 3, 3]

    # TODO: Create a set from initial_list using set()
    my_set = set()

    # TODO: Add the number 4 to the set using .add()

    # Verification
    if len(my_set) == 0:
        raise Exception(
            "my_set is empty! Create it from initial_list: set(initial_list)"
        )

    if not isinstance(my_set, set):
        raise Exception(f"my_set should be a set, got {type(my_set).__name__}")

    if 4 not in my_set:
        raise Exception("4 is not in the set! Use my_set.add(4)")

    if len(my_set) != 4:
        raise Exception(
            f"Expected 4 unique elements {{1, 2, 3, 4}}, got {len(my_set)} elements.\n"
            "Did you create the set from initial_list AND add 4?"
        )

    if my_set != {1, 2, 3, 4}:
        raise Exception(f"Expected {{1, 2, 3, 4}}, got {my_set}")

    print("Set exercise completed! Notice how duplicates were removed.")


if __name__ == "__main__":
    main()
