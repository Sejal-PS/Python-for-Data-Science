"""
03 - Gradient Boosting
----------------------
Gradient Boosting builds models sequentially to improve
previous predictions.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score


# Load dataset
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

# Create Gradient Boosting model
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Gradient Boosting Accuracy:", accuracy)

print("\nFeature Importance:")

for feature, importance in zip(
    iris.feature_names,
    model.feature_importances_
):
    print(f"{feature}: {importance:.3f}")
