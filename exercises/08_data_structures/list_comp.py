"""
Concept: List Comprehensions

What:
List comprehensions are a concise, "Pythonic" way to create lists from existing lists (or other iterables).
They combine a for-loop and list creation into a single line.

Why:
They make code cleaner and easier to read compared to standard for-loops with `.append()`.

How:
Syntax: `[ expression for item in iterable if condition ]`

Example:
```python
# Old way
squares = []
for x in range(5):
    if x % 2 == 0:
        squares.append(x**2)

# List Comprehension way
squares = [x**2 for x in range(5) if x % 2 == 0]
```

Task:
Create a list called `squares` that contains the square ($x^2$) of every number from 0 to 9, 
BUT only include the number if it is even (`x % 2 == 0`).
"""

def main():
    # FIX ME: Create the list using a list comprehension
    # squares = [x**2 for x in range(10) if x % 2 == 0]
    squares = []
    
    expected = [0, 4, 16, 36, 64] # 0^2, 2^2, 4^2, 6^2, 8^2
    
    if squares != expected:
        raise Exception(f"Expected {expected}, got {squares}")

if __name__ == "__main__":
    main()
