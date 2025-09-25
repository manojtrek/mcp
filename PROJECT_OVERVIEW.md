# Project Overview

## 🎯 **What This Project Is**

A **modular Streamlit application** that integrates with **MCP (Model Context Protocol) servers** to provide an AI-powered interface for managing Linear projects and development workflows.

## 🏗️ **Architecture**

### **Core Modules**
- **`main.py`** - Main application entry point
- **`config.py`** - Configuration and constants
- **`mcp_handlers.py`** - MCP server management
- **`user_management.py`** - User roles and permissions
- **`ui_components.py`** - Reusable UI components

### **Supporting Files**
- **`demo_mcp_servers.py`** - Demo MCP server implementations
- **`start_demo_servers.sh`** - Script to start demo servers
- **`requirements.txt`** - Python dependencies
- **`.env`** - Environment variables (create this)

## 🚀 **Key Features**

### **1. User Management**
- **Role-based access** (Project Manager, Developer, Team Lead)
- **Dynamic task generation** based on user permissions
- **User switching** between different profiles
- **Personalized interfaces** for each role

### **2. MCP Server Integration**
- **Server management** (add, remove, connect)
- **Tool discovery** from connected servers
- **Demo tools** for testing
- **Public server library** with common MCP servers

### **3. AI Chat Interface**
- **Azure OpenAI integration** for intelligent responses
- **Tool calling** to execute MCP tools
- **Context-aware** responses based on user role
- **Streaming responses** for better UX

## 🎯 **Use Cases**

### **Project Managers**
- Get project overviews and status reports
- Analyze team workload and capacity
- Generate stakeholder reports
- Identify risks and blockers

### **Developers**
- View assigned tasks and priorities
- Check code review status
- Prepare for daily standups
- Monitor code quality metrics

### **Team Leads**
- Manage team workload and resources
- Plan sprints and iterations
- Conduct team retrospectives
- Review team performance

## 🔧 **Available MCP Servers**

| Server | Purpose | Tools |
|--------|---------|-------|
| **Filesystem** | File operations | read_file, write_file, list_directory |
| **Git** | Repository management | git_status, git_log, git_branch |
| **Web Search** | Internet search | search_web, get_webpage_content |
| **SQLite** | Database operations | execute_query, list_tables |
| **Memory** | Persistent storage | create_memory, search_memories |
| **Fetch** | HTTP requests | fetch_url |

## 🚀 **Getting Started**

### **1. Setup**
```bash
# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your Azure OpenAI credentials
```

### **2. Run**
```bash
streamlit run main.py
```

### **3. Test**
- Open `http://localhost:8501`
- Switch between user roles
- Test MCP tools with demo buttons
- Add and connect to MCP servers
- Chat with the AI assistant

## 🧪 **Testing**

### **Demo Tools**
- Use the demo buttons in the right sidebar
- Test each MCP server individually
- See simulated responses and data

### **User Roles**
- Switch between John Doe (PM), Jane Smith (Developer), Mike Wilson (Team Lead)
- See how tasks and actions change based on role
- Test role-specific functionality

### **MCP Integration**
- Add public MCP servers
- Connect to servers
- Discover available tools
- Use tools in chat conversations

## 📈 **Future Enhancements**

### **Planned Features**
- **Real MCP server integration** (currently using demo/simulation)
- **Database persistence** for user data and settings
- **Authentication system** for real user management
- **API endpoints** for external integrations
- **Real-time updates** with WebSocket connections

### **Easy to Add**
- **New MCP servers** by extending `mcp_handlers.py`
- **New user roles** by updating `user_management.py`
- **New UI components** by adding to `ui_components.py`
- **New features** by creating additional modules

## 🎉 **Benefits**

### **For Developers**
- **Modular architecture** makes it easy to maintain and extend
- **Clear separation of concerns** between different functionalities
- **Reusable components** can be used across projects
- **Easy testing** of individual modules

### **For Users**
- **Role-based interface** provides relevant tools and tasks
- **AI-powered assistance** for complex project management
- **MCP integration** extends capabilities with external tools
- **Intuitive interface** with clear navigation and feedback

## 📚 **Documentation**

- **README.md** - Main documentation and setup guide
- **DEMO_MCP_SERVERS.md** - Detailed MCP server documentation
- **Module docstrings** - Inline documentation for each module
- **Code comments** - Explanatory comments throughout the codebase

---

**This project demonstrates a modern approach to building AI-powered applications with modular architecture, MCP integration, and role-based user management.**
