"""
Feature Selection

Feature selection means selecting the most useful
features for a machine learning model.

This example uses SelectKBest with ANOVA F-test.
"""

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

feature_names = iris.feature_names


# --------------------------------------------------
# Display Original Features
# --------------------------------------------------

print("Original Features:")

for name in feature_names:
    print(name)


# --------------------------------------------------
# Feature Selection
# --------------------------------------------------

selector = SelectKBest(
    score_func=f_classif,
    k=2
)

X_selected = selector.fit_transform(
    X,
    y
)


# --------------------------------------------------
# Feature Scores
# --------------------------------------------------

scores = selector.scores_

print("\nFeature Scores:")

for name, score in zip(
    feature_names,
    scores
):
    print(
        f"{name}: {score:.2f}"
    )


# --------------------------------------------------
# Selected Features
# --------------------------------------------------

selected_features = [
    name
    for name, selected
    in zip(
        feature_names,
        selector.get_support()
    )
    if selected
]

print("\nSelected Features:")

for feature in selected_features:
    print(feature)


# --------------------------------------------------
# Shape Comparison
# --------------------------------------------------

print("\nOriginal Shape:")
print(X.shape)

print("\nSelected Shape:")
print(X_selected.shape)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Change k from 2 to 3.
# 2. Compare selected features.
# 3. Try feature selection with another dataset.
# 4. Train a classifier using only selected features.
