#!/usr/bin/env python3
"""
KD UI Framework - One-Command Setup Script

This script sets up the KD UI Framework MCP Server with an interactive TUI wizard.
It handles:
- Virtual environment creation
- Dependency installation
- MCP client configuration (Cline, Claude Desktop/Code CLI)
- Cross-platform support (Windows, Linux, macOS)

Usage:
    python setup.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run the setup wizard."""
    print("🎨 KD UI Framework Setup")
    print("=" * 50)
    print()
    
    # Get the mcp-server directory
    project_root = Path(__file__).parent
    mcp_server_dir = project_root / "mcp-server"
    
    if not mcp_server_dir.exists():
        print("❌ Error: mcp-server directory not found")
        print(f"   Expected: {mcp_server_dir}")
        return 1
    
    # Check if we need to install dependencies first
    try:
        import rich
        import questionary
        import click
    except ImportError:
        print("📦 Installing setup dependencies...")
        print()
        
        # Install the package which includes all dependencies
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", str(mcp_server_dir)],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Failed to install dependencies")
            print(result.stderr)
            return 1
        
        print("✓ Dependencies installed")
        print()
    
    # Now run the setup wizard
    print("Starting setup wizard...")
    print()
    
    # Import and run the wizard
    sys.path.insert(0, str(mcp_server_dir / "src"))
    
    try:
        from kd_ui_server.cli.setup import main as wizard_main
        return wizard_main()
    except Exception as e:
        print(f"❌ Error running setup wizard: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
