# Machine Learning Pipeline

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score


# ------------------------------------------
# Dataset
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
# Pipeline
# ------------------------------------------

pipeline = Pipeline([
    (
        "scaler",
        StandardScaler()
    ),
    (
        "model",
        LogisticRegression(
            max_iter=200
        )
    )
])


# ------------------------------------------
# Train Pipeline
# ------------------------------------------

pipeline.fit(
    X_train,
    y_train
)


# ------------------------------------------
# Prediction
# ------------------------------------------

y_pred = pipeline.predict(
    X_test
)


# ------------------------------------------
# Evaluation
# ------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "Accuracy:",
    accuracy
)


# Pipeline combines multiple
# preprocessing and modelling steps.
