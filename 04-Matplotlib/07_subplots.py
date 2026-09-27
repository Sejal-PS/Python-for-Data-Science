# Matplotlib - Subplots

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Subplot - 1 Row, 2 Columns
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


plt.subplot(1, 2, 1)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales")

plt.xlabel("Month")

plt.ylabel("Sales")


plt.subplot(1, 2, 2)

plt.plot(
    months,
    profit,
    marker="o",
    color="green"
)

plt.title("Profit")

plt.xlabel("Month")

plt.ylabel("Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 2. 2 Rows, 1 Column
# ==================================================

plt.subplot(2, 1, 1)

plt.bar(
    months,
    sales,
    color="skyblue"
)

plt.title("Monthly Sales")


plt.subplot(2, 1, 2)

plt.bar(
    months,
    profit,
    color="orange"
)

plt.title("Monthly Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 3. 2 Rows, 2 Columns
# ==================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


# First Plot

axes[0, 0].plot(
    months,
    sales,
    marker="o"
)

axes[0, 0].set_title("Sales")


# Second Plot

axes[0, 1].bar(
    months,
    profit,
    color="green"
)

axes[0, 1].set_title("Profit")


# Third Plot

axes[1, 0].scatter(
    sales,
    profit,
    color="red"
)

axes[1, 0].set_title("Sales vs Profit")

axes[1, 0].set_xlabel("Sales")

axes[1, 0].set_ylabel("Profit")


# Fourth Plot

axes[1, 1].hist(
    sales,
    bins=5,
    color="purple",
    edgecolor="black"
)

axes[1, 1].set_title("Sales Distribution")


plt.tight_layout()

plt.show()


# ==================================================
# 4. Different Charts in One Figure
# ==================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


# Line Chart

axes[0, 0].plot(
    months,
    sales,
    marker="o"
)

axes[0, 0].set_title("Line Chart")


# Bar Chart

axes[0, 1].bar(
    months,
    sales,
    color="orange"
)

axes[0, 1].set_title("Bar Chart")


# Scatter Plot

axes[1, 0].scatter(
    sales,
    profit,
    color="red"
)

axes[1, 0].set_title("Scatter Plot")


# Pie Chart

labels = [
    "Sales",
    "Profit"
]

values = [
    sum(sales),
    sum(profit)
]

axes[1, 1].pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

axes[1, 1].set_title("Sales vs Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 5. Real Data Science Dashboard Example
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


fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)


# -------------------------
# Monthly Sales
# -------------------------

axes[0, 0].plot(
    months,
    sales,
    marker="o",
    color="blue"
)

axes[0, 0].set_title(
    "Monthly Sales"
)

axes[0, 0].set_xlabel(
    "Month"
)

axes[0, 0].set_ylabel(
    "Sales"
)


# -------------------------
# Customer Count
# -------------------------

axes[0, 1].bar(
    months,
    customers,
    color="green"
)

axes[0, 1].set_title(
    "Monthly Customers"
)

axes[0, 1].set_xlabel(
    "Month"
)

axes[0, 1].set_ylabel(
    "Customers"
)


# -------------------------
# Sales vs Profit
# -------------------------

axes[1, 0].scatter(
    sales,
    profit,
    color="red",
    s=80
)

axes[1, 0].set_title(
    "Sales vs Profit"
)

axes[1, 0].set_xlabel(
    "Sales"
)

axes[1, 0].set_ylabel(
    "Profit"
)


# -------------------------
# Sales Distribution
# -------------------------

axes[1, 1].hist(
    sales,
    bins=5,
    color="purple",
    edgecolor="black"
)

axes[1, 1].set_title(
    "Sales Distribution"
)

axes[1, 1].set_xlabel(
    "Sales"
)

axes[1, 1].set_ylabel(
    "Frequency"
)


plt.suptitle(
    "Sales Data Analysis Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.show()
