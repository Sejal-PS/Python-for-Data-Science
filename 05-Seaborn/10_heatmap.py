# Seaborn - Heatmap

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# ------------------------------------------
# Create Data
# ------------------------------------------

data = {
    "Math": [80, 90, 70, 85, 95],
    "Science": [75, 85, 80, 90, 88],
    "English": [70, 80, 75, 85, 90],
    "History": [65, 78, 72, 88, 85]
}

df = pd.DataFrame(data)


# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

correlation = df.corr()

print(correlation)


# ------------------------------------------
# Basic Heatmap
# ------------------------------------------

sns.heatmap(
    correlation
)

plt.title("Correlation Heatmap")

plt.show()


# ------------------------------------------
# Heatmap with Values
# ------------------------------------------

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()


# ------------------------------------------
# Heatmap Customization
# ------------------------------------------

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.show()


# ------------------------------------------
# Understanding Correlation
# ------------------------------------------

# Correlation values generally range from -1 to +1.
#
# +1  -> Strong positive relationship
#  0  -> No linear relationship
# -1  -> Strong negative relationship
#
# Note:
# Correlation does not automatically mean causation.
