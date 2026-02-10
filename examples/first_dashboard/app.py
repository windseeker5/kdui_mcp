"""
First Dashboard Example - KD UI Framework
A simple sales dashboard to showcase the MCP server capabilities
"""

from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock data for the dashboard
def get_dashboard_data():
    """Generate mock data for the dashboard"""
    
    # Stats - format compatible with the Shadcn template
    stats = [
        {
            'title': 'Total Revenue',
            'value': '$45,231',
            'description': '+20.1% from last month',
            'icon': 'dollar-sign',
            'trend_color': 'green',
            'trend_icon': 'trending-up'
        },
        {
            'title': 'New Users',
            'value': '1,234',
            'description': '+12.5% from last month',
            'icon': 'users',
            'trend_color': 'green',
            'trend_icon': 'trending-up'
        },
        {
            'title': 'Active Sessions',
            'value': '567',
            'description': '-5.2% from last month',
            'icon': 'activity',
            'trend_color': 'red',
            'trend_icon': 'trending-down'
        },
        {
            'title': 'Conversion Rate',
            'value': '3.2%',
            'description': '+0.3% from last month',
            'icon': 'percent',
            'trend_color': 'green',
            'trend_icon': 'trending-up'
        }
    ]
    
    # Revenue trend (last 7 days)
    revenue_trend = {
        'labels': [(datetime.now() - timedelta(days=i)).strftime('%a') for i in range(6, -1, -1)],
        'data': [4200, 3800, 4500, 4100, 4800, 5200, 4900]
    }
    
    # Recent orders
    orders = [
        {'id': '#12345', 'customer': 'John Smith', 'amount': '$234.50', 'status': 'completed'},
        {'id': '#12344', 'customer': 'Sarah Johnson', 'amount': '$567.20', 'status': 'completed'},
        {'id': '#12343', 'customer': 'Mike Brown', 'amount': '$123.00', 'status': 'processing'},
        {'id': '#12342', 'customer': 'Emily Davis', 'amount': '$445.75', 'status': 'completed'},
        {'id': '#12341', 'customer': 'Chris Wilson', 'amount': '$892.30', 'status': 'pending'},
    ]
    
    return {
        'stats': stats,
        'revenue_trend': revenue_trend,
        'orders': orders
    }


@app.route('/')
def dashboard():
    """Main dashboard route"""
    data = get_dashboard_data()
    return render_template('dashboard.html', **data)


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🎨 KD UI Framework - First Dashboard Example")
    print("="*50)
    print("\n🚀 Starting Flask server...")
    print("📊 Dashboard available at: http://localhost:5001")
    print("\nPress Ctrl+C to stop\n")
    app.run(debug=True, port=5001)
