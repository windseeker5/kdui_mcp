"""Generate test_sidebar.html with actual sidebar component."""
import sys
import os

# Add the mcp-server/src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
mcp_src_path = os.path.join(current_dir, '..', '..', 'mcp-server', 'src')
sys.path.insert(0, mcp_src_path)

from kd_ui_server.tools.component import add_component

# Generate sidebar with comprehensive features
sidebar_html = add_component('sidebar', {
    'brand': 'KD UI Framework',
    'brand_icon': 'box',
    'collapsible': True,
    'items': [
        {
            'icon': 'layout-dashboard',
            'label': 'Dashboard',
            'url': '/dashboard',
            'active': True
        },
        {
            'icon': 'bar-chart',
            'label': 'Analytics',
            'url': '/analytics',
            'badge': {'text': '12', 'variant': 'default'}
        },
        {
            'icon': 'users',
            'label': 'Team',
            'url': '#',
            'submenu': [
                {'label': 'Members', 'url': '/team/members'},
                {'label': 'Invitations', 'url': '/team/invitations'},
                {'label': 'Roles', 'url': '/team/roles', 'active': True}
            ]
        },
        {
            'icon': 'folder',
            'label': 'Projects',
            'url': '#',
            'submenu': [
                {'label': 'All Projects', 'url': '/projects'},
                {'label': 'Archived', 'url': '/projects/archived'}
            ]
        },
        {
            'icon': 'file-text',
            'label': 'Documents',
            'url': '/documents'
        },
        {
            'icon': 'bell',
            'label': 'Notifications',
            'url': '/notifications',
            'badge': {'text': '3', 'variant': 'destructive'}
        },
        {
            'icon': 'settings',
            'label': 'Settings',
            'url': '/settings'
        }
    ]
})

# Read the template file
html_file_path = os.path.join(current_dir, 'test_sidebar.html')
with open(html_file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert sidebar into the placeholder
html_content = html_content.replace(
    '<div id="sidebar-container"></div>',
    sidebar_html
)

# Write the updated file
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Sidebar successfully generated and inserted into test_sidebar.html!")
print(f"📄 File location: examples/first_dashboard/test_sidebar.html")
print("\n🚀 Features included:")
print("  - Collapsible sidebar (click arrow button)")
print("  - 7 menu items with Lucide icons")
print("  - 2 nested submenus (Team, Projects)")
print("  - 2 notification badges (Analytics: 12, Notifications: 3)")
print("  - Active state on Dashboard and Team > Roles")
print("  - Theme-aware styling (test both light and dark themes)")
