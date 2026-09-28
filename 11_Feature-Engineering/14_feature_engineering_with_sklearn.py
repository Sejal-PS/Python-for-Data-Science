"""
Feature Engineering with Scikit-learn

Learn:
- SimpleImputer
- OneHotEncoder
- StandardScaler
- MinMaxScaler
- RobustScaler
- ColumnTransformer
- Pipeline
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler
)

data = {
    "age": [25, 30, None, 45, 35],
    "income": [30000, 45000, 50000, None, 75000],
    "city": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"]
}

df = pd.DataFrame(data)

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

X_processed = preprocessor.fit_transform(df)

print("Original Dataset:")
print(df)

print("\nProcessed Data Shape:")
print(X_processed.shape)

print("\nPreprocessing completed using Scikit-learn.")
