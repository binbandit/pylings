"""
Concept: JSON (JavaScript Object Notation)

JSON is a lightweight format for storing and transporting data. It looks almost
identical to Python dictionaries and lists, making it very intuitive to use.

Why it matters:
- Standard format for web APIs (REST, GraphQL responses)
- Common for configuration files
- Human-readable and easy to debug

Key functions from the `json` module:
- `json.dumps(obj)` - Serialize a Python object to a JSON string (dump to string)
- `json.loads(s)`   - Deserialize a JSON string to a Python object (load from string)

Example:
```python
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)   # '{"name": "Alice", "age": 30}'
parsed = json.loads(json_string) # {"name": "Alice", "age": 30}
```

Note: For file operations, use `json.dump()` and `json.load()` (without 's').

Task:
1. Convert the `data` dictionary into a JSON string named `json_str`
2. Parse `json_str` back into a Python dictionary named `parsed_data`
"""

import json


def main():
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}

    # TODO: Convert `data` to a JSON string using json.dumps()
    json_str = ""

    # TODO: Parse `json_str` back into a Python dictionary using json.loads()
    parsed_data = {}

    # Verification
    if not isinstance(json_str, str):
        raise Exception(
            "json_str should be a string\n"
            "Hint: json.dumps() returns a string representation"
        )

    if "Alice" not in json_str:
        raise Exception(
            "JSON string should contain 'Alice'\n"
            "Hint: Use json.dumps(data) to serialize the dictionary"
        )

    if parsed_data != data:
        raise Exception(
            f"Parsed data does not match original!\n"
            f"Expected: {data}\n"
            f"Got: {parsed_data}\n"
            "Hint: Use json.loads(json_str) to parse the JSON string"
        )

    print("JSON serialization verified!")


if __name__ == "__main__":
    main()
