# First Dashboard Example

This is a simple sales dashboard example that demonstrates the power of the KD UI Framework MCP server.

## What's Included

- **Stats Cards**: Revenue, Orders, Customers, Conversion Rate
- **Revenue Chart**: 7-day trend visualization
- **Quick Insights**: Alert-style notifications
- **Recent Orders Table**: Sortable data table with status badges

## How to Run

### Prerequisites

Make sure you have Flask installed:

```bash
pip install flask
```

### Run the App

```bash
python app.py
```

The dashboard will be available at: **http://localhost:5001**

## About This Example

This dashboard was created to showcase what you can generate using the KD UI Framework MCP tools:

- **`create_dashboard`** - Generated the overall layout
- **`add_component`** - Added individual stat cards
- **Mock data** - All data is hardcoded for demonstration

## Customize It

Feel free to modify:
- `app.py` - Change the mock data or add real data sources
- `templates/dashboard.html` - Adjust the layout and styling
- `templates/base.html` - Change the theme or add custom CSS

## No Build Step Required!

Notice that we're using CDN links for:
- Tailwind CSS
- DaisyUI
- Chart.js
- Font Awesome

This means **no npm install, no build process** - just run and go! 🚀

For production apps, you'd want to use a proper Tailwind build process, but for quick demos and prototypes, CDN is perfect.
