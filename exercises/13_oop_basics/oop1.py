"""
Concept: OOP (Classes & Init)
Classes are blueprints for creating objects. The `__init__` method helps initialize an object's state.

Task: Define a `Dog` class with an `__init__` that sets `self.name`.
"""

# FIX ME: Define a class 'Dog' with an __init__ method that sets self.name
# class Dog:
#     def __init__(self, name):
#         self.name = name

class Dog:
    pass

def main():
    try:
        rex = Dog("Rex")
    except TypeError:
         raise Exception("Dog does not accept arguments! Define __init__.")
         
    if not hasattr(rex, "name") or rex.name != "Rex":
        raise Exception("Dog does not have the correct name attribute!")
        
    print("Dog class created!")

if __name__ == "__main__":
    main()
