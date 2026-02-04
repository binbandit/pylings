"""
Concept: Properties (@property decorator)

What:
The `@property` decorator lets you define methods that behave like attributes.
When you access `obj.price`, Python calls a method behind the scenes. This
lets you add logic (like validation) without changing how users access the data.

Why:
- Validate data before setting (e.g., price can't be negative)
- Compute values on-the-fly (e.g., area from width and height)
- Keep a clean interface (users write `obj.price`, not `obj.get_price()`)

How:
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Convention: _ prefix for internal storage

    @property
    def celsius(self):
        '''Getter - called when you READ the attribute'''
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        '''Setter - called when you WRITE to the attribute'''
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

t = Temperature(25)
print(t.celsius)  # Calls the getter -> 25
t.celsius = 30    # Calls the setter
t.celsius = -300  # Raises ValueError!
```

Key points:
- Use `_variable` for internal storage (convention for "private")
- `@property` creates a getter
- `@name.setter` creates a setter for the property named `name`

Task:
1. Add a `@property` named `price` that returns `self._price`
2. Add a `@price.setter` that raises ValueError if the new price is negative
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Internal storage

    # TODO: Add a @property decorator and define a 'price' method
    # that returns self._price

    # TODO: Add a @price.setter decorator and define a 'price' method
    # that validates value >= 0 before setting self._price
    # If value < 0, raise ValueError("Price cannot be negative")


def main():
    laptop = Product("Laptop", 999)

    # Test 1: Property getter works
    try:
        current_price = laptop.price
    except AttributeError:
        raise Exception(
            "Cannot access 'price' property!\n"
            "Hint: Add @property decorator above a method named 'price'"
        )

    if current_price != 999:
        raise Exception(
            f"Expected laptop.price to be 999, got {current_price}\n"
            "Hint: The property getter should return self._price"
        )

    # Test 2: Property setter works
    try:
        laptop.price = 899
    except AttributeError:
        raise Exception(
            "Cannot set 'price' property!\n"
            "Hint: Add @price.setter decorator above a setter method"
        )

    if laptop.price != 899:
        raise Exception(
            f"After setting price to 899, got {laptop.price}\n"
            "Hint: The setter should assign the value to self._price"
        )

    # Test 3: Validation rejects negative prices
    try:
        laptop.price = -50
        raise Exception(
            "Setting negative price should raise ValueError!\n"
            "Hint: In the setter, check 'if value < 0: raise ValueError(...)'"
        )
    except ValueError:
        pass  # This is expected!

    # Test 4: Price unchanged after failed validation
    if laptop.price != 899:
        raise Exception("Price should remain 899 after rejected negative value!")

    # Test 5: Zero price is valid
    laptop.price = 0
    if laptop.price != 0:
        raise Exception("Setting price to 0 should be allowed!")

    print("Success! Your Product class has working price validation!")


if __name__ == "__main__":
    main()
