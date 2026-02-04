"""
functions4.py - Default Parameters

Functions can have default parameter values, making those parameters optional:

    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Alice")           # Uses default: "Hello, Alice!"
    greet("Bob", "Hi")       # Override default: "Hi, Bob!"

Important: Parameters with defaults must come AFTER parameters without defaults.

Your task: Fix the `power` function. It should raise `base` to the `exponent`,
with `exponent` defaulting to 2 (squaring). Currently, the default is wrong.
"""


def power(base, exponent=1):
    """Raise base to the exponent power. Default exponent is 2 (square)."""
    return base**exponent


def main():
    # power(3) should return 9 (3 squared), but it's returning 3!
    result = power(3)
    if result != 9:
        raise Exception(
            f"power(3) should be 9 (3 squared), but got {result}. Check the default value!"
        )

    # power(2, 3) should return 8 (2 cubed)
    result = power(2, 3)
    if result != 8:
        raise Exception(f"power(2, 3) should be 8, got {result}")

    print("Default parameters work correctly!")


if __name__ == "__main__":
    main()
