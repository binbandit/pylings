"""
Concept: Tuples

What:
Tuples are ordered collections of items, just like lists. 
However, tuples are **immutable**, meaning you cannot add, remove, or change elements after creation.
Tuples are created using round parentheses `()`.

Why:
- Use tuples when you want to ensure data doesn't change by accident (e.g., coordinates `(x, y)` or configuration constants).
- Tuples are slightly faster and more memory-efficient than lists.
- Tuples can be used as keys in dictionaries (lists cannot).

How:
```python
my_tuple = ("red", "green", "blue")
first_item = my_tuple[0] # "red"
# my_tuple[0] = "yellow" # ERROR! Cannot modify a tuple.
```

Task:
1. Create a tuple named `my_tuple` containing "apple", "banana", and "cherry".
2. Access the second element (index 1) and assign it to the variable `item`.
"""

def main():
    # FIX ME: Create the tuple
    # my_tuple = ...
    my_tuple = None
    
    # FIX ME: Get the second element (index 1)
    # item = ...
    item = None
    
    if not isinstance(my_tuple, tuple):
        raise Exception("my_tuple should be a tuple!")
        
    if len(my_tuple) != 3:
        raise Exception("my_tuple should have 3 elements")
        
    if item != "banana":
        raise Exception(f"Expected 'banana', got '{item}'")

    # Verify immutability (just for learning)
    try:
        my_tuple[0] = "orange"
        raise Exception("Should not be able to modify a tuple!")
    except TypeError:
        pass # This is expected!

if __name__ == "__main__":
    main()
