"""
Concept: Magic Methods (Dunder Methods)
Python classes can define special methods with double underscores (dunder methods) to customize behavior.
`__str__` defines the string representation.
`__eq__` defines equality behavior (`==`).

Task: Implement `__str__` to return "Vector(x, y)" and `__eq__` to compare vector coordinates.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # FIX ME: Implement __str__ to return "Vector(x, y)"
    # def __str__(self):
    #     return f"Vector({self.x}, {self.y})"
    
    # FIX ME: Implement __eq__ to compare two vectors
    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

def main():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    
    if str(v1) != "Vector(1, 2)":
        raise Exception(f"String representation wrong: {str(v1)}")
        
    if v1 != v2:
        raise Exception("Equality check failed!")
        
    print("Magic methods working!")

if __name__ == "__main__":
    main()
