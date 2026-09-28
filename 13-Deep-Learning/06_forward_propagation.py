"""
06 - Forward Propagation

Forward propagation moves input data through
the neural network to produce a prediction.
"""

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Input layer
inputs = np.array([2.0, 3.0])

# Hidden layer weights
weights_hidden = np.array([
    [0.5, 0.4],
    [0.3, 0.7]
])

hidden_bias = np.array([0.1, 0.2])

# Hidden layer calculation
hidden_input = np.dot(inputs, weights_hidden) + hidden_bias

hidden_output = sigmoid(hidden_input)

# Output layer
output_weights = np.array([0.6, 0.8])
output_bias = 0.1

output_input = np.dot(hidden_output, output_weights) + output_bias

prediction = sigmoid(output_input)

print("Input:", inputs)
print("Hidden Layer Output:", hidden_output)
print("Final Prediction:", prediction)
