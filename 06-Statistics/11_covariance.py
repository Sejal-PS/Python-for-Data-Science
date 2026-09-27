# Covariance

import numpy as np
import pandas as pd


data = {
    "Study_Hours": [
        1, 2, 3, 4, 5
    ],
    "Marks": [
        40, 45, 55, 65, 75
    ]
}

df = pd.DataFrame(data)


# ------------------------------------------
# Covariance Matrix
# ------------------------------------------

covariance_matrix = df.cov()

print(
    "Covariance Matrix:"
)

print(
    covariance_matrix
)


# ------------------------------------------
# Covariance between two variables
# ------------------------------------------

covariance = np.cov(
    df["Study_Hours"],
    df["Marks"]
)

print(
    "\nCovariance:"
)

print(
    covariance
)


# ------------------------------------------
# Understanding Covariance
# ------------------------------------------

# Positive covariance:
# Variables tend to move in the same direction.
#
# Negative covariance:
# Variables tend to move in opposite directions.
#
# Covariance depends on the scale of variables.
#
# Correlation is standardized covariance.
