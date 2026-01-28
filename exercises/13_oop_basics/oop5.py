"""
Concept: Magic Methods (Dunder Methods)

What:
Magic methods start and end with double underscores (`__`). They define how objects behave with operators and built-in functions.
- `__str__`: Defines behavior for `str(obj)` and `print(obj)`.
- `__add__`: Defines behavior for `+` operator.
- `__eq__`: Defines behavior for `==` operator.

Why:
They allow your custom objects to feel like native Python types.
For example, adding two `Vector` objects (`v1 + v2`) is cleaner than `v1.add(v2)`.

How:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

Task:
Implement `__str__` and `__add__` for the `Wallet` class so we can print it nicely and add two wallets together.
"""

class Wallet:
    def __init__(self, amount):
        self.amount = amount
        
    # FIX ME: Implement __str__ to return "Wallet: $X"
    # def __str__(self):
    #     return f"Wallet: ${self.amount}"
    
    # FIX ME: Implement __add__ to return a NEW Wallet with the sum of amounts
    # def __add__(self, other):
    #     return Wallet(self.amount + other.amount)
    pass

def main():
    w1 = Wallet(50)
    w2 = Wallet(30)
    
    # Test __str__
    if str(w1) != "Wallet: $50":
         raise Exception(f"Expected 'Wallet: $50', got '{str(w1)}'")
         
    # Test __add__
    try:
        w3 = w1 + w2
        if not isinstance(w3, Wallet):
            raise Exception("Adding wallets should return a Wallet")
        if w3.amount != 80:
             raise Exception(f"Expected $80, got ${w3.amount}")
    except TypeError:
        raise Exception("Addition not supported yet. Implement __add__.")

if __name__ == "__main__":
    main()
