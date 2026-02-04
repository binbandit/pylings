"""
Concept: Iterators

An iterator is an object that produces a sequence of values, one at a time.
When you use a `for` loop, Python is actually using iterators behind the scenes!

To make a class iterable, implement two magic methods:
1. `__iter__(self)`: Returns the iterator object (usually `self`)
2. `__next__(self)`: Returns the next value, or raises `StopIteration` when done

How the for loop works internally:
```python
for item in collection:
    print(item)

# Is equivalent to:
iterator = iter(collection)  # Calls collection.__iter__()
while True:
    try:
        item = next(iterator)  # Calls iterator.__next__()
        print(item)
    except StopIteration:
        break
```

Example - counting up:
```python
class CountUp:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

# Usage:
for num in CountUp(3):
    print(num)  # Prints: 1, 2, 3
```

Task:
Implement `__next__` for the CountDown class:
- Return the current value
- Decrement current by 1
- Raise StopIteration when current reaches 0 (before returning 0)
"""


class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        # TODO: Implement the countdown logic
        # 1. If current is 0 or less, raise StopIteration
        # 2. Save current value to return
        # 3. Decrement current
        # 4. Return the saved value

        # FIX ME: Replace this with proper countdown logic
        raise StopIteration


def main():
    # Test: CountDown(3) should yield 3, 2, 1
    cd = CountDown(3)
    results = list(cd)  # Collects all values from the iterator

    if results == []:
        raise Exception(
            "CountDown produced no values!\n"
            "Hint: Don't raise StopIteration immediately. "
            "Return values while current > 0"
        )

    if results != [3, 2, 1]:
        raise Exception(
            f"Expected [3, 2, 1], got {results}\n"
            "Hint: Return current value BEFORE decrementing, "
            "and stop when current reaches 0"
        )

    # Test: CountDown(1) should yield just 1
    cd2 = CountDown(1)
    if list(cd2) != [1]:
        raise Exception("CountDown(1) should yield [1]")

    # Test: CountDown(0) should yield nothing
    cd3 = CountDown(0)
    if list(cd3) != []:
        raise Exception("CountDown(0) should yield []")

    print("Iterator working correctly!")


if __name__ == "__main__":
    main()
