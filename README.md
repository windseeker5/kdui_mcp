# KD UI

MCP server that generates ready-to-use Flask + DaisyUI UI components. Ask your AI assistant to produce dashboards, forms, tables, navbars, sidebars, and more — they come out polished by default.

**Stack**: Tailwind CSS + DaisyUI 4 + Lucide Icons + Chart.js, delivered via CDN. No build step required.

---

## Installation

### 1. Clone and set up

```bash
git clone https://github.com/windseeker5/kdui_mcp.git
cd kdui_mcp

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux / macOS
# venv\Scripts\activate           # Windows

# Install the MCP server package
pip install -e mcp-server
```

### 2. Configure your AI tool

#### Claude Code (recommended — project-scoped)

A `.mcp.json` file is already at the project root. Update the `command` path to match your cloned location:

```json
{
  "mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/kdui_mcp/venv/bin/python",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/kdui_mcp/mcp-server"
    }
  }
}
```

Claude Code auto-detects `.mcp.json` when you open the project. No other config needed.

#### Claude Code (global install)

```bash
claude mcp add kd-ui \
  --command "/absolute/path/to/kdui_mcp/venv/bin/python" \
  -- -m kd_ui_server.server
```

#### VS Code — Cline extension

Open VS Code Settings → search for **Cline MCP** → add a new server entry:

| Field | Value |
|---|---|
| Name | `kd-ui` |
| Command | `/absolute/path/to/kdui_mcp/venv/bin/python` |
| Args | `-m kd_ui_server.server` |
| Working directory | `/absolute/path/to/kdui_mcp/mcp-server` |

Then reload the VS Code window.

#### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/kdui_mcp/venv/bin/python",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/kdui_mcp/mcp-server"
    }
  }
}
```

Restart Claude Desktop.

---

## Available tools

| Tool | Description |
|---|---|
| `create_dashboard` | Full dashboard layout — sidebar or top-nav, stats, charts, table |
| `create_form` | Form templates — login, register, contact, or custom fields |
| `create_table` | Data table with search, sort, and pagination |
| `add_component` | Individual components — see full list below |

### `add_component` types

**UI components**: `badge`, `button`, `alert`, `card`, `progress`, `skeleton`, `typography`, `stat_card`, `modal`, `tabs`, `breadcrumb`, `dropdown_menu`, `navbar`, `sidebar`, `navigation_menu`, `chart_container`, `theme_toggle`

**Landing page sections**: `hero`, `features`, `testimonials`, `pricing`, `cta`, `footer`

---

## Example prompts

```
Create a sales dashboard with sidebar navigation, stat cards for revenue and active users, and a monthly revenue chart.
```

```
Add a dropdown menu with Profile, Settings, and Log out items.
```

```
Generate a login form.
```

---

## See also

- `SHOWCASE.md` — run the component showcase locally to browse every component
