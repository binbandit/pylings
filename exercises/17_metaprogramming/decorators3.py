"""
Concept: Preserving Function Metadata with functools.wraps

When you wrap a function with a decorator, the wrapper function REPLACES the
original. This causes a problem: the original function's metadata is lost!

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    '''Says hello'''
    print("Hello!")

print(greet.__name__)  # Prints 'wrapper', not 'greet'!
print(greet.__doc__)   # Prints None, not 'Says hello'!
```

Why this matters:
- Debugging: Stack traces show 'wrapper' instead of actual function names
- Documentation: help(greet) shows wrong information
- Introspection: Code that relies on __name__ or __doc__ breaks

The solution: `@functools.wraps(func)`

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # <-- This copies metadata from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

`functools.wraps` copies these attributes from the original function:
- __name__: The function's name
- __doc__: The docstring
- __module__: The module where the function was defined
- __qualname__: The qualified name
- __annotations__: Type annotations

Task:
Fix the `logged` decorator by adding `@functools.wraps(func)` so that the
decorated function `add` preserves its original name and docstring.
"""

import functools


def logged(func):
    """A decorator that prints when a function is called."""

    # TODO: Add @functools.wraps(func) on the line before 'def wrapper'
    # This decorator should go ABOVE the wrapper function definition
    def wrapper(*args, **kwargs):
        """This is the wrapper's docstring - it should NOT appear on add()"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logged
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b


def main():
    # Test that the function still works
    result = add(2, 3)
    if result != 5:
        raise AssertionError(f"add(2, 3) should return 5, got {result}")

    # Check if the function name was preserved
    if add.__name__ != "add":
        raise AssertionError(
            f"Function name is '{add.__name__}', but should be 'add'.\n"
            "The decorator replaced the original function's metadata!\n"
            "Fix: Add @functools.wraps(func) above 'def wrapper':\n\n"
            "    def logged(func):\n"
            "        @functools.wraps(func)  # <-- Add this line\n"
            "        def wrapper(*args, **kwargs):\n"
            "            ..."
        )

    # Check if the docstring was preserved
    expected_doc = "Returns the sum of two numbers."
    if add.__doc__ != expected_doc:
        raise AssertionError(
            f"Docstring is '{add.__doc__}', but should be '{expected_doc}'.\n"
            "The decorator replaced the original function's docstring!\n"
            "Use @functools.wraps(func) to preserve metadata."
        )

    print("Function metadata preserved correctly!")
    print(f"  Name: {add.__name__}")
    print(f"  Doc:  {add.__doc__}")


if __name__ == "__main__":
    main()
