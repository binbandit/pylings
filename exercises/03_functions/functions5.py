"""
functions5.py - Type Hints

Type hints document what types a function expects and returns. They don't
enforce types at runtime but help with readability and IDE support:

    def add(a: int, b: int) -> int:
        return a + b

Common type hints:
- int, float, str, bool - basic types
- list, dict, tuple - collections
- -> None - function doesn't return anything useful

Your task: Add type hints to the `divide` function. It takes two floats
and returns a float.
"""


# TODO: Add type hints - both parameters are floats, return type is float
def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def main():
    result = divide(10.0, 2.0)
    print(f"10.0 / 2.0 = {result}")

    # Check that type hints were added
    hints = getattr(divide, "__annotations__", {})

    if "a" not in hints:
        raise Exception("Missing type hint for parameter 'a'")
    if "b" not in hints:
        raise Exception("Missing type hint for parameter 'b'")
    if "return" not in hints:
        raise Exception("Missing return type hint (use -> float)")

    if hints.get("a") != float:
        raise Exception(
            f"Parameter 'a' should be hinted as float, got {hints.get('a')}"
        )
    if hints.get("b") != float:
        raise Exception(
            f"Parameter 'b' should be hinted as float, got {hints.get('b')}"
        )
    if hints.get("return") != float:
        raise Exception(f"Return type should be float, got {hints.get('return')}")

    print("Type hints added correctly!")


if __name__ == "__main__":
    main()
