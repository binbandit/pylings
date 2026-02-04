"""
Concept: Lists (Appending)

What:
The `.append()` method adds a single item to the END of a list.
This modifies the list in-place (it doesn't return a new list).

Why:
Appending is one of the most common list operations. You use it when building
up a list dynamically, like adding items one at a time from user input or
from reading a file.

How:
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)  # [1, 2, 3, 4]

    # Common mistake - append returns None, not the list!
    result = numbers.append(5)  # result is None

    # Another method: .extend() adds multiple items
    numbers.extend([6, 7])  # [1, 2, 3, 4, 5, 6, 7]

Task:
Use the `.append()` method to add the number 6 to the end of the `numbers` list.
"""


def main():
    numbers = [1, 2, 3, 4, 5]

    # TODO: Append the number 6 to the list using .append()

    # Verification
    if len(numbers) == 5:
        raise Exception("The list still has 5 items. Did you forget to append 6?")

    if len(numbers) != 6:
        raise Exception(f"Expected 6 items, but got {len(numbers)}")

    if numbers[-1] != 6:
        raise Exception(f"The last item should be 6, got {numbers[-1]}")

    print("Successfully appended 6 to the list!")


if __name__ == "__main__":
    main()
