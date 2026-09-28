"""
12 - Numerical Analysis

Learn how to profile numerical variables using:

Mean

Median

Standard deviation

Percentiles

Quartiles

IQR
"""

import pandas as pd

data = {
"Age": [21, 22, 24, 25, 27, 29, 31, 35, 40],
"Salary": [25000, 28000, 32000, 35000, 40000,
45000, 52000, 65000, 90000]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Descriptive Statistics
---------------------------------------------------------

print("Descriptive Statistics:")
print(df.describe())

---------------------------------------------------------
Individual Statistics
---------------------------------------------------------

salary = df["Salary"]

print("\nMean:", salary.mean())
print("Median:", salary.median())
print("Minimum:", salary.min())
print("Maximum:", salary.max())
print("Range:", salary.max() - salary.min())
print("Variance:", salary.var())
print("Standard Deviation:", salary.std())

---------------------------------------------------------
Percentiles
---------------------------------------------------------

print("\n25th Percentile:", salary.quantile(0.25))
print("50th Percentile:", salary.quantile(0.50))
print("75th Percentile:", salary.quantile(0.75))
print("90th Percentile:", salary.quantile(0.90))

---------------------------------------------------------
IQR
---------------------------------------------------------

Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)

IQR = Q3 - Q1

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

---------------------------------------------------------
Interpretation
---------------------------------------------------------

print("\nInterpretation:")
print("Use numerical statistics to understand the center and spread of data.")
