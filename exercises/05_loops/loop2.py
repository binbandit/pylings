"""
loop2.py - Range

`range()` generates a sequence of numbers, commonly used with for loops:

    range(5)        -> 0, 1, 2, 3, 4         (start=0, stop=5)
    range(2, 5)     -> 2, 3, 4               (start=2, stop=5)
    range(0, 10, 2) -> 0, 2, 4, 6, 8         (start=0, stop=10, step=2)

Note: The stop value is NOT included in the range.

Example:
    for i in range(3):
        print(i)  # prints 0, 1, 2

Your task: Fix the range() call so the loop prints numbers 0 through 9.
Currently it only prints 0.
"""


def main():
    total = 0

    # TODO: Fix the range so this loop runs 10 times (0 through 9)
    for i in range(1):
        print(i)
        total += i

    # Sum of 0+1+2+3+4+5+6+7+8+9 = 45
    if total != 45:
        raise Exception(f"Total should be 45 (sum of 0-9), got {total}. Fix the range!")

    print(f"Sum of 0-9: {total}")
    print("Range works!")


if __name__ == "__main__":
    main()
