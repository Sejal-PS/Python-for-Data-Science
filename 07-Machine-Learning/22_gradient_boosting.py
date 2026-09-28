"""
Gradient Boosting

Gradient Boosting builds models sequentially.
Each new model attempts to improve the errors
made by previous models.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# --------------------------------------------------
# Split Data
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# Create Model
# --------------------------------------------------

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)


# --------------------------------------------------
# Train Model
# --------------------------------------------------

model.fit(X_train, y_train)


# --------------------------------------------------
# Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred
))


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Change the learning_rate.
# 2. Change n_estimators.
# 3. Compare Gradient Boosting with Random Forest.
# 4. Observe how model parameters affect accuracy.
