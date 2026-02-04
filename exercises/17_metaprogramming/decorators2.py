"""
Concept: Decorators with Arguments

Sometimes you want to configure a decorator's behavior, like `@repeat(3)` to run
a function 3 times, or `@cache(maxsize=100)` to limit cache size.

To accept arguments, you need a THREE-LEVEL nested function structure:

1. Outer function: Takes the decorator arguments (e.g., `n`)
   - Returns the actual decorator

2. Decorator: Takes the function to decorate (`func`)
   - Returns the wrapper

3. Wrapper: Takes the function's arguments (`*args`, `**kwargs`)
   - Implements the actual behavior

Example:
```python
def repeat(n):                    # Level 1: Takes decorator argument
    def decorator(func):          # Level 2: Takes the function
        def wrapper(*args, **kwargs):  # Level 3: Takes function arguments
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

# say_hi() will print "Hi!" three times
```

Why `*args, **kwargs`?
- They allow the wrapper to accept ANY arguments
- This makes the decorator work with functions that have different signatures

Task:
Implement the `@repeat(n)` decorator that executes the decorated function `n` times.
The counter should increment to 3 after calling `increment()` with `@repeat(3)`.
"""

counter = 0


def repeat(n):
    """
    A decorator factory that creates a decorator to repeat function calls.

    Args:
        n: The number of times to repeat the function call

    Returns:
        A decorator that wraps functions to be called n times
    """
    # TODO: Define the decorator function that takes `func`
    # TODO: Inside decorator, define wrapper that takes `*args, **kwargs`
    # TODO: Inside wrapper, use a loop to call func() n times
    # TODO: Return wrapper from decorator
    # TODO: Return decorator from repeat

    return None  # Replace this with your implementation


@repeat(3)
def increment():
    """Increments the global counter by 1."""
    global counter
    counter += 1


def main():
    global counter
    counter = 0  # Reset counter

    # Try to call the decorated function
    try:
        increment()
    except TypeError as e:
        raise AssertionError(
            "repeat(3) returned None instead of a decorator!\n"
            "You need to return a decorator function from repeat().\n"
            "Structure:\n"
            "  def repeat(n):\n"
            "      def decorator(func):\n"
            "          def wrapper(*args, **kwargs):\n"
            "              # loop n times and call func\n"
            "          return wrapper\n"
            "      return decorator"
        ) from e

    if counter == 0:
        raise AssertionError(
            "Counter is still 0! The function was never called.\n"
            "Make sure your wrapper calls func() inside a loop."
        )

    if counter == 1:
        raise AssertionError(
            f"Counter is {counter}, but expected 3.\n"
            "The function was only called once. Did you implement the loop?\n"
            "Use: for _ in range(n): func(*args, **kwargs)"
        )

    if counter != 3:
        raise AssertionError(
            f"Counter is {counter}, but expected 3.\n"
            "Make sure you're looping exactly n times."
        )

    print("Decorator with arguments working correctly!")
    print(f"increment() was called {counter} times")


if __name__ == "__main__":
    main()
