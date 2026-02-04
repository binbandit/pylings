"""
lambda1.py - Lambda Functions

Lambdas are small anonymous functions defined in one line:

    lambda arguments: expression

They're useful for short operations, especially with map(), filter(), sorted():

    # Regular function
    def double(x):
        return x * 2

    # Same as lambda
    double = lambda x: x * 2

    # Common use with sorted()
    names = ["Bob", "Alice", "Charlie"]
    sorted(names, key=lambda x: len(x))  # Sort by length

Your task: Create a lambda function called `double` that takes one
argument and returns that argument multiplied by 2.
"""


def main():
    # TODO: Define a lambda function that doubles its input
    double = None

    if double is None:
        raise Exception("Define the 'double' lambda function!")

    # Test the lambda
    if double(5) != 10:
        raise Exception(f"double(5) should be 10, got {double(5)}")
    if double(0) != 0:
        raise Exception(f"double(0) should be 0, got {double(0)}")
    if double(-3) != -6:
        raise Exception(f"double(-3) should be -6, got {double(-3)}")

    print(f"double(5) = {double(5)}")
    print(f"double(100) = {double(100)}")
    print("Lambda functions work!")


if __name__ == "__main__":
    main()
