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

# MCP server configurations - Empty for user to add via UI
PUBLIC_MCP_SERVERS = {}

# MCP tool definitions - Empty for user to add via UI
MCP_TOOLS = {}

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
