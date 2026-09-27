# Matplotlib - Line Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Line Chart
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [10000, 12000, 15000, 13000, 18000, 22000]

plt.plot(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 2. Line Chart with Markers
# ==================================================

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
# 3. Customized Line Chart
# ==================================================

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# ==================================================
# 4. Sales Comparison
# ==================================================

sales_2024 = [
    10000,
    12000,
    14000,
    16000,
    17000,
    19000
]

sales_2025 = [
    12000,
    15000,
    16000,
    18000,
    22000,
    25000
]

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

plt.title("Sales Comparison: 2024 vs 2025")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# ==================================================
# 5. Student Marks Trend
# ==================================================

subjects = [
    "Maths",
    "Science",
    "English",
    "Python",
    "Statistics"
]

marks = [
    75,
    82,
    78,
    90,
    85
]

plt.plot(
    subjects,
    marks,
    marker="o",
    color="blue"
)

plt.title("Student Marks")

plt.xlabel("Subject")

plt.ylabel("Marks")

plt.grid()

plt.show()


# ==================================================
# 6. Employee Salary Trend
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6
]

salary = [
    30000,
    35000,
    40000,
    47000,
    55000,
    65000
]

plt.plot(
    experience,
    salary,
    marker="o",
    color="purple"
)

plt.title("Salary vs Experience")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid()

plt.show()


# ==================================================
# 7. Multiple Line Charts
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

product_a = [
    100,
    120,
    150,
    130,
    170,
    200
]

product_b = [
    80,
    100,
    110,
    140,
    160,
    180
]

product_c = [
    60,
    90,
    100,
    120,
    150,
    170
]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A"
)

plt.plot(
    months,
    product_b,
    marker="s",
    label="Product B"
)

plt.plot(
    months,
    product_c,
    marker="^",
    label="Product C"
)

plt.title("Product Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# ==================================================
# 8. Add Data Points
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
    22000
]

plt.plot(
    months,
    sales,
    marker="o",
    color="red"
)

for month, sale in zip(months, sales):
    plt.text(
        month,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("Monthly Sales with Values")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# ==================================================
# 9. Real Data Science Example
# ==================================================

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

website_visitors = [
    120,
    150,
    140,
    180,
    220,
    300,
    250
]

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    days,
    website_visitors,
    marker="o",
    color="orange",
    linewidth=2
)

plt.title("Weekly Website Visitors")

plt.xlabel("Day")

plt.ylabel("Number of Visitors")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()
