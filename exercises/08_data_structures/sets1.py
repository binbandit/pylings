"""
Concept: Sets

What:
Sets are unordered collections of **unique** elements. 
They are created using curly braces `{1, 2, 3}` or the `set()` function.

Why:
- Removing duplicates from a list: `list(set(my_list))`
- Checking for membership is VERY fast (`if x in my_set`) compared to lists.
- Performing mathematical set operations like union, intersection, and difference.

How:
```python
my_set = {1, 2, 3}
my_set.add(4)      # {1, 2, 3, 4}
my_set.add(2)      # {1, 2, 3, 4} (No change, 2 is already there)
unique_list = list(set([1, 2, 2, 3])) # [1, 2, 3]
```

Task:
1. Create a set named `my_set` from the list `[1, 2, 2, 3, 3, 3]`. Note how duplicates disappear!
2. Add the number `4` to your set using `.add()`.
"""

def main():
    initial_list = [1, 2, 2, 3, 3, 3]
    
    # FIX ME: Create a set from initial_list
    # my_set = set(initial_list)
    my_set = set()
    
    # FIX ME: Add the number 4
    # my_set.add(4)
    
    if not isinstance(my_set, set):
        raise Exception("my_set should be a set!")
        
    if len(my_set) != 4:
        raise Exception(f"Expected 4 unique elements, got {len(my_set)}")
        
    if 4 not in my_set:
        raise Exception("4 should be in the set")
        
    if 2 not in my_set:
        raise Exception("2 should be in the set")

if __name__ == "__main__":
    main()
