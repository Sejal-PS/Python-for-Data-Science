# Hypothesis Testing

import numpy as np
from scipy import stats


# ------------------------------------------
# Example Data
# ------------------------------------------

before = [
    70,
    72,
    68,
    75,
    71,
    69,
    73,
    74
]

after = [
    75,
    78,
    72,
    80,
    76,
    74,
    79,
    81
]


# ------------------------------------------
# Mean Values
# ------------------------------------------

print(
    "Before Mean:",
    np.mean(before)
)

print(
    "After Mean:",
    np.mean(after)
)


# ------------------------------------------
# Paired t-test
# ------------------------------------------

result = stats.ttest_rel(
    before,
    after
)

print(
    "\nT-Test Result:"
)

print(
    result
)


# ------------------------------------------
# P-value
# ------------------------------------------

print(
    "\nP-value:",
    result.pvalue
)


# ------------------------------------------
# Basic Hypothesis Testing Terms
# ------------------------------------------

# Null Hypothesis (H0)
# Alternative Hypothesis (H1)
# Test Statistic
# P-value
# Significance Level
#
# A commonly used significance level is:
#
# alpha = 0.05
#
# The interpretation of a p-value depends
# on the test and assumptions.
