"""
18 - Advanced Machine Learning Mini Project
--------------------------------------------
Project: Customer Churn Prediction

Goal:
Build and evaluate an advanced classification workflow.

Workflow:

Data
 ↓
Train/Test Split
 ↓
Baseline Model
 ↓
Random Forest
 ↓
Cross-Validation
 ↓
Hyperparameter Tuning
 ↓
Evaluation
 ↓
Feature Importance
"""

import numpy as np
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# =========================================================
# 1. Create a realistic practice dataset
# =========================================================

X, y = make_classification(
    n_samples=2000,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    weights=[0.75, 0.25],
    random_state=42
)


# Give meaningful feature names
feature_names = [
    "tenure",
    "monthly_spend",
    "support_calls",
    "usage_frequency",
    "contract_length",
    "payment_delay",
    "satisfaction_score",
    "discount_rate",
    "service_count",
    "complaints"
]

X = pd.DataFrame(
    X,
    columns=feature_names
)

y = pd.Series(
    y,
    name="churn"
)


print("=" * 60)
print("CUSTOMER CHURN PREDICTION")
print("=" * 60)


# =========================================================
# 2. Understand the dataset
# =========================================================

print("\nDataset Shape:")
print(X.shape)

print("\nTarget Distribution:")
print(y.value_counts())


# =========================================================
# 3. Train/Test Split
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# =========================================================
# 4. Baseline Model
# =========================================================

baseline = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)


print("\nBaseline Performance")

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            baseline_predictions
        ),
        3
    )
)

print(
    "Precision:",
    round(
        precision_score(
            y_test,
            baseline_predictions
        ),
        3
    )
)

print(
    "Recall:",
    round(
        recall_score(
            y_test,
            baseline_predictions
        ),
        3
    )
)

print(
    "F1:",
    round(
        f1_score(
            y_test,
            baseline_predictions
        ),
        3
    )
)


# =========================================================
# 5. Cross-Validation
# =========================================================

cv_scores = cross_val_score(
    baseline,
    X_train,
    y_train,
    cv=5,
    scoring="f1"
)

print("\nCross-Validation F1 Scores:")
print(cv_scores)

print(
    "Mean CV F1:",
    round(cv_scores.mean(), 3)
)


# =========================================================
# 6. Hyperparameter Tuning
# =========================================================

parameter_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5],
    "class_weight": [None, "balanced"]
}


grid_search = GridSearchCV(
    estimator=RandomForestClassifier(
        random_state=42
    ),
    param_grid=parameter_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)


print("\nBest Parameters:")
print(grid_search.best_params_)

print(
    "\nBest Cross-Validation F1:",
    round(
        grid_search.best_score_,
        3
    )
)


# =========================================================
# 7. Final Model
# =========================================================

final_model = grid_search.best_estimator_

final_predictions = final_model.predict(X_test)


# =========================================================
# 8. Final Evaluation
# =========================================================

print("\nFinal Model Performance")

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            final_predictions
        ),
        3
    )
)

print(
    "Precision:",
    round(
        precision_score(
            y_test,
            final_predictions
        ),
        3
    )
)

print(
    "Recall:",
    round(
        recall_score(
            y_test,
            final_predictions
        ),
        3
    )
)

print(
    "F1 Score:",
    round(
        f1_score(
            y_test,
            final_predictions
        ),
        3
    )
)


# =========================================================
# 9. Confusion Matrix
# =========================================================

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        final_predictions
    )
)


# =========================================================
# 10. Classification Report
# =========================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        final_predictions
    )
)


# =========================================================
# 11. Feature Importance
# =========================================================

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": final_model.feature_importances_
})

importance = importance.sort_values(
    by="importance",
    ascending=False
)

print("\nFeature Importance:")

print(importance)


# =========================================================
# 12. Project Interpretation
# =========================================================

print("\nProject Interpretation")
print("-" * 40)

print(
    """
Use the model results to investigate:

1. Which features are most important?
2. How does the tuned model compare with the baseline?
3. Is recall important for this churn problem?
4. What types of errors does the confusion matrix show?
5. Which customers might need further investigation?
6. What additional data could improve the model?
7. Are there any potential data leakage risks?
"""
)


print("\nMini Project Completed!")
