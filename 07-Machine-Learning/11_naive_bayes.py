# Naive Bayes

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


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

model = GaussianNB()


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

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        y_pred
    )
)


# Naive Bayes is based on Bayes'
# theorem and commonly used for
# classification tasks.
