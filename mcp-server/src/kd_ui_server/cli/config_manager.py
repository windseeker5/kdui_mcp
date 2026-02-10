"""Configuration file management for MCP clients (Cline and Claude)."""

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

from .platform_utils import get_absolute_path


class ConfigManager:
    """Manages MCP client configuration files."""
    
    def __init__(self, config_path: Path):
        """
        Initialize config manager.
        
        Args:
            config_path: Path to the config file
        """
        self.config_path = config_path
    
    def exists(self) -> bool:
        """Check if config file exists."""
        return self.config_path.exists()
    
    def create_backup(self) -> Optional[Path]:
        """
        Create a backup of the config file.
        
        Returns:
            Path to backup file or None if failed
        """
        if not self.exists():
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.config_path.with_suffix(f".backup_{timestamp}.json")
        
        try:
            shutil.copy2(self.config_path, backup_path)
            return backup_path
        except Exception:
            return None
    
    def read_config(self) -> dict:
        """
        Read and parse the config file.
        
        Returns:
            Config dictionary or empty dict if file doesn't exist
        """
        if not self.exists():
            return {}
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    
    def write_config(self, config: dict) -> bool:
        """
        Write config to file.
        
        Args:
            config: Configuration dictionary
        
        Returns:
            True if successful
        """
        try:
            # Create parent directories if needed
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write with nice formatting
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
            
            return True
        except Exception:
            return False
    
    def add_mcp_server(
        self,
        server_name: str,
        python_path: Path,
        server_module: str,
        working_dir: Path
    ) -> Tuple[bool, str]:
        """
        Add or update MCP server configuration.
        
        Args:
            server_name: Name of the MCP server (e.g., "kd-ui")
            python_path: Path to Python executable in venv
            server_module: Python module to run (e.g., "kd_ui_server.server")
            working_dir: Working directory for the server
        
        Returns:
            Tuple of (success, message)
        """
        # Read existing config
        config = self.read_config()
        
        # Ensure mcpServers section exists
        if "mcpServers" not in config:
            config["mcpServers"] = {}
        
        # Add/update the server configuration
        config["mcpServers"][server_name] = {
            "command": get_absolute_path(python_path),
            "args": ["-m", server_module],
            "cwd": get_absolute_path(working_dir)
        }
        
        # Write back
        if self.write_config(config):
            return True, f"Successfully configured {server_name} MCP server"
        else:
            return False, "Failed to write configuration file"
    
    def has_mcp_server(self, server_name: str) -> bool:
        """
        Check if MCP server is already configured.
        
        Args:
            server_name: Name of the MCP server
        
        Returns:
            True if server exists in config
        """
        config = self.read_config()
        return server_name in config.get("mcpServers", {})


class ClineConfigManager(ConfigManager):
    """Manager for Cline (VS Code) settings.json."""
    
    def add_mcp_server(
        self,
        server_name: str,
        python_path: Path,
        server_module: str,
        working_dir: Path
    ) -> Tuple[bool, str]:
        """
        Add or update MCP server in Cline configuration.
        Uses cline.mcpServers instead of mcpServers.
        
        Args:
            server_name: Name of the MCP server (e.g., "kd-ui")
            python_path: Path to Python executable in venv
            server_module: Python module to run (e.g., "kd_ui_server.server")
            working_dir: Working directory for the server
        
        Returns:
            Tuple of (success, message)
        """
        # Read existing config
        config = self.read_config()
        
        # Ensure cline.mcpServers section exists
        if "cline.mcpServers" not in config:
            config["cline.mcpServers"] = {}
        
        # Add/update the server configuration
        config["cline.mcpServers"][server_name] = {
            "command": get_absolute_path(python_path),
            "args": ["-m", server_module],
            "cwd": get_absolute_path(working_dir)
        }
        
        # Write back
        if self.write_config(config):
            return True, f"Successfully configured {server_name} in Cline"
        else:
            return False, "Failed to write VS Code settings.json"
    
    def has_mcp_server(self, server_name: str) -> bool:
        """
        Check if MCP server is already configured in Cline.
        
        Args:
            server_name: Name of the MCP server
        
        Returns:
            True if server exists in config
        """
        config = self.read_config()
        return server_name in config.get("cline.mcpServers", {})


class ClaudeConfigManager(ConfigManager):
    """Manager for Claude Desktop/Code CLI claude_desktop_config.json."""
    
    pass  # Uses the default implementation from ConfigManager
