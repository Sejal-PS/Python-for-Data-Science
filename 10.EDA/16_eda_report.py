"""
16 - Professional EDA Report

This example demonstrates how analysis can be organized
into a professional EDA report.
"""

import pandas as pd

data = {
"Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
"Region": ["West", "North", "West", "South", "North"],
"Sales": [80000, 50000, 30000, 75000, 55000],
"Quantity": [8, 10, 6, 7, 11]
}

df = pd.DataFrame(data)

---------------------------------------------------------
1. Business Problem
---------------------------------------------------------

business_problem = """
Understand sales performance across products and regions.
"""

---------------------------------------------------------
2. Dataset Overview
---------------------------------------------------------

rows, columns = df.shape

---------------------------------------------------------
3. Data Quality
---------------------------------------------------------

missing_values = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

---------------------------------------------------------
4. Key Statistics
---------------------------------------------------------

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

top_product = (
df.groupby("Product")["Sales"]
.sum()
.idxmax()
)

top_region = (
df.groupby("Region")["Sales"]
.sum()
.idxmax()
)

---------------------------------------------------------
5. Generate Report
---------------------------------------------------------

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS REPORT")
print("=" * 60)

print("\n1. BUSINESS PROBLEM")
print(business_problem.strip())

print("\n2. DATASET OVERVIEW")
print("Rows:", rows)
print("Columns:", columns)

print("\n3. DATA QUALITY")
print("Missing Values:", missing_values)
print("Duplicate Rows:", duplicates)

print("\n4. KEY STATISTICS")
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))

print("\n5. KEY FINDINGS")
print("Top Product:", top_product)
print("Top Region:", top_region)

print("\n6. BUSINESS INSIGHT")
print(
f"{top_product} generated the highest observed total sales "
"among the products in this dataset."
)

print("\n7. LIMITATIONS")
print(
"This analysis uses a small example dataset. "
"Real-world conclusions require appropriate data coverage "
"and domain context."
)

print("\n8. NEXT STEPS")
print(
"Investigate sales trends, customer behavior, product-level "
"performance and additional business factors."
)

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)
