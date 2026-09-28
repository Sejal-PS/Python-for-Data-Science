"""
15 - Imbalanced Classification
------------------------------
Learn why accuracy alone can be misleading for imbalanced data.

This example creates an artificial imbalanced dataset.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)


# Create imbalanced dataset
X, y = make_classification(
    n_samples=2000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    weights=[0.90, 0.10],
    random_state=42
)

# Check class distribution
print("Class Distribution:")

unique, counts = __import__("numpy").unique(
    y,
    return_counts=True
)

for class_value, count in zip(unique, counts):
    print(f"Class {class_value}: {count}")


# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Model without class weighting
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print(
    "ROC-AUC:",
    roc_auc_score(y_test, probabilities)
)


# Model with balanced class weights
balanced_model = LogisticRegression(
    class_weight="balanced",
    max_iter=1000
)

balanced_model.fit(X_train, y_train)

balanced_predictions = balanced_model.predict(X_test)

print("\nBalanced Model Classification Report:")
print(
    classification_report(
        y_test,
        balanced_predictions
    )
)
