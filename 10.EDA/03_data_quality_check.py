"""
03 - Data Quality Check

Learn how to identify common data-quality problems:

Missing values

Duplicates

Invalid values

Incorrect categories

Incorrect data types
"""

import pandas as pd

data = {
"Name": ["Amit", "Priya", "Rahul", "Rahul", "Sneha", None],
"Age": [22, 25, 150, 28, -5, 30],
"Department": ["IT", "HR", "IT", "IT", "Sales", "sales"],
"Salary": [30000, 45000, 55000, 55000, 40000, None]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

---------------------------------------------------------
Missing Values
---------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

---------------------------------------------------------
Missing Value Percentage
---------------------------------------------------------

missing_percentage = df.isnull().mean() * 100

print("\nMissing Value Percentage:")
print(missing_percentage)

---------------------------------------------------------
Duplicate Records
---------------------------------------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

---------------------------------------------------------
Invalid Age Values
---------------------------------------------------------

invalid_age = df[(df["Age"] < 0) | (df["Age"] > 100)]

print("\nInvalid Age Records:")
print(invalid_age)

---------------------------------------------------------
Category Consistency
---------------------------------------------------------

print("\nDepartment Values:")
print(df["Department"].unique())

---------------------------------------------------------
Basic Data Types
---------------------------------------------------------

print("\nData Types:")
print(df.dtypes)

---------------------------------------------------------
Quality Summary
---------------------------------------------------------

print("\nData Quality Summary:")
print("Missing values checked.")
print("Duplicate records checked.")
print("Age range checked.")
print("Category consistency checked.")
print("Data types checked.")

---------------------------------------------------------
Key Takeaway
---------------------------------------------------------

print("\nKey Takeaway:")
print("Never begin advanced analysis before understanding data quality.")
