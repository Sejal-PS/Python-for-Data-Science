# Matplotlib - Practice Questions

import matplotlib.pyplot as plt


# ==================================================
# Practice 1 - Basic Line Plot
# ==================================================

# Create a line chart using the following data.

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    10000,
    12000,
    15000,
    13000,
    18000,
    22000
]

# Tasks:
# 1. Create a line plot.
# 2. Add a title.
# 3. Add X-axis label.
# 4. Add Y-axis label.
# 5. Add grid.
# 6. Add markers.


# ==================================================
# Practice 2 - Bar Chart
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard"
]

sales = [
    120000,
    90000,
    60000,
    45000,
    25000
]

# Tasks:
# 1. Create a bar chart.
# 2. Give the chart a title.
# 3. Add X-axis and Y-axis labels.
# 4. Change the bar color.
# 5. Display the values on top of each bar.


# ==================================================
# Practice 3 - Scatter Plot
# ==================================================

study_hours = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]

marks = [
    40,
    45,
    50,
    58,
    65,
    72,
    80,
    90
]

# Tasks:
# 1. Create a scatter plot.
# 2. Put Study Hours on X-axis.
# 3. Put Marks on Y-axis.
# 4. Change marker color.
# 5. Change marker size.
# 6. Add grid.


# ==================================================
# Practice 4 - Histogram
# ==================================================

student_marks = [
    35, 40, 45, 50, 52,
    55, 58, 60, 62, 65,
    68, 70, 72, 75, 78,
    80, 82, 85, 88, 90,
    92, 95
]

# Tasks:
# 1. Create a histogram.
# 2. Use 5 bins.
# 3. Add edgecolor.
# 4. Add title.
# 5. Add X-axis and Y-axis labels.


# ==================================================
# Practice 5 - Pie Chart
# ==================================================

expenses = [
    15000,
    8000,
    25000,
    10000,
    5000
]

categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Other"
]

# Tasks:
# 1. Create a pie chart.
# 2. Add category labels.
# 3. Show percentages.
# 4. Change the colors.
# 5. Set startangle to 90.


# ==================================================
# Practice 6 - Multiple Lines
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales_2024 = [
    100,
    120,
    150,
    160,
    180
]

sales_2025 = [
    120,
    140,
    170,
    200,
    230
]

# Tasks:
# 1. Plot both years in one chart.
# 2. Use different colors.
# 3. Add markers.
# 4. Add legend.
# 5. Add title.
# 6. Add grid.


# ==================================================
# Practice 7 - Subplots
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    22000
]

profit = [
    2000,
    3000,
    2500,
    4000,
    5500
]

customers = [
    100,
    120,
    110,
    150,
    180
]

# Tasks:
# Create a 2x2 subplot layout.

# Plot 1:
# Monthly Sales - Line Chart

# Plot 2:
# Monthly Profit - Bar Chart

# Plot 3:
# Monthly Customers - Line Chart

# Plot 4:
# Sales vs Profit - Scatter Plot


# ==================================================
# Practice 8 - Plot Customization
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    14000,
    12000,
    18000,
    25000
]

# Tasks:
# Create a line chart and customize:
#
# 1. Line color
# 2. Line style
# 3. Line width
# 4. Marker
# 5. Marker size
# 6. Title font size
# 7. Axis labels
# 8. Grid
# 9. Figure size


# ==================================================
# Practice 9 - Sales Analysis
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur",
    "Thane"
]

sales = [
    50000,
    75000,
    40000,
    60000,
    85000
]

# Tasks:
# 1. Create a bar chart.
# 2. Find the city with the highest sales.
# 3. Display values on bars.
# 4. Add title.
# 5. Add axis labels.
# 6. Customize colors.


# ==================================================
# Practice 10 - DataFrame Visualization
# ==================================================

import pandas as pd


data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Sales": [
        12000,
        15000,
        18000,
        16000,
        22000,
        25000
    ],
    "Profit": [
        2000,
        2500,
        3200,
        2800,
        4000,
        5000
    ]
}

df = pd.DataFrame(data)

# Tasks:
# 1. Display the DataFrame.
# 2. Create a line chart for Sales.
# 3. Create a line chart for Profit.
# 4. Compare Sales and Profit.
# 5. Create a bar chart for Sales.
# 6. Create a scatter plot between Sales and Profit.


# ==================================================
# Practice 11 - Save Plot
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    22000
]

# Tasks:
# 1. Create a line chart.
# 2. Save it as "sales_chart.png".
# 3. Use dpi=300.
# 4. Use bbox_inches="tight".


# ==================================================
# Practice 12 - Mini Data Analysis
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    18000,
    16000,
    22000,
    25000
]

customers = [
    100,
    120,
    150,
    140,
    180,
    210
]

profit = [
    2000,
    2500,
    3200,
    2800,
    4000,
    5000
]

# Tasks:
#
# Create a simple visualization dashboard
# containing:
#
# 1. Sales trend
# 2. Customer trend
# 3. Sales vs Profit
# 4. Sales distribution
#
# Use subplots.
#
# Add:
# - Titles
# - Axis labels
# - Colors
# - Markers where required
# - Grid where useful
# - Proper spacing
