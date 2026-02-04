"""
Concept: Recursion Basics

Recursion is when a function calls itself. Every recursive function needs:
1. A BASE CASE: When to stop recursing (prevents infinite loops)
2. A RECURSIVE CASE: How to break the problem into smaller pieces

Example - Countdown:
    def countdown(n):
        if n <= 0:           # Base case
            print("Blastoff!")
            return
        print(n)
        countdown(n - 1)     # Recursive case (smaller problem)

Example - Sum of numbers from 1 to n:
    def sum_to_n(n):
        if n == 1:           # Base case
            return 1
        return n + sum_to_n(n - 1)  # n plus sum of rest

Task 1: Implement factorial(n)
    - factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    - factorial(0) = 1 (by definition)
    - Base case: n == 0 returns 1
    - Recursive case: n * factorial(n - 1)

Task 2: Implement fibonacci(n)
    - The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    - fib(0) = 0, fib(1) = 1
    - fib(n) = fib(n-1) + fib(n-2) for n > 1
"""


def factorial(n):
    """
    Calculate n! (n factorial).

    factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    factorial(0) = 1
    """
    # TODO: Implement the base case
    # Hint: What should factorial(0) return?

    # TODO: Implement the recursive case
    # Hint: factorial(n) = n * factorial(n - 1)

    pass  # Remove this and add your implementation


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(6) = 8

    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    # TODO: Implement the base cases
    # Hint: fib(0) = 0, fib(1) = 1

    # TODO: Implement the recursive case
    # Hint: fib(n) = fib(n-1) + fib(n-2)

    pass  # Remove this and add your implementation


def main():
    # Test factorial
    print("Testing factorial...")

    result = factorial(0)
    if result != 1:
        raise Exception(
            f"factorial(0) should return 1, got {result}\n"
            "Hint: The base case is when n == 0, return 1"
        )

    result = factorial(1)
    if result != 1:
        raise Exception(
            f"factorial(1) should return 1, got {result}\n"
            "Hint: 1! = 1 * factorial(0) = 1 * 1 = 1"
        )

    result = factorial(5)
    if result != 120:
        raise Exception(
            f"factorial(5) should return 120, got {result}\n"
            "Hint: 5! = 5 * 4 * 3 * 2 * 1 = 120"
        )

    print("  factorial tests passed!")

    # Test fibonacci
    print("Testing fibonacci...")

    result = fibonacci(0)
    if result != 0:
        raise Exception(
            f"fibonacci(0) should return 0, got {result}\n"
            "Hint: This is a base case - fib(0) = 0"
        )

    result = fibonacci(1)
    if result != 1:
        raise Exception(
            f"fibonacci(1) should return 1, got {result}\n"
            "Hint: This is a base case - fib(1) = 1"
        )

    result = fibonacci(6)
    if result != 8:
        raise Exception(
            f"fibonacci(6) should return 8, got {result}\n"
            "Hint: Sequence is 0, 1, 1, 2, 3, 5, 8\n"
            "      fib(n) = fib(n-1) + fib(n-2)"
        )

    result = fibonacci(10)
    if result != 55:
        raise Exception(f"fibonacci(10) should return 55, got {result}")

    print("  fibonacci tests passed!")

    print("\nRecursion basics mastered!")


if __name__ == "__main__":
    main()
