"""
Concept: Raising Exceptions

Sometimes you need to signal that something went wrong in your code.
Python lets you "raise" exceptions to indicate errors.

Syntax:
    raise ExceptionType("Error message")

Examples:
    raise ValueError("Age cannot be negative")
    raise TypeError("Expected a string, got int")

You can also create custom exception classes by inheriting from Exception:

    class MyCustomError(Exception):
        pass

    raise MyCustomError("Something specific went wrong")

Custom exceptions are useful when you want to signal domain-specific errors
that the built-in exceptions don't cover well.

Task:
1. Define a custom exception class called `NegativeValueError`
2. In the `check_positive` function, raise `NegativeValueError` when n < 0
"""


# TODO: Define a custom exception class called 'NegativeValueError'
# It should inherit from Exception


def check_positive(n):
    """
    Check if n is positive.

    Args:
        n: A number to check

    Returns:
        n if it is positive (>= 0)

    Raises:
        NegativeValueError: If n is negative
    """
    # TODO: If n is negative, raise NegativeValueError with a message
    # TODO: Include the value of n in the error message
    return n


def main():
    # Test 1: Positive number should work fine
    result = check_positive(42)
    if result != 42:
        raise Exception(f"Expected check_positive(42) to return 42, got {result}")

    # Test 2: Zero should work fine
    result = check_positive(0)
    if result != 0:
        raise Exception(f"Expected check_positive(0) to return 0, got {result}")

    # Test 3: Negative number should raise NegativeValueError
    try:
        check_positive(-5)
        raise Exception(
            "Expected check_positive(-5) to raise NegativeValueError, but it didn't. "
            "Did you raise the exception for negative values?"
        )
    except NameError:
        raise Exception(
            "NegativeValueError is not defined. "
            "Did you create the custom exception class?"
        )
    except NegativeValueError:
        print("Correctly raised NegativeValueError for negative input!")


if __name__ == "__main__":
    main()
