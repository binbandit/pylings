"""
Concept: Itertools

What:
`itertools` is a module for creating iterators for efficient looping. It handles complex combinatorics efficiently.
- `permutations(p, r)`: Possible orderings of `r` items from `p` (Order matters: AB != BA).
- `combinations(p, r)`: Possible selections of `r` items from `p` (Order doesn't matter: AB == BA).

Why:
Solving "find all combinations" problems manually requires complex nested loops. `itertools` does it in one line, optimized in C.

How:
```python
from itertools import permutations
items = [1, 2, 3]
perms = list(permutations(items, 2)) 
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

Task:
Use `permutations` to find all possible ordered pairs (length 2) of the letters "ABC".
Assign the list of results to `perms`.
"""

from itertools import permutations

def main():
    letters = "ABC"
    
    # FIX ME: Get permutations of length 2
    # perms = list(permutations(letters, 2))
    perms = []
    
    # Expected: ('A', 'B'), ('A', 'C'), ('B', 'A'), ... 
    # Total 3 * 2 = 6 permutations
    
    if len(perms) != 6:
        raise Exception(f"Expected 6 permutations, got {len(perms)}")
        
    if ('A', 'B') not in perms:
        raise Exception("Missing ('A', 'B')")

if __name__ == "__main__":
    main()
