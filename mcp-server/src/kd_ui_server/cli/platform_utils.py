"""Cross-platform utility functions for path detection and OS-specific operations."""

import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple


def get_os_name() -> str:
    """Get the current operating system name."""
    return platform.system()


def is_windows() -> bool:
    """Check if running on Windows."""
    return get_os_name() == "Windows"


def is_linux() -> bool:
    """Check if running on Linux."""
    return get_os_name() == "Linux"


def is_macos() -> bool:
    """Check if running on macOS."""
    return get_os_name() == "Darwin"


def get_python_version() -> str:
    """Get Python version string."""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_vscode_settings_path() -> Optional[Path]:
    """
    Get the VS Code settings.json path for the current OS.
    
    Returns:
        Path to settings.json or None if not found
    """
    if is_windows():
        # Windows: %APPDATA%\Code\User\settings.json
        appdata = os.getenv("APPDATA")
        if appdata:
            path = Path(appdata) / "Code" / "User" / "settings.json"
            return path
    elif is_linux():
        # Linux: ~/.config/Code/User/settings.json
        path = Path.home() / ".config" / "Code" / "User" / "settings.json"
        return path
    elif is_macos():
        # macOS: ~/Library/Application Support/Code/User/settings.json
        path = Path.home() / "Library" / "Application Support" / "Code" / "User" / "settings.json"
        return path
    
    return None


def get_claude_config_paths() -> list[Path]:
    """
    Get possible Claude configuration file paths for the current OS.
    Returns multiple possible paths to check.
    
    Returns:
        List of possible Claude config paths
    """
    paths = []
    
    if is_windows():
        # Windows: %APPDATA%\Claude\claude_desktop_config.json
        appdata = os.getenv("APPDATA")
        if appdata:
            paths.append(Path(appdata) / "Claude" / "claude_desktop_config.json")
    elif is_linux():
        # Linux: Try multiple possible locations
        # Claude Desktop (GUI)
        paths.append(Path.home() / ".config" / "Claude" / "claude_desktop_config.json")
        # Claude Code CLI (lowercase)
        paths.append(Path.home() / ".config" / "claude" / "claude_desktop_config.json")
        # Alternative location
        paths.append(Path.home() / ".claude" / "claude_desktop_config.json")
    elif is_macos():
        # macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
        paths.append(
            Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        )
    
    return paths


def find_existing_claude_config() -> Optional[Path]:
    """
    Find an existing Claude config file.
    
    Returns:
        Path to existing config or None
    """
    for path in get_claude_config_paths():
        if path.exists():
            return path
    return None


def get_default_claude_config_path() -> Path:
    """
    Get the default Claude config path for creating new config.
    
    Returns:
        Default path for Claude config
    """
    paths = get_claude_config_paths()
    return paths[0] if paths else Path.home() / ".config" / "claude" / "claude_desktop_config.json"


def get_venv_python_path(venv_dir: Path) -> Path:
    """
    Get the Python executable path inside a virtual environment.
    
    Args:
        venv_dir: Path to the virtual environment directory
    
    Returns:
        Path to Python executable
    """
    if is_windows():
        return venv_dir / "Scripts" / "python.exe"
    else:
        return venv_dir / "bin" / "python"


def get_venv_activate_command(venv_dir: Path) -> str:
    """
    Get the command to activate a virtual environment.
    
    Args:
        venv_dir: Path to the virtual environment directory
    
    Returns:
        Activation command string
    """
    if is_windows():
        return str(venv_dir / "Scripts" / "activate.bat")
    else:
        return f"source {venv_dir / 'bin' / 'activate'}"


def check_python_available() -> Tuple[bool, Optional[str]]:
    """
    Check if Python is available in the system.
    
    Returns:
        Tuple of (is_available, version_string)
    """
    try:
        result = subprocess.run(
            [sys.executable, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            return True, version
    except Exception:
        pass
    
    return False, None


def create_venv(venv_dir: Path) -> bool:
    """
    Create a virtual environment.
    
    Args:
        venv_dir: Path where to create the venv
    
    Returns:
        True if successful, False otherwise
    """
    try:
        import venv
        venv.create(venv_dir, with_pip=True)
        return True
    except Exception:
        return False


def run_in_venv(venv_dir: Path, command: list[str]) -> Tuple[bool, str]:
    """
    Run a command inside a virtual environment.
    
    Args:
        venv_dir: Path to the virtual environment
        command: Command to run as list of strings
    
    Returns:
        Tuple of (success, output)
    """
    python_path = get_venv_python_path(venv_dir)
    
    try:
        result = subprocess.run(
            [str(python_path)] + command,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes timeout
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def get_absolute_path(path: Path) -> str:
    """
    Get absolute path as string with forward slashes (JSON-safe).
    
    Args:
        path: Path to convert
    
    Returns:
        Absolute path string with forward slashes
    """
    return str(path.resolve()).replace("\\", "/")
