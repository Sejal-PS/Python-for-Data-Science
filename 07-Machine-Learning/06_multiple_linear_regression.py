# Multiple Linear Regression

import pandas as pd

from sklearn.linear_model import LinearRegression


# ------------------------------------------
# Dataset
# ------------------------------------------

data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7],
    "Attendance": [70, 75, 80, 85, 90, 95],
    "Marks": [45, 50, 58, 65, 75, 82]
}

df = pd.DataFrame(data)


# ------------------------------------------
# Features
# ------------------------------------------

X = df[
    [
        "Study_Hours",
        "Attendance"
    ]
]


# ------------------------------------------
# Target
# ------------------------------------------

y = df["Marks"]


# ------------------------------------------
# Model
# ------------------------------------------

model = LinearRegression()

model.fit(
    X,
    y
)


# ------------------------------------------
# Prediction
# ------------------------------------------

new_data = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [92]
})

prediction = model.predict(
    new_data
)

print(
    "Predicted Marks:",
    prediction[0]
)


# ------------------------------------------
# Coefficients
# ------------------------------------------

print(
    "Coefficients:",
    model.coef_
)

print(
    "Intercept:",
    model.intercept_
)
