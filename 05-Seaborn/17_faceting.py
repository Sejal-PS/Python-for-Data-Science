"""
Faceting in Seaborn

Faceting allows us to create multiple plots
for different subsets of a dataset.
"""

import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

tips = sns.load_dataset("tips")


# --------------------------------------------------
# 1. FacetGrid
# --------------------------------------------------

g = sns.FacetGrid(
    tips,
    col="time",
    row="sex",
    height=4
)

g.map_dataframe(
    sns.scatterplot,
    x="total_bill",
    y="tip"
)

g.set_axis_labels(
    "Total Bill",
    "Tip"
)

g.set_titles(
    "{row_name} - {col_name}"
)

plt.show()


# --------------------------------------------------
# 2. relplot with columns
# --------------------------------------------------

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    col="time",
    hue="sex",
    style="smoker",
    height=4
)

plt.show()


# --------------------------------------------------
# 3. Faceted Distribution
# --------------------------------------------------

g = sns.FacetGrid(
    tips,
    col="day",
    col_wrap=2,
    height=4
)

g.map_dataframe(
    sns.histplot,
    x="total_bill",
    kde=True
)

g.set_axis_labels(
    "Total Bill",
    "Count"
)

plt.show()


# --------------------------------------------------
# 4. Faceted Categorical Plot
# --------------------------------------------------

g = sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    col="time",
    kind="box",
    height=5
)

g.set_axis_labels(
    "Day",
    "Total Bill"
)

plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create a FacetGrid using the tips dataset.
# 2. Create separate plots for lunch and dinner.
# 3. Create a faceted histogram by day.
# 4. Create a faceted box plot.
# 5. Experiment with col_wrap.
