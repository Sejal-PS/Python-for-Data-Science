# Probability Distribution

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------
# What is Distribution?
# ------------------------------------------

# Distribution describes how values
# are spread across a dataset.


data = np.array([
    10, 12, 15, 18, 20,
    22, 25, 27, 30, 32,
    35, 38, 40, 42, 45
])


# ------------------------------------------
# Basic Histogram
# ------------------------------------------

plt.hist(
    data,
    bins=5,
    edgecolor="black"
)

plt.title(
    "Data Distribution"
)

plt.xlabel(
    "Value"
)

plt.ylabel(
    "Frequency"
)

plt.show()


# ------------------------------------------
# Mean
# ------------------------------------------

print(
    "Mean:",
    np.mean(data)
)


# ------------------------------------------
# Standard Deviation
# ------------------------------------------

print(
    "Standard Deviation:",
    np.std(data)
)


# ------------------------------------------
# Important Terms
# ------------------------------------------

# Distribution
# Frequency
# Probability Distribution
# Normal Distribution
# Skewed Distribution
# Uniform Distribution
