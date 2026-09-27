# Pandas - Data Transformation

import pandas as pd


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha",
        "Sneha"
    ],
    "Age": [22, 24, 23, 21, 25],
    "Marks": [80, 90, 65, 88, 72],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Add New Column
# -------------------------

df["Passed"] = df["Marks"] >= 40

print("\nAfter Adding Passed Column:")
print(df)


# -------------------------
# 3. Add Column Using Calculation
# -------------------------

df["Bonus_Marks"] = df["Marks"] + 5

print("\nAfter Adding Bonus Marks:")
print(df)


# -------------------------
# 4. Create Percentage
# -------------------------

df["Percentage"] = (
    df["Marks"] / 100 * 100
)

print("\nPercentage:")
print(df)


# -------------------------
# 5. Create Grade
# -------------------------

def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Fail"


df["Grade"] = df["Marks"].apply(get_grade)

print("\nGrade:")
print(df)


# -------------------------
# 6. apply() with Lambda
# -------------------------

df["Marks_Double"] = df["Marks"].apply(
    lambda x: x * 2
)

print("\nMarks Doubled:")
print(df)


# -------------------------
# 7. map()
# -------------------------

city_mapping = {
    "Pune": "Maharashtra",
    "Mumbai": "Maharashtra",
    "Nashik": "Maharashtra"
}

df["State"] = df["City"].map(
    city_mapping
)

print("\nState Column:")
print(df)


# -------------------------
# 8. replace()
# -------------------------

df["City"] = df["City"].replace(
    "Mumbai",
    "Bombay"
)

print("\nAfter Replacing Mumbai:")
print(df)


# -------------------------
# 9. Rename Column
# -------------------------

df.rename(
    columns={
        "Marks": "Score"
    },
    inplace=True
)

print("\nAfter Renaming Marks:")
print(df)


# -------------------------
# 10. Update Values
# -------------------------

df["Score"] = df["Score"] + 2

print("\nAfter Increasing Score:")
print(df)


# -------------------------
# 11. Create Category
# -------------------------

df["Performance"] = df["Score"].apply(
    lambda x: (
        "Excellent" if x >= 90
        else "Good" if x >= 75
        else "Average" if x >= 60
        else "Needs Improvement"
    )
)

print("\nPerformance Category:")
print(df)


# -------------------------
# 12. Conditional Transformation
# -------------------------

df["Result"] = "Fail"

df.loc[
    df["Score"] >= 40,
    "Result"
] = "Pass"

print("\nResult:")
print(df)


# -------------------------
# 13. Create Salary Data
# -------------------------

employee_data = {
    "Employee": [
        "A", "B", "C", "D"
    ],
    "Salary": [
        30000,
        40000,
        50000,
        60000
    ]
}

employee_df = pd.DataFrame(employee_data)

print("\nEmployee Data:")
print(employee_df)


# -------------------------
# 14. Calculate Annual Salary
# -------------------------

employee_df["Annual_Salary"] = (
    employee_df["Salary"] * 12
)

print("\nAnnual Salary:")
print(employee_df)


# -------------------------
# 15. Salary Category
# -------------------------

employee_df["Salary_Category"] = employee_df[
    "Salary"
].apply(
    lambda x: (
        "High" if x >= 50000
        else "Medium" if x >= 40000
        else "Low"
    )
)

print("\nSalary Category:")
print(employee_df)


# -------------------------
# 16. Data Science Example
# -------------------------

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Price": [
        55000,
        25000,
        18000,
        22000
    ],
    "Quantity": [
        2,
        5,
        3,
        4
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Total Sales

sales_df["Total_Sales"] = (
    sales_df["Price"] *
    sales_df["Quantity"]
)

print("\nTotal Sales:")
print(sales_df)


# Discount

sales_df["Discount"] = (
    sales_df["Total_Sales"] * 0.10
)

print("\nDiscount:")
print(sales_df)


# Final Amount

sales_df["Final_Amount"] = (
    sales_df["Total_Sales"] -
    sales_df["Discount"]
)

print("\nFinal Amount:")
print(sales_df)
