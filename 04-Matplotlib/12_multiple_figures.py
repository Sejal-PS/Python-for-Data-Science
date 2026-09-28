"""
Multiple Figures in Matplotlib

Sometimes we need to create more than one
independent figure in a program.
"""

import matplotlib.pyplot as plt


# --------------------------------------------------
# Figure 1 - Line Chart
# --------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    y,
    marker="o",
    color="blue"
)

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()


# --------------------------------------------------
# Figure 2 - Bar Chart
# --------------------------------------------------

products = ["Laptop", "Mobile", "Tablet"]
sales = [50000, 35000, 20000]

plt.figure(figsize=(8, 5))

plt.bar(
    products,
    sales,
    color=["blue", "green", "orange"]
)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()


# --------------------------------------------------
# Figure 3 - Scatter Plot
# --------------------------------------------------

hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 65, 75, 85]

plt.figure(figsize=(8, 5))

plt.scatter(
    hours,
    marks,
    color="purple"
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create three independent figures.
# 2. Create a line chart in the first figure.
# 3. Create a bar chart in the second figure.
# 4. Create a scatter plot in the third figure.
