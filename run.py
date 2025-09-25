#!/usr/bin/env python3
"""
Entry point for the Streamlit MCP Linear Project Assistant
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main application
from src.main import main

if __name__ == "__main__":
    main()

