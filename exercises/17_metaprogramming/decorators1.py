"""
Concept: Decorators

What:
A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
It wraps the original function in another function.
Syntax: `@decorator_name` above the function definition.

Why:
Used for logging, authentication, caching, and more. It keeps your core logic clean by separating "cross-cutting concerns".

How:
```python
def my_decorator(func):
    def wrapper():
        print("Before calling...")
        func()
        print("After calling...")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")
```

Task:
Complete the `logger` decorator.
The inner function should:
1. Append "Before" to the `log` list.
2. Call the original `func`.
3. Append "After" to the `log` list.
"""

def wrapper(func):
    def inner():
        # FIX ME: Print "Before", call func(), then print "After"
        # print("Before")
        # func()
        # print("After")
        pass
    return inner

@wrapper
def say_hello():
    print("Hello!")

def main():
    # We will capture stdout to verify (simulated here for check)
    # in a real test runner we'd capture stdout.
    # For this exercise, we just check if the logic seems right by running it.
    
    # But since we can't easily capture stdout in this simple script without imports,
    # let's modify the requirement to append to a list.
    pass

# Redefining for testability without stdout capture complexity
log = []

def logger(func):
    def inner():
        # FIX ME: Append "Before" to log, call func, then append "After" to log
        pass
    return inner

@logger
def my_func():
    log.append("Function")

def main_test():
    my_func()
    
    expected = ["Before", "Function", "After"]
    if log != expected:
        raise Exception(f"Expected {expected}, got {log}")

if __name__ == "__main__":
    main_test()
