"""
Concept: Model Context Protocol (MCP) - Client Implementation

An MCP client connects to MCP servers to discover and use their capabilities.
A typical client workflow:

1. Connect to one or more MCP servers
2. Call list_tools() to discover what tools are available
3. When the LLM wants to use a tool, call the appropriate server
4. Return results to the LLM

In practice, MCP clients manage multiple server connections and route tool
calls to the correct server. They also handle:
- Connection lifecycle (connect, disconnect, reconnect)
- Tool discovery and caching
- Error handling and retries

For this exercise, we'll build a simplified MCP client that simulates
the connection and tool discovery process.

Task: Complete the MCPClient class to track connections and list tools.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ServerConnection:
    """Represents a connection to an MCP server."""

    name: str
    url: str
    connected: bool = False
    tools: list[dict] = field(default_factory=list)


class MCPClient:
    """A simplified MCP client that manages server connections."""

    def __init__(self):
        """Initialize the MCP client."""
        self.servers: dict[str, ServerConnection] = {}
        self.available_tools: list[str] = []

    def connect(self, server_name: str, url: str = "localhost:8080") -> bool:
        """Connect to an MCP server.

        Args:
            server_name: A friendly name for this server
            url: The server URL (simulated in this exercise)

        Returns:
            bool: True if connection successful
        """
        # TODO: Create a ServerConnection and store it in self.servers
        # 1. Create a ServerConnection with name, url, and connected=True
        # 2. Store it in self.servers dict with server_name as the key
        # 3. Return True to indicate success
        #
        # FIX ME: Implement the connection logic
        # Hint: self.servers[server_name] = ServerConnection(...)

        return False  # FIX ME: Return True after storing the connection

    def disconnect(self, server_name: str) -> bool:
        """Disconnect from an MCP server.

        Args:
            server_name: The name of the server to disconnect

        Returns:
            bool: True if disconnection successful
        """
        if server_name in self.servers:
            self.servers[server_name].connected = False
            return True
        return False

    def list_tools(self, server_name: Optional[str] = None) -> list[str]:
        """List available tools from connected servers.

        In a real implementation, this would call "tools/list" on each server.
        For this exercise, we simulate the response.

        Args:
            server_name: If provided, only list tools from this server

        Returns:
            list[str]: Names of available tools
        """
        # Simulated tools that would come from servers
        simulated_tools = {
            "filesystem": ["read_file", "write_file", "list_directory"],
            "web": ["fetch_url", "search_web"],
            "database": ["query", "insert", "update"],
        }

        # TODO: Populate self.available_tools based on connected servers
        # 1. Clear self.available_tools
        # 2. If server_name is provided, get tools for that server only
        # 3. Otherwise, get tools from all connected servers
        # 4. Use simulated_tools.get(name, []) to get tools for each server
        # 5. Store the results in self.available_tools
        #
        # FIX ME: Implement tool listing logic
        # Hint:
        #   self.available_tools = []
        #   for name, conn in self.servers.items():
        #       if conn.connected:
        #           self.available_tools.extend(simulated_tools.get(name, []))

        return self.available_tools  # Currently returns empty list

    def is_connected(self, server_name: str) -> bool:
        """Check if a server is connected.

        Args:
            server_name: The server to check

        Returns:
            bool: True if server exists and is connected
        """
        server = self.servers.get(server_name)
        return server is not None and server.connected


def main():
    print("Testing MCP Client Implementation")
    print("=" * 50)

    client = MCPClient()

    # Test 1: Connect to servers
    print("\nTest 1: Connecting to servers")
    print("-" * 30)

    result = client.connect("filesystem", "localhost:8001")

    if not result:
        raise Exception(
            "connect() returned False!\n"
            "Hint: Create a ServerConnection and store it in self.servers,\n"
            "      then return True"
        )

    if "filesystem" not in client.servers:
        raise Exception(
            "Server not stored in self.servers!\n"
            "Hint: self.servers[server_name] = ServerConnection(...)"
        )

    if not client.is_connected("filesystem"):
        raise Exception(
            "Server not marked as connected!\n"
            "Hint: Set connected=True when creating ServerConnection"
        )

    print("Connected to 'filesystem' server")

    client.connect("web", "localhost:8002")
    print("Connected to 'web' server")

    print("Test 1 PASSED!")

    # Test 2: List tools
    print("\nTest 2: Listing tools")
    print("-" * 30)

    tools = client.list_tools()

    if not tools:
        raise Exception(
            "list_tools() returned empty list!\n"
            "Hint: Iterate through connected servers and collect their tools\n"
            "      using the simulated_tools dict"
        )

    expected_tools = [
        "read_file",
        "write_file",
        "list_directory",
        "fetch_url",
        "search_web",
    ]

    for tool in expected_tools:
        if tool not in tools:
            raise Exception(
                f"Missing tool: {tool}\n"
                f"Got tools: {tools}\n"
                "Hint: Extend self.available_tools with tools from each connected server"
            )

    print(f"Available tools: {tools}")
    print("Test 2 PASSED!")

    # Test 3: Disconnect
    print("\nTest 3: Disconnecting")
    print("-" * 30)

    client.disconnect("filesystem")

    if client.is_connected("filesystem"):
        raise Exception("Server should be disconnected")

    print("Disconnected from 'filesystem'")

    # After disconnect, list_tools should only show web tools
    tools_after = client.list_tools()

    if "read_file" in tools_after:
        raise Exception(
            "Disconnected server's tools should not appear!\n"
            "Hint: Only include tools from servers where conn.connected is True"
        )

    if "fetch_url" not in tools_after:
        raise Exception("Connected server's tools should still appear")

    print(f"Tools after disconnect: {tools_after}")
    print("Test 3 PASSED!")

    print("\n" + "=" * 50)
    print("MCP Client implementation complete!")
    print("Your client can connect to servers and discover tools.")


if __name__ == "__main__":
    main()
