"""
Concept: Type Hints
Type hints allow you to specify the expected type of a variable.
`x: int` means `x` is expected to be an integer.

Task: Assign `x` the value 10 to satisfy the condition.
"""

def main():
    val = 10
    if val > 100: # FIX ME
        print("Big!")
    else:
        print("Small!")
        raise Exception("Value should be considered Big for this exercise!")

if __name__ == "__main__":
    main()
