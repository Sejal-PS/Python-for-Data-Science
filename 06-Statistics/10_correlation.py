# Correlation

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ------------------------------------------
# Create Data
# ------------------------------------------

data = {
    "Study_Hours": [
        1, 2, 3, 4, 5, 6, 7
    ],
    "Marks": [
        40, 45, 52, 60, 68, 75, 85
    ]
}

df = pd.DataFrame(data)

print(df)


# ------------------------------------------
# Correlation
# ------------------------------------------

correlation = df[
    "Study_Hours"
].corr(
    df["Marks"]
)

print(
    "Correlation:",
    correlation
)


# ------------------------------------------
# Scatter Plot
# ------------------------------------------

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks"
)

plt.title(
    "Study Hours vs Marks"
)

plt.show()


# ------------------------------------------
# Interpretation
# ------------------------------------------

# Correlation measures the strength
# and direction of a linear relationship.
#
# Values range from -1 to +1.
#
# +1 -> Strong positive linear relationship
#  0 -> No linear relationship
# -1 -> Strong negative linear relationship
#
# Important:
# Correlation does not prove causation.
