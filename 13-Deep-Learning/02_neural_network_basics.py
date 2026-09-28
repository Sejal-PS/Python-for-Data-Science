"""
02 - Neural Network Basics

Learn:
- Input layer
- Hidden layer
- Output layer
- Neurons
- Weights
- Bias
"""

import numpy as np

# Input values
inputs = np.array([2.0, 3.0])

# Weights
weights = np.array([0.5, 0.8])

# Bias
bias = 1.0

# Weighted sum
weighted_sum = np.dot(inputs, weights) + bias

print("Inputs:", inputs)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted Sum:", weighted_sum)

print("\nBasic Neural Network Structure:")
print("Input Layer -> Hidden Layer -> Output Layer")
