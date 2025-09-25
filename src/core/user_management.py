"""
User management and role-based task generation
"""

import streamlit as st
from src.config.config import USER_PROFILES


def fetch_user_profile():
    """Fetch user profile from MCP servers"""
    # For demo, return a default profile or simulate login
    return USER_PROFILES.get("john.doe@company.com", {
        "name": "Guest User",
        "email": "guest@company.com",
        "role": "user",
        "team": "General",
        "permissions": ["view_my_issues"]
    })


def fetch_user_tasks():
    """Fetch user-specific tasks from MCP servers"""
    user_profile = st.session_state.user_profile
    role = user_profile.get("role", "user")
    
    # Generate tasks based on user role and permissions
    tasks = []
    
    if "view_my_issues" in user_profile.get("permissions", []):
        tasks.append({
            "id": "my_issues",
            "title": "My Assigned Issues",
            "description": "View all issues assigned to me",
            "priority": "high",
            "category": "issues",
            "action": "Show me all issues assigned to me",
            "icon": "📋"
        })
    
    if "view_team_issues" in user_profile.get("permissions", []):
        tasks.append({
            "id": "team_issues",
            "title": "Team Issues",
            "description": "View all issues for my team",
            "priority": "medium",
            "category": "team",
            "action": "Show me all issues for my team",
            "icon": "👥"
        })
    
    if "view_analytics" in user_profile.get("permissions", []):
        tasks.append({
            "id": "team_analytics",
            "title": "Team Analytics",
            "description": "View team performance metrics",
            "priority": "medium",
            "category": "analytics",
            "action": "Show me team performance analytics",
            "icon": "📊"
        })
    
    if "manage_sprints" in user_profile.get("permissions", []):
        tasks.append({
            "id": "sprint_management",
            "title": "Sprint Management",
            "description": "Manage current sprint and planning",
            "priority": "high",
            "category": "sprints",
            "action": "Show me current sprint status and planning",
            "icon": "🏃"
        })
    
    # Add role-specific tasks
    if role == "project_manager":
        tasks.extend([
            {
                "id": "project_overview",
                "title": "Project Overview",
                "description": "Get comprehensive project status",
                "priority": "high",
                "category": "management",
                "action": "Give me a comprehensive overview of all active projects",
                "icon": "📈"
            },
            {
                "id": "stakeholder_report",
                "title": "Stakeholder Report",
                "description": "Generate stakeholder update",
                "priority": "medium",
                "category": "reports",
                "action": "Create a stakeholder update report",
                "icon": "📄"
            }
        ])
    elif role == "developer":
        tasks.extend([
            {
                "id": "my_tasks",
                "title": "My Tasks",
                "description": "View my current tasks and priorities",
                "priority": "high",
                "category": "personal",
                "action": "Show me my current tasks and their priorities",
                "icon": "✅"
            },
            {
                "id": "code_reviews",
                "title": "Code Reviews",
                "description": "Check pending code reviews",
                "priority": "medium",
                "category": "development",
                "action": "Show me pending code reviews and PRs",
                "icon": "🔍"
            }
        ])
    elif role == "team_lead":
        tasks.extend([
            {
                "id": "team_workload",
                "title": "Team Workload",
                "description": "Analyze team capacity and workload",
                "priority": "high",
                "category": "management",
                "action": "Show me team workload and capacity analysis",
                "icon": "⚖️"
            },
            {
                "id": "resource_planning",
                "title": "Resource Planning",
                "description": "Plan team resources and assignments",
                "priority": "medium",
                "category": "planning",
                "action": "Help me plan team resources for upcoming sprints",
                "icon": "🎯"
            }
        ])
    
    return tasks


def fetch_user_actions():
    """Fetch user-specific quick actions from MCP servers"""
    user_profile = st.session_state.user_profile
    role = user_profile.get("role", "user")
    
    actions = []
    
    # Common actions for all users
    actions.extend([
        {
            "id": "quick_status",
            "title": "Quick Status Check",
            "description": "Get a quick overview of current status",
            "action": "Give me a quick status update",
            "icon": "⚡"
        },
        {
            "id": "create_issue",
            "title": "Create Issue",
            "description": "Create a new issue or task",
            "action": "Help me create a new issue",
            "icon": "➕"
        }
    ])
    
    # Role-specific actions
    if role == "project_manager":
        actions.extend([
            {
                "id": "project_health",
                "title": "Project Health Check",
                "description": "Check overall project health",
                "action": "Perform a project health check",
                "icon": "🏥"
            },
            {
                "id": "risk_assessment",
                "title": "Risk Assessment",
                "description": "Identify potential risks and blockers",
                "action": "Identify potential risks and blockers in my projects",
                "icon": "⚠️"
            }
        ])
    elif role == "developer":
        actions.extend([
            {
                "id": "daily_standup",
                "title": "Daily Standup Prep",
                "description": "Prepare for daily standup",
                "action": "Help me prepare for daily standup",
                "icon": "🌅"
            },
            {
                "id": "code_quality",
                "title": "Code Quality Check",
                "description": "Check code quality metrics",
                "action": "Show me code quality metrics and suggestions",
                "icon": "🔧"
            }
        ])
    elif role == "team_lead":
        actions.extend([
            {
                "id": "team_retrospective",
                "title": "Team Retrospective",
                "description": "Prepare team retrospective",
                "action": "Help me prepare for team retrospective",
                "icon": "🔄"
            },
            {
                "id": "performance_review",
                "title": "Performance Review",
                "description": "Review team performance",
                "action": "Show me team performance metrics and insights",
                "icon": "📊"
            }
        ])
    
    return actions


def refresh_user_data():
    """Refresh user-specific data from MCP servers"""
    # Fetch user profile
    st.session_state.user_profile = fetch_user_profile()
    
    # Fetch user tasks
    st.session_state.user_tasks = fetch_user_tasks()
    
    # Fetch user actions
    st.session_state.user_actions = fetch_user_actions()


def switch_user(user_email):
    """Switch to a different user profile"""
    if user_email in USER_PROFILES:
        st.session_state.user_profile = USER_PROFILES[user_email]
        refresh_user_data()
        return True, f"Switched to {st.session_state.user_profile['name']}"
    return False, "User not found"


def get_user_permissions():
    """Get current user's permissions"""
    return st.session_state.user_profile.get("permissions", [])


def has_permission(permission):
    """Check if current user has a specific permission"""
    return permission in get_user_permissions()


def get_user_role():
    """Get current user's role"""
    return st.session_state.user_profile.get("role", "user")


def is_project_manager():
    """Check if current user is a project manager"""
    return get_user_role() == "project_manager"


def is_developer():
    """Check if current user is a developer"""
    return get_user_role() == "developer"


def is_team_lead():
    """Check if current user is a team lead"""
    return get_user_role() == "team_lead"
