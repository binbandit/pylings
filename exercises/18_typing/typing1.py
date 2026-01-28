"""
Concept: Type Hints (Function Signatures)
Type hints help document your code and allow static analysis tools (like mypy) to find bugs.
Syntax: `def func(arg: Type) -> RetType:`

Task: Add type hints to the `add` function so it accepts and returns integers.
"""

# FIX ME: Add type hints to the function arguments and return value
# def add(a: int, b: int) -> int:
#     return a + b

def add(a, b):
    return a + b

def main():
    # We inspect annotations at runtime for this exercise
    if not add.__annotations__:
        raise Exception("Function 'add' is missing type hints!")
        
    if add.__annotations__.get("a") is not int:
         raise Exception("Argument 'a' should be int")
         
    if add.__annotations__.get("return") is not int:
         raise Exception("Return type should be int")
         
    print("Type hints found!")

if __name__ == "__main__":
    main()
