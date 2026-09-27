# Statistics Basics for Data Science

import statistics
import numpy as np


# ------------------------------------------
# What is Statistics?
# ------------------------------------------

# Statistics is the process of collecting,
# organizing, analyzing and interpreting data.


data = [10, 20, 30, 40, 50]

print("Data:", data)


# ------------------------------------------
# Number of observations
# ------------------------------------------

print("Count:", len(data))


# ------------------------------------------
# Sum
# ------------------------------------------

print("Sum:", sum(data))


# ------------------------------------------
# Mean
# ------------------------------------------

print(
    "Mean:",
    statistics.mean(data)
)


# ------------------------------------------
# Median
# ------------------------------------------

print(
    "Median:",
    statistics.median(data)
)


# ------------------------------------------
# Minimum
# ------------------------------------------

print(
    "Minimum:",
    min(data)
)


# ------------------------------------------
# Maximum
# ------------------------------------------

print(
    "Maximum:",
    max(data)
)


# ------------------------------------------
# NumPy Mean
# ------------------------------------------

print(
    "NumPy Mean:",
    np.mean(data)
)


# ------------------------------------------
# NumPy Median
# ------------------------------------------

print(
    "NumPy Median:",
    np.median(data)
)


# ------------------------------------------
# Basic Data Summary
# ------------------------------------------

print("\nBasic Summary")

print("Count:", len(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
