"""
strings3.py - String Slicing

Slicing extracts a portion of a string using [start:end]:

    text = "Hello, World!"
    text[0:5]   # "Hello" (index 0 to 4)
    text[7:12]  # "World" (index 7 to 11)
    text[:5]    # "Hello" (from start to 4)
    text[7:]    # "World!" (from 7 to end)
    text[-1]    # "!" (last character)
    text[-6:]   # "World!" (last 6 characters)

Remember: the end index is NOT included in the result.

Your task: Use slicing to extract the first three letters "abc" from the alphabet.
"""


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # TODO: Fix the slice to get only "abc"
    first_three = alphabet[:]  # This gets the whole string!

    if first_three != "abc":
        raise Exception(f"Expected 'abc', got '{first_three}'. Fix the slice!")

    print(f"First three letters: {first_three}")
    print("String slicing works!")


if __name__ == "__main__":
    main()
