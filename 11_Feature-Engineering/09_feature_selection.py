"""
Feature Selection

Learn:
- Correlation-based selection
- Variance-based selection
- SelectKBest
"""

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression, VarianceThreshold

data = {
    "age": [20, 25, 30, 35, 40, 45],
    "experience": [1, 3, 5, 8, 12, 15],
    "income": [20000, 30000, 40000, 55000, 70000, 90000],
    "constant_feature": [1, 1, 1, 1, 1, 1],
    "target": [21000, 32000, 43000, 56000, 72000, 95000]
}

df = pd.DataFrame(data)

X = df.drop(columns="target")
y = df["target"]

print("Correlation with Target:")
print(df.corr(numeric_only=True)["target"])

# Remove zero-variance features
variance_selector = VarianceThreshold(threshold=0)

X_variance = variance_selector.fit_transform(X)

print("\nShape after variance selection:")
print(X_variance.shape)

# Select top features
selector = SelectKBest(score_func=f_regression, k=2)

X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("\nSelected Features:")
print(list(selected_features))

print("\nFeature selection can reduce unnecessary information and improve model efficiency.")
