"""
Concept: Generators

What:
Generators are a simpler way to create iterators using functions and the `yield` keyword.
When `yield` is called, the function pauses and saves its state. Next time `next()` is called, it resumes right there.

Why:
- **Memory Efficient**: They generate values one by one instead of creating a huge list in memory.
- **Readable**: Much easier to write than a full class with `__iter__` and `__next__`.

How:
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(3)
# next(gen) -> 1, next(gen) -> 2...
```

Task:
Implement `simple_clock` so it yields the string "tick", then yields "tock", then yields "tick" again.
"""

def simple_clock():
    # FIX ME: Yield "tick", then "tock", then "tick"
    # yield "tick"
    # yield "tock"
    # yield "tick"
    pass

def main():
    gen = simple_clock()
    
    try:
        if next(gen) != "tick": raise Exception("First should be 'tick'")
        if next(gen) != "tock": raise Exception("Second should be 'tock'")
        if next(gen) != "tick": raise Exception("Third should be 'tick'")
    except StopIteration:
        raise Exception("Generator stopped too early!")
        
    # Ensure it's exhausted
    try:
        next(gen)
        raise Exception("Generator should be exhausted now!")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
