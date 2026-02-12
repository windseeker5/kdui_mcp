"""
Generate Navigation Menu Test HTML
Demonstrates the Shadcn-style navigation menu component
"""

import sys
import os

# Add the mcp-server/src to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
mcp_src_path = os.path.join(current_dir, '..', '..', 'mcp-server', 'src')
sys.path.insert(0, mcp_src_path)

from kd_ui_server.tools.component import add_component

# Generate a comprehensive navigation menu with dropdowns
nav_menu = add_component('navigation_menu', {
    'brand': 'KD UI Framework',
    'brand_icon': 'box',
    'show_icons': True,
    'items': [
        {
            'label': 'Home',
            'url': '/',
            'icon': 'home',
            'active': True
        },
        {
            'label': 'Products',
            'url': '#',
            'icon': 'shopping-bag',
            'items': [
                {
                    'label': 'All Products',
                    'url': '/products',
                    'icon': 'package',
                    'description': 'Browse our complete catalog'
                },
                {
                    'label': 'New Arrivals',
                    'url': '/products/new',
                    'icon': 'sparkles',
                    'description': 'Check out what\'s new',
                    'active': False
                },
                {
                    'label': 'Best Sellers',
                    'url': '/products/best',
                    'icon': 'trending-up',
                    'description': 'Our most popular items'
                },
                {
                    'label': 'On Sale',
                    'url': '/products/sale',
                    'icon': 'tag',
                    'description': 'Special offers and discounts'
                }
            ]
        },
        {
            'label': 'Solutions',
            'url': '#',
            'icon': 'layers',
            'items': [
                {
                    'label': 'For Enterprise',
                    'url': '/solutions/enterprise',
                    'icon': 'building',
                    'description': 'Scale with confidence'
                },
                {
                    'label': 'For Startups',
                    'url': '/solutions/startups',
                    'icon': 'rocket',
                    'description': 'Move fast and grow'
                },
                {
                    'label': 'For Developers',
                    'url': '/solutions/developers',
                    'icon': 'code',
                    'description': 'Build amazing products'
                }
            ]
        },
        {
            'label': 'Resources',
            'url': '#',
            'icon': 'book-open',
            'items': [
                {
                    'label': 'Documentation',
                    'url': '/docs',
                    'icon': 'file-text'
                },
                {
                    'label': 'Blog',
                    'url': '/blog',
                    'icon': 'newspaper'
                },
                {
                    'label': 'Guides',
                    'url': '/guides',
                    'icon': 'compass'
                },
                {
                    'label': 'API Reference',
                    'url': '/api',
                    'icon': 'terminal'
                }
            ]
        },
        {
            'label': 'Pricing',
            'url': '/pricing',
            'icon': 'dollar-sign'
        },
        {
            'label': 'Contact',
            'url': '/contact',
            'icon': 'mail'
        }
    ]
})

# Read the HTML template
html_file = os.path.join(current_dir, 'test_nav_menu.html')
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert the navigation menu
html_content = html_content.replace(
    '<div id="nav-menu-container"></div>',
    f'<div id="nav-menu-container">\n{nav_menu}\n</div>'
)

# Write the updated HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Navigation menu generated successfully!")
print("📁 Open test_nav_menu.html in your browser to see the result")
print("\n🧪 Test Features:")
print("  • Hover over 'Products', 'Solutions', or 'Resources' to see dropdowns")
print("  • Check that 'Home' is highlighted (active state)")
print("  • Toggle between light and dark themes")
print("  • Resize browser to test mobile responsiveness")
print("  • All Lucide icons should render correctly")
