"""
NumPy Array Operations

This file covers common array operations that are useful
when working with numerical data in Data Science.
"""

import numpy as np


# --------------------------------------------------
# 1. Create Arrays
# --------------------------------------------------

sales_january = np.array([1200, 1500, 1800, 1100, 2100])
sales_february = np.array([1300, 1600, 1750, 1250, 2200])

print("January Sales:")
print(sales_january)

print("\nFebruary Sales:")
print(sales_february)


# --------------------------------------------------
# 2. Compare Two Arrays
# --------------------------------------------------

comparison = sales_february > sales_january

print("\nFebruary sales higher than January:")
print(comparison)


# --------------------------------------------------
# 3. Element-wise Maximum
# --------------------------------------------------

higher_sales = np.maximum(
    sales_january,
    sales_february
)

print("\nHigher sales for each day:")
print(higher_sales)


# --------------------------------------------------
# 4. Element-wise Minimum
# --------------------------------------------------

lower_sales = np.minimum(
    sales_january,
    sales_february
)

print("\nLower sales for each day:")
print(lower_sales)


# --------------------------------------------------
# 5. Difference Between Arrays
# --------------------------------------------------

sales_difference = sales_february - sales_january

print("\nSales difference:")
print(sales_difference)


# --------------------------------------------------
# 6. Absolute Difference
# --------------------------------------------------

absolute_difference = np.abs(
    sales_february - sales_january
)

print("\nAbsolute difference:")
print(absolute_difference)


# --------------------------------------------------
# 7. Check Conditions
# --------------------------------------------------

print("\nAny day with sales above 2000:")
print(np.any(sales_february > 2000))

print("\nAll January sales above 1000:")
print(np.all(sales_january > 1000))


# --------------------------------------------------
# 8. Find Positions
# --------------------------------------------------

positions = np.where(sales_february > sales_january)

print("\nPositions where February sales are higher:")
print(positions)


# --------------------------------------------------
# 9. Sort Data
# --------------------------------------------------

sorted_sales = np.sort(sales_february)

print("\nSorted February sales:")
print(sorted_sales)


# --------------------------------------------------
# 10. Unique Values
# --------------------------------------------------

customer_orders = np.array([
    101, 102, 101, 103, 104, 102, 105
])

unique_orders = np.unique(customer_orders)

print("\nUnique customer order IDs:")
print(unique_orders)


# --------------------------------------------------
# 11. Practical Data Science Example
# --------------------------------------------------

scores = np.array([72, 85, 91, 64, 88, 95, 70])

print("\nStudent Scores:")
print(scores)

print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))

print(
    "Number of students scoring above 80:",
    np.sum(scores > 80)
)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create two arrays containing monthly expenses.
# 2. Find which month's expenses are higher.
# 3. Calculate the difference between the arrays.
# 4. Find the maximum value at each position.
# 5. Check whether any value is greater than a given limit.
# 6. Count how many values satisfy a condition.
# 7. Sort an array.
# 8. Find unique values in an array.
