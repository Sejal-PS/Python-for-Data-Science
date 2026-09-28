"""
11 - Keras Basics

Learn:
- Creating a neural network
- Input layer
- Dense layers
- Output layer
- Compiling a model
- Training a model
- Making predictions
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras


# Simple dataset
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
], dtype=float)

y = np.array([
    [2],
    [4],
    [6],
    [8],
    [10]
], dtype=float)


# Create neural network
model = keras.Sequential([
    keras.layers.Input(shape=(1,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1)
])


# Compile model
model.compile(
    optimizer="adam",
    loss="mse"
)


print("Model Summary:")
model.summary()


# Train model
model.fit(
    X,
    y,
    epochs=100,
    verbose=0
)


# Prediction
new_value = np.array([[6.0]])

prediction = model.predict(new_value, verbose=0)

print("\nPrediction for 6:")
print(prediction)
