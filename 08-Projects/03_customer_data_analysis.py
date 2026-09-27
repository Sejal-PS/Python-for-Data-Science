import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Customer_ID": [1, 2, 3, 4, 5, 6],
    "Age": [22, 35, 28, 42, 30, 25],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Delhi",
        "Mumbai",
        "Pune"
    ],
    "Spending": [
        5000,
        8000,
        4500,
        10000,
        7000,
        6000
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Age:")
print(df["Age"].mean())

print("\nAverage Spending:")
print(df["Spending"].mean())

print("\nCustomers by City:")
print(
    df["City"].value_counts()
)

print("\nHighest Spending:")
print(
    df.loc[
        df["Spending"].idxmax()
    ]
)


sns.scatterplot(
    data=df,
    x="Age",
    y="Spending",
    hue="City"
)

plt.title("Age vs Spending")
plt.show()
