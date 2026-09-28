"""
07 - Missing Values Analysis

Learn how to:

Detect missing values

Measure missingness

Compare missing and complete records

Apply simple handling techniques
"""

import pandas as pd
import numpy as np

data = {
"Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas", "Neha"],
"Age": [22, 25, np.nan, 24, 30, 28],
"Salary": [30000, np.nan, 50000, 40000, np.nan, 55000],
"Department": ["IT", "HR", "IT", None, "Sales", "IT"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

---------------------------------------------------------
Detect Missing Values
---------------------------------------------------------

print("\nMissing Values:")
print(df.isnull())

---------------------------------------------------------
Count Missing Values
---------------------------------------------------------

print("\nMissing Count:")
print(df.isnull().sum())

---------------------------------------------------------
Missing Percentage
---------------------------------------------------------

print("\nMissing Percentage:")
print((df.isnull().mean() * 100).round(2))

---------------------------------------------------------
Complete Records
---------------------------------------------------------

print("\nComplete Records:")
print(df.dropna())

---------------------------------------------------------
Fill Numerical Missing Values
---------------------------------------------------------

df_filled = df.copy()

df_filled["Age"] = df_filled["Age"].fillna(
df_filled["Age"].median()
)

df_filled["Salary"] = df_filled["Salary"].fillna(
df_filled["Salary"].median()
)

---------------------------------------------------------
Fill Categorical Missing Values
---------------------------------------------------------

df_filled["Department"] = df_filled["Department"].fillna(
"Unknown"
)

print("\nAfter Simple Missing-Value Handling:")
print(df_filled)

---------------------------------------------------------
Important Note
---------------------------------------------------------

print("\nImportant:")
print("Missing values should be investigated before choosing a treatment.")
print("The correct approach depends on the dataset and business context.")
