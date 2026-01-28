
# DESIGN PATTERNS: FACTORY
# ========================
#
# What: A function or method that returns objects of a prototype class/interface.
#
# Why:  Decouples the creation of objects from the code that uses them.
#       Allows you to add new types without changing the client code.
#
# How:  def get_pet(pet_type):
#           if pet_type == "dog": return Dog()
#           elif pet_type == "cat": return Cat()
#
# Task:
# 1. Define classes `Dog` and `Cat` with a `speak()` method.
# 2. Define `pet_factory(pet_type)` that returns the correct instance.
# 3. Handle unknown types by raising ValueError.

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def pet_factory(pet_type):
    # TODO: Return Dog or Cat instance based on string
    pass

def test_factory():
    d = pet_factory("dog")
    assert isinstance(d, Dog)
    assert d.speak() == "Woof"
    
    c = pet_factory("cat")
    assert isinstance(c, Cat)
    
    try:
        pet_factory("fish")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    test_factory()
    print("Factory pattern passed!")
