# Skewness

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew


# ------------------------------------------
# Symmetric Data
# ------------------------------------------

symmetric_data = np.random.normal(
    50,
    10,
    1000
)


# ------------------------------------------
# Right Skewed Data
# ------------------------------------------

right_skewed = np.random.exponential(
    scale=2,
    size=1000
)


# ------------------------------------------
# Calculate Skewness
# ------------------------------------------

print(
    "Symmetric Data Skewness:",
    skew(symmetric_data)
)

print(
    "Right Skewed Data Skewness:",
    skew(right_skewed)
)


# ------------------------------------------
# Visualization
# ------------------------------------------

plt.figure(
    figsize=(10, 5)
)

plt.subplot(1, 2, 1)

plt.hist(
    symmetric_data,
    bins=30,
    edgecolor="black"
)

plt.title(
    "Approximately Symmetric"
)


plt.subplot(1, 2, 2)

plt.hist(
    right_skewed,
    bins=30,
    edgecolor="black"
)

plt.title(
    "Right Skewed"
)

plt.tight_layout()

plt.show()


# ------------------------------------------
# Interpretation
# ------------------------------------------

# Skewness ≈ 0
# Approximately symmetric
#
# Positive skewness
# Right-skewed distribution
#
# Negative skewness
# Left-skewed distribution
