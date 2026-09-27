# Seaborn - Basic Plots

import seaborn as sns
import matplotlib.pyplot as plt


# Seaborn comes with some built-in datasets.
# We will use the tips dataset for practice.

df = sns.load_dataset("tips")

print(df.head())


# ------------------------------------------
# 1. Basic Scatter Plot
# ------------------------------------------

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()


# ------------------------------------------
# 2. Basic Line Plot
# ------------------------------------------

sns.lineplot(
    data=df,
    x="size",
    y="total_bill"
)

plt.title("Size vs Total Bill")

plt.show()


# ------------------------------------------
# 3. Basic Bar Plot
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Average Bill by Day")

plt.show()


# ------------------------------------------
# 4. Basic Count Plot
# ------------------------------------------

sns.countplot(
    data=df,
    x="day"
)

plt.title("Number of Records by Day")

plt.show()


# ------------------------------------------
# 5. Basic Histogram
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 6. Basic Box Plot
# ------------------------------------------

sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Bill Distribution by Day")

plt.show()
