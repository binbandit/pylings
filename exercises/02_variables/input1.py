"""
input1.py - User Input

The `input()` function reads text from the user. It pauses the program,
waits for the user to type something, and returns what they typed as a string.

    name = input("What is your name? ")
    print(f"Hello, {name}!")

Important: input() ALWAYS returns a string, even if the user types a number:
    age = input("Enter age: ")  # If user types 25, age is "25" (string)
    age = int(age)              # Convert to integer if needed

For this automated exercise, we can't actually wait for input, so you'll
simulate it by directly assigning a value.

Your task: Assign the string "Alice" to the variable `user_name`.
"""


def main():
    # In a real program you would write:
    #     user_name = input("Enter your name: ")
    # For this exercise, directly assign "Alice" to user_name

    # TODO: Assign "Alice" to user_name
    user_name = None

    if user_name is None:
        raise Exception("You need to assign a value to user_name!")

    print(f"Hello, {user_name}!")

    if user_name != "Alice":
        raise Exception(f"user_name should be 'Alice', got '{user_name}'")

    print("Input handling complete!")


if __name__ == "__main__":
    main()
