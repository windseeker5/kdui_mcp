# Setup Wizard Documentation

## Overview

The KD UI Framework now includes an **interactive TUI (Terminal User Interface) setup wizard** that automates the entire installation and configuration process across Windows, Linux, and macOS.

## Features

### ✨ What It Does

1. **Virtual Environment Management**
   - Creates a Python virtual environment automatically
   - Installs all dependencies in isolation
   - Works on Windows, Linux, and macOS

2. **Smart Detection**
   - Auto-detects your operating system
   - Finds VS Code settings.json location
   - Searches for Claude Desktop/Code CLI config files
   - Detects Python version

3. **MCP Client Configuration**
   - Configures Cline (VS Code extension)
   - Configures Claude Desktop
   - Configures Claude Code CLI (Linux)
   - Creates config files if they don't exist
   - Backs up existing configs before modifying

4. **Validation**
   - Verifies Python installation
   - Checks virtual environment
   - Tests kd_ui_server import
   - Validates all configurations

5. **Beautiful TUI**
   - Rich terminal output with colors
   - Progress spinners for long operations
   - Interactive checkboxes for client selection
   - Clear status messages and tables

## Usage

### Quick Start

```bash
# From the project root
python setup.py
```

### What Happens

1. **Dependency Check**: Installs Rich, Questionary, and Click if needed
2. **Interactive Wizard**: Launches the TUI setup wizard
3. **Step 1**: Creates venv and installs dependencies
4. **Step 2**: Detects MCP clients and lets you choose which to configure
5. **Step 3**: Validates everything and shows results
6. **Completion**: Shows next steps (restart VS Code/Claude)

## Architecture

### File Structure

```
KD UI Framework/
├── setup.py                           # Entry point script
└── mcp-server/
    ├── pyproject.toml                 # Added CLI dependencies & entry point
    └── src/kd_ui_server/
        └── cli/                       # NEW: CLI module
            ├── __init__.py            # Module init
            ├── setup.py               # Main wizard logic
            ├── platform_utils.py      # OS detection & path handling
            └── config_manager.py      # Config file management
```

### Components

#### 1. `setup.py` (Root)
- Entry point for the wizard
- Checks and installs dependencies
- Imports and runs the wizard

#### 2. `cli/setup.py`
- **SetupWizard class**: Main wizard orchestration
- **step1_environment_setup()**: Virtual environment creation
- **step2_mcp_configuration()**: Client configuration
- **step3_validation()**: Final validation
- Beautiful Rich console output

#### 3. `cli/platform_utils.py`
- **OS Detection**: `get_os_name()`, `is_windows()`, `is_linux()`, `is_macos()`
- **Path Detection**: 
  - `get_vscode_settings_path()` - Finds VS Code settings.json
  - `get_claude_config_paths()` - Lists possible Claude config locations
  - `find_existing_claude_config()` - Finds existing config
- **Virtual Environment**:
  - `create_venv()` - Creates virtual environment
  - `get_venv_python_path()` - Gets Python executable path
  - `run_in_venv()` - Runs commands in venv
- **Path Utilities**: `get_absolute_path()` - JSON-safe paths with forward slashes

#### 4. `cli/config_manager.py`
- **ConfigManager**: Base class for config file management
  - `read_config()` - Parse JSON config
  - `write_config()` - Write JSON config
  - `create_backup()` - Backup before modifying
  - `add_mcp_server()` - Add/update MCP server entry
- **ClineConfigManager**: VS Code settings.json management (uses `cline.mcpServers`)
- **ClaudeConfigManager**: Claude Desktop/Code CLI config management (uses `mcpServers`)

## Cross-Platform Support

### Windows
- Virtual environment: `venv\Scripts\python.exe`
- VS Code settings: `%APPDATA%\Code\User\settings.json`
- Claude config: `%APPDATA%\Claude\claude_desktop_config.json`

### Linux
- Virtual environment: `venv/bin/python`
- VS Code settings: `~/.config/Code/User/settings.json`
- Claude config (multiple locations checked):
  - `~/.config/Claude/claude_desktop_config.json` (Desktop)
  - `~/.config/claude/claude_desktop_config.json` (CLI - lowercase)
  - `~/.claude/claude_desktop_config.json` (Alternative)

### macOS
- Virtual environment: `venv/bin/python`
- VS Code settings: `~/Library/Application Support/Code/User/settings.json`
- Claude config: `~/Library/Application Support/Claude/claude_desktop_config.json`

## Dependencies

### Added to `pyproject.toml`

```toml
dependencies = [
    "mcp>=0.9.0",
    "jinja2>=3.1.0",
    "rich>=13.0.0",        # Beautiful terminal output
    "questionary>=2.0.0",  # Interactive prompts
    "click>=8.0.0",        # CLI framework
]

[project.scripts]
kd-ui-setup = "kd_ui_server.cli.setup:main"
```

### What Each Does

- **Rich**: Beautiful terminal output (colors, tables, progress bars, panels)
- **Questionary**: Interactive prompts (checkboxes, confirmations)
- **Click**: CLI framework (not heavily used yet, but available for future commands)

## CLI Entry Point

After installation, you can also run:

```bash
# If installed in a venv and activated
kd-ui-setup
```

This runs the same wizard as `python setup.py`.

## Configuration Format

### Cline (VS Code)

```json
{
  "cline.mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/venv/Scripts/python.exe",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/mcp-server"
    }
  }
}
```

### Claude Desktop/Code CLI

```json
{
  "mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/mcp-server"
    }
  }
}
```

## Safety Features

1. **Backups**: Always creates timestamped backups before modifying configs
2. **Idempotent**: Can run multiple times safely
3. **Non-destructive**: Merges with existing configs, doesn't overwrite
4. **Validation**: Checks each step before proceeding
5. **Clear errors**: Helpful error messages if something fails

## Troubleshooting

### Setup Fails at Dependency Installation

```bash
# Install manually
cd mcp-server
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Linux/Mac
pip install -e .
```

### Can't Find VS Code Settings

The wizard checks standard locations. If you have a custom VS Code install:
1. Skip Cline configuration in the wizard
2. Manually add to your settings.json (see README.md)

### Claude Config Issues

- **Not found**: Wizard offers to create it
- **Wrong location**: Select custom path or create manually
- **Permissions**: Ensure you have write access to config directories

### Virtual Environment Issues

```bash
# Delete and recreate
rm -rf mcp-server/venv  # Linux/Mac
# or: rmdir /s mcp-server\venv  # Windows
python setup.py  # Run wizard again
```

## Future Enhancements

Potential additions:

1. **Uninstall command**: Remove MCP server from configs
2. **Update command**: Update to latest version
3. **Validate command**: Check if setup is still valid
4. **Custom paths**: Support non-standard installation paths
5. **Multiple Python versions**: Choose which Python to use
6. **Config export**: Export config for sharing
7. **Wizard skip**: Skip steps that are already complete

## Best Practices

1. **Run from project root**: Always run `python setup.py` from the project root
2. **One repo, multiple machines**: Clone the repo on each machine and run setup
3. **Keep venv in .gitignore**: Don't commit the virtual environment
4. **Restart after setup**: Always restart VS Code/Claude Desktop after configuration
5. **Test after setup**: Try using the MCP server immediately to verify

## Benefits

### For Users
- ⚡ **Fast**: One command instead of 10+ manual steps
- 🎯 **Accurate**: No typos in config paths
- 🔒 **Safe**: Backups and validation
- 🌍 **Cross-platform**: Works everywhere
- 💬 **Clear**: Beautiful output shows exactly what's happening

### For Developers
- 📦 **Professional**: Shows polish and care
- 🔧 **Maintainable**: One script to update vs documentation
- 🐛 **Fewer issues**: Less room for user error
- 🚀 **Better adoption**: Lower barrier to entry

---

**Built with**: Rich, Questionary, Click, and lots of ❤️
