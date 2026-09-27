# Pandas - GroupBy and Aggregation

import pandas as pd


# -------------------------
# 1. Create Sales Dataset
# -------------------------

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Tablet",
        "Mobile",
        "Monitor",
        "Tablet",
        "Laptop"
    ],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai"
    ],
    "Sales": [
        55000,
        25000,
        65000,
        18000,
        30000,
        22000,
        20000,
        60000
    ],
    "Quantity": [
        2,
        5,
        3,
        3,
        6,
        4,
        5,
        2
    ]
}

df = pd.DataFrame(data)

print("Sales Dataset:")
print(df)


# -------------------------
# 2. GroupBy - One Column
# -------------------------

print("\nSales by City:")

city_sales = df.groupby("City")["Sales"].sum()

print(city_sales)


# -------------------------
# 3. Average Sales by City
# -------------------------

print("\nAverage Sales by City:")

average_sales = df.groupby("City")["Sales"].mean()

print(average_sales)


# -------------------------
# 4. Maximum Sales by City
# -------------------------

print("\nMaximum Sales by City:")

max_sales = df.groupby("City")["Sales"].max()

print(max_sales)


# -------------------------
# 5. Minimum Sales by City
# -------------------------

print("\nMinimum Sales by City:")

min_sales = df.groupby("City")["Sales"].min()

print(min_sales)


# -------------------------
# 6. Total Quantity by City
# -------------------------

print("\nTotal Quantity by City:")

quantity_by_city = df.groupby("City")["Quantity"].sum()

print(quantity_by_city)


# -------------------------
# 7. GroupBy Product
# -------------------------

print("\nSales by Product:")

product_sales = df.groupby(
    "Product"
)["Sales"].sum()

print(product_sales)


# -------------------------
# 8. Multiple Aggregations
# -------------------------

print("\nMultiple Statistics:")

result = df.groupby("City")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)

print(result)


# -------------------------
# 9. Aggregation on Multiple Columns
# -------------------------

print("\nMultiple Column Aggregation:")

result = df.groupby("City").agg(
    {
        "Sales": ["sum", "mean"],
        "Quantity": ["sum", "mean"]
    }
)

print(result)


# -------------------------
# 10. GroupBy Multiple Columns
# -------------------------

print("\nCity and Product Wise Sales:")

result = df.groupby(
    ["City", "Product"]
)["Sales"].sum()

print(result)


# -------------------------
# 11. GroupBy with as_index=False
# -------------------------

print("\nGroupBy with Normal Columns:")

result = df.groupby(
    "City",
    as_index=False
)["Sales"].sum()

print(result)


# -------------------------
# 12. Sort Grouped Result
# -------------------------

print("\nCities Sorted by Sales:")

result = (
    df.groupby(
        "City",
        as_index=False
    )["Sales"]
    .sum()
    .sort_values(
        "Sales",
        ascending=False
    )
)

print(result)


# -------------------------
# 13. Product Performance
# -------------------------

print("\nProduct Performance:")

product_performance = (
    df.groupby(
        "Product",
        as_index=False
    )
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean"),
        Total_Quantity=("Quantity", "sum")
    )
)

print(product_performance)


# -------------------------
# 14. Highest Selling Product
# -------------------------

print("\nHighest Selling Product:")

highest_product = product_performance.sort_values(
    "Total_Sales",
    ascending=False
).head(1)

print(highest_product)


# -------------------------
# 15. City Performance
# -------------------------

print("\nCity Performance:")

city_performance = (
    df.groupby(
        "City",
        as_index=False
    )
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean"),
        Total_Quantity=("Quantity", "sum")
    )
)

print(city_performance)


# -------------------------
# 16. Count Records by City
# -------------------------

print("\nNumber of Records by City:")

print(
    df["City"].value_counts()
)


# -------------------------
# 17. Data Science Example
# -------------------------

student_data = {
    "Student": [
        "A", "B", "C", "D",
        "E", "F", "G", "H"
    ],
    "Subject": [
        "Python", "Python",
        "SQL", "SQL",
        "Python", "SQL",
        "Python", "SQL"
    ],
    "Marks": [
        80, 90, 75, 85,
        88, 92, 70, 78
    ]
}

student_df = pd.DataFrame(student_data)

print("\nStudent Data:")
print(student_df)


# Average marks by subject

print("\nAverage Marks by Subject:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].mean()
)


# Highest marks by subject

print("\nHighest Marks by Subject:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].max()
)


# Multiple statistics

print("\nSubject-wise Statistics:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].agg(
        ["count", "mean", "min", "max"]
    )
)
