# Model Evaluation

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ------------------------------------------
# Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


# ------------------------------------------
# Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------
# Model
# ------------------------------------------

model = LogisticRegression(
    max_iter=200
)

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

print(
    "Accuracy:",
    accuracy_score(y_test, y_pred)
)


# ------------------------------------------
# Precision
# ------------------------------------------

print(
    "Precision:",
    precision_score(
        y_test,
        y_pred,
        average="weighted"
    )
)


# ------------------------------------------
# Recall
# ------------------------------------------

print(
    "Recall:",
    recall_score(
        y_test,
        y_pred,
        average="weighted"
    )
)


# ------------------------------------------
# F1 Score
# ------------------------------------------

print(
    "F1 Score:",
    f1_score(
        y_test,
        y_pred,
        average="weighted"
    )
)


# ------------------------------------------
# Confusion Matrix
# ------------------------------------------

print(
    "\nConfusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ------------------------------------------
# Classification Report
# ------------------------------------------

print(
    "\nClassification Report:"
)

print(
    classification_report(
        y_test,
        y_pred
    )
)
