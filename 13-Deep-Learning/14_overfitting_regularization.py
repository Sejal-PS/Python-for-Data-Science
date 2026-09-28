"""
14 - Overfitting and Regularization

Learn:
- Overfitting
- Validation data
- Dropout
- Early stopping
- L2 regularization
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras


# Load data
iris = load_iris()

X = iris.data
y = iris.target


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Model with regularization
model = keras.Sequential([
    keras.layers.Input(shape=(4,)),

    keras.layers.Dense(
        64,
        activation="relu",
        kernel_regularizer=keras.regularizers.l2(0.001)
    ),

    keras.layers.Dropout(0.3),

    keras.layers.Dense(
        32,
        activation="relu"
    ),

    keras.layers.Dropout(0.2),

    keras.layers.Dense(
        3,
        activation="softmax"
    )
])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# Early stopping
early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)


# Training
history = model.fit(
    X_train,
    y_train,
    epochs=200,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=0
)


# Evaluation
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

print("\nTraining stopped after:")
print(len(history.history["loss"]), "epochs")
