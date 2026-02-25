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
        "navigation_menu": _generate_navigation_menu,
        "breadcrumb": _generate_breadcrumb,
        "tabs": _generate_tabs,
        "progress": _generate_progress,
        "skeleton": _generate_skeleton,
        "typography": _generate_typography,
        "dropdown_menu": _generate_dropdown_menu,
        "chart_container": _generate_chart_container,
        # Landing page components
        "hero": _generate_hero,
        "features": _generate_features,
        "testimonials": _generate_testimonials,
        "pricing": _generate_pricing,
        "cta": _generate_cta,
        "footer": _generate_footer,
        # Theme toggle
        "theme_toggle": _generate_theme_toggle,
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
<div style="background:var(--b1, white); border:1px solid oklch(var(--b3)); border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.06); padding:1.5rem;">
  <p class="text-sm text-base-content/60 mb-1">{title}</p>
  <p class="text-2xl font-semibold text-{color}">{value}</p>
  <p class="text-xs text-base-content/40 mt-1">{description}</p>
</div>
'''


def _generate_alert(config):
    """Generate a toast flash notification component."""
    import uuid
    message = config.get("message", "This is an alert message")
    alert_type = config.get("type", "info")  # info, success, warning, error
    duration = config.get("duration", 4000)   # ms, 0 = persistent
    position = config.get("position", "top-right")
    dismissable = config.get("dismissable", True)

    alert_id = f"kd-alert-{uuid.uuid4().hex[:8]}"

    position_styles = {
        "top-right":    "top:16px; right:16px;",
        "top-left":     "top:16px; left:16px;",
        "top-center":   "top:16px; left:0; right:0; margin:0 auto; max-width:400px;",
        "bottom-right": "bottom:16px; right:16px;",
        "bottom-left":  "bottom:16px; left:16px;",
        "bottom-center":"bottom:16px; left:0; right:0; margin:0 auto; max-width:400px;",
    }
    pos_style = position_styles.get(position, position_styles["top-right"])
    container_id = f"kd-toast-container-{position}"

    icons = {
        "info":    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        "success": '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        "warning": '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>',
        "error":   '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
    }

    return f'''<div id="{alert_id}" style="display:none" aria-hidden="true"></div>
<script>
(function() {{
  // Register global helpers only once
  if (!window.kdDismissAlert) {{
    window.kdDismissAlert = function(el) {{
      el.style.opacity = '0';
      el.style.transform = 'translateX(20px)';
      setTimeout(function() {{ el.remove(); }}, 300);
    }};
  }}

  if (!window.kdShowAlert) {{
    window.kdShowAlert = function(type, message, opts) {{
      opts = opts || {{}};
      var duration   = (opts.duration !== undefined) ? opts.duration : 4000;
      var position   = opts.position || 'top-right';
      var dismissable = (opts.dismissable !== undefined) ? opts.dismissable : true;

      var posStyles = {{
        'top-right':    'top:16px; right:16px;',
        'top-left':     'top:16px; left:16px;',
        'top-center':   'top:16px; left:0; right:0; margin:0 auto; max-width:400px;',
        'bottom-right': 'bottom:16px; right:16px;',
        'bottom-left':  'bottom:16px; left:16px;',
        'bottom-center':'bottom:16px; left:0; right:0; margin:0 auto; max-width:400px;'
      }};

      var icons = {{
        'info':    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        'success': '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        'warning': '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>',
        'error':   '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>'
      }};

      var containerId = 'kd-toast-container-' + position;
      var container = document.getElementById(containerId);
      if (!container) {{
        container = document.createElement('div');
        container.id = containerId;
        container.style.cssText = 'position:fixed; z-index:9999; pointer-events:none; display:flex; flex-direction:column; gap:8px; width:360px; ' + (posStyles[position] || posStyles['top-right']);
        document.body.appendChild(container);
      }}

      var alert = document.createElement('div');
      alert.className = 'alert alert-' + type + ' shadow-lg';
      alert.style.cssText = 'pointer-events:auto; opacity:0; transform:translateX(20px); transition:opacity 300ms ease, transform 300ms ease; border-radius:6px;';

      var icon = icons[type] || icons['info'];
      var closeBtn = dismissable
        ? '<button onclick="kdDismissAlert(this.closest(\\'.alert\\'))" style="margin-left:auto; background:none; border:none; cursor:pointer; padding:0; line-height:1; font-size:1.25rem; opacity:0.7;" aria-label="Close">&times;</button>'
        : '';
      alert.innerHTML = icon + '<span style="flex:1">' + message + '</span>' + closeBtn;

      container.appendChild(alert);

      // Animate in
      requestAnimationFrame(function() {{
        requestAnimationFrame(function() {{
          alert.style.opacity = '1';
          alert.style.transform = 'translateX(0)';
        }});
      }});

      if (duration > 0) {{
        setTimeout(function() {{ window.kdDismissAlert(alert); }}, duration);
      }}
    }};
  }}

  // Show this alert immediately
  window.kdShowAlert('{alert_type}', '{message}', {{
    duration: {duration},
    position: '{position}',
    dismissable: {'true' if dismissable else 'false'}
  }});
}})();
</script>'''


def _generate_badge(config):
    """Generate a Shadcn-style badge component.
    
    Variants:
    - default: Blue/primary color
    - secondary: Gray/muted
    - destructive: Red/error
    - outline: Border only
    - success: Green
    - warning: Yellow/amber
    """
    text = config.get("text", "Badge")
    variant = config.get("variant", "default")  # default, secondary, destructive, outline, success, warning
    
    # Shadcn-inspired badge styling
    base_classes = "inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors"
    
    variant_classes = {
        "default": "bg-blue-600 text-white hover:bg-blue-700",
        "secondary": "bg-base-200 text-base-content hover:bg-base-300",
        "destructive": "bg-red-600 text-white hover:bg-red-700",
        "outline": "border border-base-300 text-base-content hover:bg-base-200",
        "success": "bg-green-600 text-white hover:bg-green-700",
        "warning": "bg-amber-500 text-white hover:bg-amber-600"
    }
    
    variant_class = variant_classes.get(variant, variant_classes["default"])
    
    return f'<span class="{base_classes} {variant_class}">{text}</span>'


def _generate_button(config):
    """Generate a button component."""
    text = config.get("text", "Button")
    variant = config.get("variant", "primary")  # primary, secondary, accent, ghost, link
    size = config.get("size", "md")  # sm, md, lg

    variant_styles = {
        "primary":   "background:#2563EB; color:#fff; border:1px solid #2563EB;",
        "secondary": "background:#6B7280; color:#fff; border:1px solid #6B7280;",
        "accent":    "background:#059669; color:#fff; border:1px solid #059669;",
        "ghost":     "background:transparent; color:#374151; border:1px solid #D1D5DB;",
        "link":      "background:transparent; color:#2563EB; border:none; box-shadow:none; text-decoration:underline;",
    }

    size_styles = {
        "sm": "height:32px; min-height:0; padding:0 12px; font-size:0.8rem;",
        "md": "height:36px; min-height:0; padding:0 16px; font-size:0.875rem;",
        "lg": "height:44px; min-height:0; padding:0 20px; font-size:0.9375rem;",
    }

    base_style = "border-radius:4px; font-weight:500; white-space:nowrap;"
    v_style = variant_styles.get(variant, variant_styles["primary"])
    s_style = size_styles.get(size, size_styles["md"])

    hover_attrs = ""
    if variant == "ghost":
        hover_attrs = ' onmouseover="this.style.background=\'#F3F4F6\'" onmouseout="this.style.background=\'transparent\'"'

    return f'<button class="btn" style="{base_style} {v_style} {s_style}"{hover_attrs}>{text}</button>'


def _generate_card(config):
    """Generate a card component."""
    title = config.get("title", "Card Title")
    content = config.get("content", "Card content goes here")
    has_actions = config.get("actions", False)
    
    card_html = '''
<div style="background:var(--b1, white); border:1px solid oklch(var(--b3)); border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.06); overflow:hidden;">
  <div class="p-6">
    <h2 class="text-base font-semibold mb-2">''' + title + '''</h2>
    <p>''' + content + '''</p>
'''

    if has_actions:
        card_html += '''    <div class="flex justify-end mt-4">
      <button class="btn" style="height:36px; min-height:0; padding:0 16px; font-size:0.875rem; border-radius:4px; font-weight:500; background:#2563EB; color:#fff; border:1px solid #2563EB; white-space:nowrap;">Action</button>
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
<label for="{modal_id}" class="btn" style="height:36px; min-height:0; padding:0 16px; font-size:0.875rem; border-radius:4px; font-weight:500; background:#2563EB; color:#fff; border:1px solid #2563EB; white-space:nowrap;">Open Modal</label>

<!-- Modal -->
<input type="checkbox" id="{modal_id}" class="modal-toggle" />
<div class="modal">
  <div class="modal-box" style="border-radius:8px;">
    <h3 class="font-bold text-lg">{title}</h3>
    <p class="py-4">{content}</p>
    <div class="modal-action">
      <label for="{modal_id}" class="btn" style="height:36px; min-height:0; padding:0 16px; font-size:0.875rem; border-radius:4px; font-weight:500; background:transparent; color:#374151; border:1px solid #D1D5DB; white-space:nowrap;" onmouseover="this.style.background='#F3F4F6'" onmouseout="this.style.background='transparent'">Close</label>
    </div>
  </div>
</div>
'''


def _generate_navbar(config):
    """Generate a navbar component."""
    brand = config.get("brand", "Brand")
    items = config.get("items", ["Home", "About", "Contact"])
    theme_toggle = config.get("theme_toggle", True)  # Include theme toggle by default
    
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
'''
    
    # Add theme toggle if enabled
    if theme_toggle:
        nav_html += '''    <button id="theme-toggle" class="btn btn-ghost btn-circle ml-2" aria-label="Toggle theme">
      <i data-lucide="sun" class="w-5 h-5 hidden dark:block"></i>
      <i data-lucide="moon" class="w-5 h-5 block dark:hidden"></i>
    </button>
'''
    
    nav_html += '''  </div>
</div>
'''
    return nav_html


def _generate_sidebar(config):
    """Generate an enhanced Shadcn-style sidebar component.
    
    Features:
    - Collapsible sidebar
    - Icons for menu items (Lucide icons)
    - Nested menu items (submenu support)
    - Active state highlighting
    - Smooth animations
    - Theme-aware styling
    """
    items = config.get("items", [
        {"icon": "layout-dashboard", "label": "Dashboard", "url": "/dashboard", "active": True},
        {"icon": "bar-chart", "label": "Analytics", "url": "/analytics"},
        {"icon": "settings", "label": "Settings", "url": "/settings"},
    ])
    collapsible = config.get("collapsible", True)
    brand = config.get("brand", "App")
    brand_icon = config.get("brand_icon", "box")
    
    # Generate unique ID for this sidebar
    import random
    sidebar_id = f"sidebar-{random.randint(1000, 9999)}"
    
    # Build menu items
    menu_items_html = ""
    for item in items:
        icon = item.get("icon", "circle")
        label = item.get("label", "Menu Item")
        url = item.get("url", "#")
        active = item.get("active", False)
        badge = item.get("badge", None)
        submenu = item.get("submenu", [])
        
        # Active state styling
        active_class = "bg-base-200 text-primary" if active else "text-base-content hover:bg-base-200"
        
        # Badge HTML if present
        badge_html = ""
        if badge:
            badge_variant = badge.get("variant", "default")
            badge_text = badge.get("text", "")
            badge_colors = {
                "default": "bg-blue-600 text-white",
                "success": "bg-green-600 text-white",
                "warning": "bg-amber-500 text-white",
                "destructive": "bg-red-600 text-white"
            }
            badge_class = badge_colors.get(badge_variant, badge_colors["default"])
            badge_html = f'<span class="ml-auto rounded-full px-2 py-0.5 text-xs font-semibold {badge_class}">{badge_text}</span>'
        
        if submenu:
            # Menu item with submenu
            submenu_id = f"submenu-{random.randint(1000, 9999)}"
            menu_items_html += f'''
    <div class="mb-1">
      <button id="{submenu_id}-trigger" class="flex w-full items-center gap-3 rounded-md px-3 py-2 text-sm font-medium {active_class} transition-colors">
        <i data-lucide="{icon}" class="w-5 h-5 flex-shrink-0"></i>
        <span class="sidebar-label">{label}</span>
        <i data-lucide="chevron-down" class="w-4 h-4 ml-auto sidebar-label transition-transform" id="{submenu_id}-chevron"></i>
      </button>
      <div id="{submenu_id}-content" class="ml-8 mt-1 space-y-1 hidden">
'''
            for sub_item in submenu:
                sub_label = sub_item.get("label", "Submenu")
                sub_url = sub_item.get("url", "#")
                sub_active = sub_item.get("active", False)
                sub_active_class = "text-primary font-medium" if sub_active else "text-base-content/60 hover:text-base-content"
                
                menu_items_html += f'''
        <a href="{sub_url}" class="block rounded-md px-3 py-2 text-sm {sub_active_class} transition-colors">
          {sub_label}
        </a>
'''
            menu_items_html += '''
      </div>
    </div>
'''
        else:
            # Regular menu item
            menu_items_html += f'''
    <a href="{url}" class="flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium {active_class} transition-colors mb-1">
      <i data-lucide="{icon}" class="w-5 h-5 flex-shrink-0"></i>
      <span class="sidebar-label">{label}</span>
      {badge_html}
    </a>
'''
    
    # Collapse button HTML
    collapse_button = ""
    if collapsible:
        collapse_button = f'''
    <button id="{sidebar_id}-toggle" class="absolute top-4 -right-3 z-10 flex h-6 w-6 items-center justify-center rounded-full border border-base-300 bg-base-100 shadow-md hover:bg-base-200 transition-colors">
      <i data-lucide="chevron-left" class="w-4 h-4 text-base-content/60" id="{sidebar_id}-chevron"></i>
    </button>
'''
    
    sidebar_html = f'''
<!-- Enhanced Sidebar -->
<aside id="{sidebar_id}" class="relative flex h-screen w-64 flex-col border-r border-base-300 bg-base-100 transition-all duration-300 ease-in-out">
  {collapse_button}

  <!-- Brand -->
  <div class="flex h-16 items-center gap-3 border-b border-base-300 px-4">
    <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-blue-600">
      <i data-lucide="{brand_icon}" class="w-6 h-6 text-white"></i>
    </div>
    <span class="sidebar-label text-lg font-semibold text-base-content">{brand}</span>
  </div>

  <!-- Navigation -->
  <nav class="flex-1 overflow-y-auto p-4">
    {menu_items_html}
  </nav>

  <!-- Footer (optional user section) -->
  <div class="border-t border-base-300 p-4">
    <div class="flex items-center gap-3">
      <div class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-base-200">
        <i data-lucide="user" class="w-5 h-5 text-base-content/60"></i>
      </div>
      <div class="sidebar-label flex-1 overflow-hidden">
        <p class="text-sm font-medium text-base-content truncate">User Name</p>
        <p class="text-xs text-base-content/50 truncate">user@example.com</p>
      </div>
    </div>
  </div>
</aside>

<script>
(function() {{
  const sidebar = document.getElementById('{sidebar_id}');
  const toggleBtn = document.getElementById('{sidebar_id}-toggle');
  const chevron = document.getElementById('{sidebar_id}-chevron');
  
  // Collapse/expand functionality
  if (toggleBtn && sidebar && chevron) {{
    toggleBtn.addEventListener('click', function() {{
      sidebar.classList.toggle('w-64');
      sidebar.classList.toggle('w-16');
      
      // Hide/show labels
      const labels = sidebar.querySelectorAll('.sidebar-label');
      labels.forEach(label => {{
        label.classList.toggle('hidden');
      }});
      
      // Rotate chevron
      chevron.classList.toggle('rotate-180');
    }});
  }}
  
  // Submenu toggle functionality
  document.querySelectorAll('[id$="-trigger"]').forEach(trigger => {{
    const triggerId = trigger.id;
    const submenuId = triggerId.replace('-trigger', '-content');
    const chevronId = triggerId.replace('-trigger', '-chevron');
    const submenu = document.getElementById(submenuId);
    const chevron = document.getElementById(chevronId);
    
    if (trigger && submenu && chevron) {{
      trigger.addEventListener('click', function(e) {{
        e.preventDefault();
        submenu.classList.toggle('hidden');
        chevron.classList.toggle('rotate-180');
      }});
    }}
  }});
  
  // Initialize Lucide icons
  if (typeof lucide !== 'undefined') {{
    lucide.createIcons();
  }}
}})();
</script>
'''
    
    return sidebar_html


def _generate_navigation_menu(config):
    """Generate a Shadcn-style horizontal navigation menu component.
    
    Features:
    - Horizontal navigation bar with dropdown menus
    - Multi-level navigation support
    - Icons for menu items (Lucide icons)
    - Active state highlighting
    - Hover dropdowns with smooth animations
    - Theme-aware styling
    - Mobile responsive (optional)
    """
    items = config.get("items", [
        {"label": "Home", "url": "/", "active": True},
        {"label": "Products", "url": "#", "items": [
            {"label": "All Products", "url": "/products"},
            {"label": "New Arrivals", "url": "/products/new"},
            {"label": "Best Sellers", "url": "/products/best"}
        ]},
        {"label": "About", "url": "/about"},
        {"label": "Contact", "url": "/contact"}
    ])
    brand = config.get("brand", "Brand")
    brand_icon = config.get("brand_icon", "box")
    show_icons = config.get("show_icons", True)
    
    # Generate unique ID for this nav menu
    import random
    nav_id = f"nav-menu-{random.randint(1000, 9999)}"
    
    # Build navigation items
    nav_items_html = ""
    for item in items:
        label = item.get("label", "Menu")
        url = item.get("url", "#")
        icon = item.get("icon", "")
        active = item.get("active", False)
        subitems = item.get("items", [])
        
        # Active state styling
        active_class = "text-primary font-semibold" if active else "text-base-content hover:text-primary"
        
        # Icon HTML if present
        icon_html = f'<i data-lucide="{icon}" class="w-4 h-4"></i>' if icon and show_icons else ""
        
        if subitems:
            # Navigation item with dropdown
            dropdown_id = f"nav-dropdown-{random.randint(1000, 9999)}"
            nav_items_html += f'''
      <div class="relative group">
        <button id="{dropdown_id}-trigger" class="flex items-center gap-2 px-4 py-2 text-sm font-medium {active_class} transition-colors rounded-md hover:bg-base-200">
          {icon_html}
          <span>{label}</span>
          <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-hover:rotate-180"></i>
        </button>
        
        <!-- Dropdown Menu -->
        <div id="{dropdown_id}-content" class="absolute left-0 top-full mt-2 w-56 origin-top-left rounded-md border border-base-300 bg-base-100 shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
          <div class="p-1">
'''
            for subitem in subitems:
                sub_label = subitem.get("label", "Submenu")
                sub_url = subitem.get("url", "#")
                sub_icon = subitem.get("icon", "")
                sub_description = subitem.get("description", "")
                sub_active = subitem.get("active", False)
                
                sub_active_class = "bg-base-200 text-primary" if sub_active else "hover:bg-base-200"
                sub_icon_html = f'<i data-lucide="{sub_icon}" class="w-4 h-4 text-base-content/50"></i>' if sub_icon and show_icons else ""
                
                if sub_description:
                    # Item with description
                    nav_items_html += f'''
            <a href="{sub_url}" class="flex items-start gap-3 rounded-md px-3 py-2 text-sm {sub_active_class} transition-colors">
              {sub_icon_html}
              <div class="flex-1">
                <div class="font-medium text-base-content">{sub_label}</div>
                <div class="text-xs text-base-content/50">{sub_description}</div>
              </div>
            </a>
'''
                else:
                    # Simple item
                    nav_items_html += f'''
            <a href="{sub_url}" class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-base-content {sub_active_class} transition-colors">
              {sub_icon_html}
              <span>{sub_label}</span>
            </a>
'''
            
            nav_items_html += '''
          </div>
        </div>
      </div>
'''
        else:
            # Simple navigation link
            nav_items_html += f'''
      <a href="{url}" class="flex items-center gap-2 px-4 py-2 text-sm font-medium {active_class} transition-colors rounded-md hover:bg-base-200">
        {icon_html}
        <span>{label}</span>
      </a>
'''
    
    return f'''
<!-- Shadcn-style Navigation Menu -->
<nav id="{nav_id}" class="border-b border-base-300 bg-base-100">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="flex h-16 items-center justify-between">
      <!-- Brand -->
      <div class="flex items-center gap-3">
        <div class="flex h-8 w-8 items-center justify-center rounded-md bg-blue-600">
          <i data-lucide="{brand_icon}" class="w-5 h-5 text-white"></i>
        </div>
        <span class="text-lg font-semibold text-base-content">{brand}</span>
      </div>
      
      <!-- Navigation Items -->
      <div class="hidden md:flex items-center gap-1">
        {nav_items_html}
      </div>
      
      <!-- Mobile Menu Button -->
      <button id="{nav_id}-mobile-toggle" class="md:hidden rounded-md p-2 text-base-content hover:bg-base-200">
        <i data-lucide="menu" class="w-6 h-6"></i>
      </button>
    </div>
  </div>
  
  <!-- Mobile Menu (hidden by default) -->
  <div id="{nav_id}-mobile-menu" class="hidden md:hidden border-t border-base-300">
    <div class="space-y-1 px-4 py-3">
      {nav_items_html.replace("relative group", "").replace("group-hover:opacity-100 group-hover:visible", "").replace("opacity-0 invisible", "hidden")}
    </div>
  </div>
</nav>

<script>
(function() {{
  // Mobile menu toggle
  const mobileToggle = document.getElementById('{nav_id}-mobile-toggle');
  const mobileMenu = document.getElementById('{nav_id}-mobile-menu');
  
  if (mobileToggle && mobileMenu) {{
    mobileToggle.addEventListener('click', function() {{
      mobileMenu.classList.toggle('hidden');
    }});
  }}
  
  // Initialize Lucide icons
  if (typeof lucide !== 'undefined') {{
    lucide.createIcons();
  }}
}})();
</script>
'''


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
  <div role="tabpanel" class="tab-content bg-base-100 border-base-300 p-6" style="border-radius:0 0 8px 8px;">
    {tab['content']}
  </div>
'''
    
    tabs_html += '</div>\n'
    return tabs_html


def _generate_progress(config):
    """Generate a Shadcn-style progress bar component.
    
    Features:
    - Horizontal progress bar
    - Configurable value (0-100%)
    - Smooth animations
    - Theme-aware colors
    """
    value = config.get("value", 50)
    max_value = config.get("max", 100)
    variant = config.get("variant", "default")  # default, success, warning, destructive
    show_label = config.get("show_label", False)
    
    # Calculate percentage
    percentage = (value / max_value) * 100
    
    # Shadcn-inspired progress bar styling
    container_classes = "relative h-2 w-full overflow-hidden rounded-full bg-base-200"
    
    variant_classes = {
        "default": "bg-blue-600",
        "success": "bg-green-600",
        "warning": "bg-amber-500",
        "destructive": "bg-red-600"
    }
    
    bar_class = variant_classes.get(variant, variant_classes["default"])
    
    progress_html = f'''<div class="{container_classes}">
  <div class="h-full {bar_class} transition-all duration-300 ease-in-out" style="width: {percentage}%"></div>
</div>'''
    
    # Add label if requested
    if show_label:
        progress_html = f'''<div class="space-y-2">
  <div class="flex items-center justify-between text-sm">
    <span class="text-base-content/70">Progress</span>
    <span class="text-base-content/70 font-medium">{int(percentage)}%</span>
  </div>
  {progress_html}
</div>'''
    
    return progress_html


def _generate_skeleton(config):
    """Generate a Shadcn-style skeleton loader component.
    
    Types:
    - text: Text line placeholder
    - circle: Avatar/circular placeholder
    - rectangle: Card/rectangular placeholder
    """
    skeleton_type = config.get("type", "text")  # text, circle, rectangle
    width = config.get("width", "100%")
    height = config.get("height", "auto")
    count = config.get("count", 1)  # Number of skeleton elements
    
    # Base skeleton classes with shimmer animation
    base_classes = "animate-pulse bg-base-200"
    
    skeletons_html = ""
    
    if skeleton_type == "text":
        # Text line skeletons
        for i in range(count):
            # Vary width for more natural look
            if count > 1 and i == count - 1:
                # Last line is shorter
                line_width = "80%" if width == "100%" else width
            else:
                line_width = width
            
            skeletons_html += f'<div class="{base_classes} h-4 rounded" style="width: {line_width};"></div>\n'
            if i < count - 1:
                skeletons_html += '<div class="h-2"></div>\n'  # Spacing between lines
        
        return f'<div class="space-y-2">\n{skeletons_html}</div>'
    
    elif skeleton_type == "circle":
        # Circular skeleton (for avatars)
        size = config.get("size", "48px")  # Default avatar size
        return f'<div class="{base_classes} rounded-full" style="width: {size}; height: {size};"></div>'
    
    elif skeleton_type == "rectangle":
        # Rectangular skeleton (for cards, images)
        rect_height = height if height != "auto" else "200px"
        return f'<div class="{base_classes} rounded-lg" style="width: {width}; height: {rect_height};"></div>'
    
    else:
        # Default to text
        return f'<div class="{base_classes} h-4 rounded" style="width: {width};"></div>'


def _generate_typography(config):
    """Generate Shadcn-style typography elements.
    
    Types:
    - h1, h2, h3, h4: Headings
    - p: Paragraph
    - lead: Large intro text
    - large: Larger text
    - small: Smaller text
    - muted: Muted/subtle text
    - blockquote: Quote block
    - code: Inline code
    - list: Unordered or ordered list
    """
    typo_type = config.get("type", "p")
    text = config.get("text", "")
    items = config.get("items", [])  # For lists
    
    # Shadcn typography styles
    typography_styles = {
        "h1": f'<h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">{text}</h1>',
        "h2": f'<h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">{text}</h2>',
        "h3": f'<h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">{text}</h3>',
        "h4": f'<h4 class="scroll-m-20 text-xl font-semibold tracking-tight">{text}</h4>',
        "p": f'<p class="leading-7 [&:not(:first-child)]:mt-6">{text}</p>',
        "lead": f'<p class="text-xl text-base-content/70">{text}</p>',
        "large": f'<div class="text-lg font-semibold">{text}</div>',
        "small": f'<small class="text-sm font-medium leading-none">{text}</small>',
        "muted": f'<p class="text-sm text-base-content/50">{text}</p>',
        "blockquote": f'<blockquote class="mt-6 border-l-2 border-base-300 pl-6 italic text-base-content/70">{text}</blockquote>',
        "code": f'<code class="relative rounded bg-base-200 px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">{text}</code>',
    }
    
    # Handle lists separately
    if typo_type == "list":
        list_type = config.get("list_type", "ul")  # ul or ol
        list_html = f'<{list_type} class="my-6 ml-6 list-disc [&>li]:mt-2">\n'
        for item in items:
            list_html += f'  <li>{item}</li>\n'
        list_html += f'</{list_type}>'
        return list_html
    
    return typography_styles.get(typo_type, f'<p>{text}</p>')


def _generate_dropdown_menu(config):
    """Generate a dropdown menu component.

    The menu is rendered at document.body level with position:fixed so it
    escapes any overflow container, stacking context, or scroll wrapper —
    works correctly inside tables, modals, sidebars, and drawers.

    Features:
    - position:fixed via getBoundingClientRect() — never clipped
    - Auto-flips upward when near the bottom of the viewport
    - whitespace-nowrap on all items — no unexpected line wraps
    - DaisyUI-compatible color tokens (text-error, bg-base-200, etc.)
    - Closes on click-outside, Escape key, and window scroll
    """
    trigger_text = config.get("trigger_text", "Open Menu")
    trigger_icon = config.get("trigger_icon", "chevron-down")
    trigger_variant = config.get("trigger_variant", "outline")  # outline | ghost | default
    items = config.get("items", [
        {"type": "label", "text": "My Account"},
        {"type": "item", "icon": "user", "text": "Profile", "shortcut": "⇧⌘P"},
        {"type": "item", "icon": "settings", "text": "Settings", "shortcut": "⌘S"},
        {"type": "separator"},
        {"type": "item", "icon": "log-out", "text": "Log out", "variant": "destructive"}
    ])
    align = config.get("align", "end")  # start | center | end
    menu_width = config.get("width", 220)  # px

    import random
    dropdown_id = f"dropdown-{random.randint(1000, 9999)}"

    # Trigger button styles
    button_variants = {
        "outline": "inline-flex items-center justify-center gap-2 rounded-md border border-base-300 bg-base-100 px-4 py-2 text-sm font-medium text-base-content shadow-sm hover:bg-base-200 focus:outline-none",
        "ghost":   "inline-flex items-center justify-center gap-2 rounded-md px-4 py-2 text-sm font-medium text-base-content hover:bg-base-200 focus:outline-none",
        "default": "inline-flex items-center justify-center gap-2 rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-content shadow-sm hover:opacity-90 focus:outline-none",
    }
    button_class = button_variants.get(trigger_variant, button_variants["outline"])

    # Horizontal alignment JS expression (evaluated at open time)
    align_js = {
        "start":  "rect.left",
        "center": "rect.left + rect.width / 2 - menuWidth / 2",
        "end":    "rect.right - menuWidth",
    }.get(align, "rect.right - menuWidth")

    # Build menu items HTML
    menu_items_html = ""
    for item in items:
        item_type = item.get("type", "item")

        if item_type == "label":
            text = item.get("text", "Label")
            menu_items_html += f'<div class="px-2 py-1.5 text-xs font-semibold text-base-content/50 whitespace-nowrap">{text}</div>\n'

        elif item_type == "separator":
            menu_items_html += '<div class="my-1 h-px bg-base-300"></div>\n'

        elif item_type == "item":
            icon     = item.get("icon", "")
            text     = item.get("text", "Item")
            shortcut = item.get("shortcut", "")
            variant  = item.get("variant", "default")
            disabled = item.get("disabled", False)

            if disabled:
                item_class = "text-base-content/30 cursor-not-allowed opacity-50"
            elif variant == "destructive":
                item_class = "text-error hover:bg-error/10"
            else:
                item_class = "text-base-content hover:bg-base-200"

            icon_html     = f'<i data-lucide="{icon}" class="w-4 h-4 flex-shrink-0"></i>' if icon else ""
            shortcut_html = f'<span class="ml-auto text-xs text-base-content/40 pl-4 whitespace-nowrap">{shortcut}</span>' if shortcut else ""
            disabled_attr = "disabled" if disabled else ""

            menu_items_html += (
                f'<button class="flex w-full items-center gap-2 rounded-sm px-2 py-1.5 text-sm '
                f'{item_class} transition-colors focus:outline-none whitespace-nowrap" {disabled_attr}>'
                f'{icon_html}<span>{text}</span>{shortcut_html}</button>\n'
            )

    return f'''<!-- Dropdown Menu -->
<div class="inline-block">
  <button id="{dropdown_id}-trigger" class="{button_class}" aria-expanded="false" aria-haspopup="true">
    <span>{trigger_text}</span>
    <i data-lucide="{trigger_icon}" class="w-4 h-4"></i>
  </button>
</div>

<script>
(function() {{
  const trigger = document.getElementById('{dropdown_id}-trigger');
  if (!trigger) return;

  const menuWidth = {menu_width};

  // Render menu at body level — escapes all overflow/stacking contexts
  const menu = document.createElement('div');
  menu.id = '{dropdown_id}-menu';
  menu.style.cssText = 'position:fixed;z-index:9999;display:none;width:' + menuWidth + 'px;';
  menu.className = 'rounded-md border border-base-300 bg-base-100 p-1 shadow-lg';
  menu.setAttribute('role', 'menu');
  menu.innerHTML = `{menu_items_html}`;
  document.body.appendChild(menu);

  let isOpen = false;

  function openMenu() {{
    const rect      = trigger.getBoundingClientRect();
    const menuH     = menu.scrollHeight || 120;
    const spaceBelow = window.innerHeight - rect.bottom;
    const top  = spaceBelow > menuH + 8 ? rect.bottom + 4 : rect.top - menuH - 4;
    const left = Math.max(8, Math.min({align_js}, window.innerWidth - menuWidth - 8));
    menu.style.top     = top + 'px';
    menu.style.left    = left + 'px';
    menu.style.display = 'block';
    trigger.setAttribute('aria-expanded', 'true');
    isOpen = true;
    if (typeof lucide !== 'undefined') lucide.createIcons();
  }}

  function closeMenu() {{
    menu.style.display = 'none';
    trigger.setAttribute('aria-expanded', 'false');
    isOpen = false;
  }}

  trigger.addEventListener('click', function() {{
    isOpen ? closeMenu() : openMenu();
  }});

  document.addEventListener('click', function(e) {{
    if (!trigger.contains(e.target) && !menu.contains(e.target)) closeMenu();
  }});

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') closeMenu();
  }});

  // Close on page scroll (not inner element scroll)
  window.addEventListener('scroll', closeMenu);
}})();
</script>
'''


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


def _generate_hero(config):
    """Generate a hero section with Shadcn styling."""
    title = config.get("title", "Build Amazing Products")
    subtitle = config.get("subtitle", "The fastest way to create beautiful, responsive web applications")
    cta_primary = config.get("cta_primary", "Get Started")
    cta_secondary = config.get("cta_secondary", "Learn More")
    
    return f'''
<!-- Hero Section -->
<section class="bg-gradient-to-br from-primary/10 to-base-100 py-20 px-4">
  <div class="max-w-6xl mx-auto text-center">
    <h1 class="text-5xl md:text-6xl font-bold text-base-content mb-6">
      {title}
    </h1>
    <p class="text-xl text-base-content/60 mb-8 max-w-2xl mx-auto">
      {subtitle}
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
      <button class="btn btn-primary btn-lg gap-2">
        <i data-lucide="rocket" class="w-5 h-5"></i>
        {cta_primary}
      </button>
      <button class="btn btn-outline btn-lg gap-2">
        <i data-lucide="book-open" class="w-5 h-5"></i>
        {cta_secondary}
      </button>
    </div>
  </div>
</section>
'''


def _generate_features(config):
    """Generate a features section with Shadcn styling."""
    features = config.get("features", [
        {
            "icon": "zap",
            "title": "Lightning Fast",
            "description": "Optimized for speed and performance"
        },
        {
            "icon": "shield",
            "title": "Secure by Default",
            "description": "Built with security best practices"
        },
        {
            "icon": "code",
            "title": "Developer Friendly",
            "description": "Clean APIs and great documentation"
        }
    ])
    
    features_html = '''
<!-- Features Section -->
<section class="py-20 px-4 bg-base-100">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-base-content mb-4">Features</h2>
      <p class="text-xl text-base-content/60">Everything you need to build amazing products</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
    
    for feature in features:
        icon = feature.get("icon", "check")
        title = feature.get("title", "Feature")
        description = feature.get("description", "Description")
        
        features_html += f'''
      <div class="bg-base-100 border border-base-300 rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow duration-200">
        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
          <i data-lucide="{icon}" class="w-6 h-6 text-blue-600"></i>
        </div>
        <h3 class="text-xl font-semibold text-base-content mb-2">{title}</h3>
        <p class="text-base-content/60">{description}</p>
      </div>
'''
    
    features_html += '''
    </div>
  </div>
</section>
'''
    return features_html


def _generate_testimonials(config):
    """Generate a testimonials section with Shadcn styling."""
    testimonials = config.get("testimonials", [
        {
            "name": "Sarah Johnson",
            "role": "CEO",
            "company": "TechCorp",
            "quote": "This product has transformed how we work. Highly recommended!",
            "avatar": "SJ"
        },
        {
            "name": "Mike Chen",
            "role": "CTO",
            "company": "StartupXYZ",
            "quote": "The best investment we've made this year. Amazing results!",
            "avatar": "MC"
        },
        {
            "name": "Emily Davis",
            "role": "Product Manager",
            "company": "Innovation Labs",
            "quote": "Intuitive, powerful, and reliable. Everything we needed.",
            "avatar": "ED"
        }
    ])
    
    testimonials_html = '''
<!-- Testimonials Section -->
<section class="py-20 px-4 bg-base-200">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-base-content mb-4">What Our Customers Say</h2>
      <p class="text-xl text-base-content/60">Trusted by teams worldwide</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
    
    for testimonial in testimonials:
        name = testimonial.get("name", "Customer Name")
        role = testimonial.get("role", "Role")
        company = testimonial.get("company", "Company")
        quote = testimonial.get("quote", "Great product!")
        avatar = testimonial.get("avatar", "XX")
        
        testimonials_html += f'''
      <div class="bg-base-100 border border-base-300 rounded-lg p-6 shadow-sm">
        <div class="flex items-center gap-1 mb-4">
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
        </div>
        <p class="text-base-content/70 mb-6 italic">"{quote}"</p>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 bg-blue-600 rounded-full flex items-center justify-center text-white font-semibold">
            {avatar}
          </div>
          <div>
            <p class="font-semibold text-base-content">{name}</p>
            <p class="text-sm text-base-content/60">{role} at {company}</p>
          </div>
        </div>
      </div>
'''
    
    testimonials_html += '''
    </div>
  </div>
</section>
'''
    return testimonials_html


def _generate_pricing(config):
    """Generate a pricing section with Shadcn styling."""
    plans = config.get("plans", [
        {
            "name": "Basic",
            "price": "$9",
            "period": "per month",
            "features": ["10 Projects", "5GB Storage", "Basic Support"],
            "popular": False
        },
        {
            "name": "Pro",
            "price": "$29",
            "period": "per month",
            "features": ["Unlimited Projects", "50GB Storage", "Priority Support", "Advanced Analytics"],
            "popular": True
        },
        {
            "name": "Enterprise",
            "price": "$99",
            "period": "per month",
            "features": ["Unlimited Everything", "Custom Integration", "24/7 Support", "SLA Guarantee"],
            "popular": False
        }
    ])
    
    pricing_html = '''
<!-- Pricing Section -->
<section class="py-20 px-4 bg-base-100">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-base-content mb-4">Simple, Transparent Pricing</h2>
      <p class="text-xl text-base-content/60">Choose the plan that's right for you</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
'''
    
    for plan in plans:
        name = plan.get("name", "Plan")
        price = plan.get("price", "$0")
        period = plan.get("period", "per month")
        features = plan.get("features", [])
        popular = plan.get("popular", False)
        
        border_class = "border-blue-600 shadow-lg" if popular else "border-base-300"
        badge = '''
        <div class="absolute -top-4 left-1/2 -translate-x-1/2">
          <span class="bg-blue-600 text-white px-4 py-1 rounded-full text-sm font-semibold">Popular</span>
        </div>
''' if popular else ""
        
        pricing_html += f'''
      <div class="relative bg-base-100 border-2 {border_class} rounded-lg p-8 hover:shadow-xl transition-shadow duration-200">
        {badge}
        <h3 class="text-2xl font-bold text-base-content mb-2">{name}</h3>
        <div class="mb-6">
          <span class="text-4xl font-bold text-base-content">{price}</span>
          <span class="text-base-content/60">/{period}</span>
        </div>
        <ul class="space-y-3 mb-8">
'''
        
        for feature in features:
            pricing_html += f'''
          <li class="flex items-center gap-2 text-base-content/80">
            <i data-lucide="check" class="w-5 h-5 text-green-600"></i>
            <span>{feature}</span>
          </li>
'''
        
        btn_class = "btn-primary" if popular else "btn-outline"
        pricing_html += f'''
        </ul>
        <button class="btn {btn_class} w-full">Get Started</button>
      </div>
'''
    
    pricing_html += '''
    </div>
  </div>
</section>
'''
    return pricing_html


def _generate_cta(config):
    """Generate a call-to-action section with Shadcn styling."""
    title = config.get("title", "Ready to Get Started?")
    subtitle = config.get("subtitle", "Join thousands of satisfied customers today")
    button_text = config.get("button_text", "Start Free Trial")
    
    return f'''
<!-- CTA Section -->
<section class="py-20 px-4 bg-gradient-to-r from-blue-600 to-blue-700">
  <div class="max-w-4xl mx-auto text-center">
    <h2 class="text-4xl md:text-5xl font-bold text-white mb-4">
      {title}
    </h2>
    <p class="text-xl text-blue-100 mb-8">
      {subtitle}
    </p>
    <button class="btn btn-lg bg-white text-blue-700 hover:bg-blue-50 border-0 gap-2">
      <i data-lucide="arrow-right" class="w-5 h-5"></i>
      {button_text}
    </button>
  </div>
</section>
'''


def _generate_footer(config):
    """Generate a footer section with Shadcn styling."""
    company_name = config.get("company_name", "Your Company")
    description = config.get("description", "Building amazing products since 2024")
    
    return f'''
<!-- Footer -->
<footer class="bg-neutral text-neutral-content py-12 px-4">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
      <!-- Company Info -->
      <div class="col-span-1 md:col-span-2">
        <h3 class="text-2xl font-bold mb-3">{company_name}</h3>
        <p class="opacity-70 mb-4">{description}</p>
        <div class="flex gap-4 opacity-70">
          <a href="#" class="hover:opacity-100 transition-opacity">
            <i data-lucide="twitter" class="w-5 h-5"></i>
          </a>
          <a href="#" class="hover:opacity-100 transition-opacity">
            <i data-lucide="github" class="w-5 h-5"></i>
          </a>
          <a href="#" class="hover:opacity-100 transition-opacity">
            <i data-lucide="linkedin" class="w-5 h-5"></i>
          </a>
        </div>
      </div>
      
      <!-- Product Links -->
      <div>
        <h4 class="font-semibold mb-3">Product</h4>
        <ul class="space-y-2 opacity-70">
          <li><a href="#" class="hover:opacity-100 transition-opacity">Features</a></li>
          <li><a href="#" class="hover:opacity-100 transition-opacity">Pricing</a></li>
          <li><a href="#" class="hover:opacity-100 transition-opacity">Documentation</a></li>
        </ul>
      </div>

      <!-- Company Links -->
      <div>
        <h4 class="font-semibold mb-3">Company</h4>
        <ul class="space-y-2 opacity-70">
          <li><a href="#" class="hover:opacity-100 transition-opacity">About</a></li>
          <li><a href="#" class="hover:opacity-100 transition-opacity">Blog</a></li>
          <li><a href="#" class="hover:opacity-100 transition-opacity">Contact</a></li>
        </ul>
      </div>
    </div>

    <!-- Copyright -->
    <div class="border-t border-neutral-content/20 pt-8 text-center opacity-60">
      <p>&copy; 2024 {company_name}. All rights reserved.</p>
    </div>
  </div>
</footer>

<script>
  // Initialize Lucide icons
  if (typeof lucide !== 'undefined') {{
    lucide.createIcons();
  }}
</script>
'''


def _generate_theme_toggle(config):
    """Generate a theme toggle button with Shadcn styling."""
    position = config.get("position", "navbar")  # navbar, standalone, floating
    
    if position == "standalone":
        # Standalone toggle button
        return '''
<!-- Theme Toggle Button -->
<button id="theme-toggle" class="btn btn-ghost btn-circle" aria-label="Toggle theme">
  <i data-lucide="sun" class="w-5 h-5 hidden dark:block"></i>
  <i data-lucide="moon" class="w-5 h-5 block dark:hidden"></i>
</button>

<script>
  // Theme toggle functionality
  (function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    
    // Check for saved theme preference or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    
    // Toggle theme on click
    themeToggle.addEventListener('click', function() {
      const currentTheme = html.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Reinitialize Lucide icons to update the icon
      if (typeof lucide !== 'undefined') {
        lucide.createIcons();
      }
    });
    
    // Initialize icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  })();
</script>
'''
    elif position == "floating":
        # Floating toggle button (bottom-right)
        return '''
<!-- Floating Theme Toggle -->
<div class="fixed bottom-6 right-6 z-50">
  <button id="theme-toggle" class="btn btn-circle btn-primary shadow-lg" aria-label="Toggle theme">
    <i data-lucide="sun" class="w-5 h-5 hidden dark:block"></i>
    <i data-lucide="moon" class="w-5 h-5 block dark:hidden"></i>
  </button>
</div>

<script>
  // Theme toggle functionality
  (function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    
    // Check for saved theme preference or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    
    // Toggle theme on click
    themeToggle.addEventListener('click', function() {
      const currentTheme = html.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Reinitialize Lucide icons to update the icon
      if (typeof lucide !== 'undefined') {
        lucide.createIcons();
      }
    });
    
    // Initialize icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  })();
</script>
'''
    else:
        # Default: navbar position (inline, no script - script should be in head)
        return '''
<button id="theme-toggle" class="btn btn-ghost btn-circle" aria-label="Toggle theme">
  <i data-lucide="sun" class="w-5 h-5 hidden dark:block"></i>
  <i data-lucide="moon" class="w-5 h-5 block dark:hidden"></i>
</button>
'''
