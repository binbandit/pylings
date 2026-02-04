"""
while2.py - While True with Break

Sometimes you want a loop that runs forever until something specific happens.
Use `while True` with `break`:

    while True:
        user_input = input("Command: ")
        if user_input == "quit":
            break  # Exit the loop
        print(f"You typed: {user_input}")

This pattern is common for:
- Game loops
- Server request handlers
- Interactive command prompts

Your task: The loop below runs forever. Add an if statement that breaks
out of the loop when counter reaches 10.
"""


def main():
    counter = 0

    while True:
        counter += 1

        # TODO: If counter equals 10, break out of the loop

        # Safety check (prevents actual infinite loop during testing)
        if counter > 20:
            raise Exception("Loop went past 20! Add 'if counter == 10: break'")

    if counter != 10:
        raise Exception(f"counter should be 10, got {counter}")

    print(f"Broke out at counter = {counter}")
    print("While True with break works!")


if __name__ == "__main__":
    main()
