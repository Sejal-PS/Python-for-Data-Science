"""
Project: Real-World Style Data Cleaning

Skills:
- Missing Values
- Duplicate Records
- Text Cleaning
- Data Type Conversion
- Validation
"""

import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. Create Messy Dataset
# --------------------------------------------------

data = {
    "Name": [
        " Alice ",
        "Bob",
        "Charlie",
        "Bob",
        "David"
    ],
    "Age": [
        25,
        np.nan,
        30,
        np.nan,
        150
    ],
    "Salary": [
        50000,
        60000,
        np.nan,
        60000,
        70000
    ],
    "City": [
        "Pune",
        "Mumbai",
        " pune ",
        "Mumbai",
        "Delhi"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# --------------------------------------------------
# 2. Inspect Data
# --------------------------------------------------

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# --------------------------------------------------
# 3. Remove Duplicates
# --------------------------------------------------

df = df.drop_duplicates()


# --------------------------------------------------
# 4. Clean Text
# --------------------------------------------------

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.title()
)

df["City"] = (
    df["City"]
    .str.strip()
    .str.title()
)


# --------------------------------------------------
# 5. Handle Missing Values
# --------------------------------------------------

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)


# --------------------------------------------------
# 6. Validate Age
# --------------------------------------------------

df.loc[
    (df["Age"] < 18) |
    (df["Age"] > 100),
    "Age"
] = np.nan

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)


# --------------------------------------------------
# 7. Convert Data Type
# --------------------------------------------------

df["Age"] = df["Age"].astype(int)


# --------------------------------------------------
# 8. Final Dataset
# --------------------------------------------------

print("\nCleaned Dataset:")
print(df)

print("\nFinal Data Types:")
print(df.dtypes)


# --------------------------------------------------
# 9. Save Clean Dataset
# --------------------------------------------------

df.to_csv(
    "cleaned_employee_data.csv",
    index=False
)

print(
    "\nCleaned dataset saved successfully."
)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Add another missing-value column.
# 2. Add duplicate records.
# 3. Add inconsistent city names.
# 4. Clean the new problems.
# 5. Save the final dataset.
