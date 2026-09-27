import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Product": [
        "Laptop",
        "Phone",
        "Laptop",
        "Tablet",
        "Phone",
        "Tablet"
    ],
    "Region": [
        "Pune",
        "Mumbai",
        "Pune",
        "Delhi",
        "Mumbai",
        "Delhi"
    ],
    "Sales": [
        50000,
        30000,
        45000,
        20000,
        35000,
        25000
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nSales by Product:")
print(
    df.groupby("Product")["Sales"].sum()
)

print("\nSales by Region:")
print(
    df.groupby("Region")["Sales"].sum()
)


sns.barplot(
    data=df,
    x="Product",
    y="Sales"
)

plt.title("Product Sales")
plt.show()
