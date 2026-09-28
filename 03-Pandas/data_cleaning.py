"""
Pandas Data Cleaning

Data cleaning is an important step in Data Science.
It involves identifying and fixing problems such as:

- Missing values
- Duplicate records
- Incorrect data types
- Extra spaces
- Inconsistent text
- Incorrect values
"""

import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. Create Messy Data
# --------------------------------------------------

data = {
    "Name": [" Alice ", "Bob", "Charlie", "Bob"],
    "Age": [21, np.nan, 23, 25],
    "Salary": [50000, 60000, np.nan, 60000],
    "City": ["Pune", "Mumbai", " pune ", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# --------------------------------------------------
# 2. Inspect the Data
# --------------------------------------------------

print("\nData Types:")
print(df.dtypes)

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 3. Handle Missing Values
# --------------------------------------------------

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

# Fill missing Salary with median
df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

print("\nAfter handling missing values:")
print(df)


# --------------------------------------------------
# 4. Remove Duplicate Records
# --------------------------------------------------

print("\nDuplicate Records:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)


# --------------------------------------------------
# 5. Remove Extra Spaces
# --------------------------------------------------

df["Name"] = df["Name"].str.strip()

df["City"] = df["City"].str.strip()

print("\nAfter removing extra spaces:")
print(df)


# --------------------------------------------------
# 6. Standardize Text
# --------------------------------------------------

df["City"] = df["City"].str.title()

print("\nAfter standardizing city names:")
print(df)


# --------------------------------------------------
# 7. Rename Columns
# --------------------------------------------------

df = df.rename(
    columns={
        "Name": "Employee_Name",
        "Salary": "Annual_Salary"
    }
)

print("\nAfter renaming columns:")
print(df)


# --------------------------------------------------
# 8. Correct Data Types
# --------------------------------------------------

df["Age"] = df["Age"].astype(int)

print("\nUpdated Data Types:")
print(df.dtypes)


# --------------------------------------------------
# 9. Detect Invalid Values
# --------------------------------------------------

# Example: identify employees with unrealistic age
invalid_age = df[
    (df["Age"] < 18) |
    (df["Age"] > 100)
]

print("\nInvalid age records:")
print(invalid_age)


# --------------------------------------------------
# 10. Create a Clean Dataset
# --------------------------------------------------

cleaned_df = df.copy()

print("\nFinal Cleaned Data:")
print(cleaned_df)

print("\nFinal Shape:")
print(cleaned_df.shape)


# --------------------------------------------------
# 11. Save Cleaned Data
# --------------------------------------------------

cleaned_df.to_csv(
    "cleaned_employee_data.csv",
    index=False
)

print("\nCleaned data saved successfully.")


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a DataFrame containing missing values.
# 2. Detect missing values using isnull().
# 3. Fill numerical missing values using mean or median.
# 4. Remove duplicate records.
# 5. Remove extra spaces from text columns.
# 6. Standardize text values.
# 7. Rename columns.
# 8. Convert columns to appropriate data types.
# 9. Detect invalid values.
# 10. Save the cleaned DataFrame as a CSV file.
