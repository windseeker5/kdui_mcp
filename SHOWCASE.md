# Component Showcase

A local Flask app that renders every available KD UI component side-by-side — with light/dark theme toggle and the MCP tool call for each one.

Use it as the source of truth for visual quality. When you improve a component in `mcp-server/src/kd_ui_server/tools/`, the showcase reflects the change immediately on refresh.

**URL**: http://localhost:5005

---

## Run it

Make sure the virtual environment is active first:

```bash
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```

Then:

```bash
cd showcase
python app.py
```

Open http://localhost:5005 in your browser.

---

## What's included

| Section | Components shown |
|---|---|
| Badge | all 6 variants (default, secondary, destructive, outline, success, warning) |
| Button | 5 variants × 3 sizes |
| Alert | info, success, warning, error |
| Card | with header, body, action button |
| Progress | all 4 variants at different fill levels |
| Skeleton | text, circle, rectangle |
| Typography | h1–h4, lead, muted, blockquote, code, list |
| Stat Card | 2 cards in a row |
| Modal | with trigger button |
| Tabs | 3-tab component |
| Breadcrumb | 3-level |
| Dropdown Menu | with label, items, separator, destructive item |
| Navbar | with brand and nav links |
| Sidebar | collapsible, with badge and active state |
| Navigation Menu | horizontal with hover dropdown |
| Chart Container | Chart.js line chart |
| Form | login preset |
| Table | 3-column with search, sort, pagination |
| Hero | landing page hero section |
| Features | 3-column features grid |
| Testimonials | 3 customer quotes |
| Pricing | 3-tier pricing cards |
| CTA | call-to-action banner |
| Footer | multi-column footer |

---

## How it works

`examples/showcase/app.py` imports the tool functions directly and calls them as plain Python — no MCP protocol involved. The rendered HTML strings are passed to `showcase.html` via `{{ component | safe }}`.

For components that contain Jinja2 template syntax (form, table), the app pre-renders them with `render_template_string` before passing to the template.

This means: fixing a function in `mcp-server/src/kd_ui_server/tools/` is immediately visible in the showcase. No drift possible.
