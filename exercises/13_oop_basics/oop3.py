"""
Concept: Inheritance

What:
Inheritance allows a class (child) to acquire the properties and methods of
another class (parent). The child class can use parent methods as-is, or
override them with its own implementation.

Why:
Code reuse! If Dog, Cat, and Bird all need `eat()` and `sleep()` methods,
write them once in an Animal class. Each subclass inherits these behaviors
and only needs to define what's unique (like their specific sounds).

How:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):  # Override parent method
        return "Meow!"

# Cat automatically has __init__ from Animal
whiskers = Cat("Whiskers")
print(whiskers.name)   # Output: Whiskers (inherited)
print(whiskers.speak()) # Output: Meow! (overridden)
```

Key points:
- Use `class Child(Parent):` to inherit
- Child gets all parent methods and attributes
- Override methods by defining them with the same name
- Use `super()` to call parent methods when needed

Task:
1. Make the Dog class inherit from Animal
2. Override the speak() method to return "Woof!"
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"


# TODO: Make Dog inherit from Animal by adding (Animal) after the class name
# TODO: Override the speak method to return "Woof!"
class Dog:
    pass


def main():
    # Test that Dog can be instantiated with a name
    try:
        buddy = Dog("Buddy")
    except TypeError as e:
        raise Exception(
            "Dog doesn't accept a name argument!\n"
            "Hint: When Dog inherits from Animal, it gets Animal's __init__ method"
        ) from e

    # Test that Dog inherits from Animal
    if not issubclass(Dog, Animal):
        raise Exception(
            "Dog must inherit from Animal!\n"
            "Hint: Change 'class Dog:' to 'class Dog(Animal):'"
        )

    # Test that buddy is an instance of both Dog and Animal
    if not isinstance(buddy, Animal):
        raise Exception("A Dog instance should also be an Animal instance!")

    # Test that speak() is overridden correctly
    if buddy.speak() != "Woof!":
        raise Exception(
            f"Dog.speak() should return 'Woof!', got '{buddy.speak()}'\n"
            "Hint: Define a speak method in Dog that returns 'Woof!'"
        )

    # Test that inherited methods work
    if not hasattr(buddy, "name") or buddy.name != "Buddy":
        raise Exception("Dog should inherit the name attribute from Animal!")

    # Test the inherited describe() method uses the overridden speak()
    expected = "Buddy says Woof!"
    if buddy.describe() != expected:
        raise Exception(
            f"describe() should return '{expected}', got '{buddy.describe()}'\n"
            "This tests that inheritance is working properly!"
        )

    print("Success! Dog properly inherits from Animal and overrides speak()!")


if __name__ == "__main__":
    main()
