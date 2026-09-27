# Seaborn - Box Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Box Plot
# ------------------------------------------

sns.boxplot(
    data=df,
    y="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 2. Box Plot by Category
# ------------------------------------------

sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Bill Distribution by Day")

plt.show()


# ------------------------------------------
# 3. Box Plot with Hue
# ------------------------------------------

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Bill Distribution by Day and Gender")

plt.show()


# ------------------------------------------
# 4. Horizontal Box Plot
# ------------------------------------------

sns.boxplot(
    data=df,
    x="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 5. Box Plot for Tips
# ------------------------------------------

sns.boxplot(
    data=df,
    x="day",
    y="tip",
    color="lightgreen"
)

plt.title("Tip Distribution by Day")

plt.show()
