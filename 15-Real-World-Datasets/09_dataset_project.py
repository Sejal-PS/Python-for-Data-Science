import pandas as pd

data = {
    "Product": ["A", "B", "A", "C", "B", "C"],
    "Region": ["North", "South", "North", "West", "South", "West"],
    "Sales": [100, 150, 120, 200, 170, 180]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nBasic information:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nSales by product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop product:")
print(
    df.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)

# Next steps for learners:
# 1. Add visualizations.
# 2. Check data quality.
# 3. Find additional insights.
# 4. Write a short analysis report.
