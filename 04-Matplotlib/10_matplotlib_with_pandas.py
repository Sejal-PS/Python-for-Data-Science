# Matplotlib with Pandas

import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# 1. Create DataFrame
# ==================================================

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 16000, 22000, 25000],
    "Profit": [2000, 2500, 3200, 2800, 4000, 5000]
}

df = pd.DataFrame(data)

print(df)


# ==================================================
# 2. Line Plot using Pandas DataFrame
# ==================================================

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 3. Plot DataFrame Column Directly
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o"
)

plt.title("Monthly Sales")

plt.show()


# ==================================================
# 4. Bar Chart using Pandas
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="bar",
    color="skyblue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 5. Multiple Columns
# ==================================================

df.plot(
    x="Month",
    y=["Sales", "Profit"],
    kind="line",
    marker="o"
)

plt.title("Sales and Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 6. Multiple Bar Charts
# ==================================================

df.plot(
    x="Month",
    y=["Sales", "Profit"],
    kind="bar"
)

plt.title("Sales vs Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.show()


# ==================================================
# 7. Scatter Plot using DataFrame
# ==================================================

df.plot(
    x="Sales",
    y="Profit",
    kind="scatter",
    color="red"
)

plt.title("Sales vs Profit")

plt.xlabel("Sales")

plt.ylabel("Profit")

plt.show()


# ==================================================
# 8. Create City-wise Data
# ==================================================

city_data = {
    "City": [
        "Pune",
        "Mumbai",
        "Nashik",
        "Nagpur",
        "Thane"
    ],
    "Sales": [
        50000,
        75000,
        40000,
        60000,
        85000
    ]
}

city_df = pd.DataFrame(city_data)

print(city_df)


# ==================================================
# 9. City-wise Sales Bar Chart
# ==================================================

city_df.plot(
    x="City",
    y="Sales",
    kind="bar",
    color="green"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.xticks(
    rotation=0
)

plt.show()


# ==================================================
# 10. GroupBy + Matplotlib
# ==================================================

sales_data = {
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Mumbai",
        "Nashik",
        "Nashik"
    ],
    "Sales": [
        10000,
        15000,
        12000,
        18000,
        9000,
        11000
    ]
}

sales_df = pd.DataFrame(sales_data)

city_sales = (
    sales_df
    .groupby("City")["Sales"]
    .sum()
)

print(city_sales)


city_sales.plot(
    kind="bar",
    color="orange"
)

plt.title("Total Sales by City")

plt.xlabel("City")

plt.ylabel("Total Sales")

plt.xticks(
    rotation=0
)

plt.show()


# ==================================================
# 11. Histogram using Pandas
# ==================================================

marks_data = {
    "Marks": [
        45, 50, 55, 60,
        62, 65, 68, 70,
        72, 75, 78, 80,
        82, 85, 88, 90,
        92, 95
    ]
}

marks_df = pd.DataFrame(marks_data)

marks_df["Marks"].plot(
    kind="hist",
    bins=6,
    color="purple",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 12. DataFrame Plot with Figure Size
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o",
    figsize=(10, 5),
    color="blue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 13. Real Data Science Example
# ==================================================

customer_data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Customers": [
        100,
        120,
        150,
        140,
        180,
        210
    ],
    "Sales": [
        12000,
        15000,
        18000,
        16000,
        22000,
        25000
    ]
}

customer_df = pd.DataFrame(
    customer_data
)

fig, axes = plt.subplots(
    1,
    2,
    figsize=(12, 5)
)


# Customer Trend

axes[0].plot(
    customer_df["Month"],
    customer_df["Customers"],
    marker="o",
    color="green"
)

axes[0].set_title(
    "Customer Trend"
)

axes[0].set_xlabel(
    "Month"
)

axes[0].set_ylabel(
    "Customers"
)


# Sales Trend

axes[1].bar(
    customer_df["Month"],
    customer_df["Sales"],
    color="steelblue"
)

axes[1].set_title(
    "Sales Trend"
)

axes[1].set_xlabel(
    "Month"
)

axes[1].set_ylabel(
    "Sales"
)


plt.tight_layout()

plt.show()
