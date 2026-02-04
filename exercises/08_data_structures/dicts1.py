"""
Concept: Dictionaries (Creation)

What:
Dictionaries store key-value pairs. Each key maps to a value, like a real
dictionary where words (keys) map to definitions (values).
Keys must be immutable (strings, numbers, tuples) and unique.

Why:
- Fast lookups by key: O(1) average time
- Perfect for representing structured data (user profiles, configurations)
- More readable than lists when you want named access to items
- The foundation of JSON data handling

How:
    # Creating dictionaries
    person = {"name": "Alice", "age": 30}
    empty = {}
    also_works = dict(name="Alice", age=30)

    # Accessing values
    name = person["name"]     # "Alice"
    age = person.get("age")   # 30

    # Keys can be any immutable type
    coords = {(0, 0): "origin", (1, 1): "diagonal"}

Task:
Create a dictionary named `person` with two key-value pairs:
- "name" with value "Alice"
- "age" with value 30
"""


def main():
    # TODO: Create a dictionary with "name": "Alice" and "age": 30
    person = {}

    # Verification
    if len(person) == 0:
        raise Exception(
            "person is empty! Add key-value pairs: {'name': 'Alice', 'age': 30}"
        )

    if "name" not in person:
        raise Exception("Missing 'name' key! Add it: 'name': 'Alice'")

    if person.get("name") != "Alice":
        raise Exception(f"Expected name to be 'Alice', got '{person.get('name')}'")

    if "age" not in person:
        raise Exception("Missing 'age' key! Add it: 'age': 30")

    if person.get("age") != 30:
        raise Exception(f"Expected age to be 30, got {person.get('age')}")

    print("Dictionary created successfully!")


if __name__ == "__main__":
    main()
