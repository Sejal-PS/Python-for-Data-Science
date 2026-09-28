"""
17 - Advanced Machine Learning Practice
----------------------------------------
Practice exercises covering the concepts from this section.

Try solving the exercises before looking at the hints.
"""

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


print("=" * 60)
print("ADVANCED MACHINE LEARNING PRACTICE")
print("=" * 60)


# ---------------------------------------------------------
# Exercise 1: Random Forest
# ---------------------------------------------------------

print("\nExercise 1: Random Forest")

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "Accuracy:",
    accuracy_score(y_test, predictions)
)


# ---------------------------------------------------------
# Exercise 2
# ---------------------------------------------------------

print("\nExercise 2: Experiment with Hyperparameters")

print(
    """
Try the following:

1. Change n_estimators.
2. Change max_depth.
3. Compare the test accuracy.
4. Record your observations.
"""
)


# ---------------------------------------------------------
# Exercise 3
# ---------------------------------------------------------

print("\nExercise 3: Feature Importance")

for feature, importance in zip(
    iris.feature_names,
    model.feature_importances_
):
    print(f"{feature}: {importance:.3f}")


# ---------------------------------------------------------
# Exercise 4
# ---------------------------------------------------------

print("\nExercise 4: Model Comparison")

print(
    """
Train and compare:

1. Decision Tree
2. Random Forest
3. Gradient Boosting
4. SVM
5. KNN

Use the same train/test split and evaluation metric.
"""


)


# ---------------------------------------------------------
# Exercise 5
# ---------------------------------------------------------

print("\nExercise 5: Classification Metrics")

print(
    """
For the Breast Cancer dataset:

1. Train a classification model.
2. Calculate accuracy.
3. Calculate precision.
4. Calculate recall.
5. Calculate F1-score.
6. Display the confusion matrix.
"""
)


# ---------------------------------------------------------
# Exercise 6
# ---------------------------------------------------------

print("\nExercise 6: PCA")

print(
    """
Use the Iris dataset.

1. Standardize the features.
2. Apply PCA.
3. Reduce the dataset to 2 components.
4. Calculate explained variance.
5. Visualize the transformed data.
"""
)


# ---------------------------------------------------------
# Exercise 7
# ---------------------------------------------------------

print("\nExercise 7: Clustering")

print(
    """
Apply K-Means to a dataset.

Try K values from 2 to 6.

Compare:

- Inertia
- Silhouette Score

Then explain which K you would investigate further.
"""
)


print("\nPractice complete.")
print("Try solving each exercise independently.")
