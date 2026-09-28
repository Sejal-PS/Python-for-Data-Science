"""
05 - Bivariate Analysis

Bivariate analysis studies relationships between two variables.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Experience": [1, 2, 3, 4, 5, 6, 7, 8],
"Salary": [28000, 32000, 36000, 42000, 48000, 55000, 62000, 70000],
"Department": ["IT", "HR", "IT", "Sales", "IT", "HR", "Sales", "IT"]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Numerical vs Numerical
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
data=df,
x="Experience",
y="Salary",
hue="Department",
s=100
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

---------------------------------------------------------
Numerical vs Categorical
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
data=df,
x="Department",
y="Salary"
)

plt.title("Salary by Department")
plt.show()

---------------------------------------------------------
Group Statistics
---------------------------------------------------------

print("Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

---------------------------------------------------------
Correlation
---------------------------------------------------------

print("\nExperience-Salary Correlation:")
print(df["Experience"].corr(df["Salary"]))

---------------------------------------------------------
Key Questions
---------------------------------------------------------

print("\nQuestions:")
print("1. Does salary increase with experience?")
print("2. How does salary vary across departments?")
print("3. Is the observed relationship strong?")
