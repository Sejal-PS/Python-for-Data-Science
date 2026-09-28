"""
NumPy Boolean Indexing

Boolean indexing is used to filter numerical data
based on conditions.
"""

import numpy as np


# --------------------------------------------------
# 1. Basic Boolean Condition
# --------------------------------------------------

marks = np.array([
    45, 67, 89, 32, 76, 90, 55
])

condition = marks >= 60

print("Condition:")
print(condition)


# --------------------------------------------------
# 2. Filter Values
# --------------------------------------------------

passed_students = marks[marks >= 60]

print("\nMarks greater than or equal to 60:")
print(passed_students)


# --------------------------------------------------
# 3. Filter Values Below a Limit
# --------------------------------------------------

low_marks = marks[marks < 50]

print("\nMarks below 50:")
print(low_marks)


# --------------------------------------------------
# 4. Multiple Conditions
# --------------------------------------------------

medium_marks = marks[
    (marks >= 50) & (marks < 80)
]

print("\nMarks between 50 and 80:")
print(medium_marks)


# --------------------------------------------------
# 5. OR Condition
# --------------------------------------------------

selected_marks = marks[
    (marks < 40) | (marks > 85)
]

print("\nMarks below 40 or above 85:")
print(selected_marks)


# --------------------------------------------------
# 6. Modify Values Using Boolean Indexing
# --------------------------------------------------

updated_marks = marks.copy()

updated_marks[updated_marks < 40] = 40

print("\nMarks after applying minimum passing value:")
print(updated_marks)


# --------------------------------------------------
# 7. Boolean Indexing with Sales Data
# --------------------------------------------------

sales = np.array([
    5000,
    12000,
    7500,
    18000,
    3000,
    15000
])

high_sales = sales[sales >= 10000]

print("\nSales above or equal to 10000:")
print(high_sales)


# --------------------------------------------------
# 8. Count Values Matching a Condition
# --------------------------------------------------

count = np.sum(sales >= 10000)

print("\nNumber of high-sales records:")
print(count)


# --------------------------------------------------
# 9. Find Positions
# --------------------------------------------------

positions = np.where(sales >= 10000)

print("\nPositions of high-sales records:")
print(positions)


# --------------------------------------------------
# 10. Practical Example
# --------------------------------------------------

temperatures = np.array([
    22, 25, 31, 28, 35, 19, 33
])

hot_days = temperatures[temperatures > 30]

print("\nTemperatures above 30:")
print(hot_days)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Filter numbers greater than 50.
# 2. Filter even numbers.
# 3. Filter values between 20 and 80.
# 4. Count values above a threshold.
# 5. Replace values below a minimum with that minimum.
# 6. Find positions where a condition is True.
# 7. Filter a real-world dataset using multiple conditions.
