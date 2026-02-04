"""
Concept: Model Context Protocol (MCP) - Server Basics

The Model Context Protocol (MCP) is a standard for connecting AI models to
external tools and data sources. It uses JSON-RPC 2.0 for communication.

An MCP server exposes capabilities (tools, resources, prompts) that clients
can discover and use. The basic flow:

1. Client connects to server
2. Client calls "tools/list" to discover available tools
3. Client calls "tools/call" to execute a specific tool
4. Server returns the result

JSON-RPC 2.0 request format:
{
    "jsonrpc": "2.0",
    "id": 1,                    # Unique request ID
    "method": "tools/list",     # The method to call
    "params": {}                # Optional parameters
}

JSON-RPC 2.0 response format:
{
    "jsonrpc": "2.0",
    "id": 1,                    # Same ID as request
    "result": { ... }           # The result data
}

Key MCP methods:
- "tools/list" - List available tools
- "tools/call" - Execute a tool
- "resources/list" - List available resources
- "prompts/list" - List available prompt templates

Task: Implement a basic MCP server that handles "tools/list" requests.
"""

import json
from typing import Any


# Define the tools our server provides
SERVER_TOOLS = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "inputSchema": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
        },
    },
    {
        "name": "read_file",
        "description": "Read contents of a file",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
]


def handle_mcp_request(request_json: str) -> dict[str, Any]:
    """Handle an incoming MCP JSON-RPC request.

    Args:
        request_json: JSON string containing the request

    Returns:
        dict: JSON-RPC response
    """
    # Parse the incoming JSON request
    request = json.loads(request_json)

    # Extract request components
    request_id = request.get("id")
    method = request.get("method")

    # TODO: Handle the "tools/list" method
    # When method is "tools/list", return a response with the SERVER_TOOLS
    #
    # The response should be a dict with:
    # - "jsonrpc": "2.0"
    # - "id": <same as request_id>
    # - "result": {"tools": SERVER_TOOLS}
    #
    # FIX ME: Check if method == "tools/list" and return the proper response

    if method == "tools/list":
        # FIX ME: Return the correct JSON-RPC response
        # Hint: The response needs jsonrpc version, id, and result with tools
        return {}  # FIX ME: Return proper response

    # Handle unknown methods with an error response
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


def main():
    print("Testing MCP Server Implementation")
    print("=" * 50)

    # Test 1: tools/list request
    print("\nTest 1: tools/list request")
    print("-" * 30)

    request = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})

    print(f"Request: {request}")

    response = handle_mcp_request(request)

    print(f"Response: {json.dumps(response, indent=2)}")

    # Validate response structure
    if response.get("jsonrpc") != "2.0":
        raise Exception(
            "Response missing 'jsonrpc': '2.0'\n"
            "Hint: Every JSON-RPC response must include the version"
        )

    if response.get("id") != 1:
        raise Exception(
            f"Response 'id' should be 1, got {response.get('id')}\n"
            "Hint: The response ID must match the request ID"
        )

    result = response.get("result")
    if result is None:
        raise Exception(
            "Response missing 'result' field!\n"
            "Hint: Successful responses have a 'result' field"
        )

    tools = result.get("tools")
    if tools is None:
        raise Exception(
            "Result missing 'tools' field!\n"
            "Hint: tools/list should return {'tools': [...]}"
        )

    if len(tools) != 2:
        raise Exception(
            f"Expected 2 tools, got {len(tools)}\n"
            "Hint: Return SERVER_TOOLS in the result"
        )

    tool_names = [t["name"] for t in tools]
    if "get_weather" not in tool_names:
        raise Exception("Missing 'get_weather' tool in response")

    print("\nTest 1 PASSED!")

    # Test 2: Unknown method
    print("\nTest 2: Unknown method (should return error)")
    print("-" * 30)

    request2 = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "unknown/method"})

    response2 = handle_mcp_request(request2)

    if "error" not in response2:
        raise Exception("Unknown methods should return an error response")

    print(f"Error response: {json.dumps(response2, indent=2)}")
    print("\nTest 2 PASSED!")

    print("\n" + "=" * 50)
    print("MCP Server implementation complete!")
    print("Your server can now respond to tools/list requests.")


if __name__ == "__main__":
    main()
