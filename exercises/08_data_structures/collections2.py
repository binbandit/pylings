"""
Concept: Collections - DefaultDict

What:
`defaultdict` is a dictionary that never raises a `KeyError`. 
If you try to access a missing key, it automatically creates it using a factory function you provide.

Why:
It simplifies code specifically when you are grouping items or accumulating values.
You don't need to check `if key in my_dict:` before appending or adding.

How:
```python
from collections import defaultdict

# Grouping names by length
groups = defaultdict(list) # Default value for new keys is an empty list []
names = ["Ali", "Bob", "Anna"]

for name in names:
    length = len(name)
    groups[length].append(name) # No KeyError! It creates [] automatically.
```

Task:
1. Create a `defaultdict` of lists named `grouped`.
2. Iterate through `words`.
3. Group them by their **first letter** (e.g., 'apple' goes under 'a').
"""

from collections import defaultdict

def main():
    words = ["apple", "banana", "apricot", "cherry", "blueberry"]
    
    # FIX ME: Use defaultdict(list)
    # grouped = defaultdict(list)
    grouped = {}
    
    # FIX ME: Loop through words and append to the list corresponding to the first letter
    # for word in words:
    #     grouped[word[0]].append(word)

    if not isinstance(grouped, defaultdict):
        raise Exception("grouped should be a defaultdict")

    if set(grouped['a']) != {"apple", "apricot"}:
        raise Exception("Incorrect grouping for 'a'")
        
    if set(grouped['b']) != {"banana", "blueberry"}:
        raise Exception("Incorrect grouping for 'b'")

if __name__ == "__main__":
    main()
