"""
Feature Engineering - Mini Project

Scenario:
An e-commerce company wants to prepare customer transaction
data for Machine Learning.

Goals:
1. Inspect the dataset
2. Handle missing values
3. Create business features
4. Encode categorical variables
5. Scale numerical features
6. Prepare model-ready data

This project demonstrates a practical feature engineering workflow.
"""

import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ---------------------------------------------------------
# 1. Create Sample Dataset
# ---------------------------------------------------------

data = {
    "age": [22, 35, np.nan, 29, 51, 42, 31, np.nan],
    "city": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai"
    ],
    "quantity": [2, 5, 3, 10, 1, 4, 6, 2],
    "unit_price": [100, 250, 150, 50, 1000, 300, 200, 450],
    "customer_type": [
        "New",
        "Returning",
        "New",
        "Returning",
        "Returning",
        "New",
        "Returning",
        "New"
    ]
}

df = pd.DataFrame(data)

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)

print(df)

# ---------------------------------------------------------
# 2. Dataset Understanding
# ---------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Feature Creation
# ---------------------------------------------------------

df["total_amount"] = (
    df["quantity"] * df["unit_price"]
)

df["high_value_purchase"] = (
    df["total_amount"] >= 1000
)

print("\nAfter Feature Creation:")
print(df)

# ---------------------------------------------------------
# 4. Separate Features
# ---------------------------------------------------------

features = [
    "age",
    "city",
    "quantity",
    "unit_price",
    "total_amount",
    "customer_type"
]

X = df[features]

numeric_features = [
    "age",
    "quantity",
    "unit_price",
    "total_amount"
]

categorical_features = [
    "city",
    "customer_type"
]

# ---------------------------------------------------------
# 5. Build Preprocessing Pipelines
# ---------------------------------------------------------

numeric_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median")
    ),
    (
        "scaler",
        StandardScaler()
    )
])

categorical_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="most_frequent")
    ),
    (
        "encoder",
        OneHotEncoder(handle_unknown="ignore")
    )
])

preprocessor = ColumnTransformer([
    (
        "numeric",
        numeric_pipeline,
        numeric_features
    ),
    (
        "categorical",
        categorical_pipeline,
        categorical_features
    )
])

# ---------------------------------------------------------
# 6. Transform Dataset
# ---------------------------------------------------------

X_processed = preprocessor.fit_transform(X)

print("\n" + "=" * 60)
print("FEATURE ENGINEERING RESULT")
print("=" * 60)

print("Original feature count:", X.shape[1])
print("Processed feature count:", X_processed.shape[1])
print("Processed data shape:", X_processed.shape)

# ---------------------------------------------------------
# 7. Final Summary
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("""
The dataset was transformed through the following workflow:

Raw Dataset
     ↓
Dataset Inspection
     ↓
Missing Value Handling
     ↓
Feature Creation
     ↓
Categorical Encoding
     ↓
Numerical Scaling
     ↓
Model-Ready Dataset

Next Step:
Use the processed features in a Machine Learning model.
""")
