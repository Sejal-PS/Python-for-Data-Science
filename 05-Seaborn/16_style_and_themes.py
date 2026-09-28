"""
Seaborn Styles and Themes

Seaborn provides built-in themes and styling
options to improve the appearance of plots.
"""

import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

tips = sns.load_dataset("tips")


# --------------------------------------------------
# Available Styles
# --------------------------------------------------

# Common styles:
# white
# dark
# whitegrid
# darkgrid
# ticks


sns.set_style("whitegrid")


# --------------------------------------------------
# Basic Styled Plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    style="sex",
    s=100
)

plt.title(
    "Total Bill vs Tip",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Total Bill",
    fontsize=12
)

plt.ylabel(
    "Tip",
    fontsize=12
)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Set Theme
# --------------------------------------------------

sns.set_theme(
    style="darkgrid",
    palette="deep"
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)

plt.title("Average Total Bill by Day")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Change Color Palette
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=tips,
    x="day",
    hue="day",
    palette="Set2",
    legend=False
)

plt.title("Number of Records by Day")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Common Color Palettes
# --------------------------------------------------

# deep
# muted
# pastel
# bright
# dark
# colorblind
# Set1
# Set2
# Set3


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Try different Seaborn styles.
# 2. Try different color palettes.
# 3. Change the figure size.
# 4. Customize title and axis labels.
# 5. Create a plot using the colorblind palette.
