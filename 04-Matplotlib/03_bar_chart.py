# Matplotlib - Bar Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Bar Chart
# ==================================================

categories = [
    "Python",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "SQL"
]

students = [
    40,
    35,
    45,
    30,
    50
]

plt.bar(
    categories,
    students
)

plt.title("Students Enrolled")

plt.xlabel("Technology")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 2. Customized Bar Chart
# ==================================================

plt.bar(
    categories,
    students,
    color="skyblue"
)

plt.title("Students Enrolled")

plt.xlabel("Technology")

plt.ylabel("Number of Students")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 3. Horizontal Bar Chart
# ==================================================

plt.barh(
    categories,
    students,
    color="orange"
)

plt.title("Students Enrolled")

plt.xlabel("Number of Students")

plt.ylabel("Technology")

plt.show()


# ==================================================
# 4. Bar Chart with Different Colors
# ==================================================

colors = [
    "blue",
    "green",
    "orange",
    "purple",
    "red"
]

plt.bar(
    categories,
    students,
    color=colors
)

plt.title("Students Enrolled by Technology")

plt.xlabel("Technology")

plt.ylabel("Students")

plt.show()


# ==================================================
# 5. Sales by City
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

plt.bar(
    cities,
    sales,
    color="green"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 6. Bar Chart with Values
# ==================================================

plt.bar(
    cities,
    sales,
    color="teal"
)

for city, sale in zip(cities, sales):
    plt.text(
        city,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 7. Product Sales
# ==================================================

products = [
    "Laptop",
    "Mobile",
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
    color="steelblue"
)

plt.title("Product-wise Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.xticks(
    rotation=30
)

plt.show()


# ==================================================
# 8. Compare Two Categories
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales_2024 = [
    100,
    150,
    80,
    60
]

sales_2025 = [
    130,
    180,
    110,
    90
]

x = range(len(products))

width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    sales_2024,
    width=width,
    label="2024"
)

plt.bar(
    [i + width / 2 for i in x],
    sales_2025,
    width=width,
    label="2025"
)

plt.xticks(
    list(x),
    products
)

plt.title("Product Sales Comparison")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.legend()

plt.show()


# ==================================================
# 9. Employee Department Count
# ==================================================

departments = [
    "IT",
    "HR",
    "Sales",
    "Finance",
    "Marketing"
]

employees = [
    25,
    15,
    30,
    12,
    20
]

plt.barh(
    departments,
    employees,
    color="purple"
)

plt.title("Employees by Department")

plt.xlabel("Number of Employees")

plt.ylabel("Department")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

monthly_sales = [
    12000,
    15000,
    18000,
    14000,
    22000,
    25000
]

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    months,
    monthly_sales,
    color="cornflowerblue"
)

for month, sale in zip(
    months,
    monthly_sales
):
    plt.text(
        month,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()
