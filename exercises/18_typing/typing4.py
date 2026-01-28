"""
Concept: Advanced Typing (Callable, Any)

What:
- `Callable[[ArgType1, ArgType2], ReturnType]`: Describes a function signature.
- `Any`: A special type that disables type checking. It says "this can be literally anything".

Why:
- Use `Callable` when passing functions as arguments (common in callbacks/decorators).
- Use `Any` safely when dealing with unknown data types or dynamic libraries, but avoid using it lazily!

How:
```python
from typing import Callable, Any

def run_callback(cb: Callable[[str], None], msg: Any) -> None:
    cb(str(msg))
```

Task:
Add type hints to the `execute` function:
1. `func` should be a `Callable` that takes an `int` and returns an `int`.
2. `arg` can be `Any`.
3. The return type of `execute` is `int`.
"""

from typing import Callable, Any

# FIX ME: Add type hints. func takes an int and returns an int. arg is Any.
# def execute(func: Callable[[int], int], arg: Any) -> int:
def execute(func, arg):
    return func(arg)

def double(x: int) -> int:
    return x * 2

def main():
    # This checks runtime behavior, but the real test is static analysis.
    # For now, we just ensure it runs.
    result = execute(double, 10)
    
    if result != 20:
        raise Exception("Function failed")
        
    # We can inspect annotations at runtime!
    anns = execute.__annotations__
    
    if 'func' not in anns:
        raise Exception("Missing type hint for 'func'")
        
    # Checking specific generic types at runtime is hard/messy. 
    # Let's just check they annotated it at all.
    if 'arg' not in anns:
        raise Exception("Missing type hint for 'arg'")
        
    if 'return' not in anns:
        raise Exception("Missing return type hint")

if __name__ == "__main__":
    main()
