"""
Concept: JSON

What:
JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data.
It looks almost identical to Python dictionaries and lists.

Why:
It is the standard format for web APIs and configuration files. You will use it constantly.

How:
- `json.dumps(obj)`: Serialize (Dump) a Python object -> JSON string.
- `json.loads(str)`: Deserialize (Load) a JSON string -> Python object.

```python
import json
my_dict = {"id": 1}
json_str = json.dumps(my_dict)   # '{"id": 1}' (string)
data = json.loads(json_str)      # {"id": 1} (dict)
```

Task:
1. Serialize the `data` dictionary into a JSON string named `json_str`.
2. Parse `json_str` back into a Python object named `parsed_data`.
"""

import json

def main():
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}
    
    # FIX ME: Convert data to a JSON string
    # json_str = ...
    json_str = ""
    
    # FIX ME: Parse the variable json_str back into a Python dictionary
    # parsed_data = ...
    parsed_data = {}
    
    if not isinstance(json_str, str):
        raise Exception("json_str should be a string")
        
    if "Alice" not in json_str:
        raise Exception("JSON string should contain 'Alice'")
        
    if parsed_data != data:
        raise Exception("Parsed data does not match original data")

if __name__ == "__main__":
    main()
