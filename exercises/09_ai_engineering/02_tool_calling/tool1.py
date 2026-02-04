"""
Concept: Tool/Function Calling - Defining Tool Schemas

Modern LLMs can decide when to call external functions (tools) to accomplish tasks.
To enable this, you must describe your functions using a JSON schema that tells
the model:
- What the function does (description)
- What parameters it accepts (properties)
- Which parameters are required

The OpenAI tool schema format looks like:
{
    "type": "function",
    "function": {
        "name": "function_name",
        "description": "What the function does",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "What param1 is for"
                },
                "param2": {
                    "type": "integer",
                    "description": "What param2 is for"
                }
            },
            "required": ["param1"]
        }
    }
}

Common JSON schema types: "string", "integer", "number", "boolean", "array", "object"
You can also use "enum" to restrict values: {"type": "string", "enum": ["a", "b", "c"]}

Task: Complete the tool schema for the get_weather function below.
"""

import json


def get_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather for a location.

    Args:
        location: The city and country, e.g., "Paris, France"
        unit: Temperature unit, either "celsius" or "fahrenheit"

    Returns:
        JSON string with weather data
    """
    return json.dumps(
        {"location": location, "temperature": "22", "unit": unit, "condition": "sunny"}
    )


def create_tool_schema():
    """Create the JSON schema for the get_weather tool.

    Returns:
        dict: The complete tool schema
    """
    tool_schema = {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    # TODO: Define the "location" property
                    # It should be a string with a description
                    # Example: "location": {"type": "string", "description": "..."}
                    # TODO: Define the "unit" property
                    # It should be a string with enum values ["celsius", "fahrenheit"]
                    # and a description
                },
                # TODO: Add a "required" field listing required parameters
                # Hint: "location" is required, but "unit" has a default value
            },
        },
    }

    return tool_schema


def validate_schema(schema):
    """Validate that the tool schema is correctly defined."""
    # Check basic structure
    if schema.get("type") != "function":
        raise Exception("Schema 'type' should be 'function'")

    func = schema.get("function", {})
    if not func:
        raise Exception("Schema missing 'function' key")

    if func.get("name") != "get_weather":
        raise Exception("Function name should be 'get_weather'")

    params = func.get("parameters", {})
    if params.get("type") != "object":
        raise Exception("Parameters 'type' should be 'object'")

    props = params.get("properties", {})

    # Check location property
    if "location" not in props:
        raise Exception(
            "Missing 'location' in properties!\n"
            "Hint: Add a 'location' key with type and description"
        )

    loc = props["location"]
    if loc.get("type") != "string":
        raise Exception("'location' should have type 'string'")

    if "description" not in loc:
        raise Exception("'location' should have a description")

    # Check unit property
    if "unit" not in props:
        raise Exception(
            "Missing 'unit' in properties!\n"
            "Hint: Add a 'unit' key with type, enum, and description"
        )

    unit = props["unit"]
    if unit.get("type") != "string":
        raise Exception("'unit' should have type 'string'")

    if "enum" not in unit:
        raise Exception(
            "'unit' should have an 'enum' field!\n"
            "Hint: Use enum to restrict values to ['celsius', 'fahrenheit']"
        )

    if set(unit["enum"]) != {"celsius", "fahrenheit"}:
        raise Exception("'unit' enum should be ['celsius', 'fahrenheit']")

    # Check required field
    required = params.get("required", [])
    if "location" not in required:
        raise Exception(
            "Missing 'required' field or 'location' not in required!\n"
            "Hint: Add 'required': ['location'] to parameters"
        )


def main():
    schema = create_tool_schema()

    print("Validating tool schema...")
    validate_schema(schema)

    print("\nTool schema is valid!")
    print("\nGenerated schema:")
    print(json.dumps(schema, indent=2))

    print("\nThis schema can now be passed to an LLM to enable tool calling.")


if __name__ == "__main__":
    main()
