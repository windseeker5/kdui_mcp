import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../mcp-server/src'))

from flask import Flask, render_template, render_template_string
from kd_ui_server.tools.component import add_component
from kd_ui_server.tools.table import create_table
from kd_ui_server.tools.form import create_form

app = Flask(__name__)


@app.route('/')
def showcase():
    c = {}

    # --- Badges ---
    c['badge_default'] = add_component("badge", {"text": "Default", "variant": "default"})
    c['badge_secondary'] = add_component("badge", {"text": "Secondary", "variant": "secondary"})
    c['badge_destructive'] = add_component("badge", {"text": "Error", "variant": "destructive"})
    c['badge_outline'] = add_component("badge", {"text": "Outline", "variant": "outline"})
    c['badge_success'] = add_component("badge", {"text": "Success", "variant": "success"})
    c['badge_warning'] = add_component("badge", {"text": "Warning", "variant": "warning"})

    # --- Buttons ---
    c['btn_primary_sm'] = add_component("button", {"text": "Small", "variant": "primary", "size": "sm"})
    c['btn_primary_md'] = add_component("button", {"text": "Primary", "variant": "primary"})
    c['btn_primary_lg'] = add_component("button", {"text": "Large", "variant": "primary", "size": "lg"})
    c['btn_secondary'] = add_component("button", {"text": "Secondary", "variant": "secondary"})
    c['btn_accent'] = add_component("button", {"text": "Accent", "variant": "accent"})
    c['btn_ghost'] = add_component("button", {"text": "Ghost", "variant": "ghost"})
    c['btn_link'] = add_component("button", {"text": "Link", "variant": "link"})

    # --- Alerts ---
    c['alert_info'] = add_component("alert", {"message": "This is an informational message.", "type": "info"})
    c['alert_success'] = add_component("alert", {"message": "Operation completed successfully!", "type": "success"})
    c['alert_warning'] = add_component("alert", {"message": "Please review before continuing.", "type": "warning"})
    c['alert_error'] = add_component("alert", {"message": "Something went wrong. Please try again.", "type": "error"})

    # --- Card ---
    c['card'] = add_component("card", {
        "title": "Card Title",
        "content": "This is a card component with a header, body, and an action button.",
        "actions": True
    })

    # --- Progress ---
    c['progress_default'] = add_component("progress", {"value": 30, "variant": "default", "show_label": True})
    c['progress_success'] = add_component("progress", {"value": 65, "variant": "success", "show_label": True})
    c['progress_warning'] = add_component("progress", {"value": 80, "variant": "warning", "show_label": True})
    c['progress_destructive'] = add_component("progress", {"value": 92, "variant": "destructive", "show_label": True})

    # --- Skeleton ---
    c['skeleton_text'] = add_component("skeleton", {"type": "text", "count": 3})
    c['skeleton_circle'] = add_component("skeleton", {"type": "circle", "size": "64px"})
    c['skeleton_rectangle'] = add_component("skeleton", {"type": "rectangle", "height": "120px"})

    # --- Typography ---
    c['typo_h1'] = add_component("typography", {"type": "h1", "text": "Heading 1"})
    c['typo_h2'] = add_component("typography", {"type": "h2", "text": "Heading 2"})
    c['typo_h3'] = add_component("typography", {"type": "h3", "text": "Heading 3"})
    c['typo_h4'] = add_component("typography", {"type": "h4", "text": "Heading 4"})
    c['typo_lead'] = add_component("typography", {"type": "lead", "text": "This is lead text — larger introductory paragraph copy."})
    c['typo_muted'] = add_component("typography", {"type": "muted", "text": "This is muted/subtle helper text."})
    c['typo_blockquote'] = add_component("typography", {"type": "blockquote", "text": "Design is not just what it looks like and feels like. Design is how it works."})
    c['typo_code'] = add_component("typography", {"type": "code", "text": "npm install kd-ui"})
    c['typo_list'] = add_component("typography", {"type": "list", "items": ["First item", "Second item", "Third item"]})

    # --- Stat Card ---
    c['stat_revenue'] = add_component("stat_card", {
        "title": "Total Revenue",
        "value": "$45,231",
        "trend": "+20.1%",
        "description": "from last month",
    })
    c['stat_users'] = add_component("stat_card", {
        "title": "Active Users",
        "value": "2,350",
        "trend": "+10.5%",
        "description": "from last week",
    })

    # --- Modal ---
    c['modal'] = add_component("modal", {
        "id": "showcase_modal",
        "title": "Confirm Action",
        "content": "Are you sure you want to proceed? This action cannot be undone."
    })

    # --- Tabs ---
    c['tabs'] = add_component("tabs", {"tabs": [
        {"id": "tab_overview", "label": "Overview", "content": "<p class='text-sm py-1'>Overview content goes here.</p>", "active": True},
        {"id": "tab_analytics", "label": "Analytics", "content": "<p class='text-sm py-1'>Analytics data and charts.</p>"},
        {"id": "tab_settings", "label": "Settings", "content": "<p class='text-sm py-1'>Configuration options.</p>"},
    ]})

    # --- Breadcrumb ---
    c['breadcrumb'] = add_component("breadcrumb", {"items": [
        {"label": "Home", "url": "/"},
        {"label": "Components", "url": "/components"},
        {"label": "Breadcrumb"},
    ]})

    # --- Dropdown Menu ---
    c['dropdown'] = add_component("dropdown_menu", {
        "trigger_text": "My Account",
        "trigger_icon": "user",
        "trigger_variant": "outline",
        "items": [
            {"type": "label", "text": "My Account"},
            {"type": "item", "icon": "user", "text": "Profile", "shortcut": "⇧⌘P"},
            {"type": "item", "icon": "settings", "text": "Settings", "shortcut": "⌘S"},
            {"type": "separator"},
            {"type": "item", "icon": "log-out", "text": "Log out", "variant": "destructive"},
        ]
    })

    # --- Navbar ---
    c['navbar'] = add_component("navbar", {
        "brand": "MyApp",
        "items": ["Home", "Products", "Docs", "Blog"],
        "theme_toggle": False
    })

    # --- Sidebar ---
    c['sidebar'] = add_component("sidebar", {
        "brand": "KD UI",
        "brand_icon": "layers",
        "collapsible": True,
        "items": [
            {"icon": "layout-dashboard", "label": "Dashboard", "url": "/", "active": True},
            {"icon": "bar-chart-2", "label": "Analytics", "url": "/analytics"},
            {"icon": "users", "label": "Users", "url": "/users", "badge": {"text": "3", "variant": "destructive"}},
            {"icon": "settings", "label": "Settings", "url": "/settings"},
        ]
    })

    # --- Navigation Menu ---
    c['nav_menu'] = add_component("navigation_menu", {
        "brand": "Acme Co",
        "brand_icon": "building-2",
        "items": [
            {"label": "Home", "url": "/", "active": True},
            {"label": "Products", "url": "#", "items": [
                {"label": "Analytics", "url": "/products/analytics", "description": "Real-time data insights"},
                {"label": "Automation", "url": "/products/automation", "description": "Workflow automation tools"},
            ]},
            {"label": "Docs", "url": "/docs"},
            {"label": "About", "url": "/about"},
        ]
    })

    # --- Landing Page: Hero ---
    c['hero'] = add_component("hero", {
        "title": "Build Amazing Products",
        "subtitle": "The fastest way to create beautiful, responsive web applications with KD UI.",
        "cta_primary": "Get Started",
        "cta_secondary": "Learn More"
    })

    # --- Landing Page: Features ---
    c['features'] = add_component("features", {
        "features": [
            {"icon": "zap", "title": "Lightning Fast", "description": "Optimized for speed and performance out of the box."},
            {"icon": "shield", "title": "Secure by Default", "description": "Built with security best practices from the ground up."},
            {"icon": "code", "title": "Developer Friendly", "description": "Clean APIs, great docs, and an intuitive MCP interface."},
        ]
    })

    # --- Landing Page: Testimonials ---
    c['testimonials'] = add_component("testimonials", {
        "testimonials": [
            {"name": "Sarah Johnson", "role": "CEO", "company": "TechCorp", "quote": "This product has transformed how we build web UIs. Highly recommended!", "avatar": "SJ"},
            {"name": "Mike Chen", "role": "CTO", "company": "StartupXYZ", "quote": "The best investment we've made this year. Amazing results in days.", "avatar": "MC"},
            {"name": "Emily Davis", "role": "Product Manager", "company": "Innovation Labs", "quote": "Intuitive, powerful, and reliable. Everything we needed.", "avatar": "ED"},
        ]
    })

    # --- Landing Page: Pricing ---
    c['pricing'] = add_component("pricing", {
        "plans": [
            {"name": "Basic", "price": "$9", "period": "per month", "features": ["10 Projects", "5GB Storage", "Basic Support"], "popular": False},
            {"name": "Pro", "price": "$29", "period": "per month", "features": ["Unlimited Projects", "50GB Storage", "Priority Support", "Analytics"], "popular": True},
            {"name": "Enterprise", "price": "$99", "period": "per month", "features": ["Everything in Pro", "Custom Integration", "24/7 Support", "SLA"], "popular": False},
        ]
    })

    # --- Landing Page: CTA ---
    c['cta'] = add_component("cta", {
        "title": "Ready to Get Started?",
        "subtitle": "Join thousands of developers building faster with KD UI.",
        "button_text": "Start Free Trial"
    })

    # --- Landing Page: Footer ---
    c['footer'] = add_component("footer", {
        "company_name": "KD UI",
        "description": "Generate beautiful Flask UI components instantly via MCP."
    })

    # --- Chart Container ---
    c['chart'] = add_component("chart_container", {
        "id": "showcaseChart",
        "title": "Monthly Revenue",
        "height": "280px"
    })

    # --- Form (pre-rendered to resolve Jinja2 conditionals) ---
    raw_form = create_form(form_type="login")
    c['form'] = render_template_string(raw_form, csrf_token=None, error=None)

    # --- Table (pre-rendered with mock data) ---
    table_columns = [
        {"name": "name", "label": "Project", "sortable": True},
        {"name": "status", "label": "Status", "type": "badge", "sortable": False},
        {"name": "updated", "label": "Last Updated", "sortable": True},
    ]
    table_data = [
        {"name": "alpha-api",       "status": "Active",   "status_color": "success",     "updated": "2026-02-15"},
        {"name": "beta-dashboard",  "status": "Draft",    "status_color": "warning",     "updated": "2026-02-12"},
        {"name": "gamma-service",   "status": "Archived", "status_color": "error",       "updated": "2026-01-30"},
        {"name": "delta-worker",    "status": "Active",   "status_color": "success",     "updated": "2026-02-10"},
        {"name": "epsilon-jobs",    "status": "Draft",    "status_color": "warning",     "updated": "2026-02-08"},
        {"name": "zeta-gateway",    "status": "Active",   "status_color": "success",     "updated": "2026-02-05"},
        {"name": "eta-scheduler",   "status": "Archived", "status_color": "secondary",   "updated": "2026-01-28"},
    ]
    raw_table = create_table(table_columns, features=["search", "sort", "pagination"], title="Projects", rows_per_page=5)
    c['table'] = render_template_string(raw_table, data=table_data, total_rows=7)

    return render_template('showcase.html', c=c)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
