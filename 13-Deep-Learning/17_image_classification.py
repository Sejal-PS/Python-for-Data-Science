"""
17 - Image Classification using CNN

Dataset:
MNIST handwritten digits.

Classes:
0 to 9
"""

import numpy as np
from tensorflow import keras


# Load MNIST
(X_train, y_train), (X_test, y_test) = (
    keras.datasets.mnist.load_data()
)


# Normalize pixel values
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0


# Add channel dimension
X_train = np.expand_dims(
    X_train,
    axis=-1
)

X_test = np.expand_dims(
    X_test,
    axis=-1
)


# CNN model
model = keras.Sequential([

    keras.layers.Input(
        shape=(28, 28, 1)
    ),

    keras.layers.Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    keras.layers.MaxPooling2D(
        (2, 2)
    ),

    keras.layers.Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    keras.layers.MaxPooling2D(
        (2, 2)
    ),

    keras.layers.Flatten(),

    keras.layers.Dense(
        64,
        activation="relu"
    ),

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


# Train
model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)


# Evaluate
loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)


# Prediction
predictions = model.predict(
    X_test[:5]
)

predicted_classes = np.argmax(
    predictions,
    axis=1
)

print("\nPredicted Digits:")
print(predicted_classes)

print("\nActual Digits:")
print(y_test[:5])
