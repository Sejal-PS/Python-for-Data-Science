# Pandas - Handling Missing Values

import pandas as pd
import numpy as np


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha",
        "Sneha"
    ],
    "Age": [22, 24, np.nan, 21, 25],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        np.nan,
        "Mumbai"
    ],
    "Marks": [80, np.nan, 75, 88, np.nan]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Check Missing Values
# -------------------------

print("\nIs Null:")
print(df.isnull())


# -------------------------
# 3. Check Missing Values using isna()
# -------------------------

print("\nIs NaN:")
print(df.isna())


# -------------------------
# 4. Count Missing Values
# -------------------------

print("\nMissing Values Count:")
print(df.isnull().sum())


# -------------------------
# 5. Total Missing Values
# -------------------------

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# -------------------------
# 6. Percentage of Missing Values
# -------------------------

print("\nMissing Value Percentage:")

missing_percentage = (
    df.isnull().mean() * 100
)

print(missing_percentage)


# -------------------------
# 7. Rows Having Missing Values
# -------------------------

print("\nRows with Missing Values:")
print(df[df.isnull().any(axis=1)])


# -------------------------
# 8. Rows Without Missing Values
# -------------------------

print("\nRows without Missing Values:")
print(df.dropna())


# -------------------------
# 9. Drop Rows with Missing Values
# -------------------------

clean_df = df.dropna()

print("\nAfter dropna():")
print(clean_df)


# -------------------------
# 10. Fill Missing Values with 0
# -------------------------

filled_zero = df.fillna(0)

print("\nMissing Values Filled with 0:")
print(filled_zero)


# -------------------------
# 11. Fill Missing Age with Mean
# -------------------------

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

print("\nAge after Filling with Mean:")
print(df)


# -------------------------
# 12. Fill Missing Marks with Mean
# -------------------------

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nMarks after Filling with Mean:")
print(df)


# -------------------------
# 13. Fill Missing City with Mode
# -------------------------

df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

print("\nCity after Filling with Mode:")
print(df)


# -------------------------
# 14. Forward Fill
# -------------------------

data = {
    "Sales": [
        1000,
        np.nan,
        1500,
        np.nan,
        2000
    ]
}

sales_df = pd.DataFrame(data)

print("\nSales Data:")
print(sales_df)

print("\nForward Fill:")
print(sales_df.ffill())


# -------------------------
# 15. Backward Fill
# -------------------------

print("\nBackward Fill:")
print(sales_df.bfill())


# -------------------------
# 16. Replace Specific Values
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [80, -1, 90]
}

marks_df = pd.DataFrame(data)

print("\nOriginal Marks Data:")
print(marks_df)

marks_df["Marks"] = marks_df["Marks"].replace(
    -1,
    np.nan
)

print("\nAfter Replacing -1 with NaN:")
print(marks_df)


# -------------------------
# 17. Fill Replaced Value
# -------------------------

marks_df["Marks"] = marks_df["Marks"].fillna(
    marks_df["Marks"].mean()
)

print("\nAfter Filling Missing Marks:")
print(marks_df)


# -------------------------
# 18. Data Science Example
# -------------------------

employee_data = {
    "Employee": [
        "A", "B", "C", "D", "E"
    ],
    "Salary": [
        30000,
        40000,
        np.nan,
        50000,
        np.nan
    ],
    "Experience": [
        2,
        4,
        3,
        np.nan,
        5
    ]
}

employee_df = pd.DataFrame(employee_data)

print("\nEmployee Data:")
print(employee_df)

print("\nMissing Values:")
print(employee_df.isnull().sum())


# Fill Salary with Median

employee_df["Salary"] = employee_df["Salary"].fillna(
    employee_df["Salary"].median()
)


# Fill Experience with Mean

employee_df["Experience"] = employee_df["Experience"].fillna(
    employee_df["Experience"].mean()
)

print("\nCleaned Employee Data:")
print(employee_df)
