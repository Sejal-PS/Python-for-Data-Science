"""
05 - Loss Functions

Learn:
- Mean Squared Error
- Binary Cross-Entropy
- Categorical Cross-Entropy

Loss functions measure the difference between
actual values and model predictions.
"""

import numpy as np


# Mean Squared Error
actual = np.array([10, 20, 30])
predicted = np.array([12, 18, 29])

mse = np.mean((actual - predicted) ** 2)

print("Mean Squared Error:", mse)


# Binary Cross-Entropy
actual_binary = np.array([1, 0, 1])
predicted_binary = np.array([0.9, 0.2, 0.8])

epsilon = 1e-15

predicted_binary = np.clip(
    predicted_binary,
    epsilon,
    1 - epsilon
)

binary_cross_entropy = -np.mean(
    actual_binary * np.log(predicted_binary)
    + (1 - actual_binary) * np.log(1 - predicted_binary)
)

print("Binary Cross-Entropy:", binary_cross_entropy)


# Categorical Cross-Entropy
actual_class = np.array([1, 0, 0])

predicted_class = np.array([0.7, 0.2, 0.1])

categorical_cross_entropy = -np.sum(
    actual_class * np.log(predicted_class)
)

print("Categorical Cross-Entropy:", categorical_cross_entropy)
