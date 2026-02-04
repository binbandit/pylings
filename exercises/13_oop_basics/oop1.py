"""
Concept: Classes and the __init__ Method

What:
A class is a blueprint for creating objects. Think of it like a cookie cutter -
the class defines the shape, and each object (instance) is a cookie made from it.

The `__init__` method is a special method called automatically when you create
a new object. It initializes the object's attributes (data).

Why:
Classes let you bundle data and behavior together. Instead of passing around
separate variables, you create objects that contain related data and methods.

How:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self' refers to the instance being created
        self.age = age

# Creating an instance
alice = Person("Alice", 30)
print(alice.name)  # Output: Alice
```

Key points:
- `self` is always the first parameter of `__init__` (and other methods)
- `self.attribute = value` creates an instance attribute
- `__init__` doesn't return anything

Task:
Define a `Dog` class with an `__init__` method that accepts a `name` parameter
and stores it as `self.name`.
"""


class Dog:
    # TODO: Define an __init__ method that takes 'self' and 'name' as parameters
    # and assigns the name to self.name
    pass


def main():
    # Create a Dog instance
    try:
        rex = Dog("Rex")
    except TypeError as e:
        raise Exception(
            "Dog doesn't accept a name argument yet!\n"
            "Hint: Define __init__(self, name) and set self.name = name"
        ) from e

    # Verify the name attribute exists and has the correct value
    if not hasattr(rex, "name"):
        raise Exception(
            "Dog instance has no 'name' attribute!\n"
            "Hint: In __init__, use 'self.name = name' to store the name"
        )

    if rex.name != "Rex":
        raise Exception(
            f"Expected rex.name to be 'Rex', but got '{rex.name}'\n"
            "Hint: Make sure you're assigning the parameter to self.name"
        )

    # Test with another dog to ensure it works generally
    buddy = Dog("Buddy")
    if buddy.name != "Buddy":
        raise Exception("Each Dog instance should have its own name!")

    print("Success! You've created a Dog class with a proper __init__ method!")


if __name__ == "__main__":
    main()
