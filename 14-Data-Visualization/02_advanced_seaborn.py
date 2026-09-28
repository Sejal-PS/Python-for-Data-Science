import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Bill Distribution by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.tight_layout()
plt.show()
