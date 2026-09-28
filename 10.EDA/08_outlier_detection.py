"""
08 - Outlier Detection

Learn how to identify unusual observations using:

IQR

Z-score

Box plots
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

salary = pd.Series(
[30000, 32000, 35000, 37000, 40000,
42000, 45000, 48000, 50000, 150000]
)

---------------------------------------------------------
IQR Method
---------------------------------------------------------

Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers_iqr = salary[
(salary < lower_limit) |
(salary > upper_limit)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nIQR Outliers:")
print(outliers_iqr)

---------------------------------------------------------
Z-Score Method
---------------------------------------------------------

mean = salary.mean()
std = salary.std()

z_scores = (salary - mean) / std

outliers_zscore = salary[abs(z_scores) > 3]

print("\nZ-Score Outliers:")
print(outliers_zscore)

---------------------------------------------------------
Box Plot
---------------------------------------------------------

plt.figure(figsize=(8, 4))

sns.boxplot(x=salary)

plt.title("Salary Outlier Detection")
plt.xlabel("Salary")

plt.show()

---------------------------------------------------------
Professional Interpretation
---------------------------------------------------------

print("\nInterpretation:")
print("An outlier should not automatically be deleted.")
print("First investigate whether it is an error or a valid observation.")
