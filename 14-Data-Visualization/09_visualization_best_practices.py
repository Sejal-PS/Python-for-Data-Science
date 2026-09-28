import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(9, 5))

sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    errorbar=None,
    color="steelblue"
)

plt.title("Average Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill")

plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.show()

# Good practice:
# 1. Use meaningful titles
# 2. Label axes
# 3. Choose an appropriate chart
# 4. Avoid unnecessary decoration
# 5. Keep the visualization readable
