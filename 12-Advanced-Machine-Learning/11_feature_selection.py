"""
11 - Feature Selection
----------------------
Learn different approaches to selecting useful features.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import (
    VarianceThreshold,
    SelectKBest,
    f_classif
)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

print("Original number of features:", X.shape[1])


# Variance Threshold
selector = VarianceThreshold(threshold=0.01)

X_variance = selector.fit_transform(X)

print(
    "After Variance Threshold:",
    X_variance.shape[1]
)


# SelectKBest
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("selector", SelectKBest(
        score_func=f_classif,
        k=10
    )),
    ("classifier", LogisticRegression(max_iter=5000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "\nAccuracy with selected features:",
    accuracy_score(y_test, predictions)
)

# Selected feature names
selector = SelectKBest(
    score_func=f_classif,
    k=10
)

selector.fit(X, y)

selected_features = [
    feature
    for feature, selected
    in zip(data.feature_names, selector.get_support())
    if selected
]

print("\nSelected Features:")

for feature in selected_features:
    print("-", feature)
