"""
Concept: Dictionaries (Iteration)

What:
Dictionaries provide several ways to iterate over their contents:
- `.keys()` - iterate over keys only
- `.values()` - iterate over values only
- `.items()` - iterate over (key, value) pairs as tuples

Why:
You often need to process all entries in a dictionary - generating reports,
transforming data, or searching for specific values.

How:
    data = {"a": 1, "b": 2, "c": 3}

    # Iterate over keys (default behavior)
    for key in data:
        print(key)                # a, b, c

    # Iterate over values
    for value in data.values():
        print(value)              # 1, 2, 3

    # Iterate over key-value pairs (most common!)
    for key, value in data.items():
        print(f"{key}: {value}")  # a: 1, b: 2, c: 3

Task:
Use `.items()` to iterate over the dictionary and build a list of strings
in the format "key:value" (e.g., ["a:1", "b:2"]).
"""


def main():
    data = {"a": 1, "b": 2}

    # TODO: Iterate using .items() and build the output list
    # Hint: for key, value in data.items():
    #           output.append(f"{key}:{value}")
    output = []

    # Verification
    if len(output) == 0:
        raise Exception("output is empty! Use a for loop with data.items()")

    if "a:1" not in output:
        raise Exception(
            f"Expected 'a:1' in output, got {output}\n"
            "Format each item as f'{{key}}:{{value}}'"
        )

    if "b:2" not in output:
        raise Exception(f"Expected 'b:2' in output, got {output}")

    if len(output) != 2:
        raise Exception(f"Expected 2 items in output, got {len(output)}")

    print("Successfully iterated over the dictionary!")


if __name__ == "__main__":
    main()
