"""
Z-Score

A z-score tells us how many standard deviations
a data point is away from the mean.

Formula:

z = (x - mean) / standard_deviation
"""

import numpy as np


# --------------------------------------------------
# Sample Data
# --------------------------------------------------

data = np.array([10, 20, 30, 40, 50])


# --------------------------------------------------
# Calculate Mean
# --------------------------------------------------

mean = np.mean(data)

print("Mean:", mean)


# --------------------------------------------------
# Calculate Standard Deviation
# --------------------------------------------------

std = np.std(data)

print("Standard Deviation:", std)


# --------------------------------------------------
# Calculate Z-Scores
# --------------------------------------------------

z_scores = (data - mean) / std

print("\nZ-Scores:")
print(z_scores)


# --------------------------------------------------
# Using NumPy directly
# --------------------------------------------------

value = 40

z_score = (value - mean) / std

print("\nZ-score of", value, ":", z_score)


# --------------------------------------------------
# Identify values far from the mean
# --------------------------------------------------

unusual_values = data[np.abs(z_scores) > 1]

print("\nValues more than 1 standard deviation away:")
print(unusual_values)


# --------------------------------------------------
# Example with Student Marks
# --------------------------------------------------

marks = np.array([
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 95
])

marks_mean = np.mean(marks)
marks_std = np.std(marks)

marks_z_scores = (
    (marks - marks_mean) /
    marks_std
)

print("\nStudent Marks:")
print(marks)

print("\nStudent Z-Scores:")
print(marks_z_scores)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create an array of employee salaries.
# 2. Calculate the mean salary.
# 3. Calculate the standard deviation.
# 4. Calculate the z-score of each salary.
# 5. Identify values with an absolute z-score greater than 2.
