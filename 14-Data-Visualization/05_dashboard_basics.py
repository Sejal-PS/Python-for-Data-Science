import plotly.graph_objects as go
from plotly.subplots import make_subplots

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 140, 130, 180, 210]
profit = [20, 35, 30, 45, 55]

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Sales", "Profit")
)

fig.add_trace(
    go.Bar(x=months, y=sales, name="Sales"),
    row=1,
    col=1
)

fig.add_trace(
    go.Bar(x=months, y=profit, name="Profit"),
    row=1,
    col=2
)

fig.update_layout(
    title="Business Performance Dashboard",
    showlegend=False
)

fig.show()
