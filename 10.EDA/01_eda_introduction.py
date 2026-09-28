"""
01 - Exploratory Data Analysis Introduction

Learning Goals:

Understand what EDA means

Understand why EDA is important

Learn the basic EDA workflow

Perform a first look at a dataset
"""

import pandas as pd

---------------------------------------------------------
1. What is EDA?
---------------------------------------------------------

print("Exploratory Data Analysis (EDA)")
print("-" * 40)

print("""
EDA is the process of understanding a dataset before
building statistical or machine learning models.

A typical EDA workflow is:

Business Problem
↓
Understand Data
↓
Check Data Quality
↓
Explore Data
↓
Visualize Patterns
↓
Generate Insights
""")

---------------------------------------------------------
2. Create a Small Example Dataset
---------------------------------------------------------

data = {
"Employee": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
"Department": ["IT", "HR", "IT", "Sales", "Sales"],
"Experience": [2, 5, 3, 7, 4],
"Salary": [35000, 50000, 42000, 65000, 48000]
}

df = pd.DataFrame(data)

---------------------------------------------------------
3. First Look at the Dataset
---------------------------------------------------------

print("\nDataset:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst Records:")
print(df.head())

---------------------------------------------------------
4. Basic Statistics
---------------------------------------------------------

print("\nSummary Statistics:")
print(df.describe())

---------------------------------------------------------
5. Initial Questions
---------------------------------------------------------

print("\nInitial EDA Questions:")
print("1. How many employees are there?")
print("2. Which departments are present?")
print("3. What is the average salary?")
print("4. Is salary related to experience?")
print("5. Which department has higher salaries?")

---------------------------------------------------------
Key Takeaway
---------------------------------------------------------

print("\nKey Takeaway:")
print("EDA helps us understand the data before making decisions.")
print("Always start with questions, not just charts.")
