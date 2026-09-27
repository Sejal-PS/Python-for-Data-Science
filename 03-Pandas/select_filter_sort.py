# Pandas - Select, Filter and Sort

import pandas as pd


# -------------------------
# 1. Create Dataset
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

print("Dataset:")
print(df)


# -------------------------
# 2. Select One Column
# -------------------------

print("\nName Column:")
print(df["Name"])


# -------------------------
# 3. Select Multiple Columns
# -------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])


# -------------------------
# 4. Select First Row
# -------------------------

print("\nFirst Row:")
print(df.iloc[0])


# -------------------------
# 5. Select First Three Rows
# -------------------------

print("\nFirst Three Rows:")
print(df.iloc[0:3])


# -------------------------
# 6. Select Specific Rows
# -------------------------

print("\nFirst and Third Row:")
print(df.iloc[[0, 2]])


# -------------------------
# 7. Select Rows and Columns
# -------------------------

print("\nFirst Three Rows - Name and Marks:")
print(
    df.iloc[0:3, [0, 3]]
)


# -------------------------
# 8. loc - Label Based Selection
# -------------------------

print("\nUsing loc:")
print(df.loc[0:2, ["Name", "Marks"]])


# -------------------------
# 9. Filter by Marks
# -------------------------

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])


# -------------------------
# 10. Filter by Age
# -------------------------

print("\nStudents with Age > 22:")
print(df[df["Age"] > 22])


# -------------------------
# 11. Filter by City
# -------------------------

print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])


# -------------------------
# 12. Filter using >=
# -------------------------

print("\nStudents with Marks >= 80:")
print(df[df["Marks"] >= 80])


# -------------------------
# 13. Filter using <
# -------------------------

print("\nStudents with Marks < 80:")
print(df[df["Marks"] < 80])


# -------------------------
# 14. Multiple Conditions - AND
# -------------------------

print("\nAge > 22 AND Marks > 80:")

result = df[
    (df["Age"] > 22) &
    (df["Marks"] > 80)
]

print(result)


# -------------------------
# 15. Multiple Conditions - OR
# -------------------------

print("\nAge > 23 OR Marks > 90:")

result = df[
    (df["Age"] > 23) |
    (df["Marks"] > 90)
]

print(result)


# -------------------------
# 16. NOT Condition
# -------------------------

print("\nStudents NOT from Pune:")

result = df[df["City"] != "Pune"]

print(result)


# -------------------------
# 17. isin()
# -------------------------

print("\nStudents from Pune or Mumbai:")

result = df[
    df["City"].isin(["Pune", "Mumbai"])
]

print(result)


# -------------------------
# 18. between()
# -------------------------

print("\nStudents with Marks between 70 and 90:")

result = df[
    df["Marks"].between(70, 90)
]

print(result)


# -------------------------
# 19. Sort Ascending
# -------------------------

print("\nMarks - Ascending:")

result = df.sort_values("Marks")

print(result)


# -------------------------
# 20. Sort Descending
# -------------------------

print("\nMarks - Descending:")

result = df.sort_values(
    "Marks",
    ascending=False
)

print(result)


# -------------------------
# 21. Sort by Multiple Columns
# -------------------------

print("\nSort by City and Marks:")

result = df.sort_values(
    ["City", "Marks"]
)

print(result)


# -------------------------
# 22. Reset Index
# -------------------------

result = df.sort_values(
    "Marks",
    ascending=False
)

result = result.reset_index(drop=True)

print("\nAfter Resetting Index:")
print(result)


# -------------------------
# 23. Data Science Example
# -------------------------

print("\n--- Data Science Example ---")

sales_data = {
    "Product": [
        "Laptop", "Mobile", "Laptop",
        "Tablet", "Mobile", "Monitor"
    ],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune"
    ],
    "Sales": [
        55000, 25000, 65000,
        18000, 30000, 22000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Sales above 30000

print("\nSales above 30000:")
print(
    sales_df[
        sales_df["Sales"] > 30000
    ]
)


# Sales from Pune

print("\nSales from Pune:")
print(
    sales_df[
        sales_df["City"] == "Pune"
    ]
)


# Highest Sales

print("\nHighest Sales:")
print(
    sales_df.sort_values(
        "Sales",
        ascending=False
    ).head(1)
)
