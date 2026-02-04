"""
if3.py - Elif (Else If)

Use `elif` to check multiple conditions in sequence:

    if condition1:
        # runs if condition1 is True
    elif condition2:
        # runs if condition1 is False and condition2 is True
    elif condition3:
        # runs if condition1 and condition2 are False and condition3 is True
    else:
        # runs if all conditions are False

Only ONE block executes - the first one whose condition is True.

Your task: Add an `elif` clause to handle "Medium" values (between 10 and 100).
"""


def main():
    val = 50
    result = None

    if val < 10:
        result = "Small"
    # TODO: Add an elif for values >= 10 and < 100 (Medium)
    else:
        result = "Large"

    print(f"Value {val} is: {result}")

    if result != "Medium":
        raise Exception(
            f"val={val} should be 'Medium', but got '{result}'. Add an elif clause!"
        )

    print("Elif works correctly!")


if __name__ == "__main__":
    main()
