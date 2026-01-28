"""
Concept: Tool Calling (Schema)
To let an LLM call functions, you must describe them using a JSON schema (usually OpenAI format).

Task: Define the `parameters` schema for the `get_weather` function.
"""

import json

def get_weather(location, unit="celsius"):
    return json.dumps({"location": location, "temperature": "22", "unit": unit})

def main():
    # FIX ME: Define the JSON schema for the 'get_weather' tool
    # It should have type "function", function name "get_weather", 
    # descriptions, and parameters (location: string, unit: string/enum)
    tool_schema = {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                # Fill this in!
            }
        }
    }
    
    # Simple validation check
    params = tool_schema.get("function", {}).get("parameters", {})
    if "location" not in params.get("properties", {}):
        raise Exception("Schema missing 'location' parameter!")
        
    print("Schema defined!")

if __name__ == "__main__":
    main()
