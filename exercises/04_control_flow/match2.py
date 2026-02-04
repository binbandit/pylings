"""
match2.py - Pattern Matching with Sequences

Match can destructure sequences (lists, tuples) and bind variables:

    match command:
        case ["go", direction]:
            print(f"Going {direction}")  # direction is extracted
        case ["pick", "up", item]:
            print(f"Picking up {item}")  # item is extracted
        case [action, *rest]:
            print(f"Action: {action}, args: {rest}")  # *rest captures remaining

You can also match literal values in sequences:
    case ["quit"]:
        print("Goodbye!")  # matches exactly ["quit"]

Your task: Add a case to handle the ["look"] command that returns "Looking around".
"""


def handle_command(command):
    match command:
        case ["go", direction]:
            return f"Going {direction}"
        case ["pick", "up", item]:
            return f"Picked up {item}"
        case ["drop", *items]:
            return f"Dropped {len(items)} item(s)"
        # TODO: Add a case for ["look"] that returns "Looking around"
        case _:
            return "Unknown command"


def main():
    # Test existing patterns
    print(handle_command(["go", "north"]))
    print(handle_command(["pick", "up", "sword"]))
    print(handle_command(["drop", "key", "coin"]))

    # Test the pattern you need to add
    result = handle_command(["look"])
    print(result)

    if result != "Looking around":
        raise Exception(f'["look"] should return "Looking around", got "{result}"')

    print("Pattern matching works!")


if __name__ == "__main__":
    main()
