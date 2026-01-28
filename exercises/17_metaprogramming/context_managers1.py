"""
Concept: Context Managers

What:
Context managers allow you to allocate and release resources strictly. 
They are what powers the `with` statement.
To make a class a context manager, implement `__enter__` and `__exit__`.

Why:
Commonly used for opening files (`open()`), network connections, or acquiring locks.
It guarantees cleanup (closing the file) happens even if an error occurs.

How:
```python
class MyContext:
    def __enter__(self):
        print("Entering context...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")
        # Return True to suppress exceptions, False to let them propagate
```

Task:
Implement `__enter__` to print "Start" and `__exit__` to print "End" in the `Timer` class.
"""

class Timer:
    # FIX ME: Implement __enter__
    # def __enter__(self):
    #     print("Start")
    #     return self
    
    # FIX ME: Implement __exit__
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print("End")
    pass

def main():
    t = Timer()
    
    if not hasattr(t, '__enter__'):
        raise Exception("Missing __enter__ method")
    
    if not hasattr(t, '__exit__'):
        raise Exception("Missing __exit__ method")

    print("Testing Timer...")
    with Timer():
        print("  Inside block")
    
    # Ideally we'd capture stdout to verify "Start" and "End" printed,
    # but existence of methods is a good start for this check.

if __name__ == "__main__":
    main()
