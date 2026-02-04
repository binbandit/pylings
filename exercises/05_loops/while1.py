"""
while1.py - While Loops

The `while` loop runs as long as a condition is True:

    count = 3
    while count > 0:
        print(count)
        count -= 1  # IMPORTANT: must change the condition variable!
    # Prints: 3, 2, 1

WARNING: If you forget to modify the condition variable, you'll create
an infinite loop! Always make sure the loop can eventually end.

Your task: Write a while loop that counts down from 5 to 1.
The loop should:
1. Print the current count
2. Decrease count by 1
3. Stop when count reaches 0
"""


def main():
    count = 5
    printed = []

    # TODO: Write a while loop that:
    # - continues while count > 0
    # - appends count to printed
    # - decrements count by 1

    if count != 0:
        raise Exception(f"count should be 0 after the loop, got {count}")

    expected = [5, 4, 3, 2, 1]
    if printed != expected:
        raise Exception(f"Should have printed {expected}, got {printed}")

    print("Countdown:", printed)
    print("While loops work!")


if __name__ == "__main__":
    main()
