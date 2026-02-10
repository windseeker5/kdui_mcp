# KD UI Framework

A powerful MCP (Model Context Protocol) server that generates beautiful Flask/Jinja2 templates with DaisyUI components. Stop letting AI generate ugly UIs - use KD UI Framework to ensure consistent, modern, professional dashboards every time!

## 🎯 Problem Solved

When using AI to build Flask dashboards, you often get:
- ❌ Ugly, inconsistent UIs
- ❌ Outdated design patterns
- ❌ Non-responsive layouts
- ❌ Poor accessibility

With KD UI Framework, you get:
- ✅ Beautiful, modern dashboards
- ✅ Consistent design system
- ✅ Mobile & desktop responsive
- ✅ Accessible components
- ✅ Best practices enforced

## 🚀 Features

### MCP Server Tools

1. **`create_dashboard`** - Generate complete dashboard layouts
   - Sidebar or top navigation
   - Stats cards for KPIs
   - Chart containers
   - Data tables
   - Fully responsive

2. **`create_form`** - Generate beautiful forms
   - Predefined forms (login, register, contact)
   - Custom form builder
   - Validation support
   - Error handling

3. **`create_table`** - Generate data tables
   - Sortable columns
   - Search/filter
   - Pagination
   - Row actions
   - Responsive (cards on mobile)

4. **`add_component`** - Add individual components
   - Stat cards
   - Alerts
   - Badges, buttons, cards
   - Modals, navbars, sidebars
   - Breadcrumbs, tabs, progress bars
   - Chart containers

### Design System

- **Color Palette**: Primary, secondary, accent, semantic colors
- **Typography**: Consistent font sizes and weights
- **Spacing**: 4px-based spacing system
- **Components**: Pre-styled DaisyUI components
- **Best Practices**: Built-in UI/UX guidelines

## 📦 Installation

### 🚀 Quick Start (Recommended)

**One command to set up everything!**

```bash
# Clone the repository
git clone https://github.com/windseeker5/kdui_mcp.git
cd kdui_mcp

# Run the interactive setup wizard
python setup.py
```

The setup wizard will:
- ✅ Create a virtual environment
- ✅ Install all dependencies
- ✅ Configure Cline (VS Code) and/or Claude Desktop/Code CLI
- ✅ Validate the installation
- ✅ Work on Windows, Linux, and macOS

**That's it!** Just restart VS Code or Claude Desktop and you're ready to go! 🎉

---

### 📝 Manual Installation (Advanced)

If you prefer to set up manually:

#### Prerequisites

- Python 3.10+
- Node.js 16+ (for Tailwind CSS in your Flask projects)

#### Step 1: Install the MCP Server

```bash
cd mcp-server

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -e .
```

#### Step 2: Configure in Your AI Tool

**For Cline (VS Code Extension)**

Add to VS Code `settings.json`:

```json
{
  "cline.mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/mcp-server/venv/Scripts/python.exe",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/mcp-server"
    }
  }
}
```

**For Claude Desktop/Code CLI**

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kd-ui": {
      "command": "/absolute/path/to/mcp-server/venv/bin/python",
      "args": ["-m", "kd_ui_server.server"],
      "cwd": "/absolute/path/to/mcp-server"
    }
  }
}
```

---

### Step 3: Set Up Your Flask Project with DaisyUI

```bash
cd your-flask-project

# Initialize Node.js
npm init -y

# Install Tailwind CSS + DaisyUI
npm install -D tailwindcss daisyui

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
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
  },
}
```

**Create `static/src/input.css`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Build CSS:**

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch
```

## 🎨 Usage

### Example 1: Create a Dashboard

**You ask AI:**
> "Create a sales dashboard with sidebar navigation, stats cards for revenue and users, and a chart"

**AI uses MCP tool:**
```json
{
  "tool": "create_dashboard",
  "layout": "sidebar",
  "title": "Sales Dashboard",
  "components": ["stats", "charts"]
}
```

**You get:**
A complete, beautiful Flask template with:
- Responsive sidebar navigation
- Professional stats cards
- Chart containers ready for Chart.js
- Mobile-friendly design

### Example 2: Create a Login Form

**You ask AI:**
> "Create a login form"

**AI uses MCP tool:**
```json
{
  "tool": "create_form",
  "form_type": "login"
}
```

**You get:**
A beautiful, centered login form with:
- Email and password fields
- "Forgot password" link
- Error message display
- Link to registration page

### Example 3: Create a Data Table

**You ask AI:**
> "Create a table to display users with name, email, status, and actions"

**AI uses MCP tool:**
```json
{
  "tool": "create_table",
  "columns": [
    {"name": "name", "label": "Name"},
    {"name": "email", "label": "Email"},
    {"name": "status", "label": "Status", "type": "badge"}
  ],
  "features": ["search", "sort", "pagination", "actions"]
}
```

**You get:**
An interactive table with:
- Search functionality
- Sortable columns
- Pagination
- Edit/Delete actions

## 📁 Project Structure

```
KD UI Framework/
├── RESEARCH_AND_OPTIONS.md      # Framework options guide
├── DECISION_MATRIX.md            # Comparison of approaches
├── FLASK_INTEGRATION_GUIDE.md   # Flask + DaisyUI setup
├── README.md                     # This file
└── mcp-server/                   # MCP Server
    ├── pyproject.toml
    ├── src/
    │   └── kd_ui_server/
    │       ├── __init__.py
    │       ├── server.py         # Main MCP server
    │       ├── design_system.py  # Color palette, typography, etc.
    │       ├── resources.py      # Templates and best practices
    │       └── tools/            # Tool implementations
    │           ├── dashboard.py  # Dashboard generation
    │           ├── form.py       # Form generation
    │           ├── table.py      # Table generation
    │           └── component.py  # Individual components
    └── venv/                     # Virtual environment (created during install)
```

## 🎯 Design System

### Colors

- **Primary**: Blue (#3b82f6) - Main actions, important CTAs
- **Secondary**: Slate (#64748b) - Supporting elements
- **Accent**: Purple (#d946ef) - Highlights, special elements
- **Success**: Green (#10b981) - Positive metrics
- **Warning**: Amber (#f59e0b) - Caution states
- **Error**: Red (#ef4444) - Problems, failures

### Typography

- **Headings**: Inter, Bold (h1: 36px, h2: 30px, h3: 24px)
- **Body**: Inter, Regular (16px)
- **Small**: Inter, Regular (14px)

### Spacing

Based on 4px units: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px

## 🔧 Customization

### Changing Colors

Edit `mcp-server/src/kd_ui_server/design_system.py`:

```python
"daisyui_themes": {
    "light": {
        "primary": "#your-color",  # Change primary color
        ...
    }
}
```

### Adding New Components

1. Add function to `tools/component.py`
2. Register in `add_component()` function
3. Update tool schema in `server.py`

## 📚 Resources

- [DaisyUI Documentation](https://daisyui.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Chart.js](https://www.chartjs.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)

## 🤝 Contributing

This is a personal framework, but feel free to fork and customize for your needs!

## 📄 License

MIT License - Use freely in your projects

## ✨ Tips for Best Results

1. **Always use the MCP tools** - Don't let AI generate UI from scratch
2. **Start with dashboard/form templates** - Then customize as needed
3. **Reference the design system** - Ask AI to use the color palette
4. **Test responsiveness** - Check mobile and desktop views
5. **Keep it simple** - Don't overcomplicate layouts

## 🎓 Learning Resources

See the following guides in this repository:

- **RESEARCH_AND_OPTIONS.md** - Deep dive into UI framework options
- **DECISION_MATRIX.md** - Why we chose this approach
- **FLASK_INTEGRATION_GUIDE.md** - Detailed Flask + DaisyUI setup

## 🚀 Quick Start Example

**Complete workflow:**

1. Install MCP server (see Installation above)
2. Configure in your AI tool
3. In your Flask project, set up Tailwind + DaisyUI
4. Ask AI: "Using the KD UI Framework, create a dashboard for tracking sales with revenue, orders, and customers stats, plus a revenue chart"
5. AI uses `create_dashboard` tool
6. You get a beautiful, responsive dashboard instantly!

No more ugly AI-generated UIs! 🎉

## 🐛 Troubleshooting

### MCP Server Not Found
- Check virtual environment is activated
- Verify Python path in config
- Ensure dependencies are installed (`pip install -e .`)

### Styles Not Applying
- Make sure Tailwind CSS is built (`npm run build` or `--watch`)
- Check `output.css` is linked in your base template
- Verify DaisyUI is in `tailwind.config.js` plugins

### Components Not Rendering
- Check Jinja2 syntax in templates
- Verify variables are passed from Flask route
- Inspect browser console for errors

---

**Made with ❤️ to solve the "ugly AI UI" problem**
