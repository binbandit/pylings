"""
Concept: *args and **kwargs

What:
- `*args` (Variable Positional Arguments): Allows a function to accept any number of extra arguments as a **tuple**.
- `**kwargs` (Variable Keyword Arguments): Allows a function to accept any number of named arguments as a **dictionary**.

Why:
Use these when writing flexible functions (like decorators, wrappers, or logging utilities) that shouldn't be limited to a fixed set of parameters.

How:
```python
def example(first, *args, **kwargs):
    print(first)
    print(args)   # Tuple, e.g., (1, 2)
    print(kwargs) # Dict, e.g., {'a': 1, 'b': 2}
    
example("Hi", 1, 2, a=1, b=2)
```

Task:
Update the `logger` function to accept:
1. `message` (required argument)
2. `*args` (optional extra positional arguments)
3. `**kwargs` (optional extra keyword arguments)
"""

# FIX ME: Accept message, *args, and **kwargs
def logger(message):
    print(f"MSG: {message}")
    # Print args and kwargs if you like, for learning
    # print(args)
    # print(kwargs)

def main():
    # This call should work if defined correctly
    try:
        logger("Error", "db_connection", 500, user="admin", retry=True)
    except TypeError:
        raise Exception("logger function signature incorrect! Needs *args and **kwargs")
    
    # We can inspect the code object to be sure, or just rely on the call passing.
    import inspect
    sig = inspect.signature(logger)
    
    has_var_positional = any(p.kind == p.VAR_POSITIONAL for p in sig.parameters.values())
    has_var_keyword = any(p.kind == p.VAR_KEYWORD for p in sig.parameters.values())
    
    if not has_var_positional:
        raise Exception("Missing *args")
    
    if not has_var_keyword:
        raise Exception("Missing **kwargs")

if __name__ == "__main__":
    main()
