"""
Concept: Properties (@property)

What:
The `@property` decorator allows you to define methods that behave like attributes.
You can add logic (validation, calculation) when getting or setting a value.

Why:
It gives you control over attribute access without changing the interface. 
Users still access `obj.score` instead of `obj.get_score()`, but you can enforce `score >= 0` behind the scenes.

How:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius # Convention: _variable is internal
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
c.radius = 10  # Calls the setter
print(c.radius) # Calls the getter
```

Task:
1. Add a `@property` named `price` to the `Product` class.
2. Add a `@price.setter` that ensures the price is never negative (raise ValueError if it is).
"""

class Product:
    def __init__(self, price):
        self._price = price
        
    # FIX ME: Add @property for price returning self._price
    
    # FIX ME: Add @price.setter to validate value >= 0 before setting self._price
    pass

def main():
    p = Product(10)
    
    # Test Getter
    # if p.price != 10:
    #     raise Exception("Getter failed")
        
    # Test Setter
    # p.price = 20
    # if p.price != 20: 
    #     raise Exception("Setter failed")
        
    # Test Validation
    try:
        # p.price = -5
        pass # Remove this pass when strictly testing
    except ValueError:
        print("Validation working!")
        return

    # Once implemented, ensure we can't set negative price
    # raise Exception("Validation failed! Should raise ValueError for negative price")

if __name__ == "__main__":
    main()
