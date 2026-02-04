"""
Concept: Type Hints (Function Signatures)

Type hints are annotations that document what types a function expects and returns.
They help you catch bugs early and make your code self-documenting.

Syntax:
    def function_name(param: ParamType) -> ReturnType:
        ...

Example:
    def greet(name: str) -> str:
        return f"Hello, {name}!"

Type hints are checked by tools like `mypy`, but Python itself doesn't enforce them
at runtime. However, we can inspect them using `__annotations__`.

Task:
Add type hints to the `add` function:
1. Parameter `a` should be type `int`
2. Parameter `b` should be type `int`
3. Return type should be `int`
"""


# TODO: Add type hints to the parameters and return type
# Hint: def function(param: Type) -> ReturnType:
def add(a, b):
    return a + b


def main():
    # Test the function works correctly
    result = add(3, 5)
    if result != 8:
        raise Exception(f"add(3, 5) should return 8, got {result}")

    # Verify type hints exist
    annotations = add.__annotations__

    if not annotations:
        raise Exception(
            "No type hints found!\n"
            "Add type hints to the 'add' function parameters and return type.\n"
            "Example: def func(x: int) -> int:"
        )

    if annotations.get("a") is not int:
        raise Exception(
            "Parameter 'a' should have type hint 'int'\nExample: def add(a: int, ...)"
        )

    if annotations.get("b") is not int:
        raise Exception(
            "Parameter 'b' should have type hint 'int'\nExample: def add(..., b: int)"
        )

    if annotations.get("return") is not int:
        raise Exception("Return type should be 'int'\nExample: def add(...) -> int:")

    print("Type hints added correctly!")


if __name__ == "__main__":
    main()
