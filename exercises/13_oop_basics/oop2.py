"""
Concept: Instance Methods

What:
Instance methods are functions defined inside a class that operate on the
object's data. They always take `self` as their first parameter, which gives
them access to the instance's attributes.

Why:
Methods let objects perform actions using their own data. Instead of writing
`add_to_calculator(calc, 5)`, you write `calc.add(5)` - the object knows
how to operate on itself.

How:
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1  # Modifies instance data

    def get_count(self):
        return self.count  # Returns instance data

c = Counter()
c.increment()
c.increment()
print(c.get_count())  # Output: 2
```

Key points:
- Methods can read and modify `self.attribute`
- Methods can take additional parameters besides `self`
- Methods can return values

Task:
Implement two methods in the Calculator class:
1. `add(self, n)` - adds n to self.value
2. `subtract(self, n)` - subtracts n from self.value
"""


class Calculator:
    def __init__(self, start=0):
        self.value = start

    # TODO: Implement the 'add' method that takes a number 'n'
    # and adds it to self.value

    # TODO: Implement the 'subtract' method that takes a number 'n'
    # and subtracts it from self.value


def main():
    calc = Calculator(10)

    # Test that add method exists
    if not hasattr(calc, "add"):
        raise Exception(
            "Calculator has no 'add' method!\n"
            "Hint: Define 'def add(self, n):' inside the class"
        )

    # Test add functionality
    calc.add(5)
    if calc.value != 15:
        raise Exception(
            f"After Calculator(10).add(5), expected value=15, got {calc.value}\n"
            "Hint: The add method should do 'self.value += n'"
        )

    # Test that subtract method exists
    if not hasattr(calc, "subtract"):
        raise Exception(
            "Calculator has no 'subtract' method!\n"
            "Hint: Define 'def subtract(self, n):' inside the class"
        )

    # Test subtract functionality
    calc.subtract(3)
    if calc.value != 12:
        raise Exception(
            f"After subtracting 3 from 15, expected value=12, got {calc.value}\n"
            "Hint: The subtract method should do 'self.value -= n'"
        )

    # Test chaining operations
    calc2 = Calculator(100)
    calc2.add(50)
    calc2.subtract(25)
    calc2.add(10)
    if calc2.value != 135:
        raise Exception(f"100 + 50 - 25 + 10 should equal 135, got {calc2.value}")

    print("Success! Your Calculator methods work correctly!")


if __name__ == "__main__":
    main()
