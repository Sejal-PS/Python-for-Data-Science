# Matplotlib - Saving Plots

import matplotlib.pyplot as plt


# ==================================================
# 1. Save a Basic Line Chart
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [10000, 15000, 13000, 18000, 22000]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.savefig(
    "monthly_sales.png"
)

plt.show()


# ==================================================
# 2. Save with Figure Size
# ==================================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    months,
    sales,
    color="skyblue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_large.png"
)

plt.show()


# ==================================================
# 3. Save as PNG with High Resolution
# ==================================================

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="green"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_high_resolution.png",
    dpi=300
)

plt.show()


# ==================================================
# 4. Save with Transparent Background
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="purple"
)

plt.title("Monthly Sales")

plt.savefig(
    "monthly_sales_transparent.png",
    transparent=True
)

plt.show()


# ==================================================
# 5. Save with Tight Bounding Box
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_tight.png",
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 6. Save Bar Chart
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur"
]

city_sales = [
    50000,
    75000,
    40000,
    60000
]

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    cities,
    city_sales,
    color="orange"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.savefig(
    "city_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 7. Save Scatter Plot
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6,
    7
]

salary = [
    30000,
    35000,
    40000,
    47000,
    55000,
    65000,
    75000
]

plt.figure(
    figsize=(8, 5)
)

plt.scatter(
    experience,
    salary,
    color="red",
    s=80
)

plt.title("Experience vs Salary")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.savefig(
    "experience_vs_salary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 8. Save Histogram
# ==================================================

marks = [
    45, 50, 55, 60, 62,
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

plt.figure(
    figsize=(8, 5)
)

plt.hist(
    marks,
    bins=6,
    color="steelblue",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.savefig(
    "marks_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 9. Save Pie Chart
# ==================================================

categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Other"
]

expenses = [
    15000,
    8000,
    25000,
    10000,
    5000
]

plt.figure(
    figsize=(7, 7)
)

plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Monthly Expense Distribution")

plt.savefig(
    "expense_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 10. Save Chart in Different Formats
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="blue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

# PNG
plt.savefig(
    "sales_chart.png"
)

# PDF
plt.savefig(
    "sales_chart.pdf"
)

# SVG
plt.savefig(
    "sales_chart.svg"
)

plt.show()
