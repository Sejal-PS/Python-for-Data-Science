# Normal Distribution

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------
# Generate Normal Distribution
# ------------------------------------------

data = np.random.normal(
    loc=50,
    scale=10,
    size=1000
)


# loc = mean
# scale = standard deviation
# size = number of observations


# ------------------------------------------
# Histogram
# ------------------------------------------

plt.hist(
    data,
    bins=30,
    edgecolor="black"
)

plt.title(
    "Normal Distribution"
)

plt.xlabel(
    "Value"
)

plt.ylabel(
    "Frequency"
)

plt.show()


# ------------------------------------------
# Mean and Standard Deviation
# ------------------------------------------

print(
    "Mean:",
    np.mean(data)
)

print(
    "Standard Deviation:",
    np.std(data)
)


# ------------------------------------------
# Important Properties
# ------------------------------------------

# Normal distribution is approximately
# symmetric around the mean.
#
# Mean ≈ Median ≈ Mode
#
# Many real-world measurements can be
# approximately normally distributed.
