"""
Seaborn Distribution Plots

Distribution plots help us understand how numerical
values are distributed in a dataset.
"""

import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load sample dataset
# --------------------------------------------------

tips = sns.load_dataset("tips")

print("Tips Dataset:")
print(tips.head())


# --------------------------------------------------
# 1. KDE Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=tips,
    x="total_bill",
    fill=True,
    color="blue"
)

plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Density")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 2. Distribution by Category
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=tips,
    x="total_bill",
    hue="sex",
    fill=True,
    common_norm=False
)

plt.title("Total Bill Distribution by Gender")
plt.xlabel("Total Bill")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 3. ECDF Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.ecdfplot(
    data=tips,
    x="total_bill"
)

plt.title("ECDF of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Proportion")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Distribution using displot
# --------------------------------------------------

sns.displot(
    data=tips,
    x="total_bill",
    kde=True,
    height=5,
    aspect=1.5
)

plt.title("Total Bill Distribution")
plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a KDE plot for tip.
# 2. Compare total_bill distribution for different days.
# 3. Create an ECDF plot for tip.
# 4. Add KDE to a histogram using displot().
