"""
Median Absolute Deviation (MAD)

MAD is a robust measure of statistical dispersion.

It measures the median distance of data points
from the median.
"""

import numpy as np


# --------------------------------------------------
# Sample Data
# --------------------------------------------------

data = np.array([
    10, 12, 13, 15, 18,
    20, 21, 22, 24, 100
])

print("Data:")
print(data)

# --------------------------------------------------
# Calculate Median
# --------------------------------------------------

median = np.median(data)

print("\nMedian:")
print(median)


# --------------------------------------------------
# Calculate Absolute Deviations
# --------------------------------------------------

absolute_deviations = np.abs(
    data - median
)

print("\nAbsolute Deviations:")
print(absolute_deviations)


# --------------------------------------------------
# Calculate MAD
# --------------------------------------------------

mad = np.median(
    absolute_deviations
)

print("\nMedian Absolute Deviation:")
print(mad)


# --------------------------------------------------
# Compare Mean and Median
# --------------------------------------------------

mean = np.mean(data)

print("\nMean:", mean)
print("Median:", median)

print("\nStandard Deviation:")
print(np.std(data))


# --------------------------------------------------
# Example without extreme value
# --------------------------------------------------

clean_data = np.array([
    10, 12, 13, 15, 18,
    20, 21, 22, 24
])

clean_median = np.median(clean_data)

clean_mad = np.median(
    np.abs(clean_data - clean_median)
)

print("\nData without extreme value:")
print(clean_data)

print("\nMedian:", clean_median)
print("MAD:", clean_mad)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a dataset with an extreme value.
# 2. Calculate mean and median.
# 3. Calculate MAD.
# 4. Compare MAD with standard deviation.
# 5. Observe how an extreme value affects mean and median.
