"""
Date and Time Feature Engineering

Learn:
- Year
- Month
- Day
- Day of week
- Quarter
- Weekend indicator
"""

import pandas as pd

data = {
    "order_date": [
        "2025-01-05",
        "2025-02-12",
        "2025-03-22",
        "2025-04-19",
        "2025-05-26"
    ]
}

df = pd.DataFrame(data)

df["order_date"] = pd.to_datetime(df["order_date"])

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["day_of_week"] = df["order_date"].dt.dayofweek
df["quarter"] = df["order_date"].dt.quarter

df["is_weekend"] = df["day_of_week"] >= 5

print(df)

print("\nDate features can reveal seasonal and time-based patterns.")
