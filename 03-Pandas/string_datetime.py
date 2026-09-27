# Pandas - String and DateTime Operations

import pandas as pd


# ==================================================
# PART 1 - STRING OPERATIONS
# ==================================================


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul Patil",
        "Priya Sharma",
        "Amit Joshi",
        "Neha Kulkarni"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik"
    ],
    "Email": [
        "rahul@gmail.com",
        "priya@gmail.com",
        "amit@gmail.com",
        "neha@gmail.com"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Convert Text to Uppercase
# -------------------------

df["Name_Upper"] = df["Name"].str.upper()

print("\nUppercase Names:")
print(df["Name_Upper"])


# -------------------------
# 3. Convert Text to Lowercase
# -------------------------

df["Name_Lower"] = df["Name"].str.lower()

print("\nLowercase Names:")
print(df["Name_Lower"])


# -------------------------
# 4. Convert Text to Title Case
# -------------------------

df["Name_Title"] = df["Name"].str.title()

print("\nTitle Case Names:")
print(df["Name_Title"])


# -------------------------
# 5. String Length
# -------------------------

df["Name_Length"] = df["Name"].str.len()

print("\nName Length:")
print(df[["Name", "Name_Length"]])


# -------------------------
# 6. Check String Contains
# -------------------------

print("\nNames containing 'Rahul':")

print(
    df[df["Name"].str.contains(
        "Rahul",
        case=False,
        na=False
    )]
)


# -------------------------
# 7. City Contains 'Pune'
# -------------------------

print("\nCustomers from Pune:")

print(
    df[df["City"].str.contains(
        "Pune",
        case=False,
        na=False
    )]
)


# -------------------------
# 8. String Starts With
# -------------------------

print("\nNames starting with 'P':")

print(
    df[df["Name"].str.startswith(
        "P"
    )]
)


# -------------------------
# 9. String Ends With
# -------------------------

print("\nEmails ending with gmail.com:")

print(
    df[df["Email"].str.endswith(
        "gmail.com"
    )]
)


# -------------------------
# 10. Replace Text
# -------------------------

df["City"] = df["City"].str.replace(
    "Mumbai",
    "Bombay",
    regex=False
)

print("\nAfter Replacing Mumbai:")
print(df)


# -------------------------
# 11. Split String
# -------------------------

df["First_Name"] = df["Name"].str.split().str[0]

df["Last_Name"] = df["Name"].str.split().str[1]

print("\nFirst and Last Names:")
print(
    df[
        ["Name", "First_Name", "Last_Name"]
    ]
)


# -------------------------
# 12. Remove Extra Spaces
# -------------------------

data = {
    "Name": [
        " Rahul ",
        " Priya",
        "Amit ",
        " Neha "
    ]
}

space_df = pd.DataFrame(data)

print("\nData with Extra Spaces:")
print(space_df)

space_df["Name"] = space_df[
    "Name"
].str.strip()

print("\nAfter Removing Spaces:")
print(space_df)


# ==================================================
# PART 2 - DATETIME OPERATIONS
# ==================================================


# -------------------------
# 13. Create Date Data
# -------------------------

date_data = {
    "Customer": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ],
    "Order_Date": [
        "2025-01-15",
        "2025-02-20",
        "2025-03-10",
        "2025-04-25"
    ]
}

date_df = pd.DataFrame(date_data)

print("\nOriginal Date Data:")
print(date_df)


# -------------------------
# 14. Convert to Datetime
# -------------------------

date_df["Order_Date"] = pd.to_datetime(
    date_df["Order_Date"]
)

print("\nConverted Date:")
print(date_df)


# -------------------------
# 15. Extract Year
# -------------------------

date_df["Year"] = date_df[
    "Order_Date"
].dt.year

print("\nYear:")
print(date_df)


# -------------------------
# 16. Extract Month
# -------------------------

date_df["Month"] = date_df[
    "Order_Date"
].dt.month

print("\nMonth:")
print(date_df)


# -------------------------
# 17. Extract Day
# -------------------------

date_df["Day"] = date_df[
    "Order_Date"
].dt.day

print("\nDay:")
print(date_df)


# -------------------------
# 18. Extract Day Name
# -------------------------

date_df["Day_Name"] = date_df[
    "Order_Date"
].dt.day_name()

print("\nDay Name:")
print(date_df)


# -------------------------
# 19. Extract Month Name
# -------------------------

date_df["Month_Name"] = date_df[
    "Order_Date"
].dt.month_name()

print("\nMonth Name:")
print(date_df)


# -------------------------
# 20. Extract Quarter
# -------------------------

date_df["Quarter"] = date_df[
    "Order_Date"
].dt.quarter

print("\nQuarter:")
print(date_df)


# -------------------------
# 21. Filter by Year
# -------------------------

print("\nOrders from 2025:")

print(
    date_df[
        date_df["Year"] == 2025
    ]
)


# -------------------------
# 22. Sort by Date
# -------------------------

print("\nSorted by Date:")

print(
    date_df.sort_values(
        "Order_Date"
    )
)


# -------------------------
# 23. Date Difference
# -------------------------

today = pd.Timestamp("2025-05-01")

date_df["Days_From_Order"] = (
    today - date_df["Order_Date"]
).dt.days

print("\nDays From Order:")
print(date_df)


# -------------------------
# 24. Date Range
# -------------------------

dates = pd.date_range(
    start="2025-01-01",
    end="2025-01-10"
)

print("\nDate Range:")
print(dates)


# -------------------------
# 25. Monthly Date Range
# -------------------------

monthly_dates = pd.date_range(
    start="2025-01-01",
    periods=6,
    freq="ME"
)

print("\nMonthly Dates:")
print(monthly_dates)


# ==================================================
# PART 3 - PRACTICAL DATA SCIENCE EXAMPLE
# ==================================================


sales_data = {
    "Customer": [
        "Rahul Patil",
        "Priya Sharma",
        "Amit Joshi",
        "Neha Kulkarni"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik"
    ],
    "Order_Date": [
        "2025-01-10",
        "2025-01-15",
        "2025-02-10",
        "2025-02-20"
    ],
    "Sales": [
        50000,
        30000,
        45000,
        25000
    ]
}

sales_df = pd.DataFrame(sales_data)


# Convert date

sales_df["Order_Date"] = pd.to_datetime(
    sales_df["Order_Date"]
)


# Extract Month

sales_df["Month"] = sales_df[
    "Order_Date"
].dt.month_name()


# Extract Year

sales_df["Year"] = sales_df[
    "Order_Date"
].dt.year


print("\nSales Data:")
print(sales_df)


# -------------------------
# Monthly Sales
# -------------------------

print("\nMonthly Sales:")

monthly_sales = sales_df.groupby(
    "Month"
)["Sales"].sum()

print(monthly_sales)


# -------------------------
# Sales by City
# -------------------------

print("\nSales by City:")

city_sales = sales_df.groupby(
    "City"
)["Sales"].sum()

print(city_sales)
