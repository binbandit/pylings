"""
Concept: Try...Finally

What:
The `finally` block in a `try...except` statement contains code that **always** runs, 
no matter what happens (success, error, or even a return statement).

Why:
It is the "cleanup" block. If you open a database connection or a file, you MUST close it, 
even if your code crashes halfway through. `finally` guarantees this closure.

How:
```python
try:
    x = 1 / 0 # Crashes
except ZeroDivisionError:
    print("Caught error")
finally:
    print("This runs anyway!") 
```

Task:
Wrap the call to `process()` in a `try...finally` block.
Ensure that `cleanup()` is called in the `finally` block, so it runs even if `process()` crashes.
"""

cleaned_up = False

def cleanup():
    global cleaned_up
    cleaned_up = True

def process():
    raise ValueError("Something went wrong!")

def main():
    try:
        # FIX ME: Wrap this in try...finally to ensure cleanup() is called
        process()
    except ValueError:
        pass # Catch the error so we can check cleanup
    
    # Check if cleanup happened
    if not cleaned_up:
        raise Exception("Cleanup was not called! Did you use 'finally'?")

if __name__ == "__main__":
    main()
