"""Dashboard generation tool for Flask templates with DaisyUI."""


def create_dashboard(layout="sidebar", title="Dashboard", theme="light", components=None):
    """
    Generate a complete Flask dashboard template.
    
    Args:
        layout: "sidebar" or "topnav"
        title: Dashboard page title
        theme: "light", "dark", or "auto"
        components: List of components to include
    
    Returns:
        Complete Jinja2 template string
    """
    if components is None:
        components = ["stats", "charts"]
    
    # Base template structure
    template = f'''{{%extends "base.html" %}}

{{% block title %}}{title}{{% endblock %}}

{{% block content %}}
'''
    
    if layout == "sidebar":
        template += _generate_sidebar_layout(title, components, theme)
    else:
        template += _generate_topnav_layout(title, components, theme)
    
    template += '''
{% endblock %}
'''
    
    return template


def _generate_sidebar_layout(title, components, theme):
    """Generate sidebar layout."""
    layout = '''
<div class="drawer lg:drawer-open">
  <input id="main-drawer" type="checkbox" class="drawer-toggle" />
  
  <!-- Main content area -->
  <div class="drawer-content flex flex-col">
    <!-- Top bar -->
    <div class="navbar bg-base-200 shadow-md">
      <div class="flex-1">
        <label for="main-drawer" class="btn btn-square btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </label>
        <h1 class="text-2xl font-bold ml-2">''' + title + '''</h1>
      </div>
      <div class="flex-none">
        <button class="btn btn-ghost btn-circle">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Page content -->
    <div class="p-6 bg-base-100">
'''
    
    # Add components
    if "stats" in components:
        layout += '''
      <!-- Stats Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        {% if stats %}
          {% for stat in stats %}
          <div class="stats shadow">
            <div class="stat">
              <div class="stat-title">{{ stat.title }}</div>
              <div class="stat-value text-primary">{{ stat.value }}</div>
              <div class="stat-desc">{{ stat.description }}</div>
            </div>
          </div>
          {% endfor %}
        {% else %}
          <div class="stats shadow">
            <div class="stat">
              <div class="stat-title">Total Revenue</div>
              <div class="stat-value text-primary">$45,231</div>
              <div class="stat-desc">↗︎ 23% from last month</div>
            </div>
          </div>
          <div class="stats shadow">
            <div class="stat">
              <div class="stat-title">New Users</div>
              <div class="stat-value text-secondary">1,234</div>
              <div class="stat-desc">↗︎ 12% from last month</div>
            </div>
          </div>
          <div class="stats shadow">
            <div class="stat">
              <div class="stat-title">Active Sessions</div>
              <div class="stat-value">567</div>
              <div class="stat-desc">↘︎ 5% from last month</div>
            </div>
          </div>
          <div class="stats shadow">
            <div class="stat">
              <div class="stat-title">Conversion Rate</div>
              <div class="stat-value text-accent">3.2%</div>
              <div class="stat-desc">↗︎ 0.3% from last month</div>
            </div>
          </div>
        {% endif %}
      </div>
'''
    
    if "charts" in components:
        layout += '''
      <!-- Charts -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Revenue Trend</h2>
            <canvas id="revenueChart"></canvas>
          </div>
        </div>
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">User Growth</h2>
            <canvas id="userChart"></canvas>
          </div>
        </div>
      </div>
'''
    
    if "table" in components:
        layout += '''
      <!-- Data Table -->
      <div class="card bg-base-100 shadow-xl">
        <div class="card-body">
          <h2 class="card-title">Recent Transactions</h2>
          <div class="overflow-x-auto">
            <table class="table table-zebra">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Amount</th>
                  <th>Status</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {% if transactions %}
                  {% for transaction in transactions %}
                  <tr>
                    <td>{{ transaction.id }}</td>
                    <td>{{ transaction.name }}</td>
                    <td>${{ transaction.amount }}</td>
                    <td><span class="badge badge-success">{{ transaction.status }}</span></td>
                    <td>{{ transaction.date }}</td>
                  </tr>
                  {% endfor %}
                {% else %}
                  <tr>
                    <td>#001</td>
                    <td>John Doe</td>
                    <td>$1,234.56</td>
                    <td><span class="badge badge-success">Completed</span></td>
                    <td>2024-01-15</td>
                  </tr>
                {% endif %}
              </tbody>
            </table>
          </div>
        </div>
      </div>
'''
    
    layout += '''
    </div>
  </div>

  <!-- Sidebar -->
  <div class="drawer-side">
    <label for="main-drawer" class="drawer-overlay"></label>
    <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
      <li class="mb-2">
        <a class="text-xl font-bold">KD Dashboard</a>
      </li>
      <li><a href="/dashboard" class="active"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>Dashboard</a></li>
      <li><a href="/analytics"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>Analytics</a></li>
      <li><a href="/users"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>Users</a></li>
      <li><a href="/settings"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>Settings</a></li>
    </ul>
  </div>
</div>
'''
    
    return layout


def _generate_topnav_layout(title, components, theme):
    """Generate top navigation layout."""
    return '''
<div class="min-h-screen bg-base-100">
  <!-- Top Navigation -->
  <div class="navbar bg-base-200 shadow-md">
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">''' + title + '''</a>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal px-1">
        <li><a>Dashboard</a></li>
        <li><a>Analytics</a></li>
        <li><a>Users</a></li>
        <li><a>Settings</a></li>
      </ul>
    </div>
  </div>

  <!-- Content -->
  <div class="container mx-auto p-6">
    <!-- Add components here -->
    <p>Top navigation layout - components to be added</p>
  </div>
</div>
'''
