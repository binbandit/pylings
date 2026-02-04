"""
input1.py - User Input

The `input()` function reads text from the user. It displays a prompt,
waits for the user to type something, and returns what they typed as a string.

    name = input("What is your name? ")
    print(f"Hello, {name}!")

Important: input() ALWAYS returns a string, even if the user types a number:
    age = input("Enter age: ")  # If user types 25, age is "25" (string)
    age = int(age)              # Convert to integer if needed

Your task: Use the input() function to ask for the user's name and store
it in the variable `user_name`. Use the prompt "Enter your name: "
"""


def get_greeting():
    # TODO: Use input() to get the user's name
    # The prompt should be exactly: "Enter your name: "
    user_name = None

    return f"Hello, {user_name}!"


# === Testing code (don't modify below) ===
if __name__ == "__main__":
    from unittest.mock import patch

    # Test that input() is actually being called with correct prompt
    with patch("builtins.input", return_value="Alice") as mock_input:
        result = get_greeting()

        # Check that input() was called
        if not mock_input.called:
            raise Exception(
                "You need to use input() to get the user's name!\n"
                'Example: user_name = input("Enter your name: ")'
            )

        # Check the prompt is correct
        call_args = mock_input.call_args
        if call_args is None or len(call_args[0]) == 0:
            raise Exception(
                'Pass a prompt string to input()!\nExample: input("Enter your name: ")'
            )

        prompt = call_args[0][0]
        if "name" not in prompt.lower():
            raise Exception(
                f"Your prompt should ask for a name.\n"
                f'Got: "{prompt}"\n'
                f'Expected something like: "Enter your name: "'
            )

        # Check the result
        if "Alice" not in result:
            raise Exception(
                f"The greeting should include the user's name.\n"
                f'Got: "{result}"\n'
                f'Expected something like: "Hello, Alice!"'
            )

        print(f'Prompt used: "{prompt}"')
        print(f"Result: {result}")
        print("input() works correctly!")
