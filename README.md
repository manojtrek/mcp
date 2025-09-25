# Streamlit MCP Linear Project Assistant

A modular, professionally organized Streamlit application for managing Linear projects with MCP (Model Context Protocol) server integration.

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

## 🎯 Key Features

- **Modular Architecture**: Clean, organized code structure
- **User Management**: Role-based access and personalized tasks
- **MCP Integration**: Server management and tool execution
- **AI Chat Interface**: Azure OpenAI integration with auto-responses
- **Professional Structure**: Industry-standard Python project layout

## 📚 Documentation

- **[Complete Documentation](docs/README.md)** - Full setup and usage guide
- **[Project Overview](docs/PROJECT_OVERVIEW.md)** - Architecture and features
- **[Project Structure](docs/PROJECT_STRUCTURE.md)** - Detailed folder organization
- **[MCP Servers](docs/DEMO_MCP_SERVERS.md)** - MCP server documentation
- **[Auto-Response Feature](docs/AUTO_RESPONSE_FEATURE.md)** - Auto-response functionality

## 🏗️ Architecture

### **Core Modules**
- **`src/main.py`** - Main application entry point
- **`src/config/config.py`** - Configuration and constants
- **`src/handlers/mcp_handlers.py`** - MCP server management
- **`src/core/user_management.py`** - User roles and permissions
- **`src/ui/ui_components.py`** - Reusable UI components

### **Benefits**
- **Maintainability**: Easy to maintain and modify
- **Scalability**: Simple to add new features and modules
- **Team Collaboration**: Multiple developers can work together
- **Testing**: Individual modules can be tested separately

## 🚀 Usage

### **Running the App**
```bash
# Method 1: Using entry point (recommended)
streamlit run run.py

# Method 2: Direct module execution
streamlit run src/main.py

# Method 3: Python module execution
python -m src.main
```

### **Testing Features**
1. **User Roles**: Switch between Project Manager, Developer, Team Lead
2. **MCP Tools**: Test demo tools in the right sidebar
3. **Auto-Responses**: Click task cards to see automatic AI responses
4. **Chat Interface**: Have conversations with the AI assistant

## 🧪 Development

### **Adding New Features**
1. Identify the appropriate folder (`src/core/`, `src/ui/`, `src/handlers/`)
2. Create or modify the relevant module
3. Update imports in dependent modules
4. Test the functionality
5. Update documentation

### **Project Organization**
- **`src/core/`** - Business logic and core functionality
- **`src/ui/`** - User interface components
- **`src/handlers/`** - MCP server operations
- **`src/config/`** - Configuration and constants
- **`docs/`** - Comprehensive documentation
- **`scripts/`** - Utilities and automation

## 📄 License

This project is open source and available under the MIT License.

---

**This project demonstrates a modern, professional approach to building AI-powered applications with modular architecture, MCP integration, and role-based user management.**

