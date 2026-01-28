"""
Concept: Basic Types and Type Conversion

What:
Python is a dynamically typed language, but types still matter!
- `int`: Whole numbers (e.g., 10, -5)
- `float`: Decimal numbers (e.g., 3.14, -0.01)
- `str`: Text strings (e.g., "Hello")
- `bool`: Truth values (True, False)

Why:
You often receive input as strings (from users or files) but need to perform math on them.
Trying to add "10" (string) + 5 (int) will cause an error. You must convert types first.

How:
Use built-in functions to convert between types:
- `int("123")` -> 123 (String to Integer)
- `str(123)` -> "123" (Integer to String)
- `float("3.14")` -> 3.14 (String to Float)

Task:
1. Convert the string variable `my_string` ("123") to an integer.
2. Add 10 to that integer.
3. Convert the result back to a string and assign it to `result_string`.
"""

def main():
    my_string = "123"
    
    # FIX ME: Convert my_string to an integer, add 10, then convert back to string
    # my_number = 
    # result_string = 
    my_number = 0
    result_string = ""
    
    print(f"Result: {result_string}")
    
    if not isinstance(my_number, int):
        raise Exception("my_number should be an integer!")
    
    if my_number != 133:
        raise Exception(f"Expected 133, got {my_number}")

    if not isinstance(result_string, str):
        raise Exception("result_string should be a string!")
        
    if result_string != "133":
        raise Exception(f"Expected '133', got '{result_string}'")

if __name__ == "__main__":
    main()
