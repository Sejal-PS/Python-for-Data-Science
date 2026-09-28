"""
Feature Engineering - Practice

Try solving these tasks without looking at the solution immediately.

Tasks:
1. Handle missing values.
2. Create a total_amount feature.
3. Create an age_group feature.
4. Encode a categorical column.
5. Create a date-based feature.
6. Detect outliers using IQR.
7. Scale numerical features.
8. Create a meaningful business feature.
"""

import pandas as pd
import numpy as np

data = {
    "age": [22, 35, np.nan, 29, 52, 41],
    "city": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai", "Pune"],
    "quantity": [2, 5, 3, 10, 1, 4],
    "price": [100, 250, 150, 50, 1000, 300],
    "order_date": [
        "2025-01-05",
        "2025-02-10",
        "2025-03-15",
        "2025-04-20",
        "2025-05-25",
        "2025-06-30"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Task 1: Handle missing age
df["age"] = df["age"].fillna(df["age"].median())

# Task 2: Create total amount
df["total_amount"] = df["quantity"] * df["price"]

# Task 3: Create age group
df["age_group"] = df["age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)

# Task 4: Encode city
df = pd.get_dummies(
    df,
    columns=["city"],
    dtype=int
)

# Task 5: Date feature
df["order_date"] = pd.to_datetime(df["order_date"])
df["order_month"] = df["order_date"].dt.month

print("\nEngineered Dataset:")
print(df)

print("\nPractice completed.")
print("Try creating additional features on your own.")
