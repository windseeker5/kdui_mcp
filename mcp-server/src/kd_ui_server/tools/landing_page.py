"""Landing page generation tool."""

from .component import add_component


def create_landing_page(title="KD UI Framework", company_name="Your Company"):
    """
    Generate a complete landing page with all sections.
    
    Args:
        title: Page title
        company_name: Company name for branding
    
    Returns:
        Complete HTML template string
    """
    
    # Generate hero section
    hero = add_component("hero", {
        "title": "Build Beautiful Dashboards in Minutes",
        "subtitle": "KD UI Framework provides professional, Shadcn-quality UI components for Flask applications. Stop letting AI generate ugly UIs.",
        "cta_primary": "Get Started Free",
        "cta_secondary": "View Documentation"
    })
    
    # Generate features section
    features = add_component("features", {
        "features": [
            {
                "icon": "zap",
                "title": "Lightning Fast Setup",
                "description": "Install via MCP and start generating beautiful UIs in under 60 seconds"
            },
            {
                "icon": "palette",
                "title": "Shadcn-Quality Design",
                "description": "Modern, clean components with Lucide icons and professional styling"
            },
            {
                "icon": "code-2",
                "title": "AI-Powered",
                "description": "Integrated with Cline and Claude Desktop via Model Context Protocol"
            },
            {
                "icon": "layout-dashboard",
                "title": "Complete Dashboards",
                "description": "Generate full dashboards with stats, charts, tables, and navigation"
            },
            {
                "icon": "smartphone",
                "title": "Fully Responsive",
                "description": "Mobile-first design that looks great on all screen sizes"
            },
            {
                "icon": "shield-check",
                "title": "Best Practices",
                "description": "Built-in UI/UX guidelines and accessibility standards"
            }
        ]
    })
    
    # Generate testimonials section
    testimonials = add_component("testimonials", {
        "testimonials": [
            {
                "name": "Sarah Johnson",
                "role": "Full Stack Developer",
                "company": "TechStartup Inc",
                "quote": "KD UI Framework saved me hours of UI development. The Shadcn-quality output is incredible!",
                "avatar": "SJ"
            },
            {
                "name": "Mike Chen",
                "role": "Product Manager",
                "company": "Innovation Labs",
                "quote": "Finally, AI-generated UIs that actually look professional. Game changer for our team!",
                "avatar": "MC"
            },
            {
                "name": "Emily Davis",
                "role": "CTO",
                "company": "DataFlow Systems",
                "quote": "The MCP integration with Cline is seamless. We're building dashboards 10x faster now.",
                "avatar": "ED"
            }
        ]
    })
    
    # Generate pricing section
    pricing = add_component("pricing", {
        "plans": [
            {
                "name": "Open Source",
                "price": "$0",
                "period": "forever",
                "features": [
                    "All UI Components",
                    "Dashboard Generator",
                    "Form Builder",
                    "Community Support"
                ],
                "popular": False
            },
            {
                "name": "Pro",
                "price": "$29",
                "period": "per month",
                "features": [
                    "Everything in Open Source",
                    "Custom Themes",
                    "Priority Support",
                    "Advanced Components",
                    "Commercial License"
                ],
                "popular": True
            },
            {
                "name": "Enterprise",
                "price": "Custom",
                "period": "contact us",
                "features": [
                    "Everything in Pro",
                    "Dedicated Support",
                    "Custom Development",
                    "SLA Guarantee",
                    "Training & Onboarding"
                ],
                "popular": False
            }
        ]
    })
    
    # Generate CTA section
    cta = add_component("cta", {
        "title": "Ready to Build Beautiful UIs?",
        "subtitle": "Join developers worldwide who are creating professional dashboards with KD UI Framework",
        "button_text": "Start Building Now"
    })
    
    # Generate footer
    footer = add_component("footer", {
        "company_name": company_name,
        "description": "Professional UI components for Flask applications. Built with love for developers who care about design."
    })
    
    # Generate navbar
    navbar = add_component("navbar", {
        "brand": company_name,
        "items": ["Features", "Pricing", "Docs", "GitHub"]
    })
    
    # Combine all sections into a complete HTML page
    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    
    <!-- Inter Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS + DaisyUI -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.19/dist/full.min.css" rel="stylesheet" type="text/css">
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
    
    <style>
        body {{
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }}
    </style>
    
    <script>
        // DaisyUI theme configuration
        tailwind.config = {{
            daisyui: {{
                themes: [{{
                    light: {{
                        "primary": "#2563eb",      // Blue-600
                        "secondary": "#64748b",    // Slate-500
                        "accent": "#8b5cf6",       // Purple-500
                        "neutral": "#1f2937",      // Gray-800
                        "base-100": "#ffffff",     // White
                        "base-200": "#f9fafb",     // Gray-50
                        "base-300": "#f3f4f6",     // Gray-100
                    }}
                }}]
            }}
        }};
    </script>
</head>
<body class="bg-white">
    {navbar}
    {hero}
    {features}
    {testimonials}
    {pricing}
    {cta}
    {footer}
</body>
</html>
'''
    
    return html
