# K-Nearest Neighbors

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ------------------------------------------
# Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


# ------------------------------------------
# Split Data
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------
# KNN Model
# ------------------------------------------

model = KNeighborsClassifier(
    n_neighbors=5
)


# ------------------------------------------
# Training
# ------------------------------------------

model.fit(
    X_train,
    y_train
)


# ------------------------------------------
# Prediction
# ------------------------------------------

y_pred = model.predict(
    X_test
)


# ------------------------------------------
# Accuracy
# ------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "Accuracy:",
    accuracy
)


# ------------------------------------------
# Concept
# ------------------------------------------

# KNN predicts a data point based on
# nearby observations.
#
# K = number of neighbors considered.
