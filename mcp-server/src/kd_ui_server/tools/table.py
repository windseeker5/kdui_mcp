"""Table generation tool for Flask templates with DaisyUI."""


def create_table(columns, features=None, rows_per_page=10, striped=True, hoverable=True):
    """
    Generate a data table with sorting, filtering, and pagination.
    
    Args:
        columns: List of column definitions
        features: List of features to enable
        rows_per_page: Number of rows per page
        striped: Alternating row colors
        hoverable: Highlight row on hover
    
    Returns:
        Table template string
    """
    if features is None:
        features = ["search", "sort", "pagination"]
    
    table_classes = ["table", "w-full"]
    if striped:
        table_classes.append("table-zebra")
    if hoverable:
        table_classes.append("hover")
    
    table_class_str = " ".join(table_classes)
    
    template = '<div class="card bg-base-100 shadow-xl">\n'
    template += '  <div class="card-body">\n'
    template += '    <h2 class="card-title">Data Table</h2>\n\n'
    
    # Add search if enabled
    if "search" in features:
        template += '''    <!-- Search -->
    <div class="form-control w-full max-w-xs mb-4">
      <input type="text" id="tableSearch" placeholder="Search..." class="input input-bordered w-full" />
    </div>
'''
    
    # Table container
    template += '    <div class="overflow-x-auto">\n'
    template += f'      <table class="{table_class_str}">\n'
    template += '        <thead>\n'
    template += '          <tr>\n'
    
    # Generate headers
    for col in columns:
        col_name = col.get("name", "")
        col_label = col.get("label", col_name)
        sortable = col.get("sortable", True)
        
        if sortable and "sort" in features:
            template += f'            <th class="cursor-pointer" data-column="{col_name}">{col_label} <span class="sort-icon">⇅</span></th>\n'
        else:
            template += f'            <th>{col_label}</th>\n'
    
    if "actions" in features:
        template += '            <th>Actions</th>\n'
    
    template += '          </tr>\n'
    template += '        </thead>\n'
    template += '        <tbody id="tableBody">\n'
    
    # Generate sample row or data loop
    template += '          {% if data %}\n'
    template += '            {% for row in data %}\n'
    template += '            <tr>\n'
    
    for col in columns:
        col_name = col.get("name", "")
        col_type = col.get("type", "text")
        
        if col_type == "badge":
            template += f'              <td><span class="badge badge-{{{{ row.{col_name}_color or \'primary\' }}}}">{{{{ row.{col_name} }}}}</span></td>\n'
        elif col_type == "avatar":
            template += f'''              <td>
                <div class="flex items-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle w-12 h-12">
                      <img src="{{{{ row.{col_name}_url }}}}" alt="{{{{ row.{col_name} }}}}" />
                    </div>
                  </div>
                  <div>{{{{ row.{col_name} }}}}</div>
                </div>
              </td>\n'''
        else:
            template += f'              <td>{{{{ row.{col_name} }}}}</td>\n'
    
    if "actions" in features:
        template += '''              <td>
                <div class="flex gap-2">
                  <a href="/edit/{{ row.id }}" class="btn btn-sm btn-ghost">Edit</a>
                  <a href="/delete/{{ row.id }}" class="btn btn-sm btn-error">Delete</a>
                </div>
              </td>\n'''
    
    template += '            </tr>\n'
    template += '            {% endfor %}\n'
    template += '          {% else %}\n'
    template += '            <tr>\n'
    template += f'              <td colspan="{len(columns) + (1 if "actions" in features else 0)}" class="text-center">No data available</td>\n'
    template += '            </tr>\n'
    template += '          {% endif %}\n'
    
    template += '        </tbody>\n'
    template += '      </table>\n'
    template += '    </div>\n'
    
    # Add pagination if enabled
    if "pagination" in features:
        template += f'''
    <!-- Pagination -->
    <div class="flex justify-center mt-4">
      <div class="join">
        <button class="join-item btn btn-sm">«</button>
        <button class="join-item btn btn-sm btn-active">1</button>
        <button class="join-item btn btn-sm">2</button>
        <button class="join-item btn btn-sm">3</button>
        <button class="join-item btn btn-sm">»</button>
      </div>
    </div>
    
    <div class="text-center mt-2 text-sm text-base-content/60">
      Showing 1 to {rows_per_page} of {{{{ total_rows or 0 }}}} entries
    </div>
'''
    
    template += '  </div>\n'
    template += '</div>\n'
    
    # Add JavaScript for interactivity if needed
    if "search" in features or "sort" in features:
        template += _add_table_javascript(features)
    
    return template


def _add_table_javascript(features):
    """Add JavaScript for table interactivity."""
    js = '\n<script>\n'
    
    if "search" in features:
        js += '''  // Table search functionality
  document.getElementById('tableSearch')?.addEventListener('keyup', function() {
    const searchValue = this.value.toLowerCase();
    const rows = document.querySelectorAll('#tableBody tr');
    
    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(searchValue) ? '' : 'none';
    });
  });
'''
    
    if "sort" in features:
        js += '''
  // Table sorting functionality
  document.querySelectorAll('th[data-column]').forEach(header => {
    header.addEventListener('click', function() {
      const column = this.dataset.column;
      const table = this.closest('table');
      const tbody = table.querySelector('tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));
      const isAscending = this.classList.contains('sort-asc');
      
      // Remove sort classes from all headers
      table.querySelectorAll('th').forEach(th => {
        th.classList.remove('sort-asc', 'sort-desc');
      });
      
      // Add sort class to current header
      this.classList.add(isAscending ? 'sort-desc' : 'sort-asc');
      
      // Sort rows
      rows.sort((a, b) => {
        const aValue = a.cells[Array.from(this.parentElement.children).indexOf(this)].textContent.trim();
        const bValue = b.cells[Array.from(this.parentElement.children).indexOf(this)].textContent.trim();
        
        if (isAscending) {
          return bValue.localeCompare(aValue, undefined, {numeric: true});
        } else {
          return aValue.localeCompare(bValue, undefined, {numeric: true});
        }
      });
      
      // Re-append rows
      rows.forEach(row => tbody.appendChild(row));
    });
  });
'''
    
    js += '</script>\n'
    return js
