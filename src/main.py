"""
Main Streamlit application for the MCP Linear Project Assistant
"""

import streamlit as st
import asyncio
import json
from openai import AsyncAzureOpenAI
from dotenv import load_dotenv

# Import our modular components
from src.config.config import SYSTEM_PROMPT, AZURE_OPENAI_CONFIG, BUILTIN_TOOLS
from src.handlers.mcp_handlers import simulate_mcp_tool_execution
from src.core.user_management import refresh_user_data
from src.ui.ui_components import (
    render_header, render_custom_css, render_user_profile_section,
    render_user_tasks_section, render_mcp_servers_section, 
    render_settings_section, render_demo_tools_section, render_tools_status_section
)

# Load environment variables
load_dotenv()


def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "mcp_tools" not in st.session_state:
        st.session_state.mcp_tools = {}
    if "mcp_servers" not in st.session_state:
        st.session_state.mcp_servers = {}
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "name": "Guest User",
            "email": "",
            "role": "user",
            "team": "",
            "permissions": []
        }
    if "user_tasks" not in st.session_state:
        st.session_state.user_tasks = []
    if "user_actions" not in st.session_state:
        st.session_state.user_actions = []
    if "regular_tools" not in st.session_state:
        st.session_state.regular_tools = BUILTIN_TOOLS
    if "trigger_ai_response" not in st.session_state:
        st.session_state.trigger_ai_response = False


def show_linear_ticket(title, status, assignee, deadline, tags):
    """Display a Linear ticket in the UI"""
    status_colors = {
        "In Progress": "🟡",
        "Done": "✅",
        "Todo": "⏳",
        "Backlog": "📋"
    }
    
    status_icon = status_colors.get(status, "❓")
    
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin: 10px 0; background: #f9f9f9;">
        <h3>🎫 {title}</h3>
        <p><strong>Status:</strong> {status_icon} {status}</p>
        <p><strong>Assignee:</strong> {assignee}</p>
        <p><strong>Deadline:</strong> {deadline}</p>
        <p><strong>Tags:</strong> {', '.join(tags)}</p>
    </div>
    """, unsafe_allow_html=True)


def render_tasks_in_chat():
    """Render user tasks as chat messages"""
    if st.session_state.user_tasks:
        # Render tasks without chat message wrapper to hide bot icon
        col1, col2 = st.columns([1, 0.1])
        with col1:
            st.markdown("### 📋 Your Tasks")
        with col2:
            if st.button("🔄", help="Refresh your tasks and actions", key="refresh_tasks"):
                refresh_user_data()
                st.rerun()
        
        st.markdown("Click on any task to execute it:")
        
        # Display tasks horizontally with proper column sizing
        num_tasks = len(st.session_state.user_tasks)
        if num_tasks > 0:
            # Create columns with equal width
            task_cols = st.columns(num_tasks)
            
            for i, task in enumerate(st.session_state.user_tasks):
                with task_cols[i]:
                    # Create a compact, clickable card
                    task_text = f"{task.get('icon', '🎯')} {task['title']}\n\n{task['description']}\n\nPriority: {task.get('priority', 'Medium')}"
                    
                    if st.button(
                        task_text,
                        key=f"task_{i}",
                        help=f"Click to execute: {task['title']}",
                        use_container_width=True
                    ):
                        # Add task to chat and trigger AI response
                        st.session_state.messages.append({
                            "role": "user", 
                            "content": f"Execute this task: {task['title']} - {task['description']}"
                        })
                        st.session_state.trigger_ai_response = True
                        st.rerun()


def handle_tool_calls(tool_calls):
    """Handle tool calls from the LLM response"""
    for tool_call in tool_calls:
        if tool_call.function.name == "show_linear_ticket":
            try:
                args = json.loads(tool_call.function.arguments)
                show_linear_ticket(
                    args.get("title", "Untitled"),
                    args.get("status", "Todo"),
                    args.get("assignee", "Unassigned"),
                    args.get("deadline", "No deadline"),
                    args.get("tags", [])
                )
            except Exception as e:
                st.error(f"Error displaying ticket: {e}")


async def call_azure_openai(messages):
    """Call Azure OpenAI with the given messages"""
    try:
        client = AsyncAzureOpenAI(
            api_key=AZURE_OPENAI_CONFIG["api_key"],
            api_version=AZURE_OPENAI_CONFIG["api_version"],
            azure_endpoint=AZURE_OPENAI_CONFIG["endpoint"]
        )
        
        # Convert tools to OpenAI format
        tools = []
        for tool in st.session_state.regular_tools:
            tools.append({
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool["input_schema"]
                }
            })
        
        # Add MCP tools
        for server_name, server_tools in st.session_state.mcp_tools.items():
            for tool in server_tools:
                tools.append({
                    "type": "function",
                    "function": {
                        "name": tool["name"],
                        "description": tool["description"],
                        "parameters": tool["input_schema"]
                    }
                })
        
        response = await client.chat.completions.create(
            model=AZURE_OPENAI_CONFIG["deployment_name"],
            messages=messages,
            tools=tools if tools else None,
            tool_choice="auto" if tools else None,
            stream=True
        )
        
        return response
        
    except Exception as e:
        st.error(f"Error calling Azure OpenAI: {e}")
        return None


def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="CEVC - Planner",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Initialize user data if not already done
    if not st.session_state.user_tasks:
        refresh_user_data()
    
    # Render custom CSS
    render_custom_css()
    
    # Render header
    render_header()
    
    # Main layout with sidebar and main content
    with st.sidebar:
        # User profile section
        render_user_profile_section()
        
        # Tabs for different sections
        tab1, tab2 = st.tabs(["🛠️ MCP Servers", "⚙️ Settings"])
        
        with tab1:
            render_mcp_servers_section()
        
        with tab2:
            render_settings_section()
    
    # Always render tasks at the top
    render_tasks_in_chat()
    
    # Chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Auto-trigger AI response if flag is set
    if st.session_state.trigger_ai_response:
        # Reset the flag
        st.session_state.trigger_ai_response = False
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Create event loop for async call
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(call_azure_openai(st.session_state.messages))
                
                if response:
                    full_response = ""
                    tool_calls = []
                    
                    for chunk in response:
                        if chunk.choices[0].delta.content:
                            full_response += chunk.choices[0].delta.content
                            st.write(chunk.choices[0].delta.content, end="")
                        
                        if chunk.choices[0].delta.tool_calls:
                            for tool_call in chunk.choices[0].delta.tool_calls:
                                if tool_call.function:
                                    tool_calls.append(tool_call)
                    
                    # Handle tool calls
                    if tool_calls:
                        handle_tool_calls(tool_calls)
                    
                    # Add assistant message
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                else:
                    st.error("Failed to get response from AI")
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about your projects..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Create event loop for async call
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(call_azure_openai(st.session_state.messages))
                
                if response:
                    full_response = ""
                    tool_calls = []
                    
                    for chunk in response:
                        if chunk.choices[0].delta.content:
                            full_response += chunk.choices[0].delta.content
                            st.write(chunk.choices[0].delta.content, end="")
                        
                        if chunk.choices[0].delta.tool_calls:
                            for tool_call in chunk.choices[0].delta.tool_calls:
                                if tool_call.function:
                                    tool_calls.append(tool_call)
                    
                    # Handle tool calls
                    if tool_calls:
                        handle_tool_calls(tool_calls)
                    
                    # Add assistant message
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                else:
                    st.error("Failed to get response from AI")
    


if __name__ == "__main__":
    main()
