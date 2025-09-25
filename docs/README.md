# Streamlit MCP Linear Project Assistant

A modular Streamlit application for managing Linear projects with MCP (Model Context Protocol) server integration.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file with your Azure OpenAI credentials:
```bash
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
```

### 3. Run the Application
```bash
streamlit run run.py
```

The app will be available at `http://localhost:8501`

## 📁 Project Structure

```
mcp/
├── src/                       # Source code directory
│   ├── main.py               # Main Streamlit application
│   ├── core/                 # Core functionality
│   │   ├── user_management.py    # User roles and permissions
│   │   └── demo_mcp_servers.py  # Demo MCP servers
│   ├── ui/                   # UI components
│   │   └── ui_components.py     # Reusable UI components
│   ├── handlers/             # MCP server handlers
│   │   └── mcp_handlers.py      # MCP server operations
│   └── config/               # Configuration
│       └── config.py             # Constants and settings
├── docs/                     # Documentation
├── scripts/                  # Scripts and utilities
├── run.py                    # Main entry point
├── requirements.txt          # Dependencies
├── .env                      # Environment variables
└── README.md                 # This file
```

## 🎯 Features

### User Management
- **Role-Based Access**: Different interfaces for Project Managers, Developers, and Team Leads
- **Dynamic Tasks**: Tasks generated based on user permissions and role
- **User Switching**: Easy switching between user profiles
- **Personalized Experience**: Customized interface for each user type

### MCP Server Integration
- **Server Management**: Add, remove, connect to MCP servers
- **Tool Discovery**: Automatic tool enumeration from connected servers
- **Demo Tools**: Built-in demo tools for testing
- **Public Servers**: Pre-configured public MCP servers

### Available MCP Servers
- **Filesystem MCP**: File operations (read, write, list)
- **Git MCP**: Git repository operations (status, log, branches)
- **Web Search MCP**: Web search and content fetching
- **SQLite MCP**: Database operations (queries, tables)
- **Memory MCP**: Persistent memory storage
- **Fetch MCP**: HTTP requests and API calls

## 🧪 Testing MCP Integration

### Method 1: Demo Buttons (Easiest)
1. Open the app at `http://localhost:8501`
2. Look for "🧪 Demo MCP Tools" section in the right sidebar
3. Click demo buttons to test each MCP server:
   - **📁 Test Filesystem**: See file listing demo
   - **🔧 Test Git**: See git status demo
   - **🌐 Test Web Search**: See search results demo
   - **💾 Test Memory**: See memory creation demo

### Method 2: Add MCP Servers
1. Go to "🛠️ MCP Servers" tab in sidebar
2. Click "Add" buttons for desired servers
3. Connect to servers
4. Use tools in chat conversations

### Method 3: Quick Setup
1. Click "📁 Add All System Servers" (Filesystem + Git)
2. Click "🌐 Add All Network Servers" (Web Search + Fetch)
3. Test connections and start using tools

## 👥 User Roles

### Project Manager (John Doe)
- **Tasks**: Project overview, stakeholder reports, risk assessment
- **Actions**: Project health check, risk assessment
- **Permissions**: view_all_issues, create_issues, assign_tasks, view_analytics

### Developer (Jane Smith)
- **Tasks**: Personal tasks, code reviews, daily standup prep
- **Actions**: Daily standup prep, code quality check
- **Permissions**: view_my_issues, create_issues, update_status

### Team Lead (Mike Wilson)
- **Tasks**: Team workload, resource planning, sprint management
- **Actions**: Team retrospective, performance review
- **Permissions**: view_team_issues, assign_tasks, view_analytics, manage_sprints

## 🔧 Architecture

### Modular Design
- **main.py**: Application orchestration and chat handling
- **config.py**: Configuration, constants, and data structures
- **mcp_handlers.py**: MCP server operations and tool execution
- **user_management.py**: User profiles, roles, and permissions
- **ui_components.py**: Reusable UI components and layouts

### Benefits
- **Maintainability**: Easy to maintain and modify
- **Scalability**: Simple to add new features and modules
- **Team Collaboration**: Multiple developers can work together
- **Testing**: Individual modules can be tested separately

## 🚀 Usage Examples

### Chat with AI Assistant
```
User: "Show me all issues assigned to me"
AI: [Uses MCP tools to fetch and display issues]

User: "What's the status of my team's workload?"
AI: [Analyzes team capacity and workload distribution]

User: "Create a new issue for the bug fix"
AI: [Uses MCP tools to create issue in Linear]
```

### Using MCP Tools
```
User: "List files in my current directory"
AI: [Uses Filesystem MCP to list directory contents]

User: "Show me git status"
AI: [Uses Git MCP to show repository status]

User: "Search for information about MCP servers"
AI: [Uses Web Search MCP to find relevant information]
```

## 🛠️ Development

### Adding New MCP Servers
1. Add server configuration to `config.py`
2. Add tool definitions to `mcp_handlers.py`
3. Add UI components to `ui_components.py`
4. Test with demo tools

### Adding New User Roles
1. Add role to `USER_PROFILES` in `config.py`
2. Add role-specific tasks in `user_management.py`
3. Add UI components for new role
4. Test user switching functionality

### Adding New UI Components
1. Create component function in `ui_components.py`
2. Add component to appropriate section
3. Import and use in `main.py`
4. Test component functionality

## 🐛 Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all modules are in the same directory
2. **Session State**: Check if session state is properly initialized
3. **MCP Connections**: Verify MCP servers are running
4. **Environment Variables**: Check `.env` file configuration

### Debug Mode
```bash
export STREAMLIT_LOGGER_LEVEL=debug
streamlit run main.py
```

## 📚 Documentation

- **config.py**: Configuration constants and settings
- **mcp_handlers.py**: MCP server operations and tool execution
- **user_management.py**: User-specific functionality and role management
- **ui_components.py**: UI components and layouts
- **main.py**: Main application orchestration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This application provides a solid foundation for building complex Streamlit applications with MCP integration. The modular structure makes it easy to maintain, test, and extend as needed.