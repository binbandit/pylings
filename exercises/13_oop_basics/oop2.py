"""
Concept: OOP (Methods)
Methods are functions defined inside a class that modify the object's attributes.

Task: Implement an `add` method in the `Calculator` class.
"""

class Calculator:
    def __init__(self, start=0):
        self.value = start
        
    # FIX ME: Add an 'add' method that increases self.value
    # def add(self, n):
    #     self.value += n

def main():
    calc = Calculator(10)
    
    if not hasattr(calc, "add"):
        raise Exception("Method 'add' is missing!")
        
    calc.add(5)
    
    if calc.value != 15:
        raise Exception(f"Expected 15, got {calc.value}")

    print("Method implemented!")

if __name__ == "__main__":
    main()
