"""
Concept: Preserving Metadata (functools.wraps)

What:
When you wrap a function with a decorator, the new function (the wrapper) replaces the original.
This means `my_func.__name__` becomes `wrapper`, and `my_func.__doc__` is lost.
`@functools.wraps(func)` copies this metadata back to the wrapper.

Why:
Debuggers, IDEs, and documentation tools rely on this metadata. 
If you write a library, your users will be confused if `help(my_func)` shows help for `wrapper`.

How:
```python
import functools

def my_decorator(func):
    @functools.wraps(func) # <--- Critical line
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Task:
1. Apply the `simple_decorator`.
2. Observe that `add.__name__` is wrong.
3. Fix it by applying `@functools.wraps(func)` inside the decorator.
"""

import functools

def simple_decorator(func):
    # FIX ME: Add @functools.wraps(func) here
    def wrapper(*args, **kwargs):
        """I am the wrapper"""
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def add(a, b):
    """Returns the sum of a and b"""
    return a + b

def main():
    # If functioning correctly, the name should be "add", not "wrapper"
    if add.__name__ != "add":
        raise Exception(f"Function name lost! Got '{add.__name__}', expected 'add'. Use functools.wraps.")
        
    if add.__doc__ != "Returns the sum of a and b":
        raise Exception("Docstring lost!")

if __name__ == "__main__":
    main()
