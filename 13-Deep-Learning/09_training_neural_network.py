"""
09 - Training a Neural Network

Training process:

Input Data
    ↓
Forward Propagation
    ↓
Prediction
    ↓
Loss Calculation
    ↓
Backpropagation
    ↓
Weight Update
    ↓
Repeat
"""

import numpy as np


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


# Initial parameters
weight = 0.0
bias = 0.0

learning_rate = 0.01

epochs = 1000


for epoch in range(epochs):

    # Forward propagation
    predictions = X * weight + bias

    # Calculate error
    error = predictions - y

    # Mean Squared Error
    loss = np.mean(error ** 2)

    # Gradients
    weight_gradient = np.mean(2 * X * error)
    bias_gradient = np.mean(2 * error)

    # Update parameters
    weight -= learning_rate * weight_gradient
    bias -= learning_rate * bias_gradient


print("Training completed.")

print("Learned Weight:", weight)
print("Learned Bias:", bias)
print("Final Loss:", loss)


# Prediction
new_value = 6

prediction = new_value * weight + bias

print("\nPrediction for", new_value, ":", prediction)
