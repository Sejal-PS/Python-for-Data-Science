# Matplotlib - Pie Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Pie Chart
# ==================================================

labels = [
    "Python",
    "Pandas",
    "NumPy",
    "SQL"
]

students = [
    40,
    30,
    20,
    10
]

plt.pie(
    students,
    labels=labels
)

plt.title("Student Technology Preference")

plt.show()


# ==================================================
# 2. Show Percentage
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 3. Custom Colors
# ==================================================

colors = [
    "blue",
    "orange",
    "green",
    "purple"
]

plt.pie(
    students,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%"
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 4. Explode a Slice
# ==================================================

explode = [
    0.1,
    0,
    0,
    0
]

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 5. Shadow
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 6. Start Angle
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 7. Employee Department Distribution
# ==================================================

departments = [
    "IT",
    "HR",
    "Sales",
    "Finance",
    "Marketing"
]

employees = [
    30,
    15,
    25,
    10,
    20
]

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Employee Distribution by Department")

plt.show()


# ==================================================
# 8. Sales Distribution by Product
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    400000,
    300000,
    150000,
    100000
]

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Product")

plt.show()


# ==================================================
# 9. Donut Chart
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    400,
    300,
    150,
    100
]

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={
        "width": 0.4
    }
)

plt.title("Product Sales Distribution")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

expense_categories = [
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

colors = [
    "#ff9999",
    "#66b3ff",
    "#99ff99",
    "#ffcc99",
    "#c2c2f0"
]

plt.figure(
    figsize=(8, 6)
)

plt.pie(
    expenses,
    labels=expense_categories,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Monthly Expense Distribution")

plt.show()
