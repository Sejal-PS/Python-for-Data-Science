# Cross Validation

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


# ------------------------------------------
# Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


# ------------------------------------------
# Model
# ------------------------------------------

model = LogisticRegression(
    max_iter=200
)


# ------------------------------------------
# Cross Validation
# ------------------------------------------

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)


# ------------------------------------------
# Results
# ------------------------------------------

print(
    "Cross Validation Scores:"
)

print(
    scores
)


# ------------------------------------------
# Average Score
# ------------------------------------------

print(
    "\nAverage Score:",
    scores.mean()
)


# ------------------------------------------
# Concept
# ------------------------------------------

# Cross validation divides data into
# multiple folds.
#
# The model is trained and evaluated
# multiple times using different folds.
#
# This gives a more robust estimate
# of model performance.
