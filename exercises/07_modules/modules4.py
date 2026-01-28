"""
Concept: Creating Modules

What:
A module is simply a Python file (ending in `.py`) that contains definitions and statements.
You can import code from one file into another.

Why:
As your program grows, splitting it into multiple files makes it easier to manage, understand, and reuse.

How:
1. Create a file `my_lib.py` with a function `greet()`.
2. In another file (e.g., `main.py`), use `import my_lib` or `from my_lib import greet`.

Task:
1. We have created a helper file `exercises/07_modules/my_lib.py` for you.
2. Inside `my_lib.py`, define a function `calculate_area(length, width)` that returns `length * width`.
3. Inside THIS file (`modules4.py`), import `calculate_area` from `my_lib`.
4. Use it to calculate the area of a 5x10 rectangle.
"""

# FIX ME: Import calculate_area from my_lib
# from my_lib import calculate_area

def main():
    # FIX ME: Use the imported function
    # area = calculate_area(5, 10)
    area = 0
    
    if area != 50:
        raise Exception(f"Expected area 50, got {area}. Did you implement and import the function?")

if __name__ == "__main__":
    main()
