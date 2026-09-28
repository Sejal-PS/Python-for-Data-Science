"""
16 - Convolutional Neural Network (CNN) Basics

Learn:
- Convolution layer
- Pooling layer
- Flatten layer
- Dense layer
- CNN architecture
"""

import numpy as np
from tensorflow import keras


# Create a CNN model
model = keras.Sequential([

    keras.layers.Input(
        shape=(28, 28, 1)
    ),

    # Convolution
    keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    # Pooling
    keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Second convolution
    keras.layers.Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    ),

    keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Convert feature maps into vector
    keras.layers.Flatten(),

    # Fully connected layer
    keras.layers.Dense(
        64,
        activation="relu"
    ),

    # Output layer
    keras.layers.Dense(
        10,
        activation="softmax"
    )
])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


print("CNN Architecture:")
model.summary()
