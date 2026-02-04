"""
Concept: Typing (Generic Collections)

When you have a list or dictionary, you can specify what types they contain.
This is called "generic typing" because `List` and `Dict` are generic types
that take type parameters.

Syntax:
    from typing import List, Dict

    names: List[str] = ["Alice", "Bob"]
    scores: Dict[str, int] = {"Alice": 100, "Bob": 95}

For function parameters:
    def process(items: List[int]) -> None:
        ...

    def lookup(data: Dict[str, float]) -> float:
        ...

Note: In Python 3.9+, you can also use `list[str]` and `dict[str, int]`
directly without importing from typing.

Task:
Add type hints to the `process_data` function:
1. `names` should be a List of strings (List[str])
2. `scores` should be a Dict mapping strings to integers (Dict[str, int])
3. Return type should be None
"""

from typing import List, Dict


# TODO: Add type hints to both parameters and the return type
# Hint: def func(param: List[ElementType], other: Dict[KeyType, ValueType]) -> ReturnType:
def process_data(names, scores):
    """Process a list of names and their corresponding scores."""
    for name in names:
        if name in scores:
            print(f"{name}: {scores[name]}")


def main():
    # Test data
    test_names = ["Alice", "Bob", "Charlie"]
    test_scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

    # Function should work correctly
    process_data(test_names, test_scores)

    # Verify type hints exist
    annotations = process_data.__annotations__

    if not annotations:
        raise Exception(
            "No type hints found!\n"
            "Add type hints for 'names', 'scores', and the return type."
        )

    if "names" not in annotations:
        raise Exception(
            "Parameter 'names' needs a type hint.\n"
            "It should be List[str] - a list of strings."
        )

    if "scores" not in annotations:
        raise Exception(
            "Parameter 'scores' needs a type hint.\n"
            "It should be Dict[str, int] - a dictionary mapping strings to integers."
        )

    if "return" not in annotations:
        raise Exception(
            "Add a return type hint.\n"
            "Since the function doesn't return anything, use -> None"
        )

    print("Generic collection types added correctly!")


if __name__ == "__main__":
    main()
