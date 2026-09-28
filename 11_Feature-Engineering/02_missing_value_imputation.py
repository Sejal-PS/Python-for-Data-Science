### Missing Value Imputation

## Learn:
- Identifying missing values
- Mean imputation
- Median imputation
- Mode imputation
- Constant value imputation
- Scikit-learn SimpleImputer


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    "age": [22, 35, np.nan, 29, 51],
    "income": [30000, np.nan, 72000, 45000, 90000],
    "city": ["Pune", "Mumbai", "Pune", np.nan, "Nashik"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Mean imputation
df["age_mean"] = df["age"].fillna(df["age"].mean())

# Median imputation
df["income_median"] = df["income"].fillna(df["income"].median())

# Mode imputation
df["city_mode"] = df["city"].fillna(df["city"].mode()[0])

print("\nAfter Pandas Imputation:")
print(df)

# SimpleImputer example
numeric_columns = ["age", "income"]

imputer = SimpleImputer(strategy="median")

df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

print("\nAfter SimpleImputer:")
print(df)

print("\nImportant:")
print("Choose an imputation strategy based on the data and business context.")
