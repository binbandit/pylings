"""
Concept: Pattern Matching (Sequences)
`match` can unpack sequences like lists or tuples. You can match specific structures.

Task: Add a case that matches a list with the single element "look": `case ["look"]`.
"""

def main():
    command = ["go", "north"]
    
    match command:
        case ["go", direction]:
            print(f"Going {direction}")
        case ["drop", *items]:
            print(f"Dropping {len(items)} items")
        # FIX ME: Add a case for ["look"] that prints "Looking around"
        case _:
            print("Unknown command")
            raise Exception("Command 'look' not handled!")

if __name__ == "__main__":
    # Simulate a command that isn't handled
    # But wait, local vars are hard to mock from outside without modding file.
    # I rely on the user editing the file.
    # The file as written runs with command = ["go", "north"] which passes effectively.
    # I must make it fail.
    check_command(["look"])

def check_command(command):
    match command:
        case ["go", direction]:
            print(f"Going {direction}")
        case ["drop", *items]:
            print(f"Dropping {len(items)} items")
        # FIX ME: Add case for ["look"]
        case _:
            print("Unknown command")
            raise Exception(f"Command {command} not handled!")
