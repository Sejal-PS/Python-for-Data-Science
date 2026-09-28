"""
09 - Correlation Analysis

Learn:

Positive correlation

Negative correlation

Correlation strength

Correlation matrix

Correlation vs causation
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
"Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
"Score": [45, 50, 55, 62, 68, 74, 82, 88]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Pairwise Correlation
---------------------------------------------------------

print("Study Hours vs Score:")
print(df["StudyHours"].corr(df["Score"]))

print("\nAttendance vs Score:")
print(df["Attendance"].corr(df["Score"]))

---------------------------------------------------------
Correlation Matrix
---------------------------------------------------------

correlation_matrix = df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

---------------------------------------------------------
Heatmap
---------------------------------------------------------

plt.figure(figsize=(7, 5))

sns.heatmap(
correlation_matrix,
annot=True,
cmap="coolwarm",
fmt=".2f"
)

plt.title("Correlation Matrix")

plt.show()

---------------------------------------------------------
Scatter Plot
---------------------------------------------------------

plt.figure(figsize=(7, 5))

sns.scatterplot(
data=df,
x="StudyHours",
y="Score",
s=100
)

plt.title("Study Hours vs Score")

plt.show()

---------------------------------------------------------
Important Concept
---------------------------------------------------------

print("\nImportant:")
print("Correlation measures association between variables.")
print("Correlation alone does not establish causation.")
