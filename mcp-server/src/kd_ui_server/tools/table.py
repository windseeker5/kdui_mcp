"""Table generation tool for Flask templates."""
import uuid


def create_table(columns, features=None, rows_per_page=10, striped=True, hoverable=True, title="Data Table"):
    """
    Generate a data table with sorting, filtering, and pagination.

    Args:
        columns:       List of column definitions
        features:      List of features — "search", "sort", "pagination", "actions"
        rows_per_page: Rows visible per page
        striped:       Alternating row colors
        hoverable:     Highlight row on hover
        title:         Table heading text

    Returns:
        Self-contained Jinja2 template string (includes inline JS)
    """
    if features is None:
        features = ["search", "sort", "pagination"]

    tid = f"kd-tbl-{uuid.uuid4().hex[:8]}"

    # ── Outer wrapper ─────────────────────────────────────────────────────────
    t = f'<div id="{tid}" style="background:var(--b1, white); border:1px solid oklch(var(--b3)); border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.06); padding:1.5rem;">\n'

    # ── Header bar: title | search | total ────────────────────────────────────
    if "search" in features:
        t += f'''  <div style="display:grid; grid-template-columns:auto 1fr auto; align-items:center; gap:1rem; margin-bottom:1.25rem;">
    <h2 style="font-size:1.125rem; font-weight:600; color:oklch(var(--bc)); margin:0; white-space:nowrap;">{title}</h2>
    <div style="position:relative; max-width:360px; justify-self:center; width:100%;">
      <svg style="position:absolute; left:10px; top:50%; transform:translateY(-50%); color:oklch(var(--bc)/0.35); pointer-events:none;" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input type="text" id="{tid}-search" placeholder="Search..." style="width:100%; padding:7px 12px 7px 32px; font-size:0.875rem; background:oklch(var(--b1, white)); color:oklch(var(--bc)); border:1px solid oklch(var(--b3)); border-radius:6px; outline:none; box-sizing:border-box;" onfocus="this.style.borderColor='#2563EB'" onblur="this.style.borderColor='oklch(var(--b3))'" />
    </div>
    <span style="font-size:0.875rem; color:oklch(var(--bc)/0.45); white-space:nowrap;">{{{{ total_rows or 0 }}}} total</span>
  </div>
'''
    else:
        t += f'  <h2 style="font-size:1.125rem; font-weight:600; color:oklch(var(--bc)); margin-bottom:1.25rem;">{title}</h2>\n'

    # ── Table ─────────────────────────────────────────────────────────────────
    t += '  <div class="overflow-x-auto">\n'
    t += '    <table class="table table-sm w-full">\n'
    t += '      <thead>\n'
    t += '        <tr>\n'

    th_style = "font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; color:oklch(var(--bc)/0.45); font-weight:600;"

    for col in columns:
        col_name  = col.get("name", "")
        col_label = col.get("label", col_name)
        sortable  = col.get("sortable", True)

        if sortable and "sort" in features:
            t += f'          <th class="cursor-pointer" data-column="{col_name}" style="{th_style}">{col_label}&nbsp;<span class="sort-icon" style="color:oklch(var(--bc)/0.2); font-size:0.7rem;">⇅</span></th>\n'
        else:
            t += f'          <th style="{th_style}">{col_label}</th>\n'

    if "actions" in features:
        t += f'          <th style="{th_style}">Actions</th>\n'

    t += '        </tr>\n'
    t += '      </thead>\n'
    t += f'      <tbody id="{tid}-body">\n'

    # Badge color → inline style map (evaluated once by Jinja2 before the loop)
    t += "        {%- set _bmap = {'success':'background:#16a34a;color:#fff','warning':'background:#d97706;color:#fff','error':'background:#dc2626;color:#fff','destructive':'background:#dc2626;color:#fff','primary':'background:#2563eb;color:#fff','default':'background:#2563eb;color:#fff','secondary':'background:#f3f4f6;color:#374151'} %}\n"
    t += '        {% if data %}\n'
    t += '          {% for row in data %}\n'
    t += '          <tr>\n'

    for col in columns:
        col_name = col.get("name", "")
        col_type = col.get("type", "text")

        if col_type == "badge":
            t += (
                f'            <td>'
                f'<span style="display:inline-flex;align-items:center;border-radius:9999px;padding:2px 10px;'
                f'font-size:0.75rem;font-weight:600;'
                f'{{{{ _bmap.get(row.{col_name}_color or \'primary\', \'background:#2563eb;color:#fff\') }}}}">'
                f'{{{{ row.{col_name} }}}}</span></td>\n'
            )
        elif col_type == "avatar":
            t += f'''            <td>
              <div class="flex items-center gap-3">
                <div class="avatar"><div class="mask mask-squircle w-9 h-9">
                  <img src="{{{{ row.{col_name}_url }}}}" alt="{{{{ row.{col_name} }}}}" />
                </div></div>
                <span>{{{{ row.{col_name} }}}}</span>
              </div>
            </td>\n'''
        else:
            t += f'            <td>{{{{ row.{col_name} }}}}</td>\n'

    if "actions" in features:
        t += '''            <td>
              <div style="display:flex; gap:10px;">
                <a href="/edit/{{ row.id }}" style="font-size:0.8125rem; color:#2563EB; text-decoration:none;">Edit</a>
                <a href="/delete/{{ row.id }}" style="font-size:0.8125rem; color:#DC2626; text-decoration:none;">Delete</a>
              </div>
            </td>\n'''

    t += '          </tr>\n'
    t += '          {% endfor %}\n'
    t += '        {% else %}\n'
    t += '          <tr>\n'
    t += f'            <td colspan="{len(columns) + (1 if "actions" in features else 0)}" style="text-align:center; padding:2.5rem; color:oklch(var(--bc)/0.35); font-size:0.875rem;">No data available</td>\n'
    t += '          </tr>\n'
    t += '        {% endif %}\n'
    t += '      </tbody>\n'
    t += '    </table>\n'
    t += '  </div>\n'

    # ── Footer: count (left) | pagination (center) ────────────────────────────
    if "pagination" in features:
        t += f'''
  <div style="display:grid; grid-template-columns:1fr auto 1fr; align-items:center; margin-top:0.875rem; padding-top:0.875rem; border-top:1px solid oklch(var(--b3));">
    <span id="{tid}-count" style="font-size:0.8125rem; color:oklch(var(--bc)/0.4);"></span>
    <div id="{tid}-pages" style="display:flex; align-items:center; gap:1px;"></div>
    <span></span>
  </div>
'''

    t += '</div>\n'
    t += _table_script(tid, columns, features, rows_per_page, striped, hoverable)
    return t


# ── Scoped JavaScript ─────────────────────────────────────────────────────────

def _table_script(tid, columns, features, rows_per_page, striped, hoverable):
    js_striped   = "true"  if striped   else "false"
    js_hoverable = "true"  if hoverable else "false"
    has_search   = "true"  if "search"     in features else "false"
    has_sort     = "true"  if "sort"       in features else "false"
    has_pages    = "true"  if "pagination" in features else "false"

    return f"""
<script>
(function() {{
  var tid        = '{tid}';
  var RPP        = {rows_per_page};
  var striped    = {js_striped};
  var hoverable  = {js_hoverable};
  var hasSearch  = {has_search};
  var hasSort    = {has_sort};
  var hasPages   = {has_pages};

  var tbody    = document.getElementById(tid + '-body');
  var countEl  = document.getElementById(tid + '-count');
  var pagesEl  = document.getElementById(tid + '-pages');
  var searchEl = document.getElementById(tid + '-search');
  var curPage  = 1;
  var filtered = [];

  function allRows() {{
    return Array.from(tbody.querySelectorAll('tr'));
  }}

  function doSearch(term) {{
    var rows = allRows();
    if (!term) return rows;
    var q = term.toLowerCase();
    return rows.filter(function(r) {{ return r.textContent.toLowerCase().indexOf(q) !== -1; }});
  }}

  function renderPage(rows, page) {{
    allRows().forEach(function(r) {{ r.style.display = 'none'; }});

    var start    = (page - 1) * RPP;
    var end      = start + RPP;
    var pageRows = rows.slice(start, end);

    pageRows.forEach(function(row, i) {{
      // Use CSS variables so zebra color adapts to dark/light theme
      var base = (striped && i % 2 !== 0) ? 'oklch(var(--b2))' : 'transparent';
      row.style.display    = '';
      row.style.background = base;
      if (hoverable) {{
        row.onmouseenter = function() {{ this.style.background = 'oklch(var(--b3))'; }};
        row.onmouseleave = (function(b) {{ return function() {{ this.style.background = b; }}; }})(base);
      }}
    }});

    var from = rows.length === 0 ? 0 : start + 1;
    var to   = Math.min(end, rows.length);
    if (countEl) {{
      countEl.textContent = 'Showing ' + from + '\u2013' + to + ' of ' + rows.length;
    }}

    if (pagesEl && hasPages) buildPages(rows.length, page);
  }}

  function buildPages(total, page) {{
    var totalPages = Math.ceil(total / RPP);
    pagesEl.innerHTML = '';
    if (totalPages <= 1) return;

    pagesEl.appendChild(pgBtn('\u2039', page > 1, false, function() {{
      curPage--; renderPage(filtered, curPage);
    }}));

    for (var i = 1; i <= totalPages; i++) {{
      (function(p) {{
        pagesEl.appendChild(pgBtn(String(p), true, p === page, function() {{
          curPage = p; renderPage(filtered, curPage);
        }}));
      }})(i);
    }}

    pagesEl.appendChild(pgBtn('\u203a', page < totalPages, false, function() {{
      curPage++; renderPage(filtered, curPage);
    }}));
  }}

  function pgBtn(label, enabled, active, onClick) {{
    var b = document.createElement('button');
    b.textContent = label;
    b.disabled    = !enabled;
    var base = 'min-width:30px;height:30px;padding:0 8px;border-radius:5px;border:none;font-size:0.8125rem;line-height:1;cursor:pointer;';
    if (active) {{
      // Blue active state — consistent with brand, works on light + dark
      b.style.cssText = base + 'background:#2563EB;color:#fff;font-weight:600;';
    }} else {{
      b.style.cssText = base + 'background:transparent;color:oklch(var(--bc)/0.5);';
      if (enabled) {{
        b.onmouseenter = function() {{ this.style.background = 'oklch(var(--b2))'; }};
        b.onmouseleave = function() {{ this.style.background = 'transparent'; }};
      }} else {{
        b.style.opacity = '0.35';
        b.style.cursor  = 'default';
      }}
    }}
    b.addEventListener('click', onClick);
    return b;
  }}

  // ── Sort ──────────────────────────────────────────────────────────────────
  if (hasSort) {{
    document.querySelectorAll('#{tid} th[data-column]').forEach(function(th) {{
      th.addEventListener('click', function() {{
        var colIdx = Array.from(this.parentElement.children).indexOf(this);
        var isAsc  = this.dataset.sortDir === 'asc';

        document.querySelectorAll('#{tid} th[data-column]').forEach(function(h) {{
          delete h.dataset.sortDir;
          var ic = h.querySelector('.sort-icon');
          if (ic) {{ ic.textContent = '\u21c5'; ic.style.color = 'oklch(var(--bc)/0.2)'; }}
        }});

        this.dataset.sortDir = isAsc ? 'desc' : 'asc';
        var icon = this.querySelector('.sort-icon');
        if (icon) {{ icon.textContent = isAsc ? '\u2193' : '\u2191'; icon.style.color = 'oklch(var(--bc)/0.6)'; }}

        var rows = allRows();
        rows.sort(function(a, b) {{
          var av = a.cells[colIdx] ? a.cells[colIdx].textContent.trim() : '';
          var bv = b.cells[colIdx] ? b.cells[colIdx].textContent.trim() : '';
          var c  = av.localeCompare(bv, undefined, {{numeric: true}});
          return isAsc ? -c : c;
        }});
        rows.forEach(function(r) {{ tbody.appendChild(r); }});

        filtered = searchEl ? doSearch(searchEl.value) : allRows();
        curPage  = 1;
        renderPage(filtered, curPage);
      }});
    }});
  }}

  // ── Search ────────────────────────────────────────────────────────────────
  if (hasSearch && searchEl) {{
    searchEl.addEventListener('input', function() {{
      filtered = doSearch(this.value);
      curPage  = 1;
      renderPage(filtered, curPage);
    }});
  }}

  // ── Init ──────────────────────────────────────────────────────────────────
  filtered = allRows();
  renderPage(filtered, 1);
}})();
</script>
"""
