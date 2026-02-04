"""
functions2.py - Function Parameters

Functions can accept inputs called parameters (or arguments). You specify
them inside the parentheses when defining the function:

    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")  # Output: Hello, Alice!

Your task: Fix the function call so it passes an argument to the function.
The `call_me` function expects a `num` parameter, but it's being called
without one.
"""


def call_me(num):
    print(f"You called with: {num}")
    if num != 42:
        raise Exception(f"Expected 42, got {num}")


def main():
    # TODO: Fix this function call - it needs an argument!
    # Pass the number 42 to call_me
    call_me()
    print("Function arguments work!")


if __name__ == "__main__":
    main()
