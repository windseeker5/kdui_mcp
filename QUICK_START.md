# Quick Start Guide - KD UI Framework

Get started with beautiful Flask UIs in minutes with our **automated setup wizard**!

## 🚀 One-Command Setup

### Prerequisites

- Python 3.10+ installed
- VS Code with Cline extension (optional) or Claude Desktop/Code CLI (optional)

### Installation

```bash
# Clone the repository (or navigate to your existing directory)
cd "path/to/KD UI Framework"

# Run the interactive setup wizard
python setup.py
```

That's it! The wizard will:

1. ✅ Create a virtual environment
2. ✅ Install all dependencies
3. ✅ Detect and configure your MCP clients:
   - Cline (VS Code)
   - Claude Desktop
   - Claude Code CLI
4. ✅ Validate everything works

### What the Setup Wizard Looks Like

```
🎨 KD UI Framework Setup Wizard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Detected OS: Windows 11
📂 Project Root: c:/Users/.../KD UI Framework/mcp-server

━━━ [1/3] Virtual Environment Setup ━━━

✓ Python 3.11.0 found
✓ Virtual environment created: venv/
✓ Dependencies installed in venv
✓ kd_ui_server ready!

━━━ [2/3] MCP Client Configuration ━━━

✓ VS Code settings found
✓ Claude config found at: ~/.config/claude/claude_desktop_config.json

Select MCP clients to configure (Space to select, Enter to confirm):
  [x] Cline (VS Code)
  [x] Claude Desktop/Code CLI

💾 Backup created: settings.backup_20260210_150312.json
✓ Configured Cline
✓ Configured Claude Desktop/Code CLI

━━━ [3/3] Validation ━━━

┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Check                  ┃ Status              ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ Virtual environment    │ ✓ venv              │
│ Python in venv         │ ✓ Python 3.11.0     │
│ kd_ui_server importable│ ✓ OK                │
│ Cline configuration    │ ✓ OK                │
│ Claude configuration   │ ✓ OK                │
└────────────────────────┴─────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Setup Complete!

Virtual environment: venv

⚠️  Next Steps:
  • Restart VS Code for Cline changes to take effect
  • Restart Claude Desktop (if open)
  • Claude Code CLI is ready to use!

Your MCP server is ready to use! 🚀
```

### After Setup

1. **Restart VS Code** (if using Cline)
2. **Restart Claude Desktop** (if using Claude Desktop)
3. You're ready to generate beautiful UIs! 🎉

---

## 🎨 Using the MCP Server

### Step 1: Set Up Your Flask Project (First Time Only)

In your Flask project directory:

```bash
# Initialize npm
npm init -y

# Install Tailwind CSS + DaisyUI
npm install -D tailwindcss daisyui @tailwindcss/typography

# Initialize Tailwind
npx tailwindcss init
```

**Configure `tailwind.config.js`:**

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
    require("@tailwindcss/typography"),
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
}
```

**Create `static/src/input.css`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Add to `package.json` scripts:**

```json
{
  "scripts": {
    "build:css": "tailwindcss -i ./static/src/input.css -o ./static/dist/output.css",
    "watch:css": "tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch"
  }
}
```

**Run Tailwind (keep this terminal running):**

```bash
npm run watch:css
```

**Create `templates/base.html`:**

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My App{% endblock %}</title>
    
    <!-- Tailwind CSS + DaisyUI -->
    <link href="{{ url_for('static', filename='dist/output.css') }}" rel="stylesheet">
    
    <!-- Chart.js (if using charts) -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-base-200">
    {% block content %}{% endblock %}
    
    {% block extra_scripts %}{% endblock %}
</body>
</html>
```

### Step 2: Ask AI to Generate UI

Now when working on Flask projects, ask your AI assistant:

#### Example 1: Dashboard
> "Using the KD UI Framework MCP server, create a sales dashboard with sidebar navigation showing revenue, users, orders, and a chart"

AI will use the `create_dashboard` tool and generate beautiful code!

#### Example 2: Login Form
> "Using KD UI Framework, create a login form"

AI will use the `create_form` tool with the login preset!

#### Example 3: Data Table
> "Using KD UI Framework, create a users table with name, email, role, and actions"

AI will use the `create_table` tool!

#### Example 4: Individual Components
> "Add a stat card showing total revenue of $45,231"

AI will use the `add_component` tool!

## 🎯 Available MCP Tools

Your AI assistant now has access to:

1. **`create_dashboard`** - Complete dashboard layouts
   - Parameters: layout, title, theme, components
   - Example: `{"layout": "sidebar", "title": "Dashboard", "components": ["stats", "charts"]}`

2. **`create_form`** - Beautiful forms
   - Parameters: form_type, fields, method, action, inline
   - Presets: "login", "register", "contact"
   - Example: `{"form_type": "login"}`

3. **`create_table`** - Data tables
   - Parameters: columns, features, rows_per_page, striped, hoverable
   - Example: `{"columns": [{"name": "name", "label": "Name"}], "features": ["search", "sort"]}`

4. **`add_component`** - Individual components
   - Types: stat_card, alert, badge, button, card, modal, navbar, sidebar, breadcrumb, tabs, progress, chart_container
   - Example: `{"component_type": "stat_card", "config": {"title": "Revenue", "value": "$45K"}}`

## 🎨 Design System Reference

### Colors
- **Primary**: Blue - Main actions
- **Secondary**: Slate - Supporting elements  
- **Accent**: Purple - Highlights
- **Success**: Green - Positive states
- **Warning**: Amber - Caution
- **Error**: Red - Errors

### Spacing
Use DaisyUI/Tailwind spacing: `p-4`, `m-6`, `gap-4`, etc.
Based on 4px units: 1=4px, 2=8px, 4=16px, 6=24px, 8=32px

### Components
All components are responsive and accessible by default!

## 🔥 Pro Tips

1. **Always mention "KD UI Framework"** when asking AI to generate UI
2. **Start with templates** (dashboard, forms) then customize
3. **Use the design system colors** for consistency
4. **Test on mobile** - all components are responsive
5. **Keep Chart.js CDN** in base template if using charts

## 🐛 Troubleshooting

### Setup Wizard Issues

**Setup wizard fails to install dependencies:**
```bash
# Try installing dependencies manually first
cd mcp-server
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Linux/Mac
pip install -e .
```

**Can't find VS Code settings.json:**
- The wizard auto-detects the standard location
- If you have a custom install, you can create the config manually
- See README.md for manual configuration

**Claude config not found:**
- The wizard will offer to create it for you
- Make sure Claude Desktop or Claude Code CLI is installed

### MCP Server Not Working

**After setup, MCP server still not found:**
```bash
# Restart VS Code completely (close all windows)
# Or restart Claude Desktop

# Verify the configuration was added:
# Windows: Check %APPDATA%\Code\User\settings.json
# Linux: Check ~/.config/Code/User/settings.json
```

### Styles Not Showing

**Components render but no styles:**
```bash
# Make sure Tailwind CSS is running:
npm run watch:css

# Check output.css exists in static/dist/
# Verify base template links to output.css correctly
```

### Components Not Rendering

- Check Jinja2 syntax in templates
- Ensure variables are passed from Flask route
- Open browser console for errors

## 📚 Learn More

- See `README.md` for complete documentation
- See `RESEARCH_AND_OPTIONS.md` for deep dive into options
- See `DECISION_MATRIX.md` for why we chose this approach
- See `FLASK_INTEGRATION_GUIDE.md` for Flask setup details

---

## 🎓 Cross-Platform Notes

The setup wizard automatically handles platform differences:

- **Windows**: Uses `venv\Scripts\python.exe`, `%APPDATA%` paths
- **Linux**: Uses `venv/bin/python`, `~/.config` paths  
- **macOS**: Uses `venv/bin/python`, `~/Library/Application Support` paths

You can use the same repository on different systems! Just run `python setup.py` on each machine.

---

**You're all set! No more ugly AI UIs! 🎉**

Ask your AI assistant to create your first dashboard and see the magic happen!
