"""
functions3.py - Return Values

Functions can return values using the `return` keyword. The returned
value can be stored in a variable or used directly:

    def add(a, b):
        return a + b

    result = add(3, 4)  # result is 7
    print(add(10, 20))  # prints 30

Without a return statement, functions return `None` by default.

Your task: Fix the `square` function so it returns the square of the
input number (num * num), instead of returning None.
"""


def square(num):
    # TODO: Return the square of num
    result = num * num
    # Oops! We calculated the result but forgot to return it!


def main():
    answer = square(4)

    if answer is None:
        raise Exception("square() returned None! Did you forget to return the result?")

    if answer != 16:
        raise Exception(f"square(4) should be 16, got {answer}")

    print(f"The square of 4 is {answer}")
    print("Return values work!")


if __name__ == "__main__":
    main()
