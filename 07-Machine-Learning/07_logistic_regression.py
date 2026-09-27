# Logistic Regression

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


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
# Create Model
# ------------------------------------------

model = LogisticRegression(
    max_iter=200
)


# ------------------------------------------
# Train
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
# Sample Prediction
# ------------------------------------------

prediction = model.predict(
    [[5.1, 3.5, 1.4, 0.2]]
)

print(
    "Predicted Class:",
    prediction[0]
)


# Logistic Regression is commonly used
# for classification problems.
