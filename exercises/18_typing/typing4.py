"""
Concept: Advanced Typing (Callable and Any)

Callable describes the type of a function:
    from typing import Callable

    # A function that takes two ints and returns a bool
    Callable[[int, int], bool]

    # A function that takes no arguments and returns str
    Callable[[], str]

Any is a special type that accepts anything:
    from typing import Any

    def log_value(value: Any) -> None:
        print(value)  # Works with any type

Callable is useful when passing functions as arguments (callbacks):
    def apply_twice(func: Callable[[int], int], x: int) -> int:
        return func(func(x))

Task:
Add type hints to the `transform` function:
1. `func` is a Callable that takes an int and returns an int: Callable[[int], int]
2. `value` can be Any type
3. Return type is int
"""

from typing import Callable, Any


# TODO: Add type hints for func, value, and return type
# Hint: func is Callable[[int], int] - takes int, returns int
# Hint: value is Any - can be anything
# Hint: return type is int
def transform(func, value):
    """
    Apply a transformation function to a value.
    The value is converted to int before applying the function.
    """
    return func(int(value))


def square(x: int) -> int:
    """Return the square of x."""
    return x * x


def triple(x: int) -> int:
    """Return triple of x."""
    return x * 3


def main():
    # Test with different functions and value types
    result1 = transform(square, 5)
    result2 = transform(triple, "4")  # String that can be converted to int
    result3 = transform(square, 3.7)  # Float converted to int (3)

    if result1 != 25:
        raise Exception(f"transform(square, 5) should return 25, got {result1}")
    if result2 != 12:
        raise Exception(f"transform(triple, '4') should return 12, got {result2}")
    if result3 != 9:
        raise Exception(f"transform(square, 3.7) should return 9, got {result3}")

    # Verify type hints
    annotations = transform.__annotations__

    if not annotations:
        raise Exception(
            "No type hints found!\n"
            "Add type hints for 'func', 'value', and the return type."
        )

    if "func" not in annotations:
        raise Exception(
            "Parameter 'func' needs a type hint.\n"
            "It's a function that takes int and returns int: Callable[[int], int]"
        )

    if "value" not in annotations:
        raise Exception(
            "Parameter 'value' needs a type hint.\nIt can be any type, so use Any."
        )

    if "return" not in annotations:
        raise Exception("Add a return type hint.\nThe function returns an int.")

    print("Callable and Any types used correctly!")


if __name__ == "__main__":
    main()
