"""
Concept: Class and Static Methods

What:
- `@classmethod`: A method bound to the **class**, not the instance. It receives `cls` as the first argument.
- `@staticmethod`: A method that belongs to a class but doesn't use class (`cls`) or instance (`self`) data.

Why:
- Use `@classmethod` for **factory methods** (alternative constructors like `from_json` or `from_string`).
- Use `@staticmethod` for utility functions that logically belong to the class namespace but don't modify state.

How:
```python
class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    @classmethod
    def from_string(cls, date_str): # "12-25"
        d, m = date_str.split('-')
        return cls(d, m)
    
    @staticmethod
    def is_valid_month(m):
        return 1 <= m <= 12
```

Task:
1. Implement a class method `from_string` returning a new User from "Name-Age".
2. Implement a static method `is_valid` checking if age > 0.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # FIX ME: Create a class method that creates a User from "Name-Age" string
    # @classmethod
    # def from_string(cls, s):
    #     name, age = s.split('-')
    #     return cls(name, int(age))
    
    # FIX ME: Create a static method that checks if age is > 0
    # @staticmethod
    # def is_valid(age):
    #     return age > 0

def main():
    # Test class method
    if not hasattr(User, 'from_string'):
        raise Exception("Missing from_string method")
        
    u = User.from_string("Alice-30")
    if u.name != "Alice" or u.age != 30:
        raise Exception("from_string failed")
        
    # Test static method
    if not hasattr(User, 'is_valid'):
        raise Exception("Missing is_valid method")
        
    if not User.is_valid(20):
        raise Exception("is_valid(20) should be True")
        
    if User.is_valid(-5):
        raise Exception("is_valid(-5) should be False")

if __name__ == "__main__":
    main()
