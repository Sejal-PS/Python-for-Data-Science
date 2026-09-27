# Statistics - Practice Questions

import numpy as np
import pandas as pd


# ==================================================
# Practice 1 - Basic Statistics
# ==================================================

data = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

# Tasks:
#
# 1. Find count.
# 2. Find sum.
# 3. Find mean.
# 4. Find median.
# 5. Find minimum.
# 6. Find maximum.


# ==================================================
# Practice 2 - Mean Median Mode
# ==================================================

data = [
    10,
    20,
    20,
    30,
    30,
    30,
    40,
    50
]

# Tasks:
#
# 1. Calculate mean.
# 2. Calculate median.
# 3. Calculate mode.
# 4. Compare the three values.


# ==================================================
# Practice 3 - Variance and Standard Deviation
# ==================================================

marks = [
    45,
    50,
    55,
    60,
    65,
    70,
    75
]

# Tasks:
#
# 1. Calculate variance.
# 2. Calculate standard deviation.
# 3. Explain what the standard deviation tells you.


# ==================================================
# Practice 4 - Percentiles
# ==================================================

marks = [
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90
]

# Tasks:
#
# 1. Find Q1.
# 2. Find Q2.
# 3. Find Q3.
# 4. Calculate IQR.


# ==================================================
# Practice 5 - Probability
# ==================================================

# A dice has six sides.

# Tasks:
#
# 1. Probability of getting 1.
# 2. Probability of getting an even number.
# 3. Probability of getting a number greater than 4.


# ==================================================
# Practice 6 - Distribution
# ==================================================

# Create 1000 random values using
# NumPy normal distribution.

# Tasks:
#
# 1. Calculate mean.
# 2. Calculate standard deviation.
# 3. Create histogram.
# 4. Observe the shape of distribution.


# ==================================================
# Practice 7 - Skewness
# ==================================================

# Create:
#
# 1. Approximately symmetric data.
# 2. Right-skewed data.
#
# Tasks:
#
# Calculate skewness for both datasets
# and compare them.


# ==================================================
# Practice 8 - Correlation
# ==================================================

data = {
    "Study_Hours": [
        1, 2, 3, 4, 5, 6, 7
    ],
    "Marks": [
        40, 45, 52, 60, 68, 75, 85
    ]
}

df = pd.DataFrame(data)

# Tasks:
#
# 1. Calculate correlation.
# 2. Create scatter plot.
# 3. Interpret the relationship.


# ==================================================
# Practice 9 - Covariance
# ==================================================

# Use the same Study_Hours and Marks data.

# Tasks:
#
# 1. Calculate covariance.
# 2. Compare covariance and correlation.
# 3. Explain the difference.


# ==================================================
# Practice 10 - Sampling
# ==================================================

population = np.arange(
    1,
    101
)

# Tasks:
#
# 1. Select a random sample of 10 values.
# 2. Calculate sample mean.
# 3. Calculate population mean.
# 4. Compare both means.


# ==================================================
# Practice 11 - Hypothesis Testing
# ==================================================

before = [
    70, 72, 68, 75, 71, 69, 73, 74
]

after = [
    75, 78, 72, 80, 76, 74, 79, 81
]

# Tasks:
#
# 1. Calculate mean before.
# 2. Calculate mean after.
# 3. Perform paired t-test.
# 4. Check the p-value.
# 5. Understand what the result means.


# ==================================================
# Practice 12 - Mini Statistics Analysis
# ==================================================

sales = [
    10000,
    12000,
    15000,
    13000,
    18000,
    22000,
    25000,
    21000,
    19000,
    28000
]

# Tasks:
#
# 1. Mean sales
# 2. Median sales
# 3. Minimum sales
# 4. Maximum sales
# 5. Range
# 6. Variance
# 7. Standard deviation
# 8. Q1
# 9. Q3
# 10. IQR
#
# Finally:
# Explain what these statistics
# tell you about the sales data.
