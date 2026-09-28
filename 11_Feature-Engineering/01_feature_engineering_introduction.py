###  Feature Engineering - Introduction

## Learn:
- What is a feature?
- What is feature engineering?
- Raw vs engineered features
- Basic feature creation


import pandas as pd

# Sample customer dataset
data = {
    "age": [22, 35, 42, 29, 51],
    "annual_income": [30000, 55000, 72000, 45000, 90000],
    "purchase_amount": [500, 1200, 2500, 800, 3000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Create a new feature
df["income_per_age"] = df["annual_income"] / df["age"]

print("\nAfter Feature Engineering:")
print(df)

# Create a spending category
df["high_spender"] = df["purchase_amount"] > 1000

print("\nWith New Categorical Feature:")
print(df)

print("\nFeature Engineering means creating or transforming features")
print("so that the data represents the problem more effectively.")
