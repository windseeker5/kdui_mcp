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

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/windseeker5/kdui_mcp.git
cd kdui_mcp
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
venv\Scripts\activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### Step 4: Configure Proxy (Corporate Networks Only)

If you're behind a corporate proxy, set these environment variables:

**PowerShell:**
```powershell
$env:HTTP_PROXY="http://your-proxy:port"
$env:HTTPS_PROXY="http://your-proxy:port"
```

**CMD:**
```cmd
set HTTP_PROXY=http://your-proxy:port
set HTTPS_PROXY=http://your-proxy:port
```

**Linux/macOS:**
```bash
export HTTP_PROXY="http://your-proxy:port"
export HTTPS_PROXY="http://your-proxy:port"
```

### Step 5: Install Dependencies

```bash
pip install -e mcp-server
```

### Step 6: Run Setup Wizard

```bash
python setup.py
```

The setup wizard will configure the MCP server in your AI tool (Cline or Claude Desktop).

### Step 7: Restart Your AI Tool

- **Cline**: Reload VS Code window
- **Claude Desktop**: Restart the application

**That's it! You're ready to go! 🎉**

---

## 🚀 Your First Dashboard in 60 Seconds

After completing the setup, let's create a beautiful dashboard to see the framework in action!

### Quick Demo

1. **Navigate to the example:**
   ```bash
   cd examples/first_dashboard
   pip install flask
   python app.py
   ```

2. **Open your browser:**
   Visit **http://localhost:5001** to see a beautiful sales dashboard with:
   - 📊 Stats cards (Revenue, Orders, Customers, Conversion Rate)
   - 📈 Revenue trend chart
   - 📋 Recent orders table
   - 🎨 Fully responsive design

### Create Your Own Dashboard (Hello World!)

**The Simple Prompt - Copy & Paste This:**

```
Using the create_dashboard MCP tool, generate a sales dashboard with:
- Sidebar layout
- Title: "Sales Dashboard"
- Components: stats, charts, table
```

**Or ask naturally:**

```
Create a sales dashboard with sidebar navigation, stat cards for revenue/users/sessions/conversion, 
revenue trend chart, and a recent orders table
```

**What the MCP tool generates:**

The tool automatically creates a **Shadcn-quality** Flask template with:

✅ **Modern Lucide Icons** - Clean, professional icons throughout
✅ **Shadcn Color Palette** - Blue-600 primary, subtle gray backgrounds
✅ **Beautiful Stat Cards** - White cards with subtle borders, generous padding (p-6), and shadow-sm
✅ **Clean Sidebar** - Gray-50 background, active state highlighting, smooth hover transitions  
✅ **Professional Table** - Horizontal borders only, hover states, color-coded status badges
✅ **Chart Containers** - Icon headers, proper spacing
✅ **Inter Font** - Modern, clean typography
✅ **Fully Responsive** - Mobile drawer, desktop sidebar, responsive grid

**The Result: Production-Ready, Shadcn-Quality UI**

![Sales Dashboard](examples/first_dashboard/screenshot.png)

No hand-coding needed - the MCP tool generates everything! 🎉

---

## 🎨 Usage Examples

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

---

## 📁 Project Structure

```
KD UI Framework/
├── README.md                     # This file
├── setup.py                      # MCP configuration wizard
├── SETUP_STEPS.md               # Detailed setup instructions
├── QUICK_START.md               # Quick reference guide
├── RESEARCH_AND_OPTIONS.md      # Framework options guide
├── DECISION_MATRIX.md           # Comparison of approaches
├── FLASK_INTEGRATION_GUIDE.md   # Flask + DaisyUI setup
├── examples/                    # Example projects
│   └── first_dashboard/         # Sales dashboard demo
│       ├── app.py
│       ├── templates/
│       └── README.md
└── mcp-server/                  # MCP Server
    ├── pyproject.toml
    ├── src/
    │   └── kd_ui_server/
    │       ├── server.py        # Main MCP server
    │       ├── design_system.py # Color palette, typography
    │       ├── resources.py     # Templates and best practices
    │       └── tools/           # Tool implementations
    │           ├── dashboard.py
    │           ├── form.py
    │           ├── table.py
    │           └── component.py
    └── venv/                    # Virtual environment (you create this)
```

---

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

---

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

---

## 🐛 Troubleshooting

### Proxy Errors
If you see "Cannot connect to proxy" or "getaddrinfo failed" errors during installation:
1. Configure your proxy settings (see Step 4)
2. Run `pip install -e mcp-server` again

### Virtual Environment Not Activated
Make sure you see `(venv)` at the beginning of your terminal prompt. If not:
- Windows: Run `venv\Scripts\activate`
- Linux/macOS: Run `source venv/bin/activate`

### MCP Server Not Found in Cline/Claude
1. Check that the setup wizard completed successfully
2. Restart VS Code or Claude Desktop
3. Verify the configuration file was updated (setup wizard shows the location)

### Dependencies Not Installing
If `pip install -e mcp-server` fails:
1. Make sure your virtual environment is activated
2. Check your internet connection or proxy settings
3. Try updating pip: `python -m pip install --upgrade pip`

---

## 📚 Resources

- [DaisyUI Documentation](https://daisyui.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Chart.js](https://www.chartjs.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)

---

## ✨ Tips for Best Results

1. **Always use the MCP tools** - Don't let AI generate UI from scratch
2. **Start with dashboard/form templates** - Then customize as needed
3. **Reference the design system** - Ask AI to use the color palette
4. **Test responsiveness** - Check mobile and desktop views
5. **Keep it simple** - Don't overcomplicate layouts

---

## 🎓 Learning Resources

See the following guides in this repository:

- **RESEARCH_AND_OPTIONS.md** - Deep dive into UI framework options
- **DECISION_MATRIX.md** - Why we chose this approach
- **FLASK_INTEGRATION_GUIDE.md** - Detailed Flask + DaisyUI setup
- **SETUP_STEPS.md** - Detailed step-by-step setup guide

---

## 🤝 Contributing

This is a personal framework, but feel free to fork and customize for your needs!

---

## 📄 License

MIT License - Use freely in your projects

---

**Made with ❤️ to solve the "ugly AI UI" problem**
