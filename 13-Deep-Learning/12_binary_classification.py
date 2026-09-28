"""
12 - Binary Classification

Example:
Predict whether a student passes based on study hours.

Target:
0 = Fail
1 = Pass
"""

import numpy as np
from tensorflow import keras


# Features
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
], dtype=float)

# Target
y = np.array([
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1
], dtype=float)


# Neural network
model = keras.Sequential([
    keras.layers.Input(shape=(1,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])


# Compile
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Train
model.fit(
    X,
    y,
    epochs=100,
    verbose=0
)


# Evaluate
loss, accuracy = model.evaluate(X, y, verbose=0)

print("Loss:", loss)
print("Accuracy:", accuracy)


# Prediction
study_hours = np.array([[3.5]])

probability = model.predict(
    study_hours,
    verbose=0
)[0][0]

print("\nProbability of Passing:", probability)

if probability >= 0.5:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
