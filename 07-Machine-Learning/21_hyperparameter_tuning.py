"""
Hyperparameter Tuning

Hyperparameters are settings that are chosen before
training a machine learning model.

GridSearchCV and RandomizedSearchCV can be used to
find useful hyperparameter combinations.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# --------------------------------------------------
# Create Pipeline
# --------------------------------------------------

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(random_state=42))
])


# --------------------------------------------------
# Define Hyperparameter Grid
# --------------------------------------------------

param_grid = {
    "model__n_estimators": [50, 100, 150],
    "model__max_depth": [None, 3, 5, 10],
    "model__min_samples_split": [2, 5]
}


# --------------------------------------------------
# Grid Search
# --------------------------------------------------

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X, y)


# --------------------------------------------------
# Results
# --------------------------------------------------

print("Best Parameters:")
print(grid_search.best_params__)

print("\nBest Cross-Validation Score:")
print(grid_search.best_score_)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Try different n_estimators values.
# 2. Add another Random Forest parameter.
# 3. Change the scoring metric.
# 4. Try GridSearchCV with another classifier.
