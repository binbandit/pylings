"""
Concept: Error Handling (Try/Except)

In Python, errors that occur during program execution are called "exceptions".
When an exception occurs, the program normally crashes with an error message.

However, you can use `try/except` blocks to "catch" these exceptions and handle
them gracefully instead of crashing. This is called exception handling.

Syntax:
    try:
        # Code that might raise an exception
        risky_operation()
    except SomeExceptionType:
        # Code that runs if the exception occurs
        handle_the_error()

Common exceptions include:
- ZeroDivisionError: Dividing by zero
- ValueError: Invalid value for an operation
- TypeError: Wrong type for an operation
- FileNotFoundError: File doesn't exist

Task: The code below crashes with a `ZeroDivisionError`. Wrap the division
in a try/except block that catches ZeroDivisionError and sets `result` to 0.
"""


def safe_divide(a, b):
    """Divide a by b, returning 0 if division by zero occurs."""
    # TODO: Wrap this division in a try/except block
    # TODO: Catch ZeroDivisionError and return 0 instead of crashing
    result = a / b
    return result


def main():
    # This should return 5.0 (normal division)
    normal_result = safe_divide(10, 2)
    if normal_result != 5.0:
        raise Exception(
            f"Expected safe_divide(10, 2) to return 5.0, got {normal_result}"
        )

    # This should return 0 (handled division by zero)
    zero_result = safe_divide(10, 0)
    if zero_result != 0:
        raise Exception(
            f"Expected safe_divide(10, 0) to return 0, got {zero_result}. "
            "Did you catch ZeroDivisionError?"
        )

    print("ZeroDivisionError handled correctly!")


if __name__ == "__main__":
    main()
