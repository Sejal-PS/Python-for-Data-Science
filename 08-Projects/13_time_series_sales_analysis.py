"""
Project: Time Series Sales Analysis

Skills:
- DateTime
- Time Series
- Resampling
- Rolling Average
- Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Create Sales Data
# --------------------------------------------------

dates = pd.date_range(
    start="2025-01-01",
    periods=12,
    freq="MS"
)

sales = [
    20000, 23000, 21000,
    26000, 28000, 30000,
    29000, 32000, 35000,
    33000, 38000, 42000
]

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})


# --------------------------------------------------
# 2. Set Date as Index
# --------------------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"]
)

df = df.set_index("Date")

print("Sales Data:")
print(df)


# --------------------------------------------------
# 3. Monthly Growth
# --------------------------------------------------

df["Growth"] = df["Sales"].pct_change() * 100

print("\nMonthly Growth:")
print(df)


# --------------------------------------------------
# 4. Rolling Average
# --------------------------------------------------

df["Rolling_Average"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
)

print("\nRolling Average:")
print(df)


# --------------------------------------------------
# 5. Plot Sales
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    df.index,
    df["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    df.index,
    df["Rolling_Average"],
    linestyle="--",
    label="3-Month Average"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. Find Highest Sales Month
# --------------------------------------------------

highest_sales_date = df["Sales"].idxmax()

highest_sales = df["Sales"].max()

print("\nHighest Sales:")
print(highest_sales)

print("\nHighest Sales Month:")
print(highest_sales_date)


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Add more months.
# 2. Calculate 6-month rolling average.
# 3. Calculate monthly percentage growth.
# 4. Identify the month with the lowest sales.
# 5. Create a bar chart of monthly sales.
