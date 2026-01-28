"""
Concept: Typing (Basic)
Python is dynamically typed, but type hints allow you to specify expected types.
`x: int` means `x` is expected to be an integer.

Task: Assign the integer 10 to `x` to satisfy the check.
"""

def main():
    x: int
    if x == 10:
        print("x is 10")
    else:
        print("x is not 10")
        exit(1)

if __name__ == "__main__":
    main()
