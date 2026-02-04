"""
Concept: Decorators (Basic)

A decorator is a function that takes another function and extends its behavior
without explicitly modifying it. Decorators "wrap" the original function in
another function.

Syntax: Place `@decorator_name` above the function definition.

Why use decorators?
- Logging: Track when functions are called
- Authentication: Check permissions before executing
- Caching: Store results of expensive operations
- Timing: Measure function execution time

How decorators work:
```python
def my_decorator(func):
    def wrapper():
        print("Something before")
        func()  # Call the original function
        print("Something after")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

# When you call greet(), it actually calls wrapper()
# which prints "Something before", then "Hello!", then "Something after"
```

The `@decorator` syntax is equivalent to:
```python
greet = my_decorator(greet)
```

Task:
Complete the `logger` decorator so that when the decorated function runs:
1. "Before" is appended to the `log` list
2. The original function is called
3. "After" is appended to the `log` list
"""

# This list will track the order of operations
log = []


def logger(func):
    """A decorator that logs 'Before' and 'After' around function calls."""

    def inner():
        # TODO: Append "Before" to the log list
        # TODO: Call the original function (func)
        # TODO: Append "After" to the log list
        pass  # Remove this line when you implement the solution

    return inner


@logger
def do_work():
    """The function being decorated - it logs 'Working' when called."""
    log.append("Working")


def main():
    # Clear the log before testing
    log.clear()

    # Call the decorated function
    do_work()

    # Verify the decorator worked correctly
    expected = ["Before", "Working", "After"]

    if len(log) == 0:
        raise AssertionError(
            "The log is empty! Your decorator's inner() function needs to:\n"
            "  1. Append 'Before' to log\n"
            "  2. Call func()\n"
            "  3. Append 'After' to log"
        )

    if log != expected:
        raise AssertionError(
            f"Expected log to be {expected}, but got {log}\n"
            "Make sure your decorator appends 'Before', calls the function, "
            "then appends 'After'"
        )

    print("Decorator working correctly!")
    print(f"Log contents: {log}")


if __name__ == "__main__":
    main()
