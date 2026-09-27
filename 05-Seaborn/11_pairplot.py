# Seaborn - Pair Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("iris")

print(df.head())


# ------------------------------------------
# 1. Basic Pair Plot
# ------------------------------------------

sns.pairplot(
    df
)

plt.show()


# ------------------------------------------
# 2. Pair Plot with Hue
# ------------------------------------------

sns.pairplot(
    df,
    hue="species"
)

plt.show()


# ------------------------------------------
# 3. Pair Plot with Selected Variables
# ------------------------------------------

sns.pairplot(
    df,
    vars=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ],
    hue="species"
)

plt.show()


# ------------------------------------------
# Why Pair Plot?
# ------------------------------------------

# Pair plot helps us understand:
#
# 1. Relationship between variables
# 2. Distribution of variables
# 3. Possible patterns
# 4. Separation between categories
