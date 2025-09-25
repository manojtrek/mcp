"""
Configuration and constants for the Streamlit MCP application
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# System configuration
SYSTEM_PROMPT = """You are a helpful AI assistant integrated with MCP (Model Context Protocol) servers. 
You can help users manage their projects, files, git repositories, and more through various MCP tools.

Available capabilities:
- File system operations (read, write, list files)
- Git repository management (status, log, branches)
- Web search and content fetching
- Database operations (SQLite)
- Memory management (create, search memories)
- HTTP requests and API calls

Always be helpful and provide clear explanations of what you're doing when using MCP tools."""

# Prompt library for different categories
PROMPT_LIBRARY = {
    "Project Management": [
        {
            "name": "Project Overview",
            "prompt": "Give me a comprehensive overview of all my active projects, including status, deadlines, and team assignments.",
            "description": "Get a complete picture of your project portfolio"
        },
        {
            "name": "Team Workload Analysis",
            "prompt": "Analyze the current workload distribution across my team members and identify any bottlenecks or over-allocations.",
            "description": "Understand team capacity and resource allocation"
        },
        {
            "name": "Risk Assessment",
            "prompt": "Identify potential risks and blockers in my current projects and suggest mitigation strategies.",
            "description": "Proactive risk management and planning"
        }
    ],
    "Development": [
        {
            "name": "Code Review Status",
            "prompt": "Show me all pending code reviews and pull requests that need my attention.",
            "description": "Stay on top of code review responsibilities"
        },
        {
            "name": "Repository Health",
            "prompt": "Analyze the health of my git repositories, including commit frequency, branch management, and code quality metrics.",
            "description": "Monitor repository health and development activity"
        },
        {
            "name": "Technical Debt Analysis",
            "prompt": "Identify areas of technical debt in my codebase and suggest refactoring priorities.",
            "description": "Plan technical improvements and maintenance"
        }
    ],
    "Analytics": [
        {
            "name": "Performance Metrics",
            "prompt": "Show me key performance indicators for my projects, including velocity, completion rates, and team productivity.",
            "description": "Track project and team performance"
        },
        {
            "name": "Trend Analysis",
            "prompt": "Analyze trends in my project data over the past quarter and identify patterns or insights.",
            "description": "Understand long-term trends and patterns"
        },
        {
            "name": "Resource Utilization",
            "prompt": "Evaluate how efficiently resources are being utilized across different projects and teams.",
            "description": "Optimize resource allocation and planning"
        }
    ]
}

# User profiles for demo purposes
USER_PROFILES = {
    "john.doe@company.com": {
        "name": "John Doe",
        "email": "john.doe@company.com",
        "role": "project_manager",
        "team": "Engineering",
        "permissions": ["view_all_issues", "create_issues", "assign_tasks", "view_analytics"]
    },
    "jane.smith@company.com": {
        "name": "Jane Smith",
        "email": "jane.smith@company.com",
        "role": "developer",
        "team": "Engineering",
        "permissions": ["view_my_issues", "create_issues", "update_status"]
    },
    "mike.wilson@company.com": {
        "name": "Mike Wilson",
        "email": "mike.wilson@company.com",
        "role": "team_lead",
        "team": "Engineering",
        "permissions": ["view_team_issues", "assign_tasks", "view_analytics", "manage_sprints"]
    }
}

# MCP server configurations
PUBLIC_MCP_SERVERS = {
    "filesystem": {
        "name": "Filesystem MCP",
        "description": "File system operations (read, write, list)",
        "host": "localhost",
        "port": 3001,
        "category": "system",
        "tools": ["read_file", "write_file", "list_directory"]
    },
    "git": {
        "name": "Git MCP",
        "description": "Git repository operations",
        "host": "localhost", 
        "port": 3002,
        "category": "development",
        "tools": ["git_status", "git_log", "git_branch"]
    },
    "web_search": {
        "name": "Web Search MCP",
        "description": "Web search and content fetching",
        "host": "localhost",
        "port": 3003,
        "category": "research",
        "tools": ["search_web", "get_webpage_content"]
    },
    "sqlite": {
        "name": "SQLite MCP",
        "description": "SQLite database operations",
        "host": "localhost",
        "port": 3004,
        "category": "database",
        "tools": ["execute_query", "list_tables"]
    },
    "memory": {
        "name": "Memory MCP",
        "description": "Persistent memory storage",
        "host": "localhost",
        "port": 3005,
        "category": "storage",
        "tools": ["create_memory", "search_memories"]
    },
    "fetch": {
        "name": "Fetch MCP",
        "description": "HTTP requests and API calls",
        "host": "localhost",
        "port": 3006,
        "category": "network",
        "tools": ["fetch_url"]
    }
}

# MCP tool definitions
MCP_TOOLS = {
    "filesystem": [
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
    ],
    "git": [
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
        },
        {
            "name": "git_branch",
            "description": "List git branches",
            "input_schema": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"]
            }
        }
    ],
    "web_search": [
        {
            "name": "search_web",
            "description": "Search the web for information",
            "input_schema": {
                "type": "object",
                "properties": {"query": {"type": "string"}, "max_results": {"type": "integer"}},
                "required": ["query"]
            }
        },
        {
            "name": "get_webpage_content",
            "description": "Get content from a webpage",
            "input_schema": {
                "type": "object",
                "properties": {"url": {"type": "string"}},
                "required": ["url"]
            }
        }
    ],
    "sqlite": [
        {
            "name": "execute_query",
            "description": "Execute SQL query on database",
            "input_schema": {
                "type": "object",
                "properties": {"query": {"type": "string"}, "database": {"type": "string"}},
                "required": ["query", "database"]
            }
        },
        {
            "name": "list_tables",
            "description": "List tables in database",
            "input_schema": {
                "type": "object",
                "properties": {"database": {"type": "string"}},
                "required": ["database"]
            }
        }
    ],
    "memory": [
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
    ],
    "fetch": [
        {
            "name": "fetch_url",
            "description": "Fetch content from URL",
            "input_schema": {
                "type": "object",
                "properties": {"url": {"type": "string"}, "method": {"type": "string"}},
                "required": ["url"]
            }
        }
    ]
}

# Built-in tools
BUILTIN_TOOLS = [{
    "name": "show_linear_ticket",
    "description": "Displays a Linear ticket in the UI with its details",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "status": {"type": "string"},
            "assignee": {"type": "string"},
            "deadline": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["title", "status", "assignee", "deadline", "tags"]
    }
}]

# Azure OpenAI configuration
AZURE_OPENAI_CONFIG = {
    "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
    "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
}
