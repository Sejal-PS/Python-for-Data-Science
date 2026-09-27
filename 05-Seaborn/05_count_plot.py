# Seaborn - Count Plot

import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# ------------------------------------------
# 1. Basic Count Plot
# ------------------------------------------

sns.countplot(
    data=df,
    x="day"
)

plt.title("Number of Records by Day")

plt.show()


# ------------------------------------------
# 2. Count by Gender
# ------------------------------------------

sns.countplot(
    data=df,
    x="sex"
)

plt.title("Number of Records by Gender")

plt.show()


# ------------------------------------------
# 3. Count with Hue
# ------------------------------------------

sns.countplot(
    data=df,
    x="day",
    hue="sex"
)

plt.title("Records by Day and Gender")

plt.show()


# ------------------------------------------
# 4. Horizontal Count Plot
# ------------------------------------------

sns.countplot(
    data=df,
    y="day"
)

plt.title("Number of Records by Day")

plt.show()


# ------------------------------------------
# 5. Count by Time
# ------------------------------------------

sns.countplot(
    data=df,
    x="time"
)

plt.title("Lunch vs Dinner")

plt.show()
