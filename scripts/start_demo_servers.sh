#!/bin/bash

# Start Demo MCP Servers
echo "🚀 Starting Demo MCP Servers..."

# Start the demo servers in background
python3 demo_mcp_servers.py &

# Get the PID
SERVER_PID=$!

echo "Demo MCP servers started with PID: $SERVER_PID"
echo "Servers running on ports: 3001, 3002, 3003, 3005"
echo ""
echo "Available servers:"
echo "  📁 Filesystem MCP (port 3001) - File operations"
echo "  🔧 Git MCP (port 3002) - Git repository operations" 
echo "  🌐 Web Search MCP (port 3003) - Web search"
echo "  💾 Memory MCP (port 3005) - Persistent memory"
echo ""
echo "To stop servers: kill $SERVER_PID"
echo "Or press Ctrl+C to stop this script"

# Wait for user to stop
wait $SERVER_PID
