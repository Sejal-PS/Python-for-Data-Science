"""
Project: Customer Churn Prediction

Skills:
- Data Preparation
- Feature Encoding
- Train/Test Split
- Logistic Regression
- Model Evaluation
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# 1. Create Sample Customer Data
# --------------------------------------------------

data = {
    "Age": [
        22, 25, 30, 35, 40,
        45, 50, 28, 32, 38,
        55, 60, 27, 42, 48
    ],
    "Monthly_Charges": [
        20, 25, 30, 45, 50,
        60, 70, 28, 35, 48,
        75, 80, 24, 55, 65
    ],
    "Contract": [
        "Monthly", "Monthly", "Yearly",
        "Yearly", "Monthly", "Yearly",
        "Yearly", "Monthly", "Monthly",
        "Yearly", "Yearly", "Monthly",
        "Monthly", "Yearly", "Yearly"
    ],
    "Churn": [
        1, 1, 0, 0, 1,
        0, 0, 1, 1, 0,
        0, 1, 1, 0, 0
    ]
}

df = pd.DataFrame(data)

print("Customer Data:")
print(df)


# --------------------------------------------------
# 2. Separate Features and Target
# --------------------------------------------------

X = df.drop("Churn", axis=1)

y = df["Churn"]


# --------------------------------------------------
# 3. Identify Categorical Columns
# --------------------------------------------------

categorical_features = [
    "Contract"
]


# --------------------------------------------------
# 4. Preprocessing
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# --------------------------------------------------
# 5. Create Pipeline
# --------------------------------------------------

model = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "classifier",
        LogisticRegression()
    )
])


# --------------------------------------------------
# 6. Train/Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 7. Train Model
# --------------------------------------------------

model.fit(
    X_train,
    y_train
)


# --------------------------------------------------
# 8. Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 9. Evaluation
# --------------------------------------------------

print("\nAccuracy:")
print(
    accuracy_score(
        y_test,
        y_pred
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Add more customer features.
# 2. Try another classification model.
# 3. Compare model performance.
# 4. Add a confusion matrix.
