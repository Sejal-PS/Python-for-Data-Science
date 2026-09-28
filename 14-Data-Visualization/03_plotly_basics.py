import plotly.express as px

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 135, 180, 210, 195]
}

fig = px.line(
    data,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales"
)

fig.show()
