"""
Concept: Generators

Generators are a simpler way to create iterators using functions and the `yield`
keyword. Instead of writing a class with `__iter__` and `__next__`, you just
write a function that yields values!

How yield works:
- When a function contains `yield`, it becomes a generator function
- Calling it returns a generator object (doesn't run the code yet!)
- Each call to `next()` runs until the next `yield`, then pauses
- The function remembers its state between calls
- When the function returns/ends, StopIteration is raised automatically

Example:
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count      # Pause here, return count
        count += 1       # Resume here on next call

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # StopIteration!

# Or use in a for loop:
for num in count_up_to(3):
    print(num)  # 1, 2, 3
```

Why use generators?
- Memory efficient: values are generated one at a time, not stored in a list
- Cleaner code: no need to manage state manually like in iterator classes
- Can represent infinite sequences!

Task:
Implement `traffic_light()` generator that yields exactly three values:
1. First yield: "green"
2. Second yield: "yellow"
3. Third yield: "red"
Then it should stop (no more values).
"""


def traffic_light():
    # TODO: Yield "green", then "yellow", then "red"
    # FIX ME: Add three yield statements
    pass


def main():
    gen = traffic_light()

    # Check that it's actually a generator
    if not hasattr(gen, "__next__"):
        raise Exception(
            "traffic_light() should return a generator!\n"
            "Hint: Use 'yield' instead of 'return'. "
            "A function with yield becomes a generator."
        )

    # Collect all values
    try:
        first = next(gen)
    except StopIteration:
        raise Exception(
            "Generator stopped immediately without yielding!\n"
            "Hint: Add 'yield \"green\"' as the first statement"
        )

    if first != "green":
        raise Exception(
            f"First value should be 'green', got '{first}'\n"
            'Hint: yield "green" should be first'
        )

    try:
        second = next(gen)
    except StopIteration:
        raise Exception(
            "Generator stopped after first yield!\n"
            "Hint: Add 'yield \"yellow\"' as the second statement"
        )

    if second != "yellow":
        raise Exception(f"Second value should be 'yellow', got '{second}'")

    try:
        third = next(gen)
    except StopIteration:
        raise Exception(
            "Generator stopped after second yield!\n"
            "Hint: Add 'yield \"red\"' as the third statement"
        )

    if third != "red":
        raise Exception(f"Third value should be 'red', got '{third}'")

    # Should be exhausted now
    try:
        extra = next(gen)
        raise Exception(
            f"Generator should stop after 3 values, but got '{extra}'!\n"
            "Hint: Only yield exactly 3 values, then let the function end"
        )
    except StopIteration:
        pass  # Correct!

    print("Generator working correctly!")


if __name__ == "__main__":
    main()
