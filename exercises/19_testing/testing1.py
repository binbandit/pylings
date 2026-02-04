"""
Concept: Testing with Assert

The `assert` statement is Python's simplest testing tool. It checks if a
condition is True. If the condition is False, it raises an AssertionError.

Syntax:
    assert condition
    assert condition, "Error message if False"

Examples:
    x = 5
    assert x > 0           # Passes silently (x is greater than 0)
    assert x == 5          # Passes silently
    assert x == 10         # Raises AssertionError!
    assert x == 10, "x should be 10"  # AssertionError with message

Why use assert?
- Quick sanity checks during development
- Simple unit tests
- Documenting assumptions in your code

Task:
Complete the test functions by writing assert statements that verify:
1. test_addition: add(2, 3) equals 5
2. test_subtraction: subtract(10, 4) equals 6
3. test_multiply_negative: multiply(-3, 4) equals -12
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def test_addition():
    """Test that add() works correctly."""
    result = add(2, 3)
    # TODO: Write an assert statement to check that result equals 5
    # Hint: assert result == expected_value, "Error message"
    pass


def test_subtraction():
    """Test that subtract() works correctly."""
    result = subtract(10, 4)
    # TODO: Write an assert statement to check that result equals 6
    pass


def test_multiply_negative():
    """Test that multiply() works with negative numbers."""
    result = multiply(-3, 4)
    # TODO: Write an assert statement to check that result equals -12
    pass


def main():
    # Run all tests
    tests = [
        ("test_addition", test_addition),
        ("test_subtraction", test_subtraction),
        ("test_multiply_negative", test_multiply_negative),
    ]

    for test_name, test_func in tests:
        try:
            test_func()
            # Check if the test actually has an assert (not just pass)
            import dis
            import io
            import contextlib

            # Get the bytecode as string
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                dis.dis(test_func)
            bytecode = f.getvalue()

            # Check if there's a comparison operation (indicates assert)
            if "COMPARE_OP" not in bytecode and "CONTAINS_OP" not in bytecode:
                raise Exception(
                    f"{test_name}: No assert statement found!\n"
                    "Replace 'pass' with an assert statement.\n"
                    "Example: assert result == 5, 'Result should be 5'"
                )

            print(f"  {test_name} passed!")
        except AssertionError as e:
            raise Exception(f"{test_name} failed: {e}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
