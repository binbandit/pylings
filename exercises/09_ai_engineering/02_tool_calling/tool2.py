"""
Concept: Tool Calling (Execution)
When an LLM decides to call a tool, it returns a JSON string. You must parse this JSON and execute the corresponding Python function.

Task: Parse the arguments JSON and call the function dynamically.
"""

import json

def get_weather(location):
    return f"Weather in {location} is Sunny"

def main():
    # Simulating an LLM response requesting a tool call
    llm_response = {
        "tool_calls": [
            {
                "id": "call_123",
                "function": {
                    "name": "get_weather",
                    "arguments": "{\"location\": \"Paris\"}"
                }
            }
        ]
    }
    
    tool_call = llm_response["tool_calls"][0]
    func_name = tool_call["function"]["name"]
    args_str = tool_call["function"]["arguments"]
    
    # FIX ME: Parse the arguments JSON and call the function dynamically!
    # args = ???
    # if func_name == "get_weather":
    #     result = get_weather(**args)
    
    result = ""
    
    if result != "Weather in Paris is Sunny":
        raise Exception("Did not call the tool correctly!")

    print("Tool called successfully!")

if __name__ == "__main__":
    main()
