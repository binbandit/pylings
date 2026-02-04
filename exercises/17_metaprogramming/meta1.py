"""
Concept: Metaclasses and the Singleton Pattern

Metaclasses are "classes of classes" - they control how classes themselves are created.
Just as a class defines how instances behave, a metaclass defines how classes behave.

The class hierarchy:
    metaclass -> class -> instance
    type -> MyClass -> my_object

Every class in Python is an instance of `type` (the default metaclass):
```python
class Foo:
    pass

print(type(Foo))  # <class 'type'>
print(type(Foo()))  # <class '__main__.Foo'>
```

Creating a custom metaclass:
```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Called when the CLASS is created
        print(f"Creating class: {name}")
        return super().__new__(mcs, name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        # Called when an INSTANCE is created (when you do MyClass())
        print(f"Creating instance of: {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=MyMeta):
    pass
```

The Singleton Pattern:
A Singleton ensures only ONE instance of a class ever exists. Useful for:
- Database connections (avoid multiple connections)
- Configuration managers (single source of truth)
- Logging (centralized logging)

By overriding `__call__` in a metaclass, we can intercept instance creation
and return the same instance every time.

Task:
Fix the `SingletonMeta` metaclass so that classes using it can only have
one instance. When `Database()` is called multiple times, it should always
return the SAME object.
"""


class SingletonMeta(type):
    """
    A metaclass that implements the Singleton pattern.

    Classes using this metaclass can only have one instance.
    Subsequent calls to create instances return the existing one.
    """

    # This dict stores the single instance for each class
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Called when someone tries to create an instance of a class
        using this metaclass (e.g., Database()).

        For Singleton: Check if an instance already exists.
        - If not, create one and store it
        - If yes, return the existing one
        """
        # TODO: Check if cls is already in _instances
        # TODO: If not, create instance with super().__call__(*args, **kwargs)
        #       and store it in _instances[cls]
        # TODO: Return the instance from _instances[cls]

        # Current behavior: always creates a new instance (not singleton!)
        return super().__call__(*args, **kwargs)


class Database(metaclass=SingletonMeta):
    """A database connection class that should only have one instance."""

    def __init__(self):
        self.connected = True
        print("Database connection established")

    def query(self, sql):
        return f"Executing: {sql}"


def main():
    # Create two "instances"
    print("Creating db1...")
    db1 = Database()

    print("Creating db2...")
    db2 = Database()

    # With Singleton, both should be the SAME object
    if db1 is not db2:
        raise AssertionError(
            "db1 and db2 are different objects!\n"
            "The Singleton pattern should return the SAME instance.\n\n"
            "Fix the __call__ method in SingletonMeta:\n"
            "    def __call__(cls, *args, **kwargs):\n"
            "        if cls not in cls._instances:\n"
            "            cls._instances[cls] = super().__call__(*args, **kwargs)\n"
            "        return cls._instances[cls]"
        )

    print(f"\ndb1 is db2: {db1 is db2}")
    print(f"Same object ID: {id(db1)} == {id(db2)}")
    print("\nSingleton pattern working correctly!")
    print(
        "Only ONE Database instance exists, no matter how many times you call Database()."
    )


if __name__ == "__main__":
    main()
