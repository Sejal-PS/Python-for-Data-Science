import pandas as pd

data = {
    "Area": [800, 1000, 1200, 1500, 1800],
    "Bedrooms": [2, 2, 3, 3, 4],
    "Price": [40, 50, 65, 80, 100]
}

df = pd.DataFrame(data)

df["Price_per_sqft"] = df["Price"] / df["Area"]

print(df)

print("\nAverage price:")
print(df["Price"].mean())

print("\nAverage price by bedrooms:")
print(df.groupby("Bedrooms")["Price"].mean())
