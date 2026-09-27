# Matplotlib - Scatter Plot

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Scatter Plot
# ==================================================

x = [1, 2, 3, 4, 5]

y = [10, 15, 12, 20, 25]

plt.scatter(
    x,
    y
)

plt.title("Basic Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 2. Scatter Plot with Color
# ==================================================

plt.scatter(
    x,
    y,
    color="blue"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 3. Scatter Plot with Size
# ==================================================

plt.scatter(
    x,
    y,
    color="green",
    s=100
)

plt.title("Scatter Plot with Marker Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 4. Scatter Plot with Transparency
# ==================================================

plt.scatter(
    x,
    y,
    color="red",
    alpha=0.5
)

plt.title("Scatter Plot with Transparency")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 5. Study Hours vs Marks
# ==================================================

study_hours = [
    1,
    2,
    2.5,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

marks = [
    40,
    45,
    50,
    55,
    60,
    68,
    72,
    78,
    85,
    92
]

plt.scatter(
    study_hours,
    marks,
    color="purple",
    s=80
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 6. Age vs Salary
# ==================================================

age = [
    22,
    24,
    25,
    27,
    29,
    30,
    32,
    35,
    38,
    40
]

salary = [
    28000,
    32000,
    35000,
    40000,
    45000,
    50000,
    55000,
    65000,
    75000,
    85000
]

plt.scatter(
    age,
    salary,
    color="orange",
    s=90
)

plt.title("Age vs Salary")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 7. Two Groups in One Scatter Plot
# ==================================================

study_hours_a = [
    1,
    2,
    3,
    4,
    5
]

marks_a = [
    45,
    50,
    60,
    65,
    72
]

study_hours_b = [
    4,
    5,
    6,
    7,
    8
]

marks_b = [
    60,
    70,
    78,
    85,
    92
]

plt.scatter(
    study_hours_a,
    marks_a,
    color="blue",
    label="Group A"
)

plt.scatter(
    study_hours_b,
    marks_b,
    color="red",
    label="Group B"
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.show()


# ==================================================
# 8. Scatter Plot with Different Sizes
# ==================================================

x = [
    10,
    20,
    30,
    40,
    50
]

y = [
    20,
    35,
    30,
    55,
    70
]

sizes = [
    50,
    100,
    150,
    250,
    350
]

plt.scatter(
    x,
    y,
    s=sizes,
    color="green",
    alpha=0.6
)

plt.title("Scatter Plot with Different Sizes")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 9. Sales vs Advertising Spend
# ==================================================

advertising = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

sales = [
    20,
    25,
    35,
    42,
    50,
    60,
    65,
    75
]

plt.scatter(
    advertising,
    sales,
    color="teal",
    s=100
)

plt.title("Advertising Spend vs Sales")

plt.xlabel("Advertising Spend")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

salary = [
    30000,
    34000,
    38000,
    42000,
    47000,
    52000,
    58000,
    65000,
    73000,
    82000
]

plt.figure(
    figsize=(9, 5)
)

plt.scatter(
    experience,
    salary,
    color="darkblue",
    s=100,
    alpha=0.7
)

plt.title("Experience vs Salary")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)



here  s means size of point /marker and alpha means transparency 

plt.show()
