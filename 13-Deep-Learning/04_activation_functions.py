"""
04 - Activation Functions

Learn:
- Sigmoid
- Tanh
- ReLU
- Softmax
"""

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


values = np.array([-2, -1, 0, 1, 2], dtype=float)

print("Input:", values)

print("\nSigmoid:")
print(sigmoid(values))

print("\nTanh:")
print(np.tanh(values))

print("\nReLU:")
print(relu(values))


def softmax(x):
    exp_values = np.exp(x - np.max(x))
    return exp_values / np.sum(exp_values)


print("\nSoftmax:")
print(softmax(values))
