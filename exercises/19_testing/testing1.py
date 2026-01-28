"""
Concept: Testing with Assert

What:
The `assert` keyword is Python's built-in debugging tool.
It takes a condition (expression that returns True/False).
If the condition is **False**, it raises an `AssertionError` and crashes the program.

Why:
It's the simplest form of automated testing. 
You "assert" that something MUST be true at this point in the code (e.g., "The list must not be empty").

How:
```python
x = 5
assert x > 0        # Passes (do nothing)
assert x == 99      # Crashes! AssertionError
assert x == 99, "x should be 99" # Crashes with custom message
```

Task:
1. Use `assert` to check that `sum_vals` equals 10.
2. If the user calculates incorrectly, the assertion is our safety net.
"""

def add(a, b):
    return a + b

def main():
    sum_vals = add(3, 7)
    
    # FIX ME: Assert that sum_vals is 10
    # assert ...
    pass
    
    # If the student writes `assert sum_vals == 10`, it passes.
    # If they write `assert sum_vals == 9`, it raises AssertionError.
    # For this exercise checker to verify they WROTE an assertion, 
    # we can't easily introspect without AST, but we can check if they fixed the logic.
    # For simplicity, let's just make sure they DON'T raise an error, and we trust they used assert.
    # But to make it fail initially, we can introduce a bug.
    
    broken_sum = add(3, 6) # Equals 9
    
    # Task 2: Assert that broken_sum is NOT 10.
    # assert broken_sum != 10
    
    try:
        assert sum_vals == 10, "Sum should be 10"
        assert broken_sum != 10, "Broken sum is not 10"
        print("Tests passed!")
    except AssertionError as e:
        raise Exception(f"Assertion failed: {e}")

if __name__ == "__main__":
    main()
