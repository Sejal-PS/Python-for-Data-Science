# Train-Test Split

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# ------------------------------------------
# Load Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


# ------------------------------------------
# Train-Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------
# Check Shapes
# ------------------------------------------

print("X_train:", X_train.shape)

print("X_test:", X_test.shape)

print("y_train:", y_train.shape)

print("y_test:", y_test.shape)


# ------------------------------------------
# Why Split Data?
# ------------------------------------------

# Training data:
# Used to train the model.
#
# Testing data:
# Used to evaluate performance
# on unseen data.


# Common split:
#
# 80% Training
# 20% Testing
#
# But the correct split depends on
# the problem and dataset.
