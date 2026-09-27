# Decision Tree Classifier

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# ------------------------------------------
# Load Dataset
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

model = DecisionTreeClassifier(
    random_state=42
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
# Evaluation
# ------------------------------------------

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        y_pred
    )
)


# Decision Tree makes decisions using
# a sequence of conditions.
