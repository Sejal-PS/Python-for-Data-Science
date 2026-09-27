# Seaborn - Violin Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Violin Plot
# ------------------------------------------

sns.violinplot(
    data=df,
    y="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 2. Violin Plot by Day
# ------------------------------------------

sns.violinplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Bill Distribution by Day")

plt.show()


# ------------------------------------------
# 3. Violin Plot with Hue
# ------------------------------------------

sns.violinplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Bill Distribution by Day and Gender")

plt.show()


# ------------------------------------------
# 4. Split Style
# ------------------------------------------

sns.violinplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex",
    split=True
)

plt.title("Bill Distribution")

plt.show()
