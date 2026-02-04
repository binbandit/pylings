"""
if1.py - If Statements

The `if` statement executes code only when a condition is True:

    if condition:
        # This runs if condition is True
        do_something()

Comparison operators:
- ==  equal to
- !=  not equal to
- >   greater than
- <   less than
- >=  greater than or equal
- <=  less than or equal

Your task: Fix the condition so that "Big!" is printed when val is 10.
Currently, the condition requires val > 100, but we want it to print
"Big!" for any value 10 or greater.
"""


def main():
    val = 10

    # TODO: Fix the condition - we want "Big!" to print when val >= 10
    if val > 100:
        print("Big!")
    else:
        print("Small!")
        raise Exception("The condition is wrong! 'Big!' should be printed.")


if __name__ == "__main__":
    main()
