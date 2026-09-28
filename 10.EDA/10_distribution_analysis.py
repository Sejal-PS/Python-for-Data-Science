"""
10 - Distribution Analysis

Learn how to understand:

Center

Spread

Shape

Skewness

Distribution patterns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

salary = np.random.normal(
loc=50000,
scale=10000,
size=500
)

df = pd.DataFrame({"Salary": salary})

---------------------------------------------------------
Descriptive Statistics
---------------------------------------------------------

print("Distribution Statistics:")
print(df["Salary"].describe())

---------------------------------------------------------
Mean and Median
---------------------------------------------------------

print("\nMean:", df["Salary"].mean())
print("Median:", df["Salary"].median())

---------------------------------------------------------
Skewness
---------------------------------------------------------

print("\nSkewness:", df["Salary"].skew())

---------------------------------------------------------
Histogram
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
df["Salary"],
kde=True,
bins=30
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

---------------------------------------------------------
Box Plot
---------------------------------------------------------

plt.figure(figsize=(8, 4))

sns.boxplot(x=df["Salary"])

plt.title("Salary Distribution - Box Plot")

plt.show()

---------------------------------------------------------
Interpretation
---------------------------------------------------------

print("\nInterpretation:")
print("Check the center, spread, shape and possible outliers.")
print("A distribution should be interpreted in context.")
