# Seaborn - Line Plot

import seaborn as sns
import matplotlib.pyplot as plt


# ------------------------------------------
# Create Data
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
        12000,
        15000,
        13000,
        18000,
        22000
    ]
}


# ------------------------------------------
# Convert to DataFrame
# ------------------------------------------

import pandas as pd

df = pd.DataFrame(data)


# ------------------------------------------
# 1. Basic Line Plot
# ------------------------------------------

sns.lineplot(
    data=df,
    x="Month",
    y="Sales"
)

plt.title("Monthly Sales")

plt.show()


# ------------------------------------------
# 2. Add Marker
# ------------------------------------------

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title("Monthly Sales")

plt.show()


# ------------------------------------------
# 3. Change Color
# ------------------------------------------

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o",
    color="green"
)

plt.title("Monthly Sales")

plt.show()


# ------------------------------------------
# 4. Multiple Lines
# ------------------------------------------

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],
    "Sales_2024": [
        10000,
        12000,
        15000,
        16000,
        18000
    ],
    "Sales_2025": [
        12000,
        15000,
        17000,
        20000,
        23000
    ]
}

df = pd.DataFrame(data)

sns.lineplot(
    data=df,
    x="Month",
    y="Sales_2024",
    marker="o",
    label="2024"
)

sns.lineplot(
    data=df,
    x="Month",
    y="Sales_2025",
    marker="o",
    label="2025"
)

plt.title("Sales Comparison")

plt.legend()

plt.show()
