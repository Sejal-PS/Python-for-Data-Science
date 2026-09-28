"""
04 - Univariate Analysis

Univariate analysis studies one variable at a time.

Examples:

Salary distribution

Age distribution

Department frequency
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Age": [21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 35, 40],
"Salary": [25000, 28000, 30000, 32000, 35000, 38000,
42000, 45000, 50000, 60000, 75000, 90000],
"Department": [
"IT", "IT", "HR", "Sales", "IT", "HR",
"Sales", "IT", "Sales", "HR", "IT", "Sales"
]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Numerical Variable
---------------------------------------------------------

print("Salary Statistics:")
print(df["Salary"].describe())

---------------------------------------------------------
Histogram
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(df["Salary"], bins=6, kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

---------------------------------------------------------
Box Plot
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(x=df["Salary"])

plt.title("Salary Box Plot")
plt.xlabel("Salary")

plt.show()

---------------------------------------------------------
Categorical Variable
---------------------------------------------------------

print("\nDepartment Frequency:")
print(df["Department"].value_counts())

---------------------------------------------------------
Count Plot
---------------------------------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="Department")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()

---------------------------------------------------------
Learning Questions
---------------------------------------------------------

print("\nQuestions:")
print("1. Which salary range appears most frequently?")
print("2. Are there potential salary outliers?")
print("3. Which department has the most employees?")
