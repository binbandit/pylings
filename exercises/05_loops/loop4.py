"""
loop4.py - Break

The `break` statement exits a loop immediately:

    for i in range(100):
        if i == 5:
            break  # Exit the loop
        print(i)
    # Only prints 0, 1, 2, 3, 4

`break` is useful when you're searching for something and want to stop
once you find it.

Your task: Use `break` to exit the loop when i equals 5.
Currently, the loop continues past 5 and raises an exception.
"""


def main():
    last_i = 0

    for i in range(10):
        last_i = i
        print(i)

        if i == 5:
            # TODO: Exit the loop here
            pass

        if i > 5:
            raise Exception(f"Loop continued past 5! Got to {i}. Use 'break' to exit.")

    if last_i != 5:
        raise Exception(f"Loop should have stopped at 5, got to {last_i}")

    print("Break works!")


if __name__ == "__main__":
    main()
