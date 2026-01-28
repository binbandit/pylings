"""
Concept: Context Managers with Generators

What:
Writing a class with `__enter__` and `__exit__` is verbose.
The `@contextlib.contextmanager` decorator allows you to define a context manager using a single generator function.
- Everything *before* the `yield` is `__enter__`.
- Everything *after* the `yield` is `__exit__`.

Why:
It drastically reduces boilerplate for simple setup/teardown logic.

How:
```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Enter")
    try:
        yield "resource" # The value returned to 'as var'
    finally:
        print("Exit") # Guaranteed to run
```

Task:
Implemented `file_opener` using `@contextmanager`.
1. Open the file.
2. Yield the file object.
3. Finally, close the file.
"""

from contextlib import contextmanager

# FIX ME: Decorate with @contextmanager
def file_opener(filename, mode):
    # FIX ME: Open file, yield it, then close it in finally block
    # f = open(filename, mode)
    # try:
    #     yield f
    # finally:
    #     f.close()
    yield None

def main():
    # We use a dummy file name. In a real scenario we'd create a tmp file.
    # For this exercise we just mock the open/close behavior or rely on exceptions?
    # Let's use a real file write for simplicity.
    
    fname = "test_ctx.txt"
    try:
        with file_opener(fname, "w") as f:
            if f is None:
                raise Exception("Yielded None! Did you implement the generator?")
            f.write("Hello")
            
        if not f.closed:
            raise Exception("File was not closed! Did you use try/finally?")
    except AttributeError:
        # f is None or generated logic incorrect
        pass
    except Exception as e:
        raise e
    finally:
        # Cleanup
        import os
        if os.path.exists(fname):
            os.remove(fname)

if __name__ == "__main__":
    main()
