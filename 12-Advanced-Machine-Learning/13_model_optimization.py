"""
13 - Model Optimization
-----------------------
Understand how model complexity affects generalization.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Load data
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Decision Tree Depth Comparison")
print("-" * 40)

for depth in [1, 2, 3, 4, 5, 6, 8, 10, None]:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_score = accuracy_score(
        y_train,
        train_predictions
    )

    test_score = accuracy_score(
        y_test,
        test_predictions
    )

    print(
        f"Depth={depth!s:>4} | "
        f"Train={train_score:.3f} | "
        f"Test={test_score:.3f}"
    )


print("\nInterpretation:")
print(
    "Compare training and test performance to understand "
    "how model complexity can affect generalization."
)
