"""
Concept: Dictionary Comprehensions

What:
Just like list comprehensions, you can create dictionaries in a single line using `{}` syntax.

Why:
Useful for transforming data (e.g., swapping keys and values) or creating lookups efficiently.

How:
Syntax: `{ key_expression: value_expression for item in iterable }`

Example:
```python
names = ["Alice", "Bob"]
# Create a dict mapping name to its length
length_map = {name: len(name) for name in names} 
# Result: {'Alice': 5, 'Bob': 3}
```

Task:
Create a dictionary named `cubes` where:
- The **keys** are numbers from 0 to 4.
- The **values** are the cube of that number ($x^3$).
"""

def main():
    # FIX ME: Create the dict using a dict comprehension
    # cubes = {x: x**3 for x in range(5)}
    cubes = {}
    
    expected = {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
    
    if cubes != expected:
        raise Exception(f"Expected {expected}, got {cubes}")

if __name__ == "__main__":
    main()
