"""
Outlier Detection using the IQR Method

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 * IQR
Upper Bound = Q3 + 1.5 * IQR
"""

import numpy as np


# --------------------------------------------------
# Sample Data
# --------------------------------------------------

data = np.array([
    10, 12, 13, 15, 18,
    20, 21, 22, 24, 25,
    100
])

print("Original Data:")
print(data)


# --------------------------------------------------
# Calculate Quartiles
# --------------------------------------------------

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

print("\nQ1:", q1)
print("Q3:", q3)


# --------------------------------------------------
# Calculate IQR
# --------------------------------------------------

iqr = q3 - q1

print("\nIQR:", iqr)


# --------------------------------------------------
# Calculate Bounds
# --------------------------------------------------

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)


# --------------------------------------------------
# Identify Outliers
# --------------------------------------------------

outliers = data[
    (data < lower_bound) |
    (data > upper_bound)
]

print("\nOutliers:")
print(outliers)


# --------------------------------------------------
# Identify Normal Values
# --------------------------------------------------

normal_values = data[
    (data >= lower_bound) &
    (data <= upper_bound)
]

print("\nValues without outliers:")
print(normal_values)


# --------------------------------------------------
# Example: Detect Outliers in Salaries
# --------------------------------------------------

salaries = np.array([
    30000,
    32000,
    35000,
    36000,
    38000,
    40000,
    42000,
    45000,
    200000
])

q1_salary = np.percentile(salaries, 25)
q3_salary = np.percentile(salaries, 75)

iqr_salary = q3_salary - q1_salary

lower_salary = q1_salary - 1.5 * iqr_salary
upper_salary = q3_salary + 1.5 * iqr_salary

salary_outliers = salaries[
    (salaries < lower_salary) |
    (salaries > upper_salary)
]

print("\nSalary Outliers:")
print(salary_outliers)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a dataset containing an obvious outlier.
# 2. Calculate Q1 and Q3.
# 3. Calculate IQR.
# 4. Calculate lower and upper bounds.
# 5. Identify the outliers.
