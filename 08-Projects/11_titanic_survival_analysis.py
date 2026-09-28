"""
Project: Titanic Survival Analysis

Skills:
- Data Loading
- Data Inspection
- Missing Value Handling
- GroupBy
- Data Visualization
- Basic Statistical Analysis
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

df = sns.load_dataset("titanic")

print("First 5 rows:")
print(df.head())


# --------------------------------------------------
# 2. Basic Information
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 3. Survival Rate
# --------------------------------------------------

survival_rate = df["survived"].mean()

print("\nOverall Survival Rate:")
print(survival_rate)


# --------------------------------------------------
# 4. Survival by Gender
# --------------------------------------------------

gender_survival = df.groupby(
    "sex"
)["survived"].mean()

print("\nSurvival Rate by Gender:")
print(gender_survival)


# --------------------------------------------------
# 5. Survival by Passenger Class
# --------------------------------------------------

class_survival = df.groupby(
    "class",
    observed=True
)["survived"].mean()

print("\nSurvival Rate by Class:")
print(class_survival)


# --------------------------------------------------
# 6. Age Analysis
# --------------------------------------------------

print("\nAverage Age:")
print(df["age"].mean())

df["age"] = df["age"].fillna(
    df["age"].median()
)


# --------------------------------------------------
# 7. Visualization
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="sex",
    hue="survived"
)

plt.title("Survival Count by Gender")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 8. Class Visualization
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="class",
    y="survived",
    hue="class",
    legend=False
)

plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival Rate")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# 9. Age Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="age",
    hue="survived",
    kde=True
)

plt.title("Age Distribution by Survival")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Project Questions
# --------------------------------------------------

# 1. Which gender had a higher survival rate?
# 2. How did passenger class affect survival?
# 3. What was the average passenger age?
# 4. Which age groups had different survival patterns?
# 5. Explore survival based on embarkation port.
