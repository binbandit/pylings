"""
Concept: Lambda Functions

What:
Lambdas are small, anonymous (nameless) functions defined in a single line.
Syntax: `lambda arguments: expression`

Why:
Use them for short, throwaway functions, especially as arguments to `map()`, `filter()`, or `sorted()` (`key=...`).
If the logic requires multiple lines, define a standard function instead.

How:
```python
# Standard function
def add(x, y):
    return x + y

# Equivalent Lambda
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3)) # 8
```

Task:
Create a lambda function named `double` that takes one argument `x` and returns `x * 2`.
"""

def main():
    # FIX ME: Define the lambda
    # double = lambda x: x * 2
    double = None
    
    if double is None:
        print("Define the double lambda first!")
        return
        
    if double(5) != 10:
        raise Exception(f"double(5) should be 10, got {double(5)}")
        
    if double(10) != 20:
        raise Exception(f"double(10) should be 20, got {double(10)}")

if __name__ == "__main__":
    main()
