# Machine Learning Basics

import numpy as np
import pandas as pd


# ------------------------------------------
# What is Machine Learning?
# ------------------------------------------

# Machine Learning allows computers to
# learn patterns from data and make
# predictions or decisions.


# ------------------------------------------
# Example Dataset
# ------------------------------------------

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

print(df)


# ------------------------------------------
# Features and Target
# ------------------------------------------

# Feature:
# Input variable used by the model.
#
# Target:
# Value that the model tries to predict.


X = df[["Study_Hours"]]

y = df["Marks"]


print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# ------------------------------------------
# Training
# ------------------------------------------

# During training, the model learns
# patterns between features and target.


# ------------------------------------------
# Prediction
# ------------------------------------------

# After training, the model can predict
# values for new data.


# Example:
#
# Study Hours = 6
#
# Model may predict:
# Marks = 82
