
# RECURSION
# =========
#
# What: Repetitive execution of a function by calling itself.
#       Recursion requires a "base case" to stop the infinite loop.
#
# Why:  Essential for traversing trees, graphs, and solving divide-and-conquer problems.
#
# How:  def func(n):
#           if n == 0: return 0  <-- Base case
#           return n + func(n-1) <-- Recursive call
#
# Task:
# 1. Define a function `factorial(n)` that returns the factorial of n (n!).
#    factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
# 2. Define a function `fib(n)` that returns the nth Fibonacci number.
#    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).
#    fib(6) should be 8.

def factorial(n):
    pass

def fib(n):
    pass

def test_recursion():
    assert factorial(5) == 120, "Factorial of 5 should be 120"
    assert factorial(0) == 1, "Factorial of 0 should be 1"
    
    assert fib(0) == 0, "Fib(0) should be 0"
    assert fib(1) == 1, "Fib(1) should be 1"
    assert fib(6) == 8, "Fib(6) should be 8"

if __name__ == "__main__":
    test_recursion()
    print("Recursion basics passed!")
