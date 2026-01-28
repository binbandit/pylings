"""
Concept: While Loops

What:
A `while` loop repeatedly executes a block of code as long as a condition is True.
It is like an "if" statement that repeats itself.

Why:
Use `while` loops when you don't know exactly how many times you need to loop,
but you know the condition for stopping (e.g., "keep asking until user types 'quit'").

How:
```python
count = 5
while count > 0:
    print(count)
    count = count - 1 # VERY IMPORTANT: Update the condition variable!
```
If you forget to update the variable (like decreasing `count`), the loop will run forever (Infinite Loop).

Task:
Write a while loop that prints `count` and decrements it by 1, until it reaches 0.
"""

def main():
    count = 5
    
    # FIX ME: Use a while loop to print count and then decrement it
    # while count > 0:
    #     print(count)
    #     count -= 1
    
    if count != 0:
        raise Exception(f"Count should be 0, but it is {count}. Did you use a loop?")

if __name__ == "__main__":
    main()
