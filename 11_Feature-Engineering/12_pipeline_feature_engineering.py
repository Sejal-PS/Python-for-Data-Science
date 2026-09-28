"""
Feature Engineering Pipeline

Learn:
- Pipeline
- SimpleImputer
- OneHotEncoder
- StandardScaler
- ColumnTransformer
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = {
    "age": [25, 30, None, 40, 35],
    "income": [30000, 45000, 50000, None, 60000],
    "city": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"]
}

df = pd.DataFrame(data)

X = df

numeric_features = ["age", "income"]
categorical_features = ["city"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

X_transformed = preprocessor.fit_transform(X)

print("Original Data:")
print(X)

print("\nTransformed Shape:")
print(X_transformed.shape)

print("\nPipeline completed successfully.")
