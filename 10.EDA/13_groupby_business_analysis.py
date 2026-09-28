"""
13 - GroupBy Business Analysis

Learn how to use GroupBy to answer real-world questions.
"""

import pandas as pd

data = {
"Region": [
"West", "West", "North", "North",
"South", "South", "West", "North"
],
"Category": [
"Laptop", "Phone", "Laptop", "Phone",
"Laptop", "Phone", "Phone", "Laptop"
],
"Sales": [80000, 50000, 70000, 45000, 60000, 55000, 65000, 75000],
"Quantity": [8, 10, 7, 9, 6, 11, 12, 7]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Total Sales by Region
---------------------------------------------------------

region_sales = (
df.groupby("Region")["Sales"]
.sum()
.sort_values(ascending=False)
)

print("Total Sales by Region:")
print(region_sales)

---------------------------------------------------------
Average Sales by Category
---------------------------------------------------------

category_sales = (
df.groupby("Category")["Sales"]
.mean()
.sort_values(ascending=False)
)

print("\nAverage Sales by Category:")
print(category_sales)

---------------------------------------------------------
Multiple Aggregations
---------------------------------------------------------

summary = df.groupby("Region").agg(
Total_Sales=("Sales", "sum"),
Average_Sales=("Sales", "mean"),
Total_Quantity=("Quantity", "sum")
)

print("\nRegional Business Summary:")
print(summary)

---------------------------------------------------------
Business Questions
---------------------------------------------------------

print("\nBusiness Questions:")
print("1. Which region generates the highest total sales?")
print("2. Which category has higher average sales?")
print("3. Which region has the highest quantity sold?")

---------------------------------------------------------
Key Takeaway
---------------------------------------------------------

print("\nKey Takeaway:")
print("GroupBy helps convert raw records into business-level summaries.")
