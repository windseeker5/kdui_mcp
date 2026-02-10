"""Component generation tool for individual UI elements."""


def add_component(component_type, config=None):
    """
    Generate individual UI components.
    
    Args:
        component_type: Type of component to generate
        config: Component-specific configuration
    
    Returns:
        Component template string
    """
    if config is None:
        config = {}
    
    components = {
        "stat_card": _generate_stat_card,
        "alert": _generate_alert,
        "badge": _generate_badge,
        "button": _generate_button,
        "card": _generate_card,
        "modal": _generate_modal,
        "navbar": _generate_navbar,
        "sidebar": _generate_sidebar,
        "breadcrumb": _generate_breadcrumb,
        "tabs": _generate_tabs,
        "progress": _generate_progress,
        "chart_container": _generate_chart_container,
        # Landing page components
        "hero": _generate_hero,
        "features": _generate_features,
        "testimonials": _generate_testimonials,
        "pricing": _generate_pricing,
        "cta": _generate_cta,
        "footer": _generate_footer,
    }
    
    if component_type in components:
        return components[component_type](config)
    else:
        return f"<!-- Unknown component type: {component_type} -->"


def _generate_stat_card(config):
    """Generate a stat card component."""
    title = config.get("title", "Stat Title")
    value = config.get("value", "0")
    description = config.get("description", "Description")
    color = config.get("color", "primary")
    
    return f'''
<div class="stats shadow">
  <div class="stat">
    <div class="stat-title">{title}</div>
    <div class="stat-value text-{color}">{value}</div>
    <div class="stat-desc">{description}</div>
  </div>
</div>
'''


def _generate_alert(config):
    """Generate an alert component."""
    message = config.get("message", "This is an alert message")
    alert_type = config.get("type", "info")  # info, success, warning, error
    
    icons = {
        "info": '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        "success": '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        "warning": '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>',
        "error": '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
    }
    
    return f'''
<div class="alert alert-{alert_type}">
  {icons.get(alert_type, icons['info'])}
  <span>{message}</span>
</div>
'''


def _generate_badge(config):
    """Generate a badge component."""
    text = config.get("text", "Badge")
    color = config.get("color", "primary")
    size = config.get("size", "md")  # sm, md, lg
    
    size_class = f"badge-{size}" if size != "md" else ""
    
    return f'<span class="badge badge-{color} {size_class}">{text}</span>'


def _generate_button(config):
    """Generate a button component."""
    text = config.get("text", "Button")
    variant = config.get("variant", "primary")  # primary, secondary, accent, ghost, link
    size = config.get("size", "md")  # sm, md, lg
    
    size_class = f"btn-{size}" if size != "md" else ""
    
    return f'<button class="btn btn-{variant} {size_class}">{text}</button>'


def _generate_card(config):
    """Generate a card component."""
    title = config.get("title", "Card Title")
    content = config.get("content", "Card content goes here")
    has_actions = config.get("actions", False)
    
    card_html = '''
<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">''' + title + '''</h2>
    <p>''' + content + '''</p>
'''
    
    if has_actions:
        card_html += '''    <div class="card-actions justify-end">
      <button class="btn btn-primary">Action</button>
    </div>
'''
    
    card_html += '''  </div>
</div>
'''
    return card_html


def _generate_modal(config):
    """Generate a modal component."""
    modal_id = config.get("id", "my_modal")
    title = config.get("title", "Modal Title")
    content = config.get("content", "Modal content goes here")
    
    return f'''
<!-- Modal trigger button -->
<label for="{modal_id}" class="btn">Open Modal</label>

<!-- Modal -->
<input type="checkbox" id="{modal_id}" class="modal-toggle" />
<div class="modal">
  <div class="modal-box">
    <h3 class="font-bold text-lg">{title}</h3>
    <p class="py-4">{content}</p>
    <div class="modal-action">
      <label for="{modal_id}" class="btn">Close</label>
    </div>
  </div>
</div>
'''


def _generate_navbar(config):
    """Generate a navbar component."""
    brand = config.get("brand", "Brand")
    items = config.get("items", ["Home", "About", "Contact"])
    
    nav_html = '''
<div class="navbar bg-base-200 shadow-md">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl">''' + brand + '''</a>
  </div>
  <div class="flex-none">
    <ul class="menu menu-horizontal px-1">
'''
    
    for item in items:
        nav_html += f'      <li><a>{item}</a></li>\n'
    
    nav_html += '''    </ul>
  </div>
</div>
'''
    return nav_html


def _generate_sidebar(config):
    """Generate a sidebar component."""
    items = config.get("items", [
        {"label": "Dashboard", "url": "/dashboard", "active": True},
        {"label": "Analytics", "url": "/analytics"},
        {"label": "Settings", "url": "/settings"},
    ])
    
    sidebar_html = '''
<ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
'''
    
    for item in items:
        active_class = "active" if item.get("active", False) else ""
        sidebar_html += f'''  <li><a href="{item['url']}" class="{active_class}">{item['label']}</a></li>\n'''
    
    sidebar_html += '</ul>\n'
    return sidebar_html


def _generate_breadcrumb(config):
    """Generate a breadcrumb component."""
    items = config.get("items", [
        {"label": "Home", "url": "/"},
        {"label": "Documents", "url": "/documents"},
        {"label": "Current Page"},
    ])
    
    breadcrumb_html = '''
<div class="text-sm breadcrumbs">
  <ul>
'''
    
    for item in items:
        if "url" in item:
            breadcrumb_html += f'''    <li><a href="{item['url']}">{item['label']}</a></li>\n'''
        else:
            breadcrumb_html += f'''    <li>{item['label']}</li>\n'''
    
    breadcrumb_html += '''  </ul>
</div>
'''
    return breadcrumb_html


def _generate_tabs(config):
    """Generate tabs component."""
    tabs = config.get("tabs", [
        {"id": "tab1", "label": "Tab 1", "content": "Content 1", "active": True},
        {"id": "tab2", "label": "Tab 2", "content": "Content 2"},
        {"id": "tab3", "label": "Tab 3", "content": "Content 3"},
    ])
    
    tabs_html = '''
<div role="tablist" class="tabs tabs-lifted">
'''
    
    for tab in tabs:
        checked = "checked" if tab.get("active", False) else ""
        tabs_html += f'''  <input type="radio" name="my_tabs" role="tab" class="tab" aria-label="{tab['label']}" {checked} />
  <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6">
    {tab['content']}
  </div>
'''
    
    tabs_html += '</div>\n'
    return tabs_html


def _generate_progress(config):
    """Generate progress bar component."""
    value = config.get("value", 50)
    max_value = config.get("max", 100)
    color = config.get("color", "primary")
    
    return f'<progress class="progress progress-{color} w-full" value="{value}" max="{max_value}"></progress>'


def _generate_chart_container(config):
    """Generate a container for Chart.js charts."""
    chart_id = config.get("id", "myChart")
    title = config.get("title", "Chart")
    height = config.get("height", "400px")
    
    return f'''
<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">{title}</h2>
    <div style="height: {height};">
      <canvas id="{chart_id}"></canvas>
    </div>
  </div>
</div>

<script>
  // Initialize chart when document is ready
  document.addEventListener('DOMContentLoaded', function() {{
    const ctx = document.getElementById('{chart_id}');
    if (ctx) {{
      new Chart(ctx, {{
        type: 'line',
        data: {{
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [{{
            label: 'Dataset',
            data: [12, 19, 3, 5, 2, 3],
            borderColor: 'rgb(59, 130, 246)',
            tension: 0.1
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false
        }}
      }});
    }}
  }});
</script>
'''
