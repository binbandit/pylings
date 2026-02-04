"""
Concept: Tool/Function Calling - Executing Tool Calls

When an LLM decides to use a tool, it returns a structured response containing:
- The function name to call
- The arguments as a JSON string

Your code must:
1. Parse the JSON arguments string into a Python dictionary
2. Look up the correct function to call
3. Call the function with the parsed arguments
4. Return the result to the LLM

Example LLM tool call response:
{
    "tool_calls": [{
        "id": "call_abc123",
        "function": {
            "name": "get_weather",
            "arguments": "{\"location\": \"Paris\"}"  # JSON string!
        }
    }]
}

Key insight: The "arguments" field is a JSON STRING, not a dict!
You must use json.loads() to parse it before calling the function.

Task: Implement the execute_tool_call function to parse arguments and call the tool.
"""

import json
from typing import Callable


def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: Sunny, 22C"


def search_web(query: str, num_results: int = 3) -> str:
    """Search the web for a query."""
    return f"Found {num_results} results for '{query}'"


def calculate(expression: str) -> str:
    """Safely evaluate a math expression."""
    # In production, use a proper math parser!
    allowed = set("0123456789+-*/(). ")
    if all(c in allowed for c in expression):
        return str(eval(expression))
    return "Invalid expression"


# Registry mapping function names to actual functions
AVAILABLE_TOOLS: dict[str, Callable] = {
    "get_weather": get_weather,
    "search_web": search_web,
    "calculate": calculate,
}


def execute_tool_call(tool_call: dict) -> str:
    """Execute a tool call from an LLM response.

    Args:
        tool_call: Dict with "function" containing "name" and "arguments"

    Returns:
        str: The result of calling the tool
    """
    # Extract function name and arguments string
    function_info = tool_call["function"]
    function_name = function_info["name"]
    arguments_json = function_info["arguments"]  # This is a JSON string!

    # TODO: Parse the JSON arguments string into a Python dictionary
    # Hint: Use json.loads() to parse JSON strings
    arguments = {}  # FIX ME: Parse arguments_json

    # TODO: Look up the function in AVAILABLE_TOOLS and call it with the arguments
    # Hint: Use **arguments to unpack the dict as keyword arguments
    result = ""  # FIX ME: Call the appropriate function

    return result


def main():
    # Simulate an LLM response with a tool call
    llm_response = {
        "tool_calls": [
            {
                "id": "call_abc123",
                "function": {
                    "name": "get_weather",
                    "arguments": '{"location": "Tokyo, Japan"}',
                },
            }
        ]
    }

    print("Processing LLM tool call response...")
    print(f"Raw response: {json.dumps(llm_response, indent=2)}\n")

    # Execute the tool call
    tool_call = llm_response["tool_calls"][0]
    result = execute_tool_call(tool_call)

    expected = "Weather in Tokyo, Japan: Sunny, 22C"
    if result != expected:
        raise Exception(
            f"Tool execution failed!\n"
            f"Expected: {expected}\n"
            f"Got: {result}\n\n"
            f"Hint: Make sure you:\n"
            f"  1. Parse the arguments JSON string with json.loads()\n"
            f"  2. Look up the function in AVAILABLE_TOOLS\n"
            f"  3. Call it with **arguments to unpack the dict"
        )

    print(f"Tool call executed successfully!")
    print(f"Function: {tool_call['function']['name']}")
    print(f"Arguments: {tool_call['function']['arguments']}")
    print(f"Result: {result}")

    # Test another tool
    print("\n--- Testing calculate tool ---")
    calc_call = {
        "function": {"name": "calculate", "arguments": '{"expression": "2 + 2 * 3"}'}
    }

    calc_result = execute_tool_call(calc_call)
    if calc_result != "8":
        raise Exception(f"Calculate failed! Expected '8', got '{calc_result}'")

    print(f"Calculate result: {calc_result}")
    print("\nAll tool calls executed correctly!")


if __name__ == "__main__":
    main()
