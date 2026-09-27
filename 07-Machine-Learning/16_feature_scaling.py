# Feature Scaling

import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler
)


# ------------------------------------------
# Dataset
# ------------------------------------------

data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [
        20000,
        30000,
        45000,
        60000,
        80000
    ]
}

df = pd.DataFrame(data)

print("Original Data:")

print(df)


# ------------------------------------------
# Standard Scaling
# ------------------------------------------

standard_scaler = StandardScaler()

standard_scaled = standard_scaler.fit_transform(
    df
)

print(
    "\nStandard Scaled Data:"
)

print(
    standard_scaled
)


# ------------------------------------------
# Min-Max Scaling
# ------------------------------------------

minmax_scaler = MinMaxScaler()

minmax_scaled = minmax_scaler.fit_transform(
    df
)

print(
    "\nMin-Max Scaled Data:"
)

print(
    minmax_scaled
)


# ------------------------------------------
# Why Scaling?
# ------------------------------------------

# Some algorithms are sensitive
# to feature magnitude.
#
# Examples:
#
# KNN
# K-Means
# SVM
# Logistic Regression
#
# Scaling puts features on
# comparable scales.
