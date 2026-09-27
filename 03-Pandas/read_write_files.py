# Pandas - Read and Write Files

import pandas as pd


# ==================================================
# 1. Create DataFrame
# ==================================================

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "City": ["Pune", "Mumbai", "Pune", "Nashik"],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# ==================================================
# 2. Write DataFrame to CSV
# ==================================================

df.to_csv(
    "students.csv",
    index=False
)

print("\nCSV file created successfully.")


# ==================================================
# 3. Read CSV File
# ==================================================

df_csv = pd.read_csv(
    "students.csv"
)

print("\nData read from CSV:")
print(df_csv)


# ==================================================
# 4. Read Specific Columns from CSV
# ==================================================

df_selected = pd.read_csv(
    "students.csv",
    usecols=[
        "Name",
        "Marks"
    ]
)

print("\nSelected Columns:")
print(df_selected)


# ==================================================
# 5. Write to Excel
# ==================================================

df.to_excel(
    "students.xlsx",
    index=False
)

print("\nExcel file created successfully.")


# ==================================================
# 6. Read Excel File
# ==================================================

df_excel = pd.read_excel(
    "students.xlsx"
)

print("\nData read from Excel:")
print(df_excel)


# ==================================================
# 7. Write Only Selected Columns
# ==================================================

df[
    ["Name", "Marks"]
].to_csv(
    "student_marks.csv",
    index=False
)

print("\nSelected data saved to CSV.")


# ==================================================
# 8. Read Data with Specific Rows
# ==================================================

df_rows = pd.read_csv(
    "students.csv",
    nrows=2
)

print("\nFirst Two Rows:")
print(df_rows)


# ==================================================
# 9. Read CSV with Custom Missing Value
# ==================================================

data_with_missing = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit"
    ],
    "Marks": [
        80,
        "NA",
        75
    ]
}

missing_df = pd.DataFrame(
    data_with_missing
)

missing_df.to_csv(
    "marks_with_missing.csv",
    index=False
)

read_missing = pd.read_csv(
    "marks_with_missing.csv",
    na_values=["NA"]
)

print("\nCSV with Missing Values:")
print(read_missing)


# ==================================================
# 10. Append Data to CSV
# ==================================================

new_data = pd.DataFrame({
    "Name": ["Sneha"],
    "Age": [25],
    "City": ["Mumbai"],
    "Marks": [92]
})

new_data.to_csv(
    "students.csv",
    mode="a",
    header=False,
    index=False
)

print("\nNew data appended to CSV.")


# ==================================================
# 11. Read Final CSV
# ==================================================

final_df = pd.read_csv(
    "students.csv"
)

print("\nFinal CSV Data:")
print(final_df)


# ==================================================
# 12. Practical Data Science Example
# ==================================================

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Nashik",
        "Pune"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        22000
    ]
}

sales_df = pd.DataFrame(
    sales_data
)

print("\nSales Data:")
print(sales_df)


# Save sales data

sales_df.to_csv(
    "sales_data.csv",
    index=False
)


# Read sales data

sales = pd.read_csv(
    "sales_data.csv"
)

print("\nSales Data Read from CSV:")
print(sales)


# Calculate total sales

total_sales = sales["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)
