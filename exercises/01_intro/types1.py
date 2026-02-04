"""
types1.py - Basic Types and Type Conversion

Python has several basic types:
- `int`: Whole numbers like 10, -5, 0
- `float`: Decimal numbers like 3.14, -0.01
- `str`: Text strings like "Hello"
- `bool`: Truth values True or False

You often need to convert between types. For example, input from users
comes as strings, but you might need to do math with it.

Type conversion functions:
- int("123")  -> converts string to integer 123
- str(456)    -> converts integer to string "456"
- float("3.14") -> converts string to float 3.14

Your task:
1. Convert `num_string` (which is "123") to an integer
2. Add 10 to it
3. Convert the result back to a string and store in `result_string`
"""


def main():
    num_string = "123"

    # TODO: Convert num_string to an integer and store in `number`
    number = None

    # TODO: Add 10 to number (reassign to number)

    # TODO: Convert number back to a string and store in `result_string`
    result_string = None

    print(f"Result: {result_string}")

    # Verification
    if not isinstance(number, int):
        raise Exception("number should be an integer! Use int() to convert.")
    if number != 133:
        raise Exception(f"Expected number to be 133, got {number}. Did you add 10?")
    if not isinstance(result_string, str):
        raise Exception("result_string should be a string! Use str() to convert.")
    if result_string != "133":
        raise Exception(f"Expected result_string to be '133', got '{result_string}'")

    print("Great job! You've mastered type conversion!")


if __name__ == "__main__":
    main()
