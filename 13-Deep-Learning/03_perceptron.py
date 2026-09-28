"""
03 - Perceptron

The perceptron is one of the simplest neural network models.

Formula:

weighted_sum = inputs * weights + bias

prediction = activation(weighted_sum)
"""

import numpy as np


def step_activation(value):
    if value >= 0:
        return 1
    return 0


inputs = np.array([1, 1])

weights = np.array([0.7, 0.6])

bias = -0.5

weighted_sum = np.dot(inputs, weights) + bias

prediction = step_activation(weighted_sum)

print("Inputs:", inputs)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted Sum:", weighted_sum)
print("Prediction:", prediction)
