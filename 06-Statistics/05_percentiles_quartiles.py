# Percentiles and Quartiles

import numpy as np


data = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]


# ------------------------------------------
# Percentile
# ------------------------------------------

p25 = np.percentile(
    data,
    25
)

p50 = np.percentile(
    data,
    50
)

p75 = np.percentile(
    data,
    75
)

print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)


# ------------------------------------------
# Quartiles
# ------------------------------------------

Q1 = np.percentile(
    data,
    25
)

Q2 = np.percentile(
    data,
    50
)

Q3 = np.percentile(
    data,
    75
)

print("\nQ1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)


# ------------------------------------------
# Interquartile Range
# ------------------------------------------

IQR = Q3 - Q1

print(
    "\nIQR:",
    IQR
)


# ------------------------------------------
# Five Number Summary
# ------------------------------------------

minimum = np.min(data)

Q1 = np.percentile(data, 25)

median = np.percentile(data, 50)

Q3 = np.percentile(data, 75)

maximum = np.max(data)

print("\nFive Number Summary")

print("Minimum:", minimum)
print("Q1:", Q1)
print("Median:", median)
print("Q3:", Q3)
print("Maximum:", maximum)


# ------------------------------------------
# Use in Data Science
# ------------------------------------------

# Percentiles and quartiles are useful for:
#
# - Understanding distributions
# - Finding outliers
# - Understanding data spread
# - Creating box plots
