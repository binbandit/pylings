"""
loop3.py - Modifying Loop Variables

Inside a loop, you can (and often need to) modify variables:

    total = 0
    for i in range(5):
        total += i  # same as: total = total + i
    # total is now 10 (0+1+2+3+4)

Common operations:
    x += 1   # increment (add 1)
    x -= 1   # decrement (subtract 1)
    x *= 2   # multiply by 2
    x //= 2  # integer divide by 2

Your task: The loop should count how many even numbers are in the range 0-9.
Add code inside the loop to increment `count` when `i` is even.
Remember: a number is even if i % 2 == 0.
"""


def main():
    count = 0

    for i in range(10):
        # TODO: If i is even, increment count
        pass

    # There are 5 even numbers in 0-9: 0, 2, 4, 6, 8
    if count != 5:
        raise Exception(f"count should be 5 (even numbers in 0-9), got {count}")

    print(f"Found {count} even numbers")
    print("Loop modification works!")


if __name__ == "__main__":
    main()
