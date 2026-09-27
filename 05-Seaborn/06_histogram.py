# Seaborn - Histogram

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Histogram
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 2. Change Number of Bins
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill",
    bins=10
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 3. Add KDE
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)

plt.title("Total Bill Distribution with KDE")

plt.show()


# ------------------------------------------
# 4. Histogram by Category
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill",
    hue="sex"
)

plt.title("Bill Distribution by Gender")

plt.show()


# ------------------------------------------
# 5. Change Color
# ------------------------------------------

sns.histplot(
    data=df,
    x="tip",
    color="green",
    bins=10
)

plt.title("Tip Distribution")

plt.show()
