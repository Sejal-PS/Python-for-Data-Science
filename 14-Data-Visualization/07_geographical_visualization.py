import plotly.express as px

data = {
    "City": ["Mumbai", "Pune", "Delhi", "Bengaluru", "Chennai"],
    "Latitude": [19.0760, 18.5204, 28.6139, 12.9716, 13.0827],
    "Longitude": [72.8777, 73.8567, 77.2090, 77.5946, 80.2707],
    "Sales": [500, 350, 420, 600, 300]
}

fig = px.scatter_map(
    data,
    lat="Latitude",
    lon="Longitude",
    size="Sales",
    color="Sales",
    hover_name="City",
    zoom=4,
    title="Sales by City"
)

fig.show()
