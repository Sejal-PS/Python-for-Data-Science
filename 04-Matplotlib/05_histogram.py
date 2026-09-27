# Matplotlib - Histogram

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Histogram
# ==================================================

marks = [
    45, 50, 55, 60, 62,
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

plt.hist(marks)

plt.title("Distribution of Marks")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 2. Histogram with Bins
# ==================================================

plt.hist(
    marks,
    bins=5
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 3. Customized Histogram
# ==================================================

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 4. Exam Marks Distribution
# ==================================================

marks = [
    35, 42, 48, 50, 55,
    58, 60, 62, 65, 68,
    70, 72, 75, 78, 80,
    82, 85, 88, 90, 92,
    95, 97
]

plt.hist(
    marks,
    bins=10,
    color="green",
    edgecolor="black"
)

plt.title("Student Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 5. Employee Age Distribution
# ==================================================

ages = [
    22, 24, 25, 26, 27,
    28, 29, 30, 31, 32,
    33, 34, 35, 36, 38,
    40, 42, 45
]

plt.hist(
    ages,
    bins=6,
    color="orange",
    edgecolor="black"
)

plt.title("Employee Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Employees")

plt.show()


# ==================================================
# 6. Salary Distribution
# ==================================================

salary = [
    25000, 28000, 30000, 32000,
    35000, 38000, 40000, 42000,
    45000, 48000, 50000, 52000,
    55000, 58000, 60000, 65000,
    70000, 75000, 80000
]

plt.hist(
    salary,
    bins=7,
    color="purple",
    edgecolor="black"
)

plt.title("Salary Distribution")

plt.xlabel("Salary")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 7. Histogram with Density
# ==================================================

plt.hist(
    marks,
    bins=10,
    density=True,
    color="teal",
    edgecolor="black"
)

plt.title("Marks Distribution - Density")

plt.xlabel("Marks")

plt.ylabel("Density")

plt.show()


# ==================================================
# 8. Compare Two Distributions
# ==================================================

class_a = [
    55, 60, 62, 65, 68,
    70, 72, 75, 78, 80
]

class_b = [
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 90
]

plt.hist(
    class_a,
    bins=5,
    alpha=0.5,
    label="Class A"
)

plt.hist(
    class_b,
    bins=5,
    alpha=0.5,
    label="Class B"
)

plt.title("Class Marks Comparison")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.legend()

plt.show()


# ==================================================
# 9. Horizontal Histogram
# ==================================================

plt.hist(
    marks,
    bins=10,
    orientation="horizontal",
    color="coral",
    edgecolor="black"
)

plt.title("Horizontal Histogram")

plt.xlabel("Frequency")

plt.ylabel("Marks")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

customer_age = [
    18, 20, 21, 22, 23,
    25, 26, 27, 28, 29,
    30, 31, 32, 34, 35,
    36, 38, 40, 42, 45,
    48, 50, 52, 55, 60
]

plt.figure(
    figsize=(9, 5)
)

plt.hist(
    customer_age,
    bins=8,
    color="steelblue",
    edgecolor="black"
)

plt.title("Customer Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Customers")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()
