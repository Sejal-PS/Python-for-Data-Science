# Pandas Series and DataFrame

import pandas as pd


# -------------------------
# 1. Creating a Series
# -------------------------

marks = pd.Series([80, 75, 90, 85, 70])

print("Marks Series:")
print(marks)


# -------------------------
# 2. Series with Custom Index
# -------------------------

marks = pd.Series(
    [80, 75, 90],
    index=["Rahul", "Priya", "Amit"]
)

print("\nSeries with Custom Index:")
print(marks)


# -------------------------
# 3. Accessing Series Values
# -------------------------

print("\nRahul's Marks:")
print(marks["Rahul"])

print("\nFirst Student:")
print(marks.iloc[0])


# -------------------------
# 4. Series Properties
# -------------------------

print("\nSeries Properties")

print("Values:")
print(marks.values)

print("Index:")
print(marks.index)

print("Data Type:")
print(marks.dtype)

print("Size:")
print(marks.size)


# -------------------------
# 5. Creating DataFrame
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# -------------------------
# 6. DataFrame Properties
# -------------------------

print("\nDataFrame Properties")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 7. Selecting a Column
# -------------------------

print("\nName Column:")
print(df["Name"])

print("\nMarks Column:")
print(df["Marks"])


# -------------------------
# 8. Selecting Multiple Columns
# -------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])


# -------------------------
# 9. Adding a New Column
# -------------------------

df["Passed"] = df["Marks"] >= 40

print("\nAfter Adding Passed Column:")
print(df)


# -------------------------
# 10. DataFrame Statistics
# -------------------------

print("\nMarks Statistics")

print("Mean:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())


# -------------------------
# 11. Data Science Example
# -------------------------

sales_data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Price": [55000, 25000, 18000, 15000],
    "Quantity": [2, 5, 3, 4]
}

sales_df = pd.DataFrame(sales_data)

sales_df["Total_Sales"] = (
    sales_df["Price"] * sales_df["Quantity"]
)

print("\nSales Data:")
print(sales_df)

print("\nTotal Revenue:")
print(sales_df["Total_Sales"].sum())
