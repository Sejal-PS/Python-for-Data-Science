"""
Outlier Treatment

Learn:
- IQR method
- Detecting outliers
- Capping extreme values
- Why outliers should be investigated
"""

import pandas as pd

data = {
    "salary": [25000, 30000, 32000, 35000, 40000, 45000, 500000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[
    (df["salary"] < lower_bound) |
    (df["salary"] > upper_bound)
]

print("\nDetected Outliers:")
print(outliers)

# Capping
df["salary_capped"] = df["salary"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\nAfter Capping:")
print(df)

print("\nImportant: An outlier is not automatically an error.")
print("Always investigate the reason before removing it.")
