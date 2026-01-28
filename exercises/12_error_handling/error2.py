"""
Concept: Custom Exceptions
You can define your own exceptions by inheriting from the `Exception` class.

Task: Define `NegativeValueError` and raise it if `n` is negative.
"""

# FIX ME: Define a custom exception class named 'NegativeValueError'
# class NegativeValueError(Exception):
#     pass

class NegativeValueError(Exception):
    pass

def check_positive(n):
    if n < 0:
        # FIX ME: Raise the custom exception
        # raise NegativeValueError(f"{n} is negative!")
        pass
    return n

def main():
    try:
        check_positive(-5)
    except NegativeValueError:
        print("Caught expected error!")
        return

    raise Exception("Did not raise NegativeValueError for -5")

if __name__ == "__main__":
    main()
