"""
Concept: Lists (Removal)

What:
Python lists have several ways to remove items:
- `.remove(value)` - Removes the FIRST occurrence of the value
- `.pop(index)` - Removes and returns the item at the given index (default: last item)
- `del list[index]` - Deletes item at index (statement, not method)

Why:
Removing items is essential for managing dynamic collections, like removing
completed tasks from a todo list or deleting invalid entries from data.

How:
    items = ["a", "b", "c", "b"]

    # Remove by value (first occurrence only)
    items.remove("b")      # ["a", "c", "b"]

    # Remove by index and get the value
    last = items.pop()     # Returns "b", items is now ["a", "c"]
    first = items.pop(0)   # Returns "a", items is now ["c"]

    # Note: .remove() raises ValueError if the item doesn't exist!
    # items.remove("z")  # ValueError: list.remove(x): x not in list

Task:
Remove "paper" from the list using the `.remove()` method.
"""


def main():
    items = ["rock", "paper", "scissors"]

    # TODO: Remove "paper" from the list using .remove()

    # Verification
    if "paper" in items:
        raise Exception("'paper' is still in the list! Use items.remove('paper')")

    if len(items) != 2:
        raise Exception(f"Expected 2 items remaining, got {len(items)}")

    if items != ["rock", "scissors"]:
        raise Exception(f"Expected ['rock', 'scissors'], got {items}")

    print("Successfully removed 'paper' from the list!")


if __name__ == "__main__":
    main()
