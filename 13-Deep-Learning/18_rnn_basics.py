"""
18 - RNN Basics

Recurrent Neural Networks are designed for
sequence-based data.

Examples:
- Time series
- Text
- Speech
- Sequential events
"""

import numpy as np
from tensorflow import keras


# Example sequential dataset
X = np.array([
    [[1], [2], [3]],
    [[2], [3], [4]],
    [[3], [4], [5]],
    [[4], [5], [6]]
], dtype=float)

y = np.array([
    4,
    5,
    6,
    7
], dtype=float)


# RNN model
model = keras.Sequential([

    keras.layers.Input(
        shape=(3, 1)
    ),

    keras.layers.SimpleRNN(
        16,
        activation="tanh"
    ),

    keras.layers.Dense(
        1
    )
])


model.compile(
    optimizer="adam",
    loss="mse"
)


# Train
model.fit(
    X,
    y,
    epochs=100,
    verbose=0
)


# Prediction
test_sequence = np.array([
    [[5], [6], [7]]
], dtype=float)

prediction = model.predict(
    test_sequence,
    verbose=0
)

print("Predicted next value:")
print(prediction[0][0])
