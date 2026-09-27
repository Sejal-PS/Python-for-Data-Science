# Pandas - Handling Duplicate Data

import pandas as pd


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Rahul",
        "Neha",
        "Priya"
    ],
    "Age": [
        22,
        24,
        23,
        22,
        21,
        24
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Pune",
        "Nashik",
        "Mumbai"
    ],
    "Marks": [
        80,
        90,
        75,
        80,
        88,
        90
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Check Duplicate Rows
# -------------------------

print("\nDuplicate Rows:")
print(df.duplicated())


# -------------------------
# 3. Count Duplicate Rows
# -------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# -------------------------
# 4. Display Only Duplicate Rows
# -------------------------

print("\nDuplicate Records:")

duplicates = df[
    df.duplicated()
]

print(duplicates)


# -------------------------
# 5. Keep First Occurrence
# -------------------------

print("\nKeep First Occurrence:")

print(
    df.duplicated(
        keep="first"
    )
)


# -------------------------
# 6. Keep Last Occurrence
# -------------------------

print("\nKeep Last Occurrence:")

print(
    df.duplicated(
        keep="last"
    )
)


# -------------------------
# 7. Remove Duplicate Rows
# -------------------------

clean_df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(clean_df)


# -------------------------
# 8. Remove Duplicates Permanently
# -------------------------

df = df.drop_duplicates()

print("\nClean Dataset:")
print(df)


# -------------------------
# 9. Duplicate Based on One Column
# -------------------------

data = {
    "Customer_ID": [
        101,
        102,
        103,
        101,
        104,
        102
    ],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Rahul",
        "Neha",
        "Priya"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Pune",
        "Nashik",
        "Mumbai"
    ]
}

customer_df = pd.DataFrame(data)

print("\nCustomer Data:")
print(customer_df)


# -------------------------
# 10. Check Duplicate Customer IDs
# -------------------------

print("\nDuplicate Customer IDs:")

print(
    customer_df[
        customer_df.duplicated(
            subset="Customer_ID"
        )
    ]
)


# -------------------------
# 11. Remove Duplicate Customer IDs
# -------------------------

unique_customers = customer_df.drop_duplicates(
    subset="Customer_ID"
)

print("\nUnique Customers:")
print(unique_customers)


# -------------------------
# 12. Keep Last Record
# -------------------------

unique_customers_last = customer_df.drop_duplicates(
    subset="Customer_ID",
    keep="last"
)

print("\nUnique Customers - Keep Last:")
print(unique_customers_last)


# -------------------------
# 13. Duplicate Check Before and After
# -------------------------

print("\nDuplicate Count Before Cleaning:")

print(
    customer_df.duplicated(
        subset="Customer_ID"
    ).sum()
)

clean_customer_df = customer_df.drop_duplicates(
    subset="Customer_ID"
)

print("\nDuplicate Count After Cleaning:")

print(
    clean_customer_df.duplicated(
        subset="Customer_ID"
    ).sum()
)


# -------------------------
# 14. Data Science Example
# -------------------------

sales_data = {
    "Order_ID": [
        1001,
        1002,
        1003,
        1001,
        1004,
        1002
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Monitor",
        "Mobile"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        55000,
        22000,
        25000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)

print("\nDuplicate Orders:")

print(
    sales_df[
        sales_df.duplicated(
            subset="Order_ID"
        )
    ]
)

clean_sales = sales_df.drop_duplicates(
    subset="Order_ID"
)

print("\nClean Sales Data:")
print(clean_sales)
