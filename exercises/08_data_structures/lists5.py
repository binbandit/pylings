"""
Concept: List Comprehensions
List comprehensions provide a concise way to create lists based on existing lists.
Syntax: `[expression for item in iterable if condition]`

Task: Create a list of squares of even numbers from the `nums` list.
"""

def main():
    # List comprehension!
    nums = [1, 2, 3, 4, 5]
    
    # FIX ME: Create a new list with squares of even numbers using comprehension
    # squares = [x*x for x in nums if ???]
    squares = []
    
    if squares != [4, 16]: # 2*2=4, 4*4=16
        raise Exception(f"Expected [4, 16], got {squares}")

if __name__ == "__main__":
    main()
