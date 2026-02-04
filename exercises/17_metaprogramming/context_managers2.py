"""
Concept: Context Managers with @contextmanager

Writing a class with `__enter__` and `__exit__` can be verbose for simple cases.
The `@contextlib.contextmanager` decorator lets you write context managers as
generator functions - much more concise!

How it works:
- Everything BEFORE `yield` is the `__enter__` code (setup)
- The yielded value is what's available as `as variable`
- Everything AFTER `yield` is the `__exit__` code (cleanup)
- Use `try/finally` to ensure cleanup runs even on exceptions

Example:
```python
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield  # Control passes to the 'with' block here
    finally:
        end = time.time()
        print(f"Elapsed: {end - start:.2f}s")

with timer():
    do_something_slow()
# Prints: "Elapsed: 2.34s"
```

Yielding a value:
```python
@contextmanager
def open_file(path):
    f = open(path, 'r')
    try:
        yield f  # The file is available as 'as f'
    finally:
        f.close()  # Always close, even on error
```

Why use try/finally?
Without it, if an exception occurs in the `with` block, the cleanup code
after `yield` would never run!

Task:
Implement `managed_resource` using @contextmanager that:
1. Appends "acquired" to the `log` list (setup)
2. Yields the string "resource" (the value to use)
3. In a finally block, appends "released" to log (cleanup)
"""

from contextlib import contextmanager

# This list tracks resource lifecycle events
log = []


# TODO: Add the @contextmanager decorator
def managed_resource():
    """
    A context manager that simulates acquiring and releasing a resource.

    Usage:
        with managed_resource() as r:
            print(r)  # prints "resource"
        # "released" is logged even if an exception occurred
    """
    # TODO: Append "acquired" to log
    # TODO: Use try/finally structure
    # TODO: yield "resource" inside the try block
    # TODO: Append "released" to log in the finally block

    yield None  # Replace this with the correct implementation


def main():
    log.clear()

    # Test basic usage
    try:
        with managed_resource() as resource:
            if resource is None:
                raise AssertionError(
                    "Resource is None! You need to yield an actual value.\n"
                    "Change 'yield None' to 'yield \"resource\"'\n"
                    "And make sure to add the @contextmanager decorator!"
                )

            if resource != "resource":
                raise AssertionError(
                    f"Expected resource to be 'resource', got '{resource}'"
                )

            log.append("used")
    except TypeError as e:
        if "context manager protocol" in str(e) or "generator" in str(e):
            raise AssertionError(
                "The function is a generator but not a context manager!\n"
                "A plain generator cannot be used with 'with' statement.\n"
                "You need to add the @contextmanager decorator:\n\n"
                "    @contextmanager  # <-- Add this decorator\n"
                "    def managed_resource():\n"
                "        log.append('acquired')\n"
                "        try:\n"
                "            yield 'resource'\n"
                "        finally:\n"
                "            log.append('released')"
            ) from e
        raise

    expected = ["acquired", "used", "released"]

    if "acquired" not in log:
        raise AssertionError(
            "Log doesn't contain 'acquired'!\n"
            "Add: log.append('acquired') before the yield"
        )

    if "released" not in log:
        raise AssertionError(
            "Log doesn't contain 'released'!\n"
            "Add: log.append('released') in a finally block after yield"
        )

    if log != expected:
        raise AssertionError(
            f"Expected log to be {expected}, but got {log}\n"
            "Make sure the order is: acquire -> yield -> release"
        )

    # Test that cleanup happens even with exceptions
    log.clear()

    try:
        with managed_resource() as r:
            log.append("before_error")
            raise RuntimeError("Simulated error")
    except RuntimeError:
        pass  # Expected

    if "released" not in log:
        raise AssertionError(
            "Resource was not released when an exception occurred!\n"
            "You must use try/finally to ensure cleanup:\n\n"
            "    @contextmanager\n"
            "    def managed_resource():\n"
            "        log.append('acquired')\n"
            "        try:\n"
            "            yield 'resource'\n"
            "        finally:\n"
            "            log.append('released')"
        )

    print("Generator-based context manager working correctly!")
    print("The finally block ensures cleanup even on exceptions!")


if __name__ == "__main__":
    main()
