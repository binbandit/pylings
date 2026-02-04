"""
strings5.py - Split and Join

split() breaks a string into a list based on a delimiter:
    "a,b,c".split(",")      # ["a", "b", "c"]
    "hello world".split()   # ["hello", "world"] (splits on whitespace by default)

join() combines a list into a string with a separator:
    ",".join(["a", "b", "c"])  # "a,b,c"
    " ".join(["hello", "world"])  # "hello world"

Note: join() is called on the SEPARATOR, not the list!

Your task:
1. Split the comma-separated string into a list
2. Join the list back together with pipe (|) separators
"""


def main():
    csv_string = "apple,banana,orange"

    # TODO: Use split() to create a list of items
    items = []

    if items != ["apple", "banana", "orange"]:
        raise Exception(f"items should be ['apple', 'banana', 'orange'], got {items}")

    # TODO: Use join() to create a pipe-separated string
    pipe_string = ""

    if pipe_string != "apple|banana|orange":
        raise Exception(
            f"pipe_string should be 'apple|banana|orange', got '{pipe_string}'"
        )

    print(f"Original: {csv_string}")
    print(f"As list: {items}")
    print(f"With pipes: {pipe_string}")
    print("Split and join work!")


if __name__ == "__main__":
    main()
