"""
Concept: MCP (Client)
An MCP client connects to servers and can discover available tools.

Task: Update the `list_tools` method to populate `self.available_tools`.
"""

class SimpleMCPClient:
    def __init__(self):
        self.available_tools = []
        
    def connect(self, server_name):
        # Simulation of connecting
        pass
        
    def list_tools(self):
        # FIX ME: Return the list of tools. 
        # For this exercise, simulate receiving ["read_file", "write_file"]
        # self.available_tools = ["read_file", "write_file"]
        return self.available_tools

def main():
    client = SimpleMCPClient()
    client.connect("local-server")
    
    tools = client.list_tools()
    
    if "read_file" not in tools:
        raise Exception("Client did not list 'read_file' tool!")
        
    print("MCP Client verified!")

if __name__ == "__main__":
    main()
