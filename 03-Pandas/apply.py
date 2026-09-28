"""
Pandas apply(), map() and lambda functions

The apply() method is used to apply a function
to values in a Series or DataFrame.
"""

import pandas as pd


# --------------------------------------------------
# 1. Create a DataFrame
# --------------------------------------------------

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 72, 91, 65],
    "Salary": [50000, 60000, 75000, 55000]
})

print("Original DataFrame:")
print(df)


# --------------------------------------------------
# 2. Apply a function to a column
# --------------------------------------------------

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


df["Grade"] = df["Score"].apply(calculate_grade)

print("\nAfter applying grade function:")
print(df)


# --------------------------------------------------
# 3. Apply lambda function
# --------------------------------------------------

df["Bonus"] = df["Salary"].apply(
    lambda salary: salary * 0.10
)

print("\nAfter calculating 10% bonus:")
print(df)


# --------------------------------------------------
# 4. Apply function to create a new column
# --------------------------------------------------

df["Updated_Salary"] = df["Salary"].apply(
    lambda salary: salary * 1.05
)

print("\nAfter 5% salary increase:")
print(df)


# --------------------------------------------------
# 5. Apply function to multiple columns
# --------------------------------------------------

def calculate_total(row):
    return row["Score"] + row["Bonus"]


df["Total"] = df.apply(
    calculate_total,
    axis=1
)

print("\nAfter calculating total:")
print(df)


# --------------------------------------------------
# 6. Apply with axis=0
# --------------------------------------------------

numeric_data = df[["Score", "Salary"]]

column_totals = numeric_data.apply(
    sum,
    axis=0
)

print("\nColumn totals:")
print(column_totals)


# --------------------------------------------------
# 7. Apply with axis=1
# --------------------------------------------------

row_totals = numeric_data.apply(
    sum,
    axis=1
)

print("\nRow totals:")
print(row_totals)


# --------------------------------------------------
# 8. Using map()
# --------------------------------------------------

grade_labels = {
    "A": "Excellent",
    "B": "Good",
    "C": "Average",
    "D": "Needs Improvement"
}

df["Performance"] = df["Grade"].map(
    grade_labels
)

print("\nAfter mapping grade labels:")
print(df)


# --------------------------------------------------
# 9. Practical Data Science Example
# --------------------------------------------------

sales = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones"],
    "Sales": [75000, 50000, 30000, 15000]
})


def sales_category(amount):
    if amount >= 50000:
        return "High"
    elif amount >= 25000:
        return "Medium"
    else:
        return "Low"


sales["Category"] = sales["Sales"].apply(
    sales_category
)

print("\nSales Category:")
print(sales)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a DataFrame containing employee salaries.
# 2. Use apply() to calculate a 10% bonus.
# 3. Create a category column based on salary.
# 4. Use lambda to increase salaries by 5%.
# 5. Use map() to replace category names.
# 6. Use apply(axis=1) to calculate values using multiple columns.
