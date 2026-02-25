"""Main MCP Server implementation for KD UI Framework."""

import json
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from pydantic import AnyUrl

from .tools.dashboard import create_dashboard
from .tools.form import create_form
from .tools.table import create_table
from .tools.component import add_component
from .resources import component_templates
from .design_system import get_design_system

# Initialize MCP Server
app = Server("kd-ui-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools for generating Flask UI components."""
    return [
        Tool(
            name="create_dashboard",
            description="""Create a complete Flask dashboard template with DaisyUI components.
            
            This tool generates a responsive dashboard layout with:
            - Sidebar navigation or top navigation
            - Stats cards for key metrics
            - Chart containers
            - Data tables
            - Responsive grid layout
            
            Perfect for: Admin dashboards, analytics pages, data visualization pages
            
            Parameters:
            - layout: "sidebar" (default) or "topnav" - Navigation style
            - title: Dashboard title (default: "Dashboard")
            - theme: "light" (default), "dark", or "auto" - Color theme
            - components: List of components to include: ["stats", "charts", "table", "filters"]
            
            Returns: Complete Jinja2 template ready for Flask
            """,
            inputSchema={
                "type": "object",
                "properties": {
                    "layout": {
                        "type": "string",
                        "enum": ["sidebar", "topnav"],
                        "default": "sidebar",
                        "description": "Navigation layout style"
                    },
                    "title": {
                        "type": "string",
                        "default": "Dashboard",
                        "description": "Dashboard page title"
                    },
                    "theme": {
                        "type": "string",
                        "enum": ["light", "dark", "auto"],
                        "default": "light",
                        "description": "Color theme"
                    },
                    "components": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["stats", "charts", "table", "filters"]
                        },
                        "default": ["stats", "charts"],
                        "description": "Components to include in dashboard"
                    }
                }
            }
        ),
        Tool(
            name="create_form",
            description="""Create a beautiful form template with validation and DaisyUI styling.
            
            This tool generates forms with:
            - Input fields with proper labels and validation
            - Select dropdowns, checkboxes, radio buttons
            - File upload components
            - Submit and cancel buttons
            - Error message displays
            - Responsive layout
            
            Perfect for: Login forms, registration, data entry, settings pages
            
            Parameters:
            - form_type: "login", "register", "contact", "settings", or "custom"
            - fields: List of field configurations
            - method: "POST" (default) or "GET"
            - action: Form submission URL
            - inline: true/false - Display fields inline or stacked
            
            Returns: Form template with proper Flask-WTF integration
            """,
            inputSchema={
                "type": "object",
                "properties": {
                    "form_type": {
                        "type": "string",
                        "enum": ["login", "register", "contact", "settings", "custom"],
                        "default": "custom",
                        "description": "Predefined form type or custom"
                    },
                    "fields": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string", "enum": ["text", "email", "password", "number", "textarea", "select", "checkbox", "radio", "file"]},
                                "label": {"type": "string"},
                                "placeholder": {"type": "string"},
                                "required": {"type": "boolean", "default": False},
                                "options": {"type": "array", "items": {"type": "string"}}
                            },
                            "required": ["name", "type", "label"]
                        },
                        "description": "Form field configurations"
                    },
                    "method": {
                        "type": "string",
                        "enum": ["POST", "GET"],
                        "default": "POST"
                    },
                    "action": {
                        "type": "string",
                        "default": "",
                        "description": "Form submission URL"
                    },
                    "inline": {
                        "type": "boolean",
                        "default": False,
                        "description": "Display fields inline"
                    }
                },
                "required": ["fields"]
            }
        ),
        Tool(
            name="create_table",
            description="""Create a data table with sorting, filtering, and pagination.
            
            This tool generates tables with:
            - Sortable columns
            - Search/filter functionality
            - Pagination controls
            - Row actions (edit, delete, view)
            - Responsive design (cards on mobile)
            - Loading states
            
            Perfect for: User lists, product catalogs, transaction history, any data display
            
            Parameters:
            - columns: List of column definitions (name, label, sortable, type)
            - features: ["search", "sort", "pagination", "actions"]
            - rows_per_page: Number of rows per page (default: 10)
            - striped: Alternating row colors (default: true)
            - hoverable: Highlight row on hover (default: true)
            
            Returns: Table template with JavaScript for interactivity
            """,
            inputSchema={
                "type": "object",
                "properties": {
                    "columns": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "label": {"type": "string"},
                                "sortable": {"type": "boolean", "default": True},
                                "type": {"type": "string", "enum": ["text", "number", "date", "badge", "avatar"], "default": "text"}
                            },
                            "required": ["name", "label"]
                        },
                        "description": "Table column definitions"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["search", "sort", "pagination", "actions"]
                        },
                        "default": ["search", "sort", "pagination"],
                        "description": "Table features to enable"
                    },
                    "rows_per_page": {
                        "type": "integer",
                        "default": 10,
                        "description": "Rows per page for pagination"
                    },
                    "striped": {
                        "type": "boolean",
                        "default": True,
                        "description": "Alternating row colors"
                    },
                    "hoverable": {
                        "type": "boolean",
                        "default": True,
                        "description": "Highlight row on hover"
                    }
                },
                "required": ["columns"]
            }
        ),
        Tool(
            name="add_component",
            description="""Add individual UI components to your Flask templates.

            Available components:
            - stat_card: Metric display card with value, title, and trend
            - alert: Toast flash notification (fixed overlay, auto-dismisses). Supports type, duration, position, dismissable
            - badge: Status indicators and labels
            - button: Various button styles (primary, secondary, ghost, etc.)
            - card: Content container with optional header and footer
            - modal: Dialog/popup overlay
            - navbar: Top navigation bar
            - sidebar: Side navigation menu
            - navigation_menu: Navigation menu component
            - breadcrumb: Navigation breadcrumb trail
            - tabs: Tabbed content sections
            - progress: Progress bars and loading indicators
            - skeleton: Loading skeleton placeholders
            - typography: Typography and text components
            - dropdown_menu: Dropdown menu with items, icons, separators, and variants
            - chart_container: Container for Chart.js charts
            - theme_toggle: Light/dark theme toggle button

            Landing page sections:
            - hero: Hero/banner section
            - features: Features showcase section
            - testimonials: Testimonials/reviews section
            - pricing: Pricing plans section
            - cta: Call-to-action section
            - footer: Page footer section

            Parameters:
            - component_type: Type of component to generate
            - config: Component-specific configuration

            Returns: Component template snippet
            """,
            inputSchema={
                "type": "object",
                "properties": {
                    "component_type": {
                        "type": "string",
                        "enum": [
                            "stat_card", "alert", "badge", "button", "card",
                            "modal", "navbar", "sidebar", "navigation_menu",
                            "breadcrumb", "tabs", "progress", "skeleton",
                            "typography", "dropdown_menu", "chart_container",
                            "theme_toggle", "hero", "features", "testimonials",
                            "pricing", "cta", "footer"
                        ],
                        "description": "Type of component to generate"
                    },
                    "config": {
                        "type": "object",
                        "description": "Component-specific configuration",
                        "additionalProperties": True
                    }
                },
                "required": ["component_type"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls to generate UI components."""
    
    if name == "create_dashboard":
        template = create_dashboard(
            layout=arguments.get("layout", "sidebar"),
            title=arguments.get("title", "Dashboard"),
            theme=arguments.get("theme", "light"),
            components=arguments.get("components", ["stats", "charts"])
        )
        return [TextContent(type="text", text=template)]
    
    elif name == "create_form":
        template = create_form(
            form_type=arguments.get("form_type", "custom"),
            fields=arguments.get("fields", []),
            method=arguments.get("method", "POST"),
            action=arguments.get("action", ""),
            inline=arguments.get("inline", False)
        )
        return [TextContent(type="text", text=template)]
    
    elif name == "create_table":
        template = create_table(
            columns=arguments.get("columns", []),
            features=arguments.get("features", ["search", "sort", "pagination"]),
            rows_per_page=arguments.get("rows_per_page", 10),
            striped=arguments.get("striped", True),
            hoverable=arguments.get("hoverable", True)
        )
        return [TextContent(type="text", text=template)]
    
    elif name == "add_component":
        template = add_component(
            component_type=arguments.get("component_type"),
            config=arguments.get("config", {})
        )
        return [TextContent(type="text", text=template)]
    
    else:
        raise ValueError(f"Unknown tool: {name}")


@app.list_resources()
async def list_resources() -> list[Any]:
    """List available component templates and design system resources."""
    return [
        {
            "uri": "template://components/stat_card",
            "name": "Stat Card Component",
            "mimeType": "text/html",
            "description": "Reusable stat card template for displaying metrics"
        },
        {
            "uri": "template://components/chart_container",
            "name": "Chart Container Component",
            "mimeType": "text/html",
            "description": "Container for Chart.js charts with responsive sizing"
        },
        {
            "uri": "template://components/sidebar",
            "name": "Sidebar Navigation Component",
            "mimeType": "text/html",
            "description": "Responsive sidebar navigation menu"
        },
        {
            "uri": "template://components/navbar",
            "name": "Top Navigation Component",
            "mimeType": "text/html",
            "description": "Top navigation bar with logo and menu"
        },
        {
            "uri": "template://layouts/base",
            "name": "Base Layout Template",
            "mimeType": "text/html",
            "description": "Base Flask template with DaisyUI setup"
        },
        {
            "uri": "config://design-system",
            "name": "Design System Configuration",
            "mimeType": "application/json",
            "description": "Color palette, typography, spacing, and component styles"
        },
        {
            "uri": "docs://best-practices",
            "name": "UI Best Practices Guide",
            "mimeType": "text/markdown",
            "description": "Guidelines for creating beautiful, accessible dashboards"
        },
        {
            "uri": "docs://uiux-design-rules",
            "name": "UI/UX Design Rules & Standards",
            "mimeType": "text/markdown",
            "description": "Comprehensive UI/UX design rules, constraints, and anti-patterns from expert sources"
        },
        {
            "uri": "docs://dashboard-architecture",
            "name": "Dashboard Architecture Guide",
            "mimeType": "text/markdown",
            "description": "Navigation models, information density, and layout logic for dashboards"
        },
        {
            "uri": "docs://visual-style-system",
            "name": "Visual Style System",
            "mimeType": "text/markdown",
            "description": "Typography, spacing, color, and visual polish guidelines"
        },
        {
            "uri": "docs://anti-patterns",
            "name": "UI Anti-Patterns to Avoid",
            "mimeType": "text/markdown",
            "description": "Common UI/UX mistakes and how to avoid them"
        }
    ]


@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read component templates and design system resources."""
    uri_str = str(uri)
    
    if uri_str == "config://design-system":
        return json.dumps(get_design_system(), indent=2)
    
    elif uri_str.startswith("template://"):
        template_name = uri_str.replace("template://", "")
        return component_templates.get_template(template_name)
    
    elif uri_str == "docs://best-practices":
        return component_templates.get_best_practices()
    
    elif uri_str == "docs://uiux-design-rules":
        return component_templates.get_uiux_design_rules()
    
    elif uri_str == "docs://dashboard-architecture":
        return component_templates.get_dashboard_architecture()
    
    elif uri_str == "docs://visual-style-system":
        return component_templates.get_visual_style_system()
    
    elif uri_str == "docs://anti-patterns":
        return component_templates.get_anti_patterns()
    
    else:
        raise ValueError(f"Unknown resource: {uri}")


async def main():
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
