"""Resource templates and documentation for KD UI Framework."""


class ComponentTemplates:
    """Manage component templates and best practices."""
    
    def get_template(self, template_name):
        """Get a specific template by name."""
        templates = {
            "layouts/base": self._get_base_layout(),
            "components/stat_card": self._get_stat_card_template(),
            "components/chart_container": self._get_chart_container_template(),
            "components/sidebar": self._get_sidebar_template(),
            "components/navbar": self._get_navbar_template(),
        }
        
        return templates.get(template_name, f"<!-- Template not found: {template_name} -->")
    
    def get_uiux_design_rules(self):
        """Get comprehensive UI/UX design rules and standards."""
        return """# UI/UX Design Standards & Logic for KD UI Framework

## 1. Dashboard Architecture & Layout Logic
*Use these rules when the user request involves "Dashboards," "Admin Panels," or "Data Visualization."*

*   **Navigation Models:**
    *   **Split Navigation:** Do not use a single menu for everything. Place global actions (User Profile, Settings, Logout) in a **Top Bar**. Place context-specific views (Data Types, Views) in a **Left Sidebar** (The "Spine").
    *   **Sidebar Hierarchy:** Group links by relevance. Place high-frequency links at the top; place "Settings" or "Help" at the bottom. Use collapsible menus for depth to reduce cognitive load.
    *   **Breadcrumbs:** Always implement breadcrumbs for deep content flows to maintain user context.
*   **Information Density & Grid:**
    *   **Dashboard vs. Landing Page:** Dashboards require higher information density. Use smaller font sizes and stricter grids than marketing pages.
    *   **Compact Spacing:** Avoid excess padding and whitespace in data-heavy views. Data must be available with the least amount of scrolling.
    *   **Grid Structure:** Use a strict grid (e.g., 2-column or 3-column) to organize widgets. Place the most critical metrics or actions (e.g., Project Status, Financial Totals) at the very top left or center.
*   **Dynamic Content:**
    *   Prioritize dynamic, changing data. Do not dedicate prime screen real estate to static content that does not change.

## 2. Visual Style System (The "Look & Feel")
*Apply these rules to normalize the aesthetics of generated web pages and components.*

*   **Typography Rules:**
    *   **Font Limit:** Use a maximum of 2 fonts. (Recommendation: 1 for Headings, 1 for Body, or 1 font family with different weights).
    *   **Hierarchy Scale:**
        *   **H1:** Hero sections/Page Titles.
        *   **H2:** Section Headings.
        *   **H3/Body Large:** Subcategories.
        *   **Body Small:** Details/Metadata.
    *   **Readability:** Ensure text containers do not exceed **600px** in width to maintain optimal reading experience.
*   **Relationship-Based Spacing (The Multiplier Rule):**
    *   Define spacing based on element relationships.
    *   *Rule:* If elements are related (e.g., Header + Body), use space `X` (e.g., 16px). If elements are distinct (e.g., Text Group + Button), use space `2X` (e.g., 32px).
    *   **Section Spacing:** For general web pages, use large vertical gaps (80px–160px) between major sections to create "breathing room".
*   **Color System:**
    *   **The 3-Color Rule:** Limit the palette to:
        1.  **Base:** Background color.
        2.  **Primary:** Call-to-Action (CTA) and accents.
        3.  **Neutral:** Text (Dark or Light).
    *   **Text Hierarchy via Opacity:** Instead of different gray hex codes, use the Neutral color with opacity:
        *   Primary Text: 100% or 80% opacity.
        *   Secondary Text: 60-70% opacity.
*   **Visual Polish:**
    *   **Banish "Flat" Design:** Add subtle inner shadows (white, low opacity) and drop shadows to buttons to make them tactile. Add subtle borders (5% opacity) to cards to define structure.
    *   **Break the Monotony:** While adhering to grids, occasionally break the layout with overflowing carousels or centered text to maintain visual interest.

## 3. Component & Interaction Logic
*Standardized rules for specific UI elements.*

*   **Charts & Data Visualization:**
    *   **Intent Matching:**
        *   Use **Bar Charts** for comparing data points.
        *   Use **Line Graphs** for plotting trends over time.
    *   **Simplicity:** Always include grid lines, clear axis numbers, and a summary/total at the top of the chart.
*   **Tables vs. Lists:**
    *   Use **Lists** for simple data (visual separation via spacing or dividers).
    *   Use **Tables** when functionality is required. Tables *must* include Search, Filter, and Sort capabilities.
*   **Modals vs. Popovers vs. Toasts:**
    *   **Popover:** Use for simple, non-blocking context (e.g., display settings) where the user can click away.
    *   **Modal:** Use for complex, blocking actions that require focus (e.g., creating a new item).
    *   **Toast:** Use for system feedback (success/error messages) that does not require user action.
*   **Empty States:**
    *   Always design an "Empty State" for lists/dashboards when no data exists yet. Do not leave a blank white space.

## 4. The "Anti-Patterns" (Mistakes to Avoid)
*Hard constraints: The Server must REJECT these patterns.*

1.  **Navigation Overload:** Do not cram all navigation links into a single sidebar or top menu. Segregate global vs. local nav.
2.  **Mental Model Mismatch:** Do not categorize menu items based on database structure; categorize them based on user workflow (User Research/Card Sorting logic).
3.  **Static Dashboarding:** Do not build dashboards that look like static web pages. If the content doesn't change, it doesn't belong on a dashboard.
4.  **Inconsistent Visuals:** Do not use raw colors without a defined palette. Do not mix more than 2 font families.
5.  **Lorem Ipsum Dependence:** Where possible, generate realistic content for the UI to test real-world text wrapping and layout, rather than relying solely on Lorem Ipsum.

### System Instruction:
"You are a UI Design Engine. When generating code or layouts, you must strictly adhere to the 'Dashboard Architecture' for application interfaces and 'Visual Style System' for general pages. You will reject requests to create 'flat' unstyled buttons, enforcing the 3-color rule and opacity-based hierarchy. For data inputs, you will automatically select the appropriate visualization (Bar vs Line) based on the data context."
"""

    def get_dashboard_architecture(self):
        """Get dashboard architecture guidelines."""
        return """# Dashboard Architecture Guide

## Navigation Models

### Split Navigation (REQUIRED for Dashboards)
- **Top Bar**: Global actions (User Profile, Settings, Logout, Notifications)
- **Left Sidebar ("The Spine")**: Context-specific views (Data Types, Different Views, Sections)

**Why:** Reduces cognitive load, provides clear separation between global and contextual navigation.

### Sidebar Hierarchy Rules
1. **Top Section**: Most frequently accessed items
2. **Middle Section**: Context-specific navigation
3. **Bottom Section**: Settings, Help, Admin functions

**Best Practice**: Use collapsible menus for deep hierarchies to prevent overwhelming users.

### Breadcrumbs
- **Always implement** for deep content flows (3+ levels)
- Shows current location and enables quick backtracking
- Format: Home > Section > Subsection > Current Page

## Information Density

### Dashboard vs Landing Page
- **Dashboards**: Higher information density, smaller fonts, stricter grids
- **Landing Pages**: More whitespace, larger fonts, marketing focus

### Grid Structure
- Use **2-column or 3-column** grids for widgets
- Place **most critical metrics** at top-left or center
- Examples of critical metrics:
  - Project Status
  - Financial Totals
  - Key Performance Indicators (KPIs)

### Compact Spacing for Data Views
- Minimize padding in data-heavy sections
- Data should be accessible with minimal scrolling
- Balance between readability and information density

## Dynamic Content Priority
- **Prime real estate** (top, center) = Dynamic, changing data
- **Secondary areas** = Static content, navigation, metadata
- If content doesn't change frequently, it doesn't belong on a dashboard
"""

    def get_visual_style_system(self):
        """Get visual style system guidelines."""
        return """# Visual Style System

## Typography Rules

### Font Limit: Maximum 2 Fonts
- **Option 1**: One font family with different weights (recommended)
  - Example: Inter (Light, Regular, Medium, Semi-Bold, Bold)
- **Option 2**: One for headings, one for body
  - Example: Poppins (headings) + Inter (body)

### Hierarchy Scale
- **H1 (48px-64px)**: Hero sections, page titles
- **H2 (32px-40px)**: Major section headings
- **H3 (24px-28px)**: Subsection headings
- **Body Large (18px-20px)**: Important body text
- **Body (16px)**: Standard text
- **Body Small (14px)**: Metadata, captions

### Readability Constraints
- **Max width for text containers**: 600px (optimal reading)
- **Line height**: 1.5 for body text, 1.2 for headings

## Relationship-Based Spacing (Multiplier Rule)

### The Multiplier System
- **Base unit**: 16px (or 8px for tighter designs)
- **Related elements** (header + description): 1X spacing (16px)
- **Distinct elements** (text block + button): 2X spacing (32px)
- **Major sections**: 5X-10X spacing (80px-160px)

### Application
```
Card Title
↓ 16px (1X - related)
Card Description
↓ 32px (2X - distinct)
[Action Button]
↓ 80px (5X - major section)
Next Section Title
```

## Color System: The 3-Color Rule

### Required Colors
1. **Base**: Background color
   - Light theme: #FFFFFF or #F9FAFB
   - Dark theme: #0F172A or #1E293B

2. **Primary**: Call-to-Action and accents
   - Example: #3B82F6 (blue), #8B5CF6 (purple)
   - Use for: Buttons, links, active states

3. **Neutral**: Text color
   - Light theme: #0F172A (dark)
   - Dark theme: #F9FAFB (light)

### Text Hierarchy via Opacity (NOT different grays)
- **Primary text**: 100% opacity (headings, important content)
- **Secondary text**: 80% opacity (body text)
- **Tertiary text**: 60-70% opacity (metadata, timestamps)

**Why**: Maintains color consistency, easier to maintain, scales better

## Visual Polish: Banish Flat Design

### Subtle Depth
- **Cards**: Add subtle border (5% opacity) + soft shadow
  ```css
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  border: 1px solid rgba(0,0,0,0.05);
  ```

- **Buttons**: Inner highlight + drop shadow
  ```css
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.1), 0 2px 4px rgba(0,0,0,0.2);
  ```

### Breaking Monotony
- Use grids as foundation, but occasionally:
  - Overflow carousels beyond container
  - Center important text sections
  - Use full-width images to break sections
  - Add diagonal or curved dividers between sections
"""

    def get_anti_patterns(self):
        """Get UI anti-patterns to avoid."""
        return """# UI Anti-Patterns to Avoid

## 1. Navigation Overload ❌
**Problem**: Cramming all navigation links into a single sidebar or top menu.

**Why it fails**: Cognitive overload, difficult to find items, unclear information architecture.

**Solution**: Use split navigation (top bar + sidebar). Categorize by user workflow, not database structure.

## 2. Mental Model Mismatch ❌
**Problem**: Organizing menu items based on how data is stored in the database.

**Why it fails**: Users don't think in terms of your database schema. They think in terms of tasks.

**Solution**: Use card sorting and user research to understand user mental models. Group by workflow/task.

## 3. Static Dashboarding ❌
**Problem**: Building dashboards that look like static web pages with content that never changes.

**Why it fails**: Dashboards should show dynamic, real-time data. Static content wastes prime screen space.

**Solution**: Reserve dashboard space for metrics that update frequently. Move static content to separate pages.

## 4. Inconsistent Visuals ❌
**Problem**: Using raw colors without a defined palette, mixing multiple font families randomly.

**Why it fails**: Looks unprofessional, creates visual chaos, harder to maintain.

**Solution**: Follow the 3-color rule. Use maximum 2 fonts. Create a design system and stick to it.

## 5. Excessive Flat Design ❌
**Problem**: Completely flat buttons and cards with no visual depth.

**Why it fails**: Reduces affordance (users can't tell what's clickable), looks unfinished.

**Solution**: Add subtle shadows and borders. Make interactive elements look interactive.

## 6. Lorem Ipsum Dependence ❌
**Problem**: Using Lorem Ipsum for all placeholder text during design.

**Why it fails**: Real content often breaks layouts. Lorem Ipsum doesn't test real-world scenarios.

**Solution**: Use realistic content examples that match actual use cases. Test with long/short variations.

## 7. Ignoring Empty States ❌
**Problem**: Leaving blank white space when lists or dashboards have no data.

**Why it fails**: Confusing user experience. Users don't know if it's broken or empty.

**Solution**: Design helpful empty states with:
- Illustration or icon
- Clear message ("No data yet")
- Call-to-action ("Create your first item")

## 8. Missing Table Functionality ❌
**Problem**: Creating data tables without search, filter, or sort.

**Why it fails**: Unusable for large datasets. Users expect basic table functionality.

**Solution**: Tables MUST include:
- Search/filter
- Column sorting
- Pagination (for 25+ items)

## 9. Poor Color Contrast ❌
**Problem**: Low contrast between text and background.

**Why it fails**: Accessibility issues, difficult to read, especially on mobile or in bright light.

**Solution**: Maintain minimum 4.5:1 contrast ratio for normal text, 3:1 for large text.

## 10. Inconsistent Spacing ❌
**Problem**: Random padding/margins without a system.

**Why it fails**: Looks messy, harder to maintain, inconsistent visual rhythm.

**Solution**: Use a spacing scale (4px, 8px, 16px, 24px, 32px, 48px, 64px). Apply consistently.
"""

    def get_best_practices(self):
        """Get UI/UX best practices guide."""
        return """# UI/UX Best Practices for Dashboards

## 1. Visual Hierarchy
- Use size, color, and spacing to guide the user's attention
- Most important metrics should be larger and positioned prominently
- Use consistent heading styles (h1 for page titles, h2 for sections)

## 2. Color Usage
- **Primary color**: Main actions, important CTAs
- **Secondary color**: Supporting elements
- **Success**: Positive metrics, completed actions
- **Warning**: Caution, pending states
- **Error**: Problems, failed states
- **Neutral**: General content, backgrounds

## 3. Spacing & Layout
- Use consistent spacing (multiples of 4px: 8px, 16px, 24px, 32px)
- Give elements room to breathe - avoid cramming too much
- Use grid systems for alignment
- Maintain consistent margins between sections

## 4. Typography
- **Headings**: Bold, larger sizes (24px, 32px, 48px)
- **Body text**: 16px minimum for readability
- **Small text**: 14px for metadata, captions
- Limit to 2-3 font weights
- Use line-height of 1.5 for body text

## 5. Data Visualization
- Choose the right chart type for your data
- Label axes clearly
- Use consistent colors across charts
- Provide legends when needed
- Keep charts simple and focused

## 6. Responsive Design
- Mobile-first approach
- Test on multiple screen sizes
- Use breakpoints: 640px (sm), 768px (md), 1024px (lg), 1280px (xl)
- Stack elements vertically on mobile
- Hide less important elements on small screens

## 7. Accessibility
- Maintain 4.5:1 contrast ratio for text
- Use semantic HTML (header, nav, main, aside)
- Provide alt text for images
- Ensure keyboard navigation works
- Use ARIA labels where needed

## 8. Performance
- Lazy load images and charts
- Minimize DOM elements
- Use CSS animations sparingly
- Optimize assets (compress images)
- Load critical CSS inline

## 9. User Feedback
- Show loading states
- Display error messages clearly
- Confirm destructive actions
- Provide success messages
- Use progress indicators for long operations

## 10. Consistency
- Use the design system consistently
- Same components for same purposes
- Consistent button styles and placement
- Uniform spacing throughout
- Predictable navigation patterns
"""
    
    def _get_base_layout(self):
        """Base Flask layout template."""
        return '''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Dashboard{% endblock %}</title>
    
    <!-- Tailwind CSS + DaisyUI -->
    <link href="{{ url_for('static', filename='dist/output.css') }}" rel="stylesheet">
    
    <!-- Chart.js for charts -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    
    <!-- Font (Optional but recommended) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
    </style>
    
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-base-200">
    {% block content %}{% endblock %}
    
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block extra_scripts %}{% endblock %}
</body>
</html>
'''
    
    def _get_stat_card_template(self):
        """Stat card template."""
        return '''<!-- Stat Card Component -->
<!-- Usage: Include this with title, value, and description variables -->
<div class="stats shadow">
  <div class="stat">
    <div class="stat-title">{{ title }}</div>
    <div class="stat-value text-{{ color|default('primary') }}">{{ value }}</div>
    <div class="stat-desc">{{ description }}</div>
  </div>
</div>
'''
    
    def _get_chart_container_template(self):
        """Chart container template."""
        return '''<!-- Chart Container Component -->
<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">{{ chart_title }}</h2>
    <canvas id="{{ chart_id }}"></canvas>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('{{ chart_id }}');
    if (ctx) {
        new Chart(ctx, {
            type: '{{ chart_type|default("line") }}',
            data: {{ chart_data|tojson|safe }},
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'top',
                    }
                }
            }
        });
    }
});
</script>
'''
    
    def _get_sidebar_template(self):
        """Sidebar template."""
        return '''<!-- Sidebar Component -->
<ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
  <li class="mb-2">
    <a class="text-xl font-bold">{{ app_name|default('Dashboard') }}</a>
  </li>
  {% for item in menu_items %}
  <li>
    <a href="{{ item.url }}" class="{% if item.active %}active{% endif %}">
      {% if item.icon %}{{ item.icon|safe }}{% endif %}
      {{ item.label }}
    </a>
  </li>
  {% endfor %}
</ul>
'''
    
    def _get_navbar_template(self):
        """Navbar template."""
        return '''<!-- Navbar Component -->
<div class="navbar bg-base-200 shadow-md">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl">{{ app_name|default('Dashboard') }}</a>
  </div>
  <div class="flex-none">
    <ul class="menu menu-horizontal px-1">
      {% for item in menu_items %}
      <li><a href="{{ item.url }}">{{ item.label }}</a></li>
      {% endfor %}
    </ul>
  </div>
</div>
'''


# Create global instance
component_templates = ComponentTemplates()
