"""
MCP (Model Context Protocol) server management and tool execution
"""

import socket
import streamlit as st
from src.config.config import MCP_TOOLS, PUBLIC_MCP_SERVERS


def test_mcp_connection(host, port):
    """Test connection to MCP server"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, int(port)))
        sock.close()
        return result == 0
    except Exception as e:
        return False


def discover_mcp_tools(server_name):
    """Discover tools from MCP server"""
    return MCP_TOOLS.get(server_name.lower(), [])


def get_public_mcp_servers():
    """Get list of publicly available MCP servers"""
    return PUBLIC_MCP_SERVERS


def add_mcp_server(name, host, port, description):
    """Add a new MCP server to the session state"""
    st.session_state.mcp_servers[name] = {
        "host": host,
        "port": port,
        "description": description,
        "status": "disconnected",
        "tools": []
    }


def remove_mcp_server(name):
    """Remove an MCP server from the session state"""
    if name in st.session_state.mcp_servers:
        del st.session_state.mcp_servers[name]
        # Also remove from mcp_tools
        if name in st.session_state.mcp_tools:
            del st.session_state.mcp_tools[name]


def connect_to_mcp_server(server_name):
    """Connect to MCP server and discover tools"""
    if server_name not in st.session_state.mcp_servers:
        return False, "Server not found"
    
    server = st.session_state.mcp_servers[server_name]
    
    # Test connection
    if not test_mcp_connection(server["host"], server["port"]):
        return False, "Connection failed"
    
    # Discover tools
    tools = discover_mcp_tools(server_name)
    st.session_state.mcp_tools[server_name] = tools
    st.session_state.mcp_servers[server_name]["status"] = "connected"
    st.session_state.mcp_servers[server_name]["tools"] = tools
    
    return True, f"Connected successfully. Found {len(tools)} tools."


def disconnect_mcp_server(server_name):
    """Disconnect from an MCP server"""
    if server_name in st.session_state.mcp_servers:
        st.session_state.mcp_servers[server_name]["status"] = "disconnected"
        if server_name in st.session_state.mcp_tools:
            del st.session_state.mcp_tools[server_name]
        return True, "Disconnected successfully"
    return False, "Server not found"


def simulate_mcp_tool_execution(server_name, tool_name, arguments):
    """Simulate MCP tool execution for demo purposes"""
    # This would normally call the actual MCP server
    # For demo purposes, we'll simulate responses
    
    if server_name.lower() == "filesystem mcp":
        if tool_name == "read_file":
            path = arguments.get("path", "")
            return {
                "content": f"Demo content from {path}",
                "success": True,
                "message": f"Successfully read {path}"
            }
        elif tool_name == "list_directory":
            path = arguments.get("path", ".")
            return {
                "files": ["demo_file1.txt", "demo_file2.py", "demo_folder/"],
                "success": True,
                "message": f"Listed contents of {path}"
            }
    
    elif server_name.lower() == "git mcp":
        if tool_name == "git_status":
            return {
                "status": "M  demo_file.py\nA  new_file.txt",
                "success": True,
                "message": "Git status retrieved"
            }
        elif tool_name == "git_log":
            return {
                "log": "abc1234 Fix demo bug\ndef5678 Add new feature\nghi9012 Initial commit",
                "success": True,
                "message": "Git log retrieved"
            }
    
    elif server_name.lower() == "web search mcp":
        if tool_name == "search_web":
            query = arguments.get("query", "")
            return {
                "results": [
                    {
                        "title": f"Search result for '{query}'",
                        "url": "https://example.com/result1",
                        "snippet": f"This is a demo search result for '{query}'"
                    }
                ],
                "success": True,
                "message": f"Found results for '{query}'"
            }
    
    elif server_name.lower() == "memory mcp":
        if tool_name == "create_memory":
            content = arguments.get("content", "")
            return {
                "memory": {
                    "id": 1,
                    "content": content,
                    "created_at": "2024-01-01T00:00:00Z"
                },
                "success": True,
                "message": "Memory created successfully"
            }
        elif tool_name == "search_memories":
            return {
                "memories": [
                    {
                        "id": 1,
                        "content": "Demo memory content",
                        "created_at": "2024-01-01T00:00:00Z"
                    }
                ],
                "success": True,
                "message": "Memories found"
            }
    
    return {
        "success": False,
        "message": f"Tool '{tool_name}' not found in server '{server_name}'"
    }


def get_mcp_server_status():
    """Get status of all MCP servers"""
    status = {}
    for server_name, server_info in st.session_state.mcp_servers.items():
        status[server_name] = {
            "connected": server_info.get("status") == "connected",
            "host": server_info["host"],
            "port": server_info["port"],
            "tools_count": len(server_info.get("tools", []))
        }
    return status


def get_available_tools():
    """Get all available tools from connected MCP servers"""
    tools = {}
    for server_name, server_info in st.session_state.mcp_servers.items():
        if server_info.get("status") == "connected":
            tools[server_name] = server_info.get("tools", [])
    return tools
