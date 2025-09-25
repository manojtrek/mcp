#!/usr/bin/env python3
"""
Demo MCP Servers for testing the Streamlit application
These are simplified implementations of common MCP servers
"""

import asyncio
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Simple MCP server implementations
class DemoMCPServer:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.tools = []
    
    async def start(self):
        print(f"Starting {self.name} on port {self.port}")
        # In a real implementation, this would start an MCP server
        # For demo purposes, we'll just simulate the server running
        return True

class FilesystemMCPServer(DemoMCPServer):
    def __init__(self):
        super().__init__("Filesystem MCP", 3001)
        self.tools = [
            {
                "name": "read_file",
                "description": "Read contents of a file",
                "input_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"]
                }
            },
            {
                "name": "write_file", 
                "description": "Write content to a file",
                "input_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
                    "required": ["path", "content"]
                }
            },
            {
                "name": "list_directory",
                "description": "List contents of a directory", 
                "input_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"]
                }
            }
        ]
    
    async def execute_tool(self, tool_name, arguments):
        if tool_name == "read_file":
            path = arguments.get("path")
            try:
                with open(path, 'r') as f:
                    return {"content": f.read(), "success": True}
            except Exception as e:
                return {"error": str(e), "success": False}
        
        elif tool_name == "write_file":
            path = arguments.get("path")
            content = arguments.get("content")
            try:
                with open(path, 'w') as f:
                    f.write(content)
                return {"success": True, "message": f"File written to {path}"}
            except Exception as e:
                return {"error": str(e), "success": False}
        
        elif tool_name == "list_directory":
            path = arguments.get("path", ".")
            try:
                files = os.listdir(path)
                return {"files": files, "success": True}
            except Exception as e:
                return {"error": str(e), "success": False}

class GitMCPServer(DemoMCPServer):
    def __init__(self):
        super().__init__("Git MCP", 3002)
        self.tools = [
            {
                "name": "git_status",
                "description": "Get git repository status",
                "input_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"]
                }
            },
            {
                "name": "git_log",
                "description": "Get git commit history",
                "input_schema": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}, "limit": {"type": "integer"}},
                    "required": ["path"]
                }
            }
        ]
    
    async def execute_tool(self, tool_name, arguments):
        path = arguments.get("path", ".")
        
        if tool_name == "git_status":
            try:
                result = subprocess.run(["git", "status", "--porcelain"], 
                                      cwd=path, capture_output=True, text=True)
                return {"status": result.stdout, "success": True}
            except Exception as e:
                return {"error": str(e), "success": False}
        
        elif tool_name == "git_log":
            limit = arguments.get("limit", 10)
            try:
                result = subprocess.run(["git", "log", f"--max-count={limit}", "--oneline"], 
                                      cwd=path, capture_output=True, text=True)
                return {"log": result.stdout, "success": True}
            except Exception as e:
                return {"error": str(e), "success": False}

class WebSearchMCPServer(DemoMCPServer):
    def __init__(self):
        super().__init__("Web Search MCP", 3003)
        self.tools = [
            {
                "name": "search_web",
                "description": "Search the web for information",
                "input_schema": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}, "max_results": {"type": "integer"}},
                    "required": ["query"]
                }
            }
        ]
    
    async def execute_tool(self, tool_name, arguments):
        if tool_name == "search_web":
            query = arguments.get("query")
            max_results = arguments.get("max_results", 5)
            
            # Simulate web search results
            results = [
                {
                    "title": f"Search result 1 for '{query}'",
                    "url": f"https://example.com/result1",
                    "snippet": f"This is a simulated search result for '{query}'"
                },
                {
                    "title": f"Search result 2 for '{query}'", 
                    "url": f"https://example.com/result2",
                    "snippet": f"Another simulated result for '{query}'"
                }
            ]
            
            return {"results": results[:max_results], "success": True}

class MemoryMCPServer(DemoMCPServer):
    def __init__(self):
        super().__init__("Memory MCP", 3005)
        self.memories = []
        self.tools = [
            {
                "name": "create_memory",
                "description": "Create a new memory",
                "input_schema": {
                    "type": "object",
                    "properties": {"content": {"type": "string"}, "tags": {"type": "array", "items": {"type": "string"}}},
                    "required": ["content"]
                }
            },
            {
                "name": "search_memories",
                "description": "Search existing memories",
                "input_schema": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"]
                }
            }
        ]
    
    async def execute_tool(self, tool_name, arguments):
        if tool_name == "create_memory":
            content = arguments.get("content")
            tags = arguments.get("tags", [])
            
            memory = {
                "id": len(self.memories) + 1,
                "content": content,
                "tags": tags,
                "created_at": datetime.now().isoformat()
            }
            self.memories.append(memory)
            return {"memory": memory, "success": True}
        
        elif tool_name == "search_memories":
            query = arguments.get("query", "").lower()
            matching_memories = [
                mem for mem in self.memories 
                if query in mem["content"].lower() or any(query in tag.lower() for tag in mem["tags"])
            ]
            return {"memories": matching_memories, "success": True}

# Demo server instances
DEMO_SERVERS = {
    "filesystem": FilesystemMCPServer(),
    "git": GitMCPServer(), 
    "web_search": WebSearchMCPServer(),
    "memory": MemoryMCPServer()
}

async def start_demo_servers():
    """Start all demo MCP servers"""
    print("Starting Demo MCP Servers...")
    
    for server_id, server in DEMO_SERVERS.items():
        try:
            await server.start()
            print(f"✅ {server.name} started on port {server.port}")
        except Exception as e:
            print(f"❌ Failed to start {server.name}: {e}")
    
    print("\nDemo servers are running!")
    print("You can now test the Streamlit app with these servers.")
    print("Press Ctrl+C to stop all servers.")

if __name__ == "__main__":
    try:
        asyncio.run(start_demo_servers())
    except KeyboardInterrupt:
        print("\nStopping demo servers...")
        sys.exit(0)
