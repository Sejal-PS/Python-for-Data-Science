# Pandas - Reading Data

import pandas as pd


# -------------------------
# 1. Reading a CSV File
# -------------------------

# Example:
# df = pd.read_csv("data.csv")

# print(df)


# -------------------------
# 2. Reading CSV with Different Separator
# -------------------------

# Some files use ; instead of ,

# df = pd.read_csv("data.csv", sep=";")

# print(df)


# -------------------------
# 3. Reading Excel File
# -------------------------

# df = pd.read_excel("data.xlsx")

# print(df)


# -------------------------
# 4. Reading a Specific Excel Sheet
# -------------------------

# df = pd.read_excel(
#     "data.xlsx",
#     sheet_name="Sheet1"
# )

# print(df)


# -------------------------
# 5. Reading JSON File
# -------------------------

# df = pd.read_json("data.json")

# print(df)


# -------------------------
# 6. Creating a Sample CSV File
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "City": ["Pune", "Mumbai", "Pune", "Nashik"],
    "Marks": [80, 90, 75, 88]
}

sample_df = pd.DataFrame(data)

print("Sample Data:")
print(sample_df)


# -------------------------
# 7. Saving DataFrame as CSV
# -------------------------

sample_df.to_csv(
    "students.csv",
    index=False
)

print("\nCSV file created successfully.")


# -------------------------
# 8. Reading the Created CSV
# -------------------------

df = pd.read_csv("students.csv")

print("\nData Read from CSV:")
print(df)


# -------------------------
# 9. Reading Selected Columns
# -------------------------

df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)

print("\nSelected Columns:")
print(df)


# -------------------------
# 10. Reading Limited Rows
# -------------------------

df = pd.read_csv(
    "students.csv",
    nrows=2
)

print("\nFirst Two Rows:")
print(df)


# -------------------------
# 11. Checking File Data
# -------------------------

df = pd.read_csv("students.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 12. Basic Data Analysis
# -------------------------

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())
