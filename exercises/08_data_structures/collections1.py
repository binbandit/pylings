"""
Concept: Collections - Counter

What:
`Counter` is a specialized dictionary designed for counting things. 
It takes an iterable (string, list, etc.) and returns a dictionary where keys are elements and values are their count.

Why:
Counting frequency is a very common interview task and data science need options. 
Writing a manual loop with a dictionary is verbose; `Counter` does it in one optimized line.

How:
```python
from collections import Counter
counts = Counter("hello")
# Result: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Get the most common items
print(counts.most_common(1)) # [('l', 2)]
```

Task:
Use `Counter` to count the frequency of each character in the string "abracadabra".
Assign the result to `counts`.
"""

from collections import Counter

def main():
    text = "abracadabra"
    
    # FIX ME: Use Counter to count characters
    # counts = Counter(text)
    counts = None
    
    if not isinstance(counts, Counter):
        raise Exception("counts should be a Counter object")
        
    if counts['a'] != 5:
        raise Exception(f"Expected 5 'a's, got {counts['a']}")
        
    if counts['b'] != 2:
        raise Exception(f"Expected 2 'b's, got {counts['b']}")

if __name__ == "__main__":
    main()
