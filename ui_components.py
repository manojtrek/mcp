"""
UI components for the Streamlit MCP application
"""

import streamlit as st
from config import PROMPT_LIBRARY, USER_PROFILES
from mcp_handlers import (
    add_mcp_server, remove_mcp_server, connect_to_mcp_server, 
    disconnect_mcp_server, get_public_mcp_servers, simulate_mcp_tool_execution
)
from user_management import refresh_user_data, switch_user


def render_header():
    """Render the application header"""
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Linear Project Assistant</h1>
        <p>Your AI-powered Linear workspace management tool</p>
    </div>
    """, unsafe_allow_html=True)


def render_custom_css():
    """Render custom CSS for the application"""
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .chat-container {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    .prompt-card {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .prompt-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    .prompt-card h4 {
        margin: 0 0 8px 0;
        color: #333;
        font-size: 1.1rem;
    }
    
    .prompt-card p {
        margin: 0 0 8px 0;
        color: #666;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    .prompt-card small {
        color: #888;
        font-size: 0.8rem;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
    }
    
    .user-profile {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .status-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-connected {
        background-color: #28a745;
    }
    
    .status-disconnected {
        background-color: #dc3545;
    }
    </style>
    """, unsafe_allow_html=True)


def render_user_profile_section():
    """Render user profile section in sidebar"""
    st.markdown("### 👤 User Profile")
    user_profile = st.session_state.user_profile
    
    # User login/selection
    with st.expander("🔐 Login/User Selection", expanded=False):
        selected_user = st.selectbox(
            "Select User:",
            list(USER_PROFILES.keys()),
            key="user_selector"
        )
        
        if st.button("🔄 Refresh User Data"):
            success, message = switch_user(selected_user)
            if success:
                st.success(message)
                st.rerun()
            else:
                st.error(message)
    
    # Display current user info
    st.info(f"""
    **{user_profile['name']}**  
    {user_profile['role'].title()} | {user_profile['team']}  
    📧 {user_profile['email']}
    """)


def render_user_tasks_section():
    """Render user-specific tasks section"""
    st.header("📋 My Tasks & Actions")
    st.markdown("Personalized tasks based on your role and permissions:")
    
    # User-specific tasks
    if st.session_state.user_tasks:
        st.subheader("🎯 My Tasks")
        for task in st.session_state.user_tasks:
            priority_color = "🔴" if task["priority"] == "high" else "🟡" if task["priority"] == "medium" else "🟢"
            
            with st.container():
                st.markdown(f"""
                <div class="prompt-card">
                    <h4>{priority_color} {task['icon']} {task['title']}</h4>
                    <p>{task['description']}</p>
                    <small>Category: {task['category']}</small>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Execute: {task['title']}", key=f"task_{task['id']}"):
                    # Add user message
                    st.session_state.messages.append({
                        "role": "user", 
                        "content": task['action']
                    })
                    # Set flag to trigger AI response
                    st.session_state.trigger_ai_response = True
                    st.rerun()
    
    # User-specific actions
    if st.session_state.user_actions:
        st.subheader("⚡ Quick Actions")
        for action in st.session_state.user_actions:
            with st.container():
                st.markdown(f"""
                <div class="prompt-card">
                    <h4>{action['icon']} {action['title']}</h4>
                    <p>{action['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Run: {action['title']}", key=f"action_{action['id']}"):
                    # Add user message
                    st.session_state.messages.append({
                        "role": "user", 
                        "content": action['action']
                    })
                    # Set flag to trigger AI response
                    st.session_state.trigger_ai_response = True
                    st.rerun()
    
    # Refresh button
    if st.button("🔄 Refresh My Data"):
        refresh_user_data()
        st.success("User data refreshed!")
        st.rerun()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", type="secondary"):
        st.session_state.messages = []
        st.rerun()


def render_mcp_servers_section():
    """Render MCP servers management section"""
    st.header("🛠️ MCP Server Management")
    
    # Add new MCP server
    with st.expander("➕ Add New MCP Server", expanded=False):
        with st.form("add_server_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Server Name", placeholder="My MCP Server")
                host = st.text_input("Host", value="localhost")
            with col2:
                port = st.number_input("Port", value=3001, min_value=1, max_value=65535)
                description = st.text_area("Description", placeholder="Server description")
            
            if st.form_submit_button("Add Server"):
                if name and host and port:
                    add_mcp_server(name, host, port, description)
                    st.success(f"Added server: {name}")
                    st.rerun()
                else:
                    st.error("Please fill in all required fields")
    
    # Manage existing servers
    if st.session_state.mcp_servers:
        st.subheader("📡 Configured Servers")
        for server_name, server_info in st.session_state.mcp_servers.items():
            with st.container():
                status_icon = "🟢" if server_info["status"] == "connected" else "🔴"
                st.write(f"{status_icon} **{server_name}**")
                st.caption(f"{server_info['host']}:{server_info['port']} - {server_info['description']}")
                
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if server_info["status"] == "connected":
                        if st.button(f"Disconnect", key=f"disconnect_{server_name}"):
                            disconnect_mcp_server(server_name)
                            st.rerun()
                    else:
                        if st.button(f"Connect", key=f"connect_{server_name}"):
                            success, message = connect_to_mcp_server(server_name)
                            if success:
                                st.success(message)
                            else:
                                st.error(message)
                            st.rerun()
                
                with col2:
                    if st.button(f"Test", key=f"test_{server_name}"):
                        # Test connection logic here
                        st.info("Connection test would be performed here")
                
                with col3:
                    if st.button(f"Remove", key=f"remove_{server_name}"):
                        remove_mcp_server(server_name)
                        st.rerun()
    else:
        st.info("No MCP servers configured. Add one above to get started!")
    
    # Public MCP servers
    st.subheader("🌐 Public MCP Servers")
    st.markdown("Add publicly available MCP servers:")
    
    public_servers = get_public_mcp_servers()
    
    # Display public servers in a grid
    cols = st.columns(2)
    for i, (server_id, server_info) in enumerate(public_servers.items()):
        with cols[i % 2]:
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; margin: 5px 0;">
                    <h4>{server_info['name']}</h4>
                    <p>{server_info['description']}</p>
                    <small>Category: {server_info['category']}</small>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Add {server_info['name']}", key=f"add_{server_id}"):
                    add_mcp_server(
                        server_info['name'], 
                        server_info['host'], 
                        server_info['port'], 
                        server_info['description']
                    )
                    st.success(f"Added {server_info['name']}")
                    st.rerun()
    
    # Quick setup for common servers
    st.subheader("🚀 Quick Setup")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📁 Add All System Servers", help="Add filesystem and git servers"):
            add_mcp_server("Filesystem MCP", "localhost", 3001, "File system operations")
            add_mcp_server("Git MCP", "localhost", 3002, "Git repository operations")
            st.success("Added system servers!")
            st.rerun()
    
    with col2:
        if st.button("🌐 Add All Network Servers", help="Add web search and fetch servers"):
            add_mcp_server("Web Search MCP", "localhost", 3003, "Web search and content fetching")
            add_mcp_server("Fetch MCP", "localhost", 3006, "HTTP requests and API calls")
            st.success("Added network servers!")
            st.rerun()


def render_settings_section():
    """Render settings section"""
    st.header("⚙️ Settings")
    
    # Azure OpenAI Configuration
    st.subheader("🤖 Azure OpenAI Configuration")
    st.info("Configure your Azure OpenAI settings in the .env file")
    
    # Display current configuration
    from config import AZURE_OPENAI_CONFIG
    config_status = "✅ Configured" if AZURE_OPENAI_CONFIG["api_key"] else "❌ Not configured"
    st.write(f"**Status:** {config_status}")
    
    if AZURE_OPENAI_CONFIG["api_key"]:
        st.success("Azure OpenAI is properly configured!")
    else:
        st.error("Please configure Azure OpenAI in your .env file")
        st.code("""
# Add these to your .env file:
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
        """)
    
    # Theme selection
    st.subheader("🎨 Theme Settings")
    theme = st.selectbox("Select Theme", ["Light", "Dark", "Auto"])
    st.caption("Theme changes will be applied on next restart")
    
    # Chat parameters
    st.subheader("💬 Chat Parameters")
    max_tokens = st.slider("Max Tokens", 100, 4000, 2000)
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    
    # Save settings
    if st.button("💾 Save Settings"):
        st.success("Settings saved! (Note: Some changes require app restart)")


def render_demo_tools_section():
    """Render demo MCP tools section"""
    st.subheader("🧪 Demo MCP Tools")
    st.markdown("Test MCP tools with demo data:")
    
    # Filesystem demo
    if st.button("📁 Test Filesystem"):
        result = simulate_mcp_tool_execution("Filesystem MCP", "list_directory", {"path": "."})
        st.success(f"Demo result: {result['message']}")
        if 'files' in result:
            st.write("Files found:", result['files'])
    
    # Git demo
    if st.button("🔧 Test Git"):
        result = simulate_mcp_tool_execution("Git MCP", "git_status", {"path": "."})
        st.success(f"Demo result: {result['message']}")
        if 'status' in result:
            st.code(result['status'])
    
    # Web search demo
    if st.button("🌐 Test Web Search"):
        result = simulate_mcp_tool_execution("Web Search MCP", "search_web", {"query": "MCP servers"})
        st.success(f"Demo result: {result['message']}")
        if 'results' in result:
            for res in result['results']:
                st.write(f"**{res['title']}**")
                st.write(res['snippet'])
    
    # Memory demo
    if st.button("💾 Test Memory"):
        result = simulate_mcp_tool_execution("Memory MCP", "create_memory", {"content": "Demo memory content", "tags": ["demo", "test"]})
        st.success(f"Demo result: {result['message']}")
        if 'memory' in result:
            st.write("Created memory:", result['memory']['content'])


def render_tools_status_section():
    """Render tools and status section"""
    st.subheader("📡 MCP Servers")
    if st.session_state.mcp_servers:
        for server_name, server in st.session_state.mcp_servers.items():
            status_icon = "🟢" if server["status"] == "connected" else "🔴"
            st.write(f"{status_icon} **{server_name}**")
            st.caption(f"{server['host']}:{server['port']}")
            if server["tools"]:
                st.caption(f"📋 {len(server['tools'])} tools")
    else:
        st.info("No MCP servers configured")
        st.caption("Go to MCP Servers tab to add servers")
    
    # Available Tools
    st.subheader("🔧 Available Tools")
    
    # Built-in tools
    st.write("**Built-in Tools:**")
    for tool in st.session_state.regular_tools:
        st.caption(f"• {tool['name']}")
    
    # MCP tools
    if st.session_state.mcp_tools:
        st.write("**MCP Tools:**")
        for connection, tools in st.session_state.mcp_tools.items():
            st.write(f"**{connection}:**")
            for tool in tools:
                st.caption(f"• {tool['name']}")
    
    # Quick actions
    st.subheader("⚡ Quick Actions")
    if st.button("📋 View All Issues"):
        st.session_state.messages.append({
            "role": "user", 
            "content": "Show me all open issues in my Linear workspace"
        })
        st.session_state.trigger_ai_response = True
        st.rerun()
    
    if st.button("📊 Project Status"):
        st.session_state.messages.append({
            "role": "user", 
            "content": "What's the current status of my active projects?"
        })
        st.session_state.trigger_ai_response = True
        st.rerun()
    
    if st.button("👥 Team Workload"):
        st.session_state.messages.append({
            "role": "user", 
            "content": "Show me the current workload for my team members"
        })
        st.session_state.trigger_ai_response = True
        st.rerun()
    
    if st.button("🔄 Refresh Status"):
        st.rerun()
