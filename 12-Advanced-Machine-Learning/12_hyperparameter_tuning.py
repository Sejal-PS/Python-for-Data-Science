"""
12 - Hyperparameter Tuning
--------------------------
Use GridSearchCV and RandomizedSearchCV to search for
better model configurations.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load data
iris = load_iris()

X = iris.data
y = iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Base model
model = RandomForestClassifier(
    random_state=42
)


# Grid Search
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [None, 3, 5, 10],
    "min_samples_split": [2, 5]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Grid Search Parameters:")
print(grid_search.best_params_)

print(
    "\nBest Cross-Validation Score:",
    grid_search.best_score_
)

predictions = grid_search.predict(X_test)

print(
    "Test Accuracy:",
    accuracy_score(y_test, predictions)
)


# Random Search
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_grid,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("\nBest Random Search Parameters:")
print(random_search.best_params_)
