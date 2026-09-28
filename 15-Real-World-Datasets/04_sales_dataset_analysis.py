import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
    "Region": ["West", "West", "North", "North", "South"],
    "Sales": [80000, 50000, 90000, 30000, 55000]
}

df = pd.DataFrame(data)

print("Total Sales:", df["Sales"].sum())

print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop Product:")
print(
    df.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)
