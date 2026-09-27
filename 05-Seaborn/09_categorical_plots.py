# Seaborn - Categorical Plots

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Strip Plot
# ------------------------------------------

sns.stripplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Total Bill by Day")

plt.show()


# ------------------------------------------
# 2. Strip Plot with Hue
# ------------------------------------------

sns.stripplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Bill by Day and Gender")

plt.show()


# ------------------------------------------
# 3. Swarm Plot
# ------------------------------------------

sns.swarmplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Total Bill by Day")

plt.show()


# ------------------------------------------
# 4. Swarm Plot with Hue
# ------------------------------------------

sns.swarmplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Bill by Day and Gender")

plt.show()


# ------------------------------------------
# 5. Cat Plot
# ------------------------------------------

sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="box"
)

plt.show()


# ------------------------------------------
# 6. Cat Plot with Bar
# ------------------------------------------

sns.catplot(
    data=df,
    x="day",
    y="total_bill",
    kind="bar"
)

plt.show()
