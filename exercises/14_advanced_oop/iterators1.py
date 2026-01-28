"""
Concept: Iterators

What:
An iterator is an object that represents a stream of data.
To make a class an iterator, you must implement:
1. `__iter__(self)`: Returns the iterator object itself (usually `self`).
2. `__next__(self)`: Returns the next value or raises `StopIteration` when done.

Why:
It gives you full control over iteration logic, unlike standard lists. 
You can generate infinite sequences or lazy-load data.

How:
```python
class Counter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count
```

Task:
Implement `__next__` for the `CountDown` class.
It should return the `current` value and decrement it.
When `current` goes below 1, raise `StopIteration`.
"""

class CountDown:
    def __init__(self, start):
        self.current = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        # FIX ME: clear logic here
        # if self.current <= 0:
        #     raise StopIteration
        # val = self.current
        # self.current -= 1
        # return val
        raise StopIteration

def main():
    cd = CountDown(3)
    
    results = []
    for num in cd:
        results.append(num)
        
    # Should get [3, 2, 1]
    if results != [3, 2, 1]:
        raise Exception(f"Expected [3, 2, 1], got {results}")

if __name__ == "__main__":
    main()
