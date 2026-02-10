"""Interactive TUI setup wizard for KD UI Framework MCP Server."""

import sys
from pathlib import Path
from typing import List, Optional

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from .config_manager import ClineConfigManager, ClaudeConfigManager
from .platform_utils import (
    check_python_available,
    create_venv,
    find_existing_claude_config,
    get_absolute_path,
    get_claude_config_paths,
    get_default_claude_config_path,
    get_os_name,
    get_python_version,
    get_venv_python_path,
    get_vscode_settings_path,
    run_in_venv,
)

console = Console()


class SetupWizard:
    """Interactive setup wizard for KD UI Framework."""
    
    def __init__(self):
        """Initialize the setup wizard."""
        # Determine the project root (mcp-server directory)
        # This script is in src/kd_ui_server/cli/setup.py
        # So we go up 4 levels to get to mcp-server/
        self.script_dir = Path(__file__).parent
        self.project_root = self.script_dir.parent.parent.parent
        self.venv_dir = self.project_root / "venv"
        self.server_module = "kd_ui_server.server"
        self.server_name = "kd-ui"
        
        self.configured_clients = []
    
    def print_header(self):
        """Print the setup wizard header."""
        console.print()
        header = Text("KD UI Framework Setup Wizard", style="bold cyan")
        console.print(Panel(header, border_style="cyan"))
        console.print()
        console.print(f"📍 Detected OS: [bold]{get_os_name()}[/bold]")
        console.print(f"📂 Project Root: [dim]{self.project_root}[/dim]")
        console.print()
    
    def step1_environment_setup(self) -> bool:
        """
        Step 1: Set up Python virtual environment.
        
        Returns:
            True if successful
        """
        console.print("[bold cyan]━━━ [1/3] Virtual Environment Setup ━━━[/bold cyan]")
        console.print()
        
        # Check Python
        py_available, py_version = check_python_available()
        if not py_available:
            console.print("❌ Python not found", style="red")
            return False
        
        console.print(f"✓ Python {get_python_version()} found", style="green")
        
        # Create or verify venv
        if self.venv_dir.exists():
            console.print(f"✓ Virtual environment exists: [dim]{self.venv_dir}[/dim]", style="green")
        else:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                task = progress.add_task("Creating virtual environment...", total=None)
                
                if not create_venv(self.venv_dir):
                    console.print("❌ Failed to create virtual environment", style="red")
                    return False
                
                progress.update(task, completed=True)
            
            console.print(f"✓ Virtual environment created: [dim]{self.venv_dir}[/dim]", style="green")
        
        # Install dependencies
        python_path = get_venv_python_path(self.venv_dir)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Installing dependencies in venv...", total=None)
            
            # Upgrade pip first
            run_in_venv(self.venv_dir, ["-m", "pip", "install", "--upgrade", "pip"])
            
            # Install the package in editable mode
            success, output = run_in_venv(
                self.venv_dir,
                ["-m", "pip", "install", "-e", str(self.project_root)]
            )
            
            progress.update(task, completed=True)
        
        if not success:
            console.print("❌ Failed to install dependencies", style="red")
            console.print(f"[dim]{output}[/dim]")
            return False
        
        console.print("✓ Dependencies installed in venv", style="green")
        
        # Verify kd_ui_server can be imported
        success, output = run_in_venv(
            self.venv_dir,
            ["-c", "import kd_ui_server; print('OK')"]
        )
        
        if success and "OK" in output:
            console.print("✓ kd_ui_server ready!", style="green")
        else:
            console.print("❌ Failed to import kd_ui_server", style="red")
            return False
        
        console.print()
        return True
    
    def step2_mcp_configuration(self) -> bool:
        """
        Step 2: Configure MCP clients.
        
        Returns:
            True if successful
        """
        console.print("[bold cyan]━━━ [2/3] MCP Client Configuration ━━━[/bold cyan]")
        console.print()
        
        # Detect available clients
        clients = []
        
        # Check for Cline (VS Code)
        vscode_settings_path = get_vscode_settings_path()
        if vscode_settings_path:
            if vscode_settings_path.exists():
                clients.append(("Cline (VS Code)", "cline", vscode_settings_path))
                console.print(f"✓ VS Code settings found", style="green")
            else:
                clients.append(("Cline (VS Code) - will create config", "cline", vscode_settings_path))
                console.print(f"? VS Code settings not found - can create", style="yellow")
        
        # Check for Claude Desktop/Code CLI
        claude_config_path = find_existing_claude_config()
        if claude_config_path:
            clients.append(("Claude Desktop/Code CLI", "claude", claude_config_path))
            console.print(f"✓ Claude config found at: [dim]{claude_config_path}[/dim]", style="green")
        else:
            default_path = get_default_claude_config_path()
            clients.append(("Claude Desktop/Code CLI - will create config", "claude", default_path))
            console.print(f"? Claude config not found - can create at: [dim]{default_path}[/dim]", style="yellow")
        
        console.print()
        
        if not clients:
            console.print("❌ No MCP clients detected", style="red")
            return False
        
        # Ask user which clients to configure
        choices = [
            questionary.Choice(title=name, value=(client_type, path))
            for name, client_type, path in clients
        ]
        
        selected = questionary.checkbox(
            "Select MCP clients to configure (Space to select, Enter to confirm):",
            choices=choices
        ).ask()
        
        if not selected:
            console.print("⚠️  No clients selected - skipping configuration", style="yellow")
            return True
        
        console.print()
        
        # Configure each selected client
        python_path = get_venv_python_path(self.venv_dir)
        
        for client_type, config_path in selected:
            if client_type == "cline":
                self._configure_cline(config_path, python_path)
            elif client_type == "claude":
                self._configure_claude(config_path, python_path)
        
        console.print()
        return True
    
    def _configure_cline(self, config_path: Path, python_path: Path):
        """Configure Cline (VS Code) settings."""
        manager = ClineConfigManager(config_path)
        
        # Create backup if file exists
        if manager.exists():
            backup_path = manager.create_backup()
            if backup_path:
                console.print(f"💾 Backup created: [dim]{backup_path.name}[/dim]", style="blue")
        
        # Add MCP server
        success, message = manager.add_mcp_server(
            self.server_name,
            python_path,
            self.server_module,
            self.project_root
        )
        
        if success:
            console.print(f"✓ Configured Cline", style="green")
            self.configured_clients.append("Cline (VS Code)")
        else:
            console.print(f"❌ {message}", style="red")
    
    def _configure_claude(self, config_path: Path, python_path: Path):
        """Configure Claude Desktop/Code CLI."""
        manager = ClaudeConfigManager(config_path)
        
        # Create backup if file exists
        if manager.exists():
            backup_path = manager.create_backup()
            if backup_path:
                console.print(f"💾 Backup created: [dim]{backup_path.name}[/dim]", style="blue")
        
        # Add MCP server
        success, message = manager.add_mcp_server(
            self.server_name,
            python_path,
            self.server_module,
            self.project_root
        )
        
        if success:
            console.print(f"✓ Configured Claude Desktop/Code CLI", style="green")
            self.configured_clients.append("Claude Desktop/Code CLI")
        else:
            console.print(f"❌ {message}", style="red")
    
    def step3_validation(self) -> bool:
        """
        Step 3: Validate the setup.
        
        Returns:
            True if successful
        """
        console.print("[bold cyan]━━━ [3/3] Validation ━━━[/bold cyan]")
        console.print()
        
        # Create validation table
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Check", style="dim")
        table.add_column("Status")
        
        # Check venv
        if self.venv_dir.exists():
            table.add_row(
                f"Virtual environment",
                f"[green]✓[/green] {self.venv_dir.relative_to(self.project_root)}"
            )
        else:
            table.add_row("Virtual environment", "[red]✗ Not found[/red]")
        
        # Check Python in venv
        python_path = get_venv_python_path(self.venv_dir)
        if python_path.exists():
            table.add_row(
                "Python in venv",
                f"[green]✓[/green] Python {get_python_version()}"
            )
        else:
            table.add_row("Python in venv", "[red]✗ Not found[/red]")
        
        # Check kd_ui_server import
        success, _ = run_in_venv(
            self.venv_dir,
            ["-c", "import kd_ui_server"]
        )
        table.add_row(
            "kd_ui_server importable",
            "[green]✓ OK[/green]" if success else "[red]✗ Failed[/red]"
        )
        
        # Check configured clients
        for client in self.configured_clients:
            table.add_row(f"{client} configuration", "[green]✓ OK[/green]")
        
        console.print(table)
        console.print()
        
        return True
    
    def print_completion(self):
        """Print completion message and next steps."""
        console.print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
        console.print()
        console.print("🎉 [bold green]Setup Complete![/bold green]")
        console.print()
        console.print(f"Virtual environment: [dim]{self.venv_dir.relative_to(self.project_root)}[/dim]")
        console.print()
        
        if self.configured_clients:
            console.print("⚠️  [bold yellow]Next Steps:[/bold yellow]")
            console.print()
            
            if "Cline (VS Code)" in self.configured_clients:
                console.print("  • Restart VS Code for Cline changes to take effect")
            
            if "Claude Desktop/Code CLI" in self.configured_clients:
                console.print("  • Restart Claude Desktop (if open)")
                console.print("  • Claude Code CLI is ready to use!")
            
            console.print()
        
        console.print("Your MCP server is ready to use! 🚀")
        console.print()
    
    def run(self) -> bool:
        """
        Run the complete setup wizard.
        
        Returns:
            True if setup completed successfully
        """
        try:
            self.print_header()
            
            # Step 1: Environment setup
            if not self.step1_environment_setup():
                console.print("\n❌ [bold red]Setup failed at environment setup[/bold red]\n")
                return False
            
            # Step 2: MCP configuration
            if not self.step2_mcp_configuration():
                console.print("\n❌ [bold red]Setup failed at MCP configuration[/bold red]\n")
                return False
            
            # Step 3: Validation
            if not self.step3_validation():
                console.print("\n❌ [bold red]Setup failed at validation[/bold red]\n")
                return False
            
            # Completion
            self.print_completion()
            
            return True
            
        except KeyboardInterrupt:
            console.print("\n\n⚠️  Setup cancelled by user\n", style="yellow")
            return False
        except Exception as e:
            console.print(f"\n\n❌ [bold red]Unexpected error:[/bold red] {e}\n")
            return False


def main():
    """Main entry point for the setup wizard."""
    wizard = SetupWizard()
    success = wizard.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
