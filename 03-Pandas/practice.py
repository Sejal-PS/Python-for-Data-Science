# Pandas - Practice Exercises

import pandas as pd
import numpy as np


# ==================================================
# PRACTICE DATASET
# ==================================================

data = {
    "Employee_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110
    ],
    "Name": [
        "Rahul", "Priya", "Amit", "Neha", "Sneha",
        "Rohit", "Pooja", "Kiran", "Anjali", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Sales", "IT", "HR", "Sales"
    ],
    "City": [
        "Pune", "Mumbai", "Pune", "Nashik", "Mumbai",
        "Pune", "Nashik", "Pune", "Mumbai", "Pune"
    ],
    "Age": [
        25, 28, 24, 30, 27,
        26, 29, 23, 31, 28
    ],
    "Salary": [
        45000, 50000, 40000, 55000, 48000,
        52000, 46000, 42000, 60000, 58000
    ],
    "Experience": [
        2, 4, 1, 6, 3,
        4, 5, 1, 7, 5
    ]
}

df = pd.DataFrame(data)

print("Employee Dataset:")
print(df)


# ==================================================
# BASIC INSPECTION
# ==================================================

# Exercise 1
# Display the first 5 rows.


# Exercise 2
# Display the last 3 rows.


# Exercise 3
# Find the number of rows and columns.


# Exercise 4
# Display all column names.


# Exercise 5
# Display the data types.


# Exercise 6
# Display basic statistical information.


# ==================================================
# COLUMN SELECTION
# ==================================================

# Exercise 7
# Select only the Name column.


# Exercise 8
# Select Name, Department and Salary.


# Exercise 9
# Select Age and Experience.


# ==================================================
# FILTERING
# ==================================================

# Exercise 10
# Find employees whose salary is greater than 50000.


# Exercise 11
# Find employees whose age is greater than 27.


# Exercise 12
# Find employees from Pune.


# Exercise 13
# Find employees from the IT department.


# Exercise 14
# Find employees whose salary is between 40000 and 50000.


# Exercise 15
# Find employees from Pune AND salary greater than 45000.


# Exercise 16
# Find employees from IT OR Sales department.


# Exercise 17
# Find employees who are NOT from Mumbai.


# ==================================================
# SORTING
# ==================================================

# Exercise 18
# Sort employees by Salary in ascending order.


# Exercise 19
# Sort employees by Salary in descending order.


# Exercise 20
# Sort employees by Experience in descending order.


# Exercise 21
# Sort employees first by Department and then by Salary.


# ==================================================
# COLUMNS AND TRANSFORMATION
# ==================================================

# Exercise 22
# Create a new column:
# Annual_Salary = Salary * 12


# Exercise 23
# Create a new column:
# Experience_Level
#
# If Experience >= 5:
# "Senior"
#
# Otherwise:
# "Junior"


# Exercise 24
# Create a new column:
# Salary_Category
#
# Salary >= 55000 -> High
# Salary >= 45000 -> Medium
# Otherwise -> Low


# Exercise 25
# Increase Salary by 10% and store
# the result in a new column called
# Updated_Salary.


# ==================================================
# GROUPBY
# ==================================================

# Exercise 26
# Find total salary by Department.


# Exercise 27
# Find average salary by Department.


# Exercise 28
# Find maximum salary by Department.


# Exercise 29
# Find minimum salary by Department.


# Exercise 30
# Find employee count by Department.


# Exercise 31
# Find average salary by City.


# Exercise 32
# Find total salary by City.


# ==================================================
# AGGREGATION
# ==================================================

# Exercise 33
# For each Department calculate:
#
# total salary
# average salary
# minimum salary
# maximum salary


# Exercise 34
# For each Department calculate:
#
# employee count
# average age
# average experience


# ==================================================
# STRING OPERATIONS
# ==================================================

# Exercise 35
# Convert employee names to uppercase.


# Exercise 36
# Convert department names to lowercase.


# Exercise 37
# Find employees whose name starts with "P".


# Exercise 38
# Find employees whose city contains "Pune".


# ==================================================
# INDEX OPERATIONS
# ==================================================

# Exercise 39
# Set Employee_ID as the DataFrame index.


# Exercise 40
# Reset the index.


# ==================================================
# MISSING VALUES PRACTICE
# ==================================================

missing_data = {
    "Name": [
        "A", "B", "C", "D", "E"
    ],
    "Age": [
        25, np.nan, 30, 28, np.nan
    ],
    "Salary": [
        40000, 50000, np.nan, 60000, 55000
    ]
}

missing_df = pd.DataFrame(missing_data)

print("\nMissing Value Dataset:")
print(missing_df)


# Exercise 41
# Find the number of missing values
# in each column.


# Exercise 42
# Fill missing Age values
# using the mean.


# Exercise 43
# Fill missing Salary values
# using the median.


# Exercise 44
# Remove rows containing missing values.


# ==================================================
# DUPLICATE PRACTICE
# ==================================================

duplicate_data = {
    "Customer_ID": [
        101, 102, 103, 101, 104, 102
    ],
    "Name": [
        "Rahul", "Priya", "Amit",
        "Rahul", "Neha", "Priya"
    ]
}

duplicate_df = pd.DataFrame(duplicate_data)

print("\nDuplicate Dataset:")
print(duplicate_df)


# Exercise 45
# Find duplicate Customer_ID values.


# Exercise 46
# Remove duplicate Customer_ID records.


# ==================================================
# PRACTICAL DATA ANALYSIS
# ==================================================

sales_data = {
    "Product": [
        "Laptop", "Mobile", "Laptop",
        "Tablet", "Mobile", "Monitor",
        "Laptop", "Tablet"
    ],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune",
        "Mumbai", "Nashik"
    ],
    "Sales": [
        55000, 25000, 65000,
        18000, 30000, 22000,
        60000, 20000
    ],
    "Quantity": [
        2, 5, 3, 3,
        6, 4, 2, 5
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Dataset:")
print(sales_df)


# Exercise 47
# Calculate Total_Sales:
#
# Sales * Quantity


# Exercise 48
# Find total sales by City.


# Exercise 49
# Find total quantity sold by Product.


# Exercise 50
# Find the product with the highest
# total sales.


# Exercise 51
# Find the city with the highest
# total sales.


# Exercise 52
# Sort the sales data by
# Total_Sales in descending order.


# ==================================================
# FINAL CHALLENGE
# ==================================================

# Use the employee dataset and answer:
#
# 1. Which department has the highest
#    average salary?
#
# 2. What is the average salary of
#    employees from Pune?
#
# 3. How many employees have more
#    than 3 years of experience?
#
# 4. Which employee has the highest salary?
#
# 5. What is the average age of
#    IT employees?
#
# 6. Create a Salary_Category column.
#
# 7. Create an Experience_Level column.
#
# 8. Create Annual_Salary column.
#
# 9. Display employees with salary
#    greater than 50000.
#
# 10. Display the final cleaned and
#     transformed DataFrame.
