"""
Concept: MCP (Server Handling)
The Model Context Protocol (MCP) uses JSON-RPC. A server must handle requests like `tools/list` and return a standard response.

Task: Implement the handler for `tools/list` to return the available tools.
"""

import json

def handle_json_rpc(request_str):
    request = json.loads(request_str)
    
    # FIX ME: Implement a basic MCP "list_tools" handler
    # if request["method"] == "tools/list":
    #     return {
    #         "jsonrpc": "2.0",
    #         "id": request["id"],
    #         "result": {
    #             "tools": [{"name": "get_weather"}]
    #         }
    #     }
    
    return {}

def main():
    req = json.dumps({
        "jsonrpc": "2.0", 
        "id": 1, 
        "method": "tools/list"
    })
    
    response = handle_json_rpc(req)
    
    if response.get("result", {}).get("tools", []) != [{"name": "get_weather"}]:
        raise Exception("Did not return correct tools list!")
        
    print("MCP Server handled request!")

if __name__ == "__main__":
    main()
