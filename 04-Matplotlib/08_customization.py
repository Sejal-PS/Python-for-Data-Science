# Matplotlib - Plot Customization

import matplotlib.pyplot as plt


# ==================================================
# 1. Color
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [10000, 15000, 13000, 18000, 22000]

plt.plot(
    months,
    sales,
    color="blue"
)

plt.title("Sales")

plt.show()


# ==================================================
# 2. Line Style
# ==================================================

plt.plot(
    months,
    sales,
    linestyle="--"
)

plt.title("Dashed Line")

plt.show()


# ==================================================
# 3. Line Width
# ==================================================

plt.plot(
    months,
    sales,
    linewidth=4
)

plt.title("Thick Line")

plt.show()


# ==================================================
# 4. Markers
# ==================================================

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Line with Markers")

plt.show()


# ==================================================
# 5. Marker Size and Color
# ==================================================

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    markersize=8
)

plt.title("Customized Markers")

plt.show()


# ==================================================
# 6. Complete Line Customization
# ==================================================

plt.plot(
    months,
    sales,
    color="purple",
    linestyle="--",
    linewidth=2,
    marker="o",
    markersize=8
)

plt.title(
    "Monthly Sales",
    fontsize=16
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 7. Legend
# ==================================================

sales_2024 = [10000, 12000, 15000, 16000, 18000]

sales_2025 = [12000, 15000, 17000, 20000, 23000]

plt.plot(
    months,
    sales_2024,
    marker="o",
    label="2024"
)

plt.plot(
    months,
    sales_2025,
    marker="o",
    label="2025"
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 8. Legend Location
# ==================================================

plt.plot(
    months,
    sales_2024,
    label="2024"
)

plt.plot(
    months,
    sales_2025,
    label="2025"
)

plt.title("Sales Comparison")

plt.legend(
    loc="upper left"
)

plt.show()


# ==================================================
# 9. Rotate X-axis Labels
# ==================================================

products = [
    "Laptop",
    "Mobile Phone",
    "Tablet",
    "Monitor",
    "Keyboard"
]

product_sales = [
    120000,
    90000,
    60000,
    45000,
    25000
]

plt.bar(
    products,
    product_sales,
    color="skyblue"
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.xticks(
    rotation=30
)

plt.show()


# ==================================================
# 10. Figure Size
# ==================================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 11. Grid Customization
# ==================================================

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales with Grid")

plt.grid(
    color="gray",
    linestyle="--",
    linewidth=0.7,
    alpha=0.6
)

plt.show()


# ==================================================
# 12. Set Axis Limits
# ==================================================

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xlim(
    1,
    5
)

plt.ylim(
    0,
    60
)

plt.title("Axis Limits")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# ==================================================
# 13. Add Text / Annotation
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
    25000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.annotate(
    "Highest Sales",
    xy=("May", 25000),
    xytext=("Mar", 22000),
    arrowprops={
        "arrowstyle": "->"
    }
)

plt.title("Monthly Sales")

plt.show()


# ==================================================
# 14. Bar Chart Customization
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur"
]

sales = [
    50000,
    75000,
    40000,
    60000
]

plt.bar(
    cities,
    sales,
    color=[
        "blue",
        "green",
        "orange",
        "purple"
    ],
    edgecolor="black"
)

plt.title(
    "City-wise Sales",
    fontsize=16
)

plt.xlabel("City")

plt.ylabel("Sales")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 15. Real Data Science Visualization
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

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    months,
    sales,
    color="#2563EB",
    linestyle="-",
    linewidth=2.5,
    marker="o",
    markersize=7,
    markerfacecolor="white",
    markeredgewidth=2
)

plt.title(
    "Monthly Sales Analysis",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.xticks(
    fontsize=10
)

plt.yticks(
    fontsize=10
)

plt.tight_layout()

plt.show()
