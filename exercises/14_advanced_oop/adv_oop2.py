"""
Concept: Properties
The `@property` decorator allows you to define methods that can be accessed like attributes. This is useful for getters and setters with validation logic.

Task: Use `@property` to create a getter for `radius` and `@radius.setter` to ensure `radius` is positive.
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    # FIX ME: Use @property to make 'radius' accessible
    # @property
    # def radius(self):
    #     return self._radius
    
    # FIX ME: Add a setter to ensure radius > 0
    # @radius.setter
    # def radius(self, value):
    #     if value <= 0: raise ValueError("Positive only!")
    #     self._radius = value
    
    def area(self):
        return 3.14 * self._radius ** 2

def main():
    c = Circle(5)
    
    # Validation 1: Get property
    try:
        r = c.radius
    except AttributeError:
        raise Exception("Cannot access c.radius!")
        
    # Validation 2: Set property valid
    try:
        c.radius = 10
        if c._radius != 10: raise Exception("Setter didn't update backing field")
    except AttributeError:
        raise Exception("Cannot set c.radius!")
        
    # Validation 3: Set property invalid
    try:
        c.radius = -1
        raise Exception("Should have raised ValueError for negative radius")
    except ValueError:
        pass # Correct
    except AttributeError:
         raise Exception("Setter missing!")

    print("Properties passed!")

if __name__ == "__main__":
    main()
