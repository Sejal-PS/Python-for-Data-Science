# Seaborn with Pandas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ------------------------------------------
# Create DataFrame
# ------------------------------------------

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Sales": [
        10000,
        15000,
        13000,
        18000,
        22000,
        25000
    ],
    "Profit": [
        2000,
        3000,
        2500,
        4000,
        5500,
        6000
    ]
}

df = pd.DataFrame(data)

print(df)


# ------------------------------------------
# 1. Sales Visualization
# ------------------------------------------

sns.barplot(
    data=df,
    x="Month",
    y="Sales"
)

plt.title("Monthly Sales")

plt.show()


# ------------------------------------------
# 2. Profit Visualization
# ------------------------------------------

sns.lineplot(
    data=df,
    x="Month",
    y="Profit",
    marker="o"
)

plt.title("Monthly Profit")

plt.show()


# ------------------------------------------
# 3. Sales vs Profit
# ------------------------------------------

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    s=100
)

plt.title("Sales vs Profit")

plt.show()


# ------------------------------------------
# 4. Data Distribution
# ------------------------------------------

sns.histplot(
    data=df,
    x="Sales",
    kde=True
)

plt.title("Sales Distribution")

plt.show()


# ------------------------------------------
# 5. Box Plot
# ------------------------------------------

sns.boxplot(
    data=df,
    y="Sales"
)

plt.title("Sales Distribution")

plt.show()


# ------------------------------------------
# 6. Correlation Heatmap
# ------------------------------------------

numeric_df = df[
    ["Sales", "Profit"]
]

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Sales and Profit Correlation")

plt.show()


# ------------------------------------------
# Data Science Flow
# ------------------------------------------

# Pandas
#    ↓
# DataFrame
#    ↓
# Data Cleaning
#    ↓
# Seaborn
#    ↓
# Visualization
#    ↓
# EDA
