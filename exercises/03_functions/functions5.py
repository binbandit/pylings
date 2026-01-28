"""
Concept: Functions (Return Types)
Functions return values using the `return` keyword. You can hint the return type using `-> Type`.

Task: Ensure the function returns an integer as promised by its type hint.
"""

def square(num) -> int:
    return num * num

def main():
    answer = square(3)
    print(answer)
    # Let's force a type error or logic check
    if not isinstance(answer, int):
        raise TypeError("Did not return an int!")

if __name__ == "__main__":
    main()
