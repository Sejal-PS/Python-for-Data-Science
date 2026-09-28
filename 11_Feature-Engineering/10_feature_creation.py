"""
Feature Creation

Learn how to create meaningful features from existing columns.
"""

import pandas as pd

data = {
    "quantity": [2, 5, 10, 3, 8],
    "unit_price": [100, 200, 50, 500, 150],
    "cost": [70, 150, 35, 400, 100]
}

df = pd.DataFrame(data)

# Total sales
df["total_amount"] = df["quantity"] * df["unit_price"]

# Total cost
df["total_cost"] = df["quantity"] * df["cost"]

# Profit
df["profit"] = df["total_amount"] - df["total_cost"]

# Profit margin
df["profit_margin"] = (
    df["profit"] / df["total_amount"]
) * 100

# Average selling price
df["price_per_unit"] = df["total_amount"] / df["quantity"]

print(df)

print("\nThese engineered features provide additional business information.")
