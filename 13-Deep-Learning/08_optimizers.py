"""
08 - Optimizers

Learn:
- Gradient Descent
- SGD concept
- Adam concept
- Learning Rate

Optimizers control how model parameters
are updated during training.
"""

import numpy as np


# Simple Gradient Descent example

weight = 0.0
target = 10.0
learning_rate = 0.1

print("Gradient Descent Training\n")

for epoch in range(10):

    prediction = weight

    error = prediction - target

    gradient = 2 * error

    weight = weight - learning_rate * gradient

    print(
        f"Epoch {epoch + 1}: "
        f"Prediction = {prediction:.4f}, "
        f"Weight = {weight:.4f}"
    )


print("\nOptimizer Concepts:")
print("- Gradient Descent")
print("- Stochastic Gradient Descent (SGD)")
print("- Adam")
print("- Learning Rate")
