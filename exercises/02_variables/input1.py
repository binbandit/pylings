"""
Concept: User Input

What:
The `input()` function pauses your program and waits for the user to type something and press Enter.
It ALWAYS returns the input as a string (str), even if the user types a number.

Why:
Interactive programs need to get data from users—whether it's a name, a choice in a game, or a configuration value.

How:
```python
name = input("Enter your name: ")
age = input("Enter your age: ") # "25" (string)
age_number = int(age) # Convert to int
```

Task:
Simulate a user input of "Alice" and assign it to `user_name`.
(In this automated exercise, we manually assign the variable instead of calling input(), 
but conceptually this is handling user input).
"""

def main():
    # In a real app, you would do: user_name = input("Enter your name: ")
    # For this exercise, just assign the value "Alice" to the variable `user_name`
    
    user_name = None # FIX ME
    
    if user_name is None:
        print("Please set the user_name variable!")
        return

    print(f"Hello, {user_name}!")
    
    if user_name != "Alice":
        raise Exception("user_name should be 'Alice'")

if __name__ == "__main__":
    main()
