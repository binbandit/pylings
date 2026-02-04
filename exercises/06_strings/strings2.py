"""
strings2.py - F-Strings (Formatted String Literals)

F-strings let you embed expressions directly in strings using {}:

    name = "Alice"
    age = 30
    message = f"My name is {name} and I'm {age} years old"
    # Result: "My name is Alice and I'm 30 years old"

F-strings can contain any expression:
    f"2 + 2 = {2 + 2}"      # "2 + 2 = 4"
    f"Length: {len(name)}"  # "Length: 5"

Your task: Create an f-string that produces "I am learning Python version 3.12"
using the variables `name` and `version`.
"""


def main():
    name = "Python"
    version = 3.12

    # TODO: Create message using an f-string (starts with f"...")
    message = None

    expected = "I am learning Python version 3.12"

    if message is None:
        raise Exception("Assign an f-string to 'message'")

    if message != expected:
        raise Exception(f"Expected '{expected}', got '{message}'")

    print(message)
    print("F-strings work!")


if __name__ == "__main__":
    main()
