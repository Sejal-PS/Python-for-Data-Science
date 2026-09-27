# Range, Variance and Standard Deviation

import statistics
import numpy as np


data = [
    10,
    20,
    30,
    40,
    50
]


# ------------------------------------------
# Range
# ------------------------------------------

data_range = max(data) - min(data)

print("Range:", data_range)


# ------------------------------------------
# Population Variance
# ------------------------------------------

population_variance = statistics.pvariance(
    data
)

print(
    "Population Variance:",
    population_variance
)


# ------------------------------------------
# Sample Variance
# ------------------------------------------

sample_variance = statistics.variance(
    data
)

print(
    "Sample Variance:",
    sample_variance
)


# ------------------------------------------
# Population Standard Deviation
# ------------------------------------------

population_std = statistics.pstdev(
    data
)

print(
    "Population Standard Deviation:",
    population_std
)


# ------------------------------------------
# Sample Standard Deviation
# ------------------------------------------

sample_std = statistics.stdev(
    data
)

print(
    "Sample Standard Deviation:",
    sample_std
)


# ------------------------------------------
# NumPy
# ------------------------------------------

print(
    "NumPy Variance:",
    np.var(data)
)

print(
    "NumPy Standard Deviation:",
    np.std(data)
)


# ------------------------------------------
# Interpretation
# ------------------------------------------

# Range:
# Difference between maximum and minimum.
#
# Variance:
# Measures how spread out values are.
#
# Standard Deviation:
# Measures the typical spread around the mean.
