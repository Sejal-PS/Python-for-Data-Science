"""
13 - Multiclass Classification

Example:
Iris flower classification using a neural network.

Classes:
0 = Setosa
1 = Versicolor
2 = Virginica
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras


# Load dataset
iris = load_iris()

X = iris.data
y = iris.target


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Neural network
model = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(3, activation="softmax")
])


# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# Train
model.fit(
    X_train,
    y_train,
    epochs=50,
    validation_split=0.2,
    verbose=0
)


# Evaluate
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy)


# Prediction
sample = X_test[:5]

predictions = model.predict(
    sample,
    verbose=0
)

predicted_classes = np.argmax(
    predictions,
    axis=1
)

print("\nPredicted Classes:")
print(predicted_classes)

print("\nActual Classes:")
print(y_test[:5])
