"""
Concept: Inheritance

What:
Inheritance allows a class (Child) to acquire the properties and methods of another class (Parent).
This promotes code reuse and hierarchical organization.

Why:
If you have `Dog`, `Cat`, and `Bird` classes, they all share common behaviors like `eat()` or `sleep()`.
Instead of writing these 3 times, write them once in an `Animal` class and have others inherit from it.

How:
```python
class Parent:
    def greet(self):
        print("Hello")

class Child(Parent):
    pass # Inherits greet() automatically

c = Child()
c.greet() # Output: Hello
```

Task:
1. Define a class `Dog` that inherits from `Animal`.
2. Override the `speak` method to return "Woof!".
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "..."

# FIX ME: Define Dog class inheriting from Animal
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

class Dog: # Remove this placeholder
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

def main():
    dog = Dog("Buddy")
    
    if not isinstance(dog, Animal):
        # This check is tricky if Dog doesn't inherit. 
        # Ideally we want: issubclass(Dog, Animal) 
        # But if they haven't changed Dog yet, it won't be a subclass.
        pass
        
    if dog.speak() != "Woof!":
        raise Exception("Dog should say 'Woof!'")
        
    # Check inheritance
    if not issubclass(Dog, Animal):
        raise Exception("Dog must inherit from Animal")

if __name__ == "__main__":
    main()
