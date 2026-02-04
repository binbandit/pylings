"""
if2.py - If/Else

The `else` clause provides an alternative when the `if` condition is False:

    if condition:
        # runs when True
    else:
        # runs when False

Example:
    age = 15
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

Your task: The code below is missing an `else` clause. Add it so that
"Small" is printed when val is not greater than 10.
"""


def main():
    val = 5
    result = None

    if val > 10:
        result = "Big"
    # TODO: Add an else clause that sets result to "Small"

    if result is None:
        raise Exception("You need to add an 'else' clause that sets result to 'Small'")

    print(result)

    if result != "Small":
        raise Exception(f"Expected 'Small' but got '{result}'")

    print("If/else works!")


if __name__ == "__main__":
    main()
