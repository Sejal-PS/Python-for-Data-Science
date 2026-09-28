"""
14 - Ensemble Learning
----------------------
Compare individual and ensemble classifiers.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    VotingClassifier,
    RandomForestClassifier,
    GradientBoostingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
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


# Individual models
logistic = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

gradient_boosting = GradientBoostingClassifier(
    random_state=42
)


# Voting ensemble
voting_model = VotingClassifier(
    estimators=[
        ("logistic", logistic),
        ("random_forest", random_forest),
        ("gradient_boosting", gradient_boosting)
    ],
    voting="hard"
)


# Train
voting_model.fit(X_train, y_train)

# Predict
predictions = voting_model.predict(X_test)

# Evaluate
print(
    "Voting Ensemble Accuracy:",
    accuracy_score(y_test, predictions)
)

print("\nIndividual Model Performance:")

models = {
    "Logistic Regression": logistic,
    "Random Forest": random_forest,
    "Gradient Boosting": gradient_boosting
}

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    score = accuracy_score(y_test, pred)

    print(f"{name}: {score:.3f}")
