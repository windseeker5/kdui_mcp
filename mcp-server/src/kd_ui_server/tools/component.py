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
        "skeleton": _generate_skeleton,
        "typography": _generate_typography,
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
        "secondary": "bg-gray-100 text-gray-900 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-100",
        "destructive": "bg-red-600 text-white hover:bg-red-700",
        "outline": "border border-gray-300 text-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:text-gray-300 dark:hover:bg-gray-800",
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
    container_classes = "relative h-2 w-full overflow-hidden rounded-full bg-gray-200 dark:bg-gray-800"
    
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
    <span class="text-gray-700 dark:text-gray-300">Progress</span>
    <span class="text-gray-700 dark:text-gray-300 font-medium">{int(percentage)}%</span>
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
    base_classes = "animate-pulse bg-gray-200 dark:bg-gray-700"
    
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
        "lead": f'<p class="text-xl text-gray-700 dark:text-gray-300">{text}</p>',
        "large": f'<div class="text-lg font-semibold">{text}</div>',
        "small": f'<small class="text-sm font-medium leading-none">{text}</small>',
        "muted": f'<p class="text-sm text-gray-500 dark:text-gray-400">{text}</p>',
        "blockquote": f'<blockquote class="mt-6 border-l-2 border-gray-300 pl-6 italic text-gray-700 dark:text-gray-300">{text}</blockquote>',
        "code": f'<code class="relative rounded bg-gray-100 dark:bg-gray-800 px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">{text}</code>',
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
<section class="bg-gradient-to-br from-blue-50 to-white py-20 px-4">
  <div class="max-w-6xl mx-auto text-center">
    <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
      {title}
    </h1>
    <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
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
<section class="py-20 px-4 bg-white">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-gray-900 mb-4">Features</h2>
      <p class="text-xl text-gray-600">Everything you need to build amazing products</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
    
    for feature in features:
        icon = feature.get("icon", "check")
        title = feature.get("title", "Feature")
        description = feature.get("description", "Description")
        
        features_html += f'''
      <div class="bg-white border border-gray-200 rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow duration-200">
        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
          <i data-lucide="{icon}" class="w-6 h-6 text-blue-600"></i>
        </div>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-gray-600">{description}</p>
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
<section class="py-20 px-4 bg-gray-50">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-gray-900 mb-4">What Our Customers Say</h2>
      <p class="text-xl text-gray-600">Trusted by teams worldwide</p>
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
      <div class="bg-white border border-gray-200 rounded-lg p-6 shadow-sm">
        <div class="flex items-center gap-1 mb-4">
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
          <i data-lucide="star" class="w-4 h-4 fill-yellow-400 text-yellow-400"></i>
        </div>
        <p class="text-gray-700 mb-6 italic">"{quote}"</p>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 bg-blue-600 rounded-full flex items-center justify-center text-white font-semibold">
            {avatar}
          </div>
          <div>
            <p class="font-semibold text-gray-900">{name}</p>
            <p class="text-sm text-gray-600">{role} at {company}</p>
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
<section class="py-20 px-4 bg-white">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold text-gray-900 mb-4">Simple, Transparent Pricing</h2>
      <p class="text-xl text-gray-600">Choose the plan that's right for you</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
'''
    
    for plan in plans:
        name = plan.get("name", "Plan")
        price = plan.get("price", "$0")
        period = plan.get("period", "per month")
        features = plan.get("features", [])
        popular = plan.get("popular", False)
        
        border_class = "border-blue-600 shadow-lg" if popular else "border-gray-200"
        badge = '''
        <div class="absolute -top-4 left-1/2 -translate-x-1/2">
          <span class="bg-blue-600 text-white px-4 py-1 rounded-full text-sm font-semibold">Popular</span>
        </div>
''' if popular else ""
        
        pricing_html += f'''
      <div class="relative bg-white border-2 {border_class} rounded-lg p-8 hover:shadow-xl transition-shadow duration-200">
        {badge}
        <h3 class="text-2xl font-bold text-gray-900 mb-2">{name}</h3>
        <div class="mb-6">
          <span class="text-4xl font-bold text-gray-900">{price}</span>
          <span class="text-gray-600">/{period}</span>
        </div>
        <ul class="space-y-3 mb-8">
'''
        
        for feature in features:
            pricing_html += f'''
          <li class="flex items-center gap-2 text-gray-700">
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
    <button class="btn btn-lg bg-white text-blue-600 hover:bg-gray-100 border-0 gap-2">
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
<footer class="bg-gray-900 text-gray-300 py-12 px-4">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
      <!-- Company Info -->
      <div class="col-span-1 md:col-span-2">
        <h3 class="text-2xl font-bold text-white mb-3">{company_name}</h3>
        <p class="text-gray-400 mb-4">{description}</p>
        <div class="flex gap-4">
          <a href="#" class="hover:text-white transition-colors">
            <i data-lucide="twitter" class="w-5 h-5"></i>
          </a>
          <a href="#" class="hover:text-white transition-colors">
            <i data-lucide="github" class="w-5 h-5"></i>
          </a>
          <a href="#" class="hover:text-white transition-colors">
            <i data-lucide="linkedin" class="w-5 h-5"></i>
          </a>
        </div>
      </div>
      
      <!-- Product Links -->
      <div>
        <h4 class="text-white font-semibold mb-3">Product</h4>
        <ul class="space-y-2">
          <li><a href="#" class="hover:text-white transition-colors">Features</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Pricing</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Documentation</a></li>
        </ul>
      </div>
      
      <!-- Company Links -->
      <div>
        <h4 class="text-white font-semibold mb-3">Company</h4>
        <ul class="space-y-2">
          <li><a href="#" class="hover:text-white transition-colors">About</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Blog</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Contact</a></li>
        </ul>
      </div>
    </div>
    
    <!-- Copyright -->
    <div class="border-t border-gray-800 pt-8 text-center text-gray-400">
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
