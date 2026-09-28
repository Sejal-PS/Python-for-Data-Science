import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 135, 180, 210, 195],
    "Profit": [20, 30, 25, 40, 55, 48]
}

df = pd.DataFrame(data)

print(df)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df, x="Month", y="Sales", ax=axes[0])
axes[0].set_title("Monthly Sales")

sns.lineplot(
    data=df,
    x="Month",
    y="Profit",
    marker="o",
    ax=axes[1]
)
axes[1].set_title("Monthly Profit")

plt.tight_layout()
plt.show()

print("Highest sales:", df.loc[df["Sales"].idxmax(), "Month"])
print("Highest profit:", df.loc[df["Profit"].idxmax(), "Month"])
