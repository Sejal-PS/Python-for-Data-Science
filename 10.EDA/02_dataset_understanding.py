"""
02 - Dataset Understanding

Learn how to inspect an unfamiliar dataset before analysis.
"""

import pandas as pd

data = {
"Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas", "Neha"],
"Age": [22, 25, 28, 24, 30, 26],
"City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai", "Pune"],
"Salary": [30000, 45000, 55000, 35000, 70000, 48000],
"Experience": [1, 3, 5, 2, 7, 4]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Dataset Shape
---------------------------------------------------------

print("Shape:")
print(df.shape)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

---------------------------------------------------------
Column Names
---------------------------------------------------------

print("\nColumns:")
print(df.columns.tolist())

---------------------------------------------------------
First and Last Records
---------------------------------------------------------

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

---------------------------------------------------------
Random Sample
---------------------------------------------------------

print("\nRandom Sample:")
print(df.sample(3, random_state=42))

---------------------------------------------------------
Data Types
---------------------------------------------------------

print("\nData Types:")
print(df.dtypes)

---------------------------------------------------------
Dataset Information
---------------------------------------------------------

print("\nDataset Information:")
df.info()

---------------------------------------------------------
Unique Values
---------------------------------------------------------

print("\nUnique Cities:")
print(df["City"].unique())

print("\nNumber of Unique Cities:")
print(df["City"].nunique())

---------------------------------------------------------
Statistical Summary
---------------------------------------------------------

print("\nNumerical Summary:")
print(df.describe())

---------------------------------------------------------
Business Questions
---------------------------------------------------------

print("\nBusiness Questions:")
print("What is the average salary?")
print("Which city has the highest number of employees?")
print("What is the average experience?")
