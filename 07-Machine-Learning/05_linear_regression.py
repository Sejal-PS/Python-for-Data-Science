# Linear Regression

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


# ------------------------------------------
# Dataset
# ------------------------------------------

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([
    40,
    45,
    55,
    65,
    75
])


# ------------------------------------------
# Create Model
# ------------------------------------------

model = LinearRegression()


# ------------------------------------------
# Train Model
# ------------------------------------------

model.fit(
    X,
    y
)


# ------------------------------------------
# Prediction
# ------------------------------------------

prediction = model.predict(
    [[6]]
)

print(
    "Predicted Marks:",
    prediction[0]
)


# ------------------------------------------
# Coefficient
# ------------------------------------------

print(
    "Coefficient:",
    model.coef_[0]
)


# ------------------------------------------
# Intercept
# ------------------------------------------

print(
    "Intercept:",
    model.intercept_
)


# ------------------------------------------
# Regression Line
# ------------------------------------------

plt.scatter(
    X,
    y,
    color="blue"
)

plt.plot(
    X,
    model.predict(X),
    color="red"
)

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.title("Linear Regression")

plt.show()
