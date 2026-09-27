# Pandas - Index and Column Management

import pandas as pd


# -------------------------
# 1. Create DataFrame
# -------------------------

data = {
    "Student_ID": [101, 102, 103, 104],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ],
    "Age": [22, 24, 23, 21],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# -------------------------
# 2. View Index
# -------------------------

print("\nIndex:")
print(df.index)


# -------------------------
# 3. View Columns
# -------------------------

print("\nColumns:")
print(df.columns)


# -------------------------
# 4. Set a Column as Index
# -------------------------

df_indexed = df.set_index(
    "Student_ID"
)

print("\nStudent_ID as Index:")
print(df_indexed)


# -------------------------
# 5. Access Data Using Index
# -------------------------

print("\nStudent 101:")
print(df_indexed.loc[101])


# -------------------------
# 6. Access Multiple Index Values
# -------------------------

print("\nStudents 101 and 103:")

print(
    df_indexed.loc[[101, 103]]
)


# -------------------------
# 7. Reset Index
# -------------------------

reset_df = df_indexed.reset_index()

print("\nAfter Resetting Index:")
print(reset_df)


# -------------------------
# 8. Set Index Permanently
# -------------------------

df.set_index(
    "Student_ID",
    inplace=True
)

print("\nPermanent Index:")
print(df)


# -------------------------
# 9. Reset Index Permanently
# -------------------------

df.reset_index(
    inplace=True
)

print("\nIndex Reset:")
print(df)


# -------------------------
# 10. Rename Columns
# -------------------------

df.rename(
    columns={
        "Student_ID": "ID",
        "Marks": "Score"
    },
    inplace=True
)

print("\nRenamed Columns:")
print(df)


# -------------------------
# 11. Rename All Columns
# -------------------------

df.columns = [
    "Student_ID",
    "Student_Name",
    "Student_Age",
    "Student_Score"
]

print("\nAll Columns Renamed:")
print(df)


# -------------------------
# 12. Add New Column
# -------------------------

df["Result"] = "Pass"

print("\nNew Column Added:")
print(df)


# -------------------------
# 13. Add Column at Specific Position
# -------------------------

df.insert(
    1,
    "Department",
    [
        "IT",
        "HR",
        "IT",
        "Sales"
    ]
)

print("\nColumn Inserted:")
print(df)


# -------------------------
# 14. Move Column
# -------------------------

result_column = df.pop("Result")

df["Result"] = result_column

print("\nResult Column Moved:")
print(df)


# -------------------------
# 15. Delete a Column
# -------------------------

df_without_department = df.drop(
    columns=["Department"]
)

print("\nAfter Removing Department:")
print(df_without_department)


# -------------------------
# 16. Drop Multiple Columns
# -------------------------

result = df.drop(
    columns=[
        "Department",
        "Result"
    ]
)

print("\nAfter Removing Multiple Columns:")
print(result)


# -------------------------
# 17. Reorder Columns
# -------------------------

result = df[
    [
        "Student_ID",
        "Student_Name",
        "Department",
        "Student_Age",
        "Student_Score",
        "Result"
    ]
]

print("\nReordered Columns:")
print(result)


# -------------------------
# 18. Check Column Names
# -------------------------

print("\nColumn Names:")
print(list(df.columns))


# -------------------------
# 19. Check Index Values
# -------------------------

print("\nIndex Values:")
print(df.index.tolist())


# -------------------------
# 20. Data Science Example
# -------------------------

sales_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        22000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Set Order_ID as index

sales_df.set_index(
    "Order_ID",
    inplace=True
)

print("\nOrder_ID as Index:")
print(sales_df)


# Access one order

print("\nOrder 1001:")
print(sales_df.loc[1001])


# Reset index

sales_df.reset_index(
    inplace=True
)

print("\nAfter Reset:")
print(sales_df)
