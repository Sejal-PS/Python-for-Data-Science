"""
18 - EDA Mini Project
Customer Sales Analysis

Goal:
Perform an end-to-end Exploratory Data Analysis workflow.

Project Workflow:

Business Problem

Dataset Understanding

Data Quality

Numerical Analysis

Categorical Analysis

GroupBy Analysis

Visualization

Insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

=========================================================
1. BUSINESS PROBLEM
=========================================================

print("=" * 60)
print("CUSTOMER SALES EDA MINI PROJECT")
print("=" * 60)

print("""
Business Problem:

A company wants to understand its customer sales performance.

The analysis should identify:

Regional performance

Product category performance

Customer spending

Sales patterns

Potential business insights
""")

=========================================================
2. DATASET
=========================================================

data = {
"Customer": [
"Amit", "Priya", "Rahul", "Sneha",
"Vikas", "Neha", "Rohan", "Pooja",
"Kiran", "Anita", "Akash", "Meena"
],
"Region": [
"West", "West", "North", "South",
"North", "West", "South", "North",
"West", "South", "North", "West"
],
"Category": [
"Electronics", "Clothing", "Electronics", "Grocery",
"Clothing", "Electronics", "Grocery", "Electronics",
"Clothing", "Grocery", "Electronics", "Clothing"
],
"Sales": [
85000, 42000, 72000, 28000,
50000, 95000, 35000, 68000,
45000, 32000, 78000, 48000
],
"Quantity": [
8, 12, 7, 10,
9, 6, 13, 7,
11, 9, 8, 10
]
}

df = pd.DataFrame(data)

=========================================================
3. DATASET UNDERSTANDING
=========================================================

print("\n" + "=" * 60)
print("1. DATASET OVERVIEW")
print("=" * 60)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst Records:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

=========================================================
4. DATA QUALITY CHECK
=========================================================

print("\n" + "=" * 60)
print("2. DATA QUALITY")
print("=" * 60)

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Regions:")
print(df["Region"].unique())

print("\nUnique Categories:")
print(df["Category"].unique())

=========================================================
5. NUMERICAL ANALYSIS
=========================================================

print("\n" + "=" * 60)
print("3. NUMERICAL ANALYSIS")
print("=" * 60)

print("Total Sales:", df["Sales"].sum())

print("Average Sales:", round(df["Sales"].mean(), 2))

print("Maximum Sales:", df["Sales"].max())

print("Minimum Sales:", df["Sales"].min())

print("Total Quantity:", df["Quantity"].sum())

=========================================================
6. CATEGORICAL ANALYSIS
=========================================================

print("\n" + "=" * 60)
print("4. CATEGORICAL ANALYSIS")
print("=" * 60)

print("Customers by Region:")
print(df["Region"].value_counts())

print("\nCustomers by Category:")
print(df["Category"].value_counts())

=========================================================
7. GROUPBY BUSINESS ANALYSIS
=========================================================

print("\n" + "=" * 60)
print("5. BUSINESS ANALYSIS")
print("=" * 60)

region_sales = (
df.groupby("Region")["Sales"]
.sum()
.sort_values(ascending=False)
)

print("Sales by Region:")
print(region_sales)

category_sales = (
df.groupby("Category")["Sales"]
.sum()
.sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)

customer_sales = (
df.groupby("Customer")["Sales"]
.sum()
.sort_values(ascending=False)
)

print("\nCustomer Sales:")
print(customer_sales)

=========================================================
8. VISUALIZATION
=========================================================

sns.set_theme(style="whitegrid")

Regional Sales

plt.figure(figsize=(8, 5))

sns.barplot(
x=region_sales.index,
y=region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

Category Sales

plt.figure(figsize=(8, 5))

sns.barplot(
x=category_sales.index,
y=category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

Sales Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
data=df,
x="Sales",
kde=True,
bins=6
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

=========================================================
9. BUSINESS INSIGHTS
=========================================================

print("\n" + "=" * 60)
print("6. BUSINESS INSIGHTS")
print("=" * 60)

top_region = region_sales.idxmax()
top_region_sales = region_sales.max()

top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

top_customer = customer_sales.idxmax()
top_customer_sales = customer_sales.max()

print(
f"1. {top_region} has the highest observed regional sales "
f"of {top_region_sales}."
)

print(
f"2. {top_category} has the highest observed category sales "
f"of {top_category_sales}."
)

print(
f"3. {top_customer} has the highest observed customer sales "
f"of {top_customer_sales}."
)

=========================================================
10. FURTHER QUESTIONS
=========================================================

print("\n" + "=" * 60)
print("7. FURTHER QUESTIONS")
print("=" * 60)

print("""

Which products are driving regional performance?

Are high-sales customers concentrated in particular regions?

Does quantity sold explain differences in sales?

How does customer behavior differ across categories?

Would the findings change with a larger dataset?

What additional business information would improve the analysis?
""")

=========================================================
FINAL TAKEAWAY
=========================================================

print("\n" + "=" * 60)
print("PROJECT COMPLETE")
print("=" * 60)

print("""
This project demonstrates a complete EDA workflow:

Dataset Understanding
↓
Data Quality
↓
Numerical Analysis
↓
Categorical Analysis
↓
GroupBy Analysis
↓
Visualization
↓
Business Insights
↓
Further Questions
""")
