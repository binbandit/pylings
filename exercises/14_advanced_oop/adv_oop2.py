"""
Concept: Properties (@property decorator)

The `@property` decorator lets you define methods that behave like attributes.
This is useful for:
- Adding validation when setting values
- Computing values on-the-fly (derived attributes)
- Making attributes read-only

How it works:
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # "private" backing field (convention)

    @property
    def celsius(self):
        '''Getter: called when you access obj.celsius'''
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        '''Setter: called when you assign obj.celsius = value'''
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

# Usage:
t = Temperature(25)
print(t.celsius)    # Calls the getter -> 25
t.celsius = 30      # Calls the setter
t.celsius = -300    # Raises ValueError!
```

Task:
1. Create a `@property` getter for `radius` that returns `self._radius`
2. Create a `@radius.setter` that validates radius > 0 (raise ValueError if not)
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # TODO: Add @property decorator and implement the getter
    def radius(self):
        pass  # FIX ME: Return self._radius

    # TODO: Add @radius.setter decorator and implement validation
    # def radius(self, value):
    #     FIX ME: Check if value > 0, raise ValueError if not
    #     FIX ME: Set self._radius = value

    def area(self):
        return 3.14159 * self._radius**2


def main():
    c = Circle(5)

    # Test 1: Property getter works
    try:
        r = c.radius
        if r != 5:
            raise Exception(f"Expected radius=5, got {r}")
    except TypeError:
        raise Exception(
            "c.radius is being called as a method, not a property!\n"
            "Hint: Add the @property decorator above the radius method"
        )

    # Test 2: Property setter works
    try:
        c.radius = 10
        if c._radius != 10:
            raise Exception("Setter didn't update the backing field _radius")
    except AttributeError:
        raise Exception(
            "Cannot set c.radius - setter is missing!\n"
            "Hint: Add @radius.setter decorator for the setter method"
        )

    # Test 3: Validation rejects invalid values
    try:
        c.radius = -5
        raise Exception(
            "Setting radius=-5 should raise ValueError!\n"
            "Hint: Add validation in the setter: if value <= 0: raise ValueError(...)"
        )
    except ValueError:
        pass  # This is correct behavior!

    print("Properties working correctly!")


if __name__ == "__main__":
    main()
