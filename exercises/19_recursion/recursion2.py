"""
Concept: Recursion with Nested Structures

Recursion is perfect for processing nested data structures like:
- Lists containing other lists
- Dictionaries with nested dictionaries
- Tree-like data (JSON, XML, file systems)

The pattern:
1. Check if the current item needs recursion (e.g., is it a list?)
2. If yes, recurse into it
3. If no, process the item directly

Example - Count all items in nested lists:
    def count_items(data):
        total = 0
        for item in data:
            if isinstance(item, list):
                total += count_items(item)  # Recurse!
            else:
                total += 1
        return total

    count_items([1, [2, 3], [[4]]]) -> 4

Task: Implement flatten(nested_list)
    - Takes a list that may contain integers and other lists (any depth)
    - Returns a flat list with all integers in order

    Example:
        flatten([1, [2, [3, 4], 5], 6])
        -> [1, 2, 3, 4, 5, 6]
"""


def flatten(nested_list):
    """
    Flatten a nested list into a single list of integers.

    Example:
        flatten([1, [2, 3], [[4, 5]]]) -> [1, 2, 3, 4, 5]
        flatten([]) -> []
        flatten([1, 2, 3]) -> [1, 2, 3]  (already flat)
    """
    result = []

    # TODO: Iterate through each item in nested_list
    # For each item:
    #   - If the item is a list (use isinstance(item, list)),
    #     recursively flatten it and extend result
    #   - Otherwise, append the item to result
    #
    # Hint: result.extend(flatten(item)) adds all items from the flattened sublist
    # Hint: result.append(item) adds a single item

    return result


def main():
    # Test 1: Simple nested list
    print("Testing flatten...")

    input1 = [1, [2, [3, 4], 5], 6]
    expected1 = [1, 2, 3, 4, 5, 6]
    result1 = flatten(input1)

    if result1 != expected1:
        raise Exception(
            f"flatten({input1})\n"
            f"  Expected: {expected1}\n"
            f"  Got:      {result1}\n"
            "Hint: Check each item - if it's a list, recurse; otherwise append"
        )
    print(f"  flatten({input1}) = {result1}")

    # Test 2: Deeply nested
    input2 = [[[1], 2], [3]]
    expected2 = [1, 2, 3]
    result2 = flatten(input2)

    if result2 != expected2:
        raise Exception(
            f"flatten({input2})\n"
            f"  Expected: {expected2}\n"
            f"  Got:      {result2}\n"
            "Hint: Recursion handles any depth automatically!"
        )
    print(f"  flatten({input2}) = {result2}")

    # Test 3: Empty list
    input3 = []
    expected3 = []
    result3 = flatten(input3)

    if result3 != expected3:
        raise Exception(
            f"flatten({input3})\n  Expected: {expected3}\n  Got:      {result3}"
        )
    print(f"  flatten({input3}) = {result3}")

    # Test 4: Already flat
    input4 = [1, 2, 3]
    expected4 = [1, 2, 3]
    result4 = flatten(input4)

    if result4 != expected4:
        raise Exception(
            f"flatten({input4})\n  Expected: {expected4}\n  Got:      {result4}"
        )
    print(f"  flatten({input4}) = {result4}")

    # Test 5: Complex nesting
    input5 = [1, [], [2, [3, [4, [5]]]]]
    expected5 = [1, 2, 3, 4, 5]
    result5 = flatten(input5)

    if result5 != expected5:
        raise Exception(
            f"flatten({input5})\n  Expected: {expected5}\n  Got:      {result5}"
        )
    print(f"  flatten({input5}) = {result5}")

    print("\nNested list flattening mastered!")


if __name__ == "__main__":
    main()
