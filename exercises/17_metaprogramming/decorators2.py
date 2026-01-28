"""
Concept: Decorators with Arguments

What:
Sometimes you want to pass configuration to your decorator, like `@repeat(3)` or `@timeout(30)`.
To do this, you need a **three-level** nested function structure.

Why:
It allows your decorators to be flexible and reusable with different settings.

How:
1. **Outer Function**: Takes the *decorator arguments* (`n`). Returns the *decorator*.
2. **Decorator**: Takes the *function* (`func`). Returns the *wrapper*.
3. **Wrapper**: Takes the *function arguments* (`*args`, `**kwargs`). Runs the logic.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
```

Task:
Implement the `@repeat(n)` decorator to execute the decorated function `n` times.
"""

def repeat(n):
    # FIX ME: Implement the 3-level decorator
    # def decorator(func):
    #    def wrapper(*args, **kwargs):
    #        ...
    #    return wrapper
    # return decorator
    pass

count = 0

@repeat(3)
def increment():
    global count
    count += 1

def main():
    try:
        increment()
    except TypeError:
        # Expected if repeat returns None
        pass
    
    if count != 3:
        raise Exception(f"Expected count to be 3, got {count}. Did the loop run?")

if __name__ == "__main__":
    main()
