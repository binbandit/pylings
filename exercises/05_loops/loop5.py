"""
loop5.py - Continue

The `continue` statement skips the rest of the current iteration and
moves to the next one:

    for i in range(5):
        if i == 2:
            continue  # Skip printing 2
        print(i)
    # Prints: 0, 1, 3, 4 (skips 2)

`continue` is useful when you want to skip certain items but keep looping.

Your task: Use `continue` to skip even numbers. The total should be the
sum of only the odd numbers: 1 + 3 + 5 + 7 + 9 = 25.
"""


def main():
    total = 0

    for i in range(10):
        if i % 2 == 0:
            # TODO: Skip even numbers (0, 2, 4, 6, 8)
            pass

        total += i

    # Sum of odd numbers 1+3+5+7+9 = 25
    if total != 25:
        raise Exception(
            f"total should be 25 (sum of odd numbers), got {total}. Use 'continue' to skip evens!"
        )

    print(f"Sum of odd numbers 0-9: {total}")
    print("Continue works!")


if __name__ == "__main__":
    main()
