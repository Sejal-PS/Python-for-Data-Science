"""
16 - Model Interpretability
---------------------------
Learn basic techniques for understanding model behavior.

This example demonstrates:
1. Feature importance
2. Permutation importance
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
import pandas as pd


# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Convert to DataFrame
X = pd.DataFrame(
    X,
    columns=iris.feature_names
)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Built-in feature importance
importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="importance",
    ascending=False
)

print("Random Forest Feature Importance:")
print(importance_df)


# Permutation importance
result = permutation_importance(
    model,
    X_test,
    y_test,
    n_repeats=10,
    random_state=42
)

permutation_df = pd.DataFrame({
    "feature": X.columns,
    "importance": result.importances_mean
})

permutation_df = permutation_df.sort_values(
    by="importance",
    ascending=False
)

print("\nPermutation Importance:")
print(permutation_df)


print("\nInterpretation:")
print(
    "Feature importance indicates how useful a feature "
    "was to the trained model. It should be interpreted "
    "as model behavior, not as proof of causation."
)
