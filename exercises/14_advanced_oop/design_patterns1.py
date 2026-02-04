"""
Concept: Singleton Pattern

The Singleton pattern ensures a class has only ONE instance, and provides a
global point of access to it.

When to use:
- Database connections (one shared connection pool)
- Configuration managers (one source of truth)
- Logging (one logger instance)
- Caches (one shared cache)

How it works in Python:
Override `__new__` to control object creation. `__new__` is called BEFORE
`__init__` and is responsible for creating and returning the new instance.

```python
class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            # First time: create the instance
            cls._instance = super().__new__(cls)
        # Always return the same instance
        return cls._instance
```

Important: `__init__` still runs every time you call `Class()`, but `__new__`
ensures you always get the same object.

Task:
Complete the `__new__` method in Logger so that:
1. If `_instance` is None, create a new instance using `super().__new__(cls)`
2. Always return `_instance`
"""


class Logger:
    _instance = None

    def __new__(cls):
        # TODO: Implement Singleton pattern
        # 1. Check if cls._instance is None
        # 2. If None, create instance with super().__new__(cls)
        # 3. Return cls._instance

        # FIX ME: Currently creates a new instance every time!
        return super().__new__(cls)

    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)


def main():
    # Create two "instances"
    logger1 = Logger()
    logger2 = Logger()

    # Test: They should be the SAME object
    if logger1 is not logger2:
        raise Exception(
            "logger1 and logger2 are different objects!\n"
            "Hint: Store the instance in cls._instance and return it.\n"
            "Only call super().__new__(cls) if _instance is None."
        )

    # Test: Changes to one affect the other (because they're the same!)
    logger1.log("Hello")
    logger2.log("World")

    if len(logger1.logs) != 2:
        raise Exception(
            f"Expected 2 logs, got {len(logger1.logs)}\n"
            "If singleton works, logger1 and logger2 share the same logs list"
        )

    if logger1.logs != ["Hello", "World"]:
        raise Exception(f"Expected ['Hello', 'World'], got {logger1.logs}")

    # Verify they share identity
    if id(logger1) != id(logger2):
        raise Exception("logger1 and logger2 should have the same id()")

    print("Singleton pattern working correctly!")


if __name__ == "__main__":
    main()
