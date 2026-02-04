"""
Concept: Magic Methods (Dunder Methods)

Python classes can define special methods with double underscores (called "dunder"
methods) to customize how objects behave with built-in operations.

Common magic methods:
- `__str__(self)`: Called by `str()` and `print()`. Returns a human-readable string.
- `__repr__(self)`: Called by `repr()`. Returns a developer-friendly string.
- `__eq__(self, other)`: Called by `==`. Returns True/False for equality.
- `__len__(self)`: Called by `len()`. Returns an integer length.
- `__add__(self, other)`: Called by `+`. Returns the result of addition.

Example:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

Task:
1. Implement `__str__` to return the format "Vector(x, y)" (e.g., "Vector(1, 2)")
2. Implement `__eq__` to return True when two vectors have the same x and y values
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: Implement __str__ to return "Vector(x, y)"
    def __str__(self):
        return None  # FIX ME: Return the correct string format

    # TODO: Implement __eq__ to compare two vectors by their coordinates
    def __eq__(self, other):
        return None  # FIX ME: Compare self.x/self.y with other.x/other.y


def main():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    v3 = Vector(3, 4)

    # Test __str__
    str_result = str(v1)
    if str_result != "Vector(1, 2)":
        raise Exception(
            f"__str__ returned '{str_result}', expected 'Vector(1, 2)'\n"
            'Hint: Use an f-string like f"Vector({self.x}, {self.y})"'
        )

    # Test __eq__ for equal vectors
    if not (v1 == v2):
        raise Exception(
            "v1 == v2 returned False, but they have the same coordinates!\n"
            "Hint: Compare both x and y values"
        )

    # Test __eq__ for different vectors
    if v1 == v3:
        raise Exception(
            "v1 == v3 returned True, but they have different coordinates!\n"
            "Hint: Make sure you're comparing BOTH x and y"
        )

    print("Magic methods working correctly!")


if __name__ == "__main__":
    main()
