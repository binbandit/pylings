"""
Concept: Magic Methods (Dunder Methods)

What:
Magic methods (also called "dunder" methods for Double UNDERscore) let you
define how your objects behave with Python's built-in operations and functions.

Common magic methods:
- `__str__`: Called by str() and print() - returns human-readable string
- `__repr__`: Called by repr() - returns developer-friendly string
- `__add__`: Called by + operator
- `__eq__`: Called by == operator
- `__len__`: Called by len()

Why:
They make your objects feel like native Python types. Writing `v1 + v2` is
more intuitive than `v1.add(v2)`, and `print(wallet)` is cleaner than
`print(wallet.to_string())`.

How:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)        # Output: Vector(1, 2)
v3 = v1 + v2     # Uses __add__
print(v3)        # Output: Vector(4, 6)
print(v1 == v2)  # Output: False (uses __eq__)
```

Task:
Implement three magic methods in the Wallet class:
1. `__str__`: Return "Wallet: $X" where X is the amount
2. `__add__`: Return a NEW Wallet with the combined amounts
3. `__eq__`: Return True if two wallets have the same amount
"""


class Wallet:
    def __init__(self, amount):
        self.amount = amount

    # TODO: Implement __str__ to return "Wallet: $X" where X is self.amount

    # TODO: Implement __add__ to return a NEW Wallet with combined amounts
    # Remember: don't modify self, create and return a new Wallet

    # TODO: Implement __eq__ to compare amounts between two wallets


def main():
    w1 = Wallet(50)
    w2 = Wallet(30)
    w3 = Wallet(50)

    # Test 1: __str__ method
    str_result = str(w1)
    if str_result != "Wallet: $50":
        if "Wallet object at" in str_result:
            raise Exception(
                f"Got default str(): {str_result}\n"
                "Hint: Define __str__(self) to return a custom string"
            )
        raise Exception(
            f"Expected 'Wallet: $50', got '{str_result}'\n"
            "Hint: Return f'Wallet: ${{self.amount}}' from __str__"
        )

    # Test 2: __add__ method
    try:
        w4 = w1 + w2
    except TypeError:
        raise Exception(
            "Cannot add two Wallets with + operator!\n"
            "Hint: Define __add__(self, other) that returns a new Wallet"
        )

    if not isinstance(w4, Wallet):
        raise Exception(
            f"w1 + w2 should return a Wallet, got {type(w4).__name__}\n"
            "Hint: Return Wallet(self.amount + other.amount)"
        )

    if w4.amount != 80:
        raise Exception(
            f"Wallet(50) + Wallet(30) should have amount=80, got {w4.amount}"
        )

    # Test 3: Original wallets unchanged (immutability)
    if w1.amount != 50 or w2.amount != 30:
        raise Exception(
            "Adding wallets should not modify the original wallets!\n"
            "Hint: Create a NEW Wallet in __add__, don't modify self"
        )

    # Test 4: __eq__ method
    try:
        are_equal = w1 == w3
    except Exception:
        raise Exception(
            "Error comparing wallets with ==\n"
            "Hint: Define __eq__(self, other) that compares amounts"
        )

    if not are_equal:
        raise Exception(
            "Wallet(50) == Wallet(50) should be True!\n"
            "Hint: Return self.amount == other.amount from __eq__"
        )

    if w1 == w2:
        raise Exception("Wallet(50) == Wallet(30) should be False!")

    # Test 5: Combined test
    w5 = Wallet(40) + Wallet(40)
    if not (w5 == Wallet(80)):
        raise Exception("Wallet(40) + Wallet(40) should equal Wallet(80)!")

    print("Success! Your Wallet class has working magic methods!")
    print(f"  {w1} + {w2} = {w1 + w2}")
    print(f"  {w1} == {w3}: {w1 == w3}")


if __name__ == "__main__":
    main()
