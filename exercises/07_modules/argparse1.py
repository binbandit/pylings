"""
Concept: Command Line Arguments with argparse

The `argparse` module helps you build user-friendly command-line interfaces.
It automatically handles argument parsing, help messages, and error handling.

Basic usage:
    import argparse

    # Create a parser
    parser = argparse.ArgumentParser(description="My program")

    # Add arguments
    parser.add_argument("--name", help="Your name")
    parser.add_argument("--count", type=int, help="Number of times")
    parser.add_argument("--verbose", action="store_true", help="Verbose mode")

    # Parse arguments
    args = parser.parse_args()

    # Access values
    print(args.name)
    print(args.count)

Argument types:
- `--flag`: Optional argument (accessed as args.flag)
- `type=int`: Convert input to integer
- `action="store_true"`: Boolean flag (True if present, False if not)
- `required=True`: Make argument mandatory
- `default="value"`: Default value if not provided

Task:
1. Add an argument `--count` that accepts an integer (use type=int)
2. Parse the provided fake_args list
3. The parsed args should have args.count equal to 5
"""

import argparse


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Argument parsing exercise")

    # TODO: Add a --count argument that accepts an integer
    # Hint: parser.add_argument("--count", type=int, help="A count value")

    # We simulate command line input: python script.py --count 5
    fake_args = ["--count", "5"]

    # TODO: Parse the fake_args
    # Hint: args = parser.parse_args(fake_args)
    args = None  # TODO: Replace with parser.parse_args(...)

    # Verification
    if args is None:
        raise AssertionError(
            "args is None!\n"
            "Use args = parser.parse_args(fake_args) to parse the arguments."
        )

    if not hasattr(args, "count"):
        raise AssertionError(
            "args has no 'count' attribute!\n"
            "Did you add the --count argument with parser.add_argument('--count', ...)?"
        )

    if args.count != 5:
        raise AssertionError(
            f"Expected args.count to be 5, but got {args.count}.\n"
            "Make sure you added type=int to the --count argument."
        )

    print(f"Parsed argument: --count = {args.count}")
    print("Successfully used argparse!")


if __name__ == "__main__":
    main()
