# Mean, Median and Mode

import statistics
import numpy as np


data = [
    10,
    20,
    20,
    30,
    40,
    50,
    20
]


# ------------------------------------------
# Mean
# ------------------------------------------

mean_value = statistics.mean(data)

print("Mean:", mean_value)


# ------------------------------------------
# Median
# ------------------------------------------

median_value = statistics.median(data)

print("Median:", median_value)


# ------------------------------------------
# Mode
# ------------------------------------------

mode_value = statistics.mode(data)

print("Mode:", mode_value)


# ------------------------------------------
# NumPy
# ------------------------------------------

print(
    "NumPy Mean:",
    np.mean(data)
)

print(
    "NumPy Median:",
    np.median(data)
)


# ------------------------------------------
# Understanding
# ------------------------------------------

# Mean:
# Average value of the data.
#
# Median:
# Middle value after sorting.
#
# Mode:
# Most frequently occurring value.


# ------------------------------------------
# Effect of Outlier
# ------------------------------------------

data_with_outlier = [
    10,
    20,
    20,
    30,
    40,
    1000
]

print("\nWith Outlier")

print(
    "Mean:",
    statistics.mean(data_with_outlier)
)

print(
    "Median:",
    statistics.median(data_with_outlier)
)

# Median is generally less affected
# by extreme values than mean.
