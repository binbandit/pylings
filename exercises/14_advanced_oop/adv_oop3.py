"""
Concept: Class Methods and Static Methods

Python has three types of methods in a class:
1. Instance methods: Take `self`, operate on instance data
2. Class methods: Take `cls`, operate on class-level data
3. Static methods: Take neither, just utility functions in the class namespace

@classmethod:
- Receives the class (`cls`) as the first argument
- Can access/modify class state
- Perfect for "factory methods" (alternative constructors)

@staticmethod:
- Doesn't receive `self` or `cls`
- Can't access instance or class state
- Just a regular function that logically belongs to the class

Example:
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        '''Factory method: creates Date from "YYYY-MM-DD"'''
        year, month, day = date_string.split('-')
        return cls(int(year), int(month), int(day))

    @staticmethod
    def is_leap_year(year):
        '''Utility: doesn't need instance or class data'''
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Usage:
d = Date.from_string("2024-01-15")  # Factory method
print(Date.is_leap_year(2024))      # Static utility -> True
```

Task:
1. Implement `from_string` as a @classmethod that parses "Name-Age" format
2. Implement `is_valid_age` as a @staticmethod that returns True if age > 0
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # TODO: Add @classmethod decorator
    # This method should parse a string like "Alice-30" and return a User
    def from_string(cls, user_string):
        # FIX ME: Split the string on '-', convert age to int, return cls(name, age)
        pass

    # TODO: Add @staticmethod decorator
    # This method should return True if age > 0, False otherwise
    def is_valid_age(age):
        # FIX ME: Return whether age is positive
        pass


def main():
    # Test 1: Class method exists and works
    try:
        user = User.from_string("Alice-30")
    except TypeError as e:
        if "positional argument" in str(e):
            raise Exception(
                "from_string needs @classmethod decorator!\n"
                "Hint: Add @classmethod above the method definition"
            )
        raise

    if user is None:
        raise Exception(
            "from_string returned None!\n"
            "Hint: Parse the string and return cls(name, int(age))"
        )

    if user.name != "Alice" or user.age != 30:
        raise Exception(
            f"Expected User('Alice', 30), got User('{user.name}', {user.age})\n"
            "Hint: Split on '-' and convert age to int"
        )

    # Test 2: Static method exists and works
    try:
        result = User.is_valid_age(25)
    except TypeError as e:
        if "positional argument" in str(e):
            raise Exception(
                "is_valid_age needs @staticmethod decorator!\n"
                "Hint: Add @staticmethod above the method definition"
            )
        raise

    if result is None:
        raise Exception("is_valid_age returned None!\nHint: Return age > 0")

    if not User.is_valid_age(25):
        raise Exception("is_valid_age(25) should return True!")

    if User.is_valid_age(-5):
        raise Exception("is_valid_age(-5) should return False!")

    if User.is_valid_age(0):
        raise Exception("is_valid_age(0) should return False!")

    print("Class and static methods working correctly!")


if __name__ == "__main__":
    main()
