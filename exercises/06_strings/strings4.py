"""
strings4.py - String Methods

Strings have many built-in methods. Here are some common ones:

    text = "  Hello World  "

    text.upper()      # "  HELLO WORLD  "
    text.lower()      # "  hello world  "
    text.strip()      # "Hello World" (removes leading/trailing whitespace)
    text.replace("World", "Python")  # "  Hello Python  "
    text.startswith("  He")  # True
    text.endswith("  ")      # True

Methods return a NEW string - they don't modify the original!

Your task: Use the .lower() method to convert the loud message to lowercase.
"""


def main():
    loud_message = "STOP SHOUTING!"

    # TODO: Use .lower() to make the message lowercase
    quiet_message = loud_message  # This doesn't change anything!

    if quiet_message != "stop shouting!":
        raise Exception(
            f"Expected 'stop shouting!', got '{quiet_message}'. Use .lower()!"
        )

    print(f"Before: {loud_message}")
    print(f"After: {quiet_message}")
    print("String methods work!")


if __name__ == "__main__":
    main()
