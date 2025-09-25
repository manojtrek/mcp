# Demo MCP Servers

This directory contains demo implementations of common MCP (Model Context Protocol) servers for testing the Streamlit application.

## Available Demo Servers

### 1. 📁 Filesystem MCP (Port 3001)
**Tools:**
- `read_file` - Read contents of a file
- `write_file` - Write content to a file  
- `list_directory` - List contents of a directory

**Demo Usage:**
```python
# List directory contents
result = simulate_mcp_tool_execution("Filesystem MCP", "list_directory", {"path": "."})
```

### 2. 🔧 Git MCP (Port 3002)
**Tools:**
- `git_status` - Get git repository status
- `git_log` - Get git commit history
- `git_branch` - List git branches

**Demo Usage:**
```python
# Get git status
result = simulate_mcp_tool_execution("Git MCP", "git_status", {"path": "."})
```

### 3. 🌐 Web Search MCP (Port 3003)
**Tools:**
- `search_web` - Search the web for information
- `get_webpage_content` - Get content from a webpage

**Demo Usage:**
```python
# Search the web
result = simulate_mcp_tool_execution("Web Search MCP", "search_web", {"query": "MCP servers"})
```

### 4. 💾 Memory MCP (Port 3005)
**Tools:**
- `create_memory` - Create a new memory
- `search_memories` - Search existing memories

**Demo Usage:**
```python
# Create a memory
result = simulate_mcp_tool_execution("Memory MCP", "create_memory", {
    "content": "Demo memory content", 
    "tags": ["demo", "test"]
})
```

### 5. 🗄️ SQLite MCP (Port 3004)
**Tools:**
- `execute_query` - Execute SQL query on database
- `list_tables` - List tables in database

### 6. 🌐 Fetch MCP (Port 3006)
**Tools:**
- `fetch_url` - Fetch content from URL

## Quick Start

### Option 1: Use Demo Buttons
1. Open the Streamlit app at `http://localhost:8501`
2. Go to the right sidebar
3. Click the demo buttons under "🧪 Demo MCP Tools"
4. See simulated results for each MCP server

### Option 2: Add MCP Servers
1. Go to the "🛠️ MCP Servers" tab in the sidebar
2. Click "Add" buttons for the public MCP servers
3. Connect to the servers
4. Use the tools in your chat

### Option 3: Start Demo Servers (Advanced)
```bash
# Make the script executable
chmod +x start_demo_servers.sh

# Start demo servers
./start_demo_servers.sh
```

## Testing the Integration

### 1. Test Individual Tools
Use the demo buttons in the right sidebar to test each MCP server individually.

### 2. Test Through Chat
Ask the AI assistant to use MCP tools:
- "List the files in my current directory"
- "Show me the git status of this repository"
- "Search the web for information about MCP servers"
- "Create a memory about our project"

### 3. Test User-Specific Tasks
Switch between different user profiles to see how tasks change based on role:
- **John Doe (Project Manager)**: Project overview, stakeholder reports
- **Jane Smith (Developer)**: Personal tasks, code reviews
- **Mike Wilson (Team Lead)**: Team workload, resource planning

## Real MCP Server Integration

To connect to real MCP servers:

1. **Install MCP servers** (if available):
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   npm install -g @modelcontextprotocol/server-git
   ```

2. **Start MCP servers**:
   ```bash
   # Start filesystem server
   mcp-server-filesystem --port 3001
   
   # Start git server  
   mcp-server-git --port 3002
   ```

3. **Update connection details** in the Streamlit app to point to real servers.

## Troubleshooting

### Common Issues:
1. **Port conflicts**: Make sure ports 3001-3006 are available
2. **Connection timeouts**: Check if MCP servers are running
3. **Tool execution errors**: Verify tool arguments match expected schema

### Debug Mode:
Enable debug logging by setting environment variable:
```bash
export MCP_DEBUG=1
streamlit run streamlit_app.py
```

## Next Steps

1. **Add more MCP servers**: Extend the demo with additional server types
2. **Real server integration**: Connect to actual MCP servers
3. **Custom tools**: Add your own MCP tools and servers
4. **Production deployment**: Deploy with real MCP server infrastructure

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)
- [Streamlit Documentation](https://docs.streamlit.io/)
