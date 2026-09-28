import plotly.graph_objects as go
from plotly.subplots import make_subplots

categories = ["Electronics", "Clothing", "Books", "Home"]
sales = [45000, 32000, 18000, 27000]

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Sales by Category", "Sales Trend")
)

fig.add_trace(
    go.Bar(x=categories, y=sales),
    row=1,
    col=1
)

months = ["Jan", "Feb", "Mar", "Apr", "May"]
monthly_sales = [25000, 30000, 28000, 36000, 42000]

fig.add_trace(
    go.Scatter(
        x=months,
        y=monthly_sales,
        mode="lines+markers"
    ),
    row=1,
    col=2
)

fig.update_layout(
    title="Business Sales Dashboard",
    height=500
)

fig.show()
