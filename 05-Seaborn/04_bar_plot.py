# Seaborn - Bar Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Bar Plot
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Average Bill by Day")

plt.show()


# ------------------------------------------
# 2. Add Hue
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Average Bill by Day and Gender")

plt.show()


# ------------------------------------------
# 3. Change Color
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    color="skyblue"
)

plt.title("Average Bill")

plt.show()


# ------------------------------------------
# 4. Different Estimator
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    estimator="sum"
)

plt.title("Total Bill by Day")

plt.show()


# ------------------------------------------
# 5. Horizontal Bar Plot
# ------------------------------------------

sns.barplot(
    data=df,
    x="total_bill",
    y="day"
)

plt.title("Average Bill by Day")

plt.show()
