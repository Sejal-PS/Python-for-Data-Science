"""
07 - Backpropagation

Backpropagation calculates how much each weight
contributed to the prediction error.

This example demonstrates the basic idea of
gradient-based weight updating.
"""

import numpy as np


# Initial values
x = 2.0
weight = 0.5
bias = 0.0
target = 4.0

learning_rate = 0.01

# Forward pass
prediction = x * weight + bias

# Error
error = prediction - target

# Gradient calculation
gradient_weight = 2 * error * x
gradient_bias = 2 * error

# Weight update
weight = weight - learning_rate * gradient_weight
bias = bias - learning_rate * gradient_bias

print("Initial Prediction:", prediction)
print("Error:", error)

print("\nUpdated Weight:", weight)
print("Updated Bias:", bias)

# New prediction
new_prediction = x * weight + bias

print("New Prediction:", new_prediction)
