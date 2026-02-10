#!/usr/bin/env python3
"""
KD UI Framework - MCP Configuration Wizard

This script configures the KD UI Framework MCP Server in your AI tool.

Prerequisites:
- Virtual environment created and activated
- Dependencies installed (pip install -e mcp-server)

Usage:
    python setup.py
"""

import subprocess
import sys
from pathlib import Path


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    
    try:
        import rich
    except ImportError:
        missing.append("rich")
    
    try:
        import questionary
    except ImportError:
        missing.append("questionary")
    
    try:
        import click
    except ImportError:
        missing.append("click")
    
    return missing


def main():
    """Run the MCP configuration wizard."""
    print("🎨 KD UI Framework - MCP Configuration")
    print("=" * 50)
    print()
    
    # Get the project directories
    project_root = Path(__file__).parent
    mcp_server_dir = project_root / "mcp-server"
    
    if not mcp_server_dir.exists():
        print("❌ Error: mcp-server directory not found")
        print(f"   Expected: {mcp_server_dir}")
        return 1
    
    # Check if dependencies are installed
    missing = check_dependencies()
    
    if missing:
        print("❌ Missing dependencies detected!")
        print()
        print("The following packages are required but not installed:")
        for pkg in missing:
            print(f"  - {pkg}")
        print()
        print("📋 Please install dependencies first:")
        print()
        print("   1. Make sure your virtual environment is activated")
        print("      You should see (venv) in your terminal prompt")
        print()
        print("   2. Install the MCP server:")
        print(f"      pip install -e {mcp_server_dir}")
        print()
        print("   3. Run setup again:")
        print("      python setup.py")
        print()
        print("💡 Need help? See README.md for detailed instructions")
        return 1
    
    # Dependencies are installed, proceed with configuration
    print("✓ All dependencies are installed")
    print()
    print("🚀 Starting MCP configuration wizard...")
    print()
    
    # Import and run the wizard
    sys.path.insert(0, str(mcp_server_dir / "src"))
    
    try:
        from kd_ui_server.cli.setup import main as wizard_main
        return wizard_main()
    except Exception as e:
        print(f"❌ Error running configuration wizard: {e}")
        import traceback
        traceback.print_exc()
        print()
        print("💡 If you're seeing import errors, make sure:")
        print("   1. Your virtual environment is activated")
        print("   2. Dependencies are installed: pip install -e mcp-server")
        return 1


if __name__ == "__main__":
    sys.exit(main())
