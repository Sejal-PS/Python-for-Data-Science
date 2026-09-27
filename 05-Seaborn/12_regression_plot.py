# Seaborn - Regression Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Regression Plot
# ------------------------------------------

sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()


# ------------------------------------------
# 2. Scatter Plot with Regression Line
# ------------------------------------------

sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter_kws={
        "color": "blue"
    },
    line_kws={
        "color": "red"
    }
)

plt.title("Bill vs Tip with Regression Line")

plt.show()


# ------------------------------------------
# 3. lmplot
# ------------------------------------------

sns.lmplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.show()


# ------------------------------------------
# 4. Regression by Category
# ------------------------------------------

sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.show()


# ------------------------------------------
# Important
# ------------------------------------------

# Regression plots help visualize
# the relationship and trend between
# two numerical variables.
