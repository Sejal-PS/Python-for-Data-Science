# Pandas - Data Inspection

import pandas as pd


# -------------------------
# 1. Create Sample Dataset
# -------------------------

data = {
    "Name": [
        "Rahul", "Priya", "Amit",
        "Neha", "Sneha", "Rohit"
    ],
    "Age": [22, 24, 23, 21, 25, 22],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune"
    ],
    "Marks": [80, 90, 75, 88, 67, 95]
}

df = pd.DataFrame(data)


# -------------------------
# 2. Display Dataset
# -------------------------

print("Dataset:")
print(df)


# -------------------------
# 3. First 5 Rows
# -------------------------

print("\nFirst 5 Rows:")
print(df.head())


# -------------------------
# 4. First 3 Rows
# -------------------------

print("\nFirst 3 Rows:")
print(df.head(3))


# -------------------------
# 5. Last 5 Rows
# -------------------------

print("\nLast 5 Rows:")
print(df.tail())


# -------------------------
# 6. Last 2 Rows
# -------------------------

print("\nLast 2 Rows:")
print(df.tail(2))


# -------------------------
# 7. Shape
# -------------------------

print("\nShape:")
print(df.shape)


# -------------------------
# 8. Number of Rows
# -------------------------

print("\nNumber of Rows:")
print(df.shape[0])


# -------------------------
# 9. Number of Columns
# -------------------------

print("\nNumber of Columns:")
print(df.shape[1])


# -------------------------
# 10. Column Names
# -------------------------

print("\nColumn Names:")
print(df.columns)


# -------------------------
# 11. Index
# -------------------------

print("\nIndex:")
print(df.index)


# -------------------------
# 12. Data Types
# -------------------------

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 13. Dataset Information
# -------------------------

print("\nDataset Information:")
df.info()


# -------------------------
# 14. Statistical Summary
# -------------------------

print("\nStatistical Summary:")
print(df.describe())


# -------------------------
# 15. Numerical Columns Only
# -------------------------

print("\nNumerical Columns:")
print(df.select_dtypes(include="number"))


# -------------------------
# 16. Object/String Columns
# -------------------------

print("\nString Columns:")
print(df.select_dtypes(include="object"))


# -------------------------
# 17. Unique Values
# -------------------------

print("\nUnique Cities:")
print(df["City"].unique())


# -------------------------
# 18. Number of Unique Values
# -------------------------

print("\nNumber of Unique Cities:")
print(df["City"].nunique())


# -------------------------
# 19. Value Counts
# -------------------------

print("\nCity Counts:")
print(df["City"].value_counts())


# -------------------------
# 20. Missing Values
# -------------------------

print("\nMissing Values:")
print(df.isnull())


# -------------------------
# 21. Missing Value Count
# -------------------------

print("\nMissing Values Count:")
print(df.isnull().sum())


# -------------------------
# 22. Duplicate Rows
# -------------------------

print("\nDuplicate Rows:")
print(df.duplicated())


# -------------------------
# 23. Number of Duplicate Rows
# -------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# -------------------------
# 24. Basic Statistics
# -------------------------

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())


# -------------------------
# 25. Data Inspection Summary
# -------------------------

print("\n--- Data Inspection Summary ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
