"""
06 - Multivariate Analysis

Study relationships among multiple variables.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Age": [22, 25, 28, 30, 35, 40, 26, 32],
"Experience": [1, 3, 5, 7, 10, 15, 4, 8],
"Salary": [30000, 40000, 50000, 60000, 80000, 120000, 45000, 70000],
"Performance": [65, 70, 78, 82, 90, 95, 75, 85]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Correlation Matrix
---------------------------------------------------------

correlation = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation)

---------------------------------------------------------
Heatmap
---------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
correlation,
annot=True,
cmap="coolwarm",
fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()

---------------------------------------------------------
Pair Plot
---------------------------------------------------------

sns.pairplot(df)

plt.show()

---------------------------------------------------------
Multivariate Question
---------------------------------------------------------

print("\nQuestions:")
print("How are age, experience, salary and performance related?")
print("Which relationships appear stronger?")
print("Do these relationships imply causation? No — further investigation is required.")
