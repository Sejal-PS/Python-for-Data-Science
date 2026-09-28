"""
21 - End-to-End Deep Learning Project

Project:
Iris Flower Classification

Workflow:

Problem Definition
        ↓
Data Loading
        ↓
Train/Test Split
        ↓
Feature Scaling
        ↓
Neural Network
        ↓
Training
        ↓
Evaluation
        ↓
Prediction
"""

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

from tensorflow import keras


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset Shape:", X.shape)
print("Number of Classes:", len(np.unique(y)))


# --------------------------------------------------
# 2. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 3. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# --------------------------------------------------
# 4. Build Neural Network
# --------------------------------------------------

model = keras.Sequential([

    keras.layers.Input(
        shape=(4,)
    ),

    keras.layers.Dense(
        32,
        activation="relu"
    ),

    keras.layers.Dropout(
        0.2
    ),

    keras.layers.Dense(
        16,
        activation="relu"
    ),

    keras.layers.Dense(
        3,
        activation="softmax"
    )
])


# --------------------------------------------------
# 5. Compile Model
# --------------------------------------------------

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# --------------------------------------------------
# 6. Display Model
# --------------------------------------------------

print("\nModel Architecture:")

model.summary()


# --------------------------------------------------
# 7. Train Model
# --------------------------------------------------

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    validation_split=0.2,
    verbose=0
)


print("\nTraining completed.")


# --------------------------------------------------
# 8. Evaluate Model
# --------------------------------------------------

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)


# --------------------------------------------------
# 9. Predictions
# --------------------------------------------------

probabilities = model.predict(
    X_test,
    verbose=0
)

y_pred = np.argmax(
    probabilities,
    axis=1
)


# --------------------------------------------------
# 10. Evaluation Metrics
# --------------------------------------------------

print("\nAccuracy Score:")

print(
    accuracy_score(
        y_test,
        y_pred
    )
)


print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# --------------------------------------------------
# 11. New Prediction
# --------------------------------------------------

new_flower = np.array([
    [5.1, 3.5, 1.4, 0.2]
])


new_flower_scaled = scaler.transform(
    new_flower
)


prediction_probability = model.predict(
    new_flower_scaled,
    verbose=0
)


predicted_class = np.argmax(
    prediction_probability,
    axis=1
)[0]


print("\nNew Flower Prediction:")

print(
    "Predicted Class:",
    iris.target_names[predicted_class]
)


print(
    "Prediction Probabilities:",
    prediction_probability[0]
)


print("\nDeep Learning project completed successfully!")
