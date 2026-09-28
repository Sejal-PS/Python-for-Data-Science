"""
14 - EDA with Visualization

Combine Pandas, Matplotlib and Seaborn
to answer business questions visually.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
"Sales": [45000, 52000, 48000, 60000, 68000, 75000],
"Customers": [120, 135, 128, 150, 165, 180],
"Category": [
"Electronics", "Clothing", "Electronics",
"Grocery", "Electronics", "Clothing"
]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Sales Trend
---------------------------------------------------------

plt.figure(figsize=(9, 5))

sns.lineplot(
data=df,
x="Month",
y="Sales",
marker="o",
linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

---------------------------------------------------------
Customer Count
---------------------------------------------------------

plt.figure(figsize=(9, 5))

sns.barplot(
data=df,
x="Month",
y="Customers"
)

plt.title("Monthly Customers")
plt.xlabel("Month")
plt.ylabel("Customers")

plt.tight_layout()
plt.show()

---------------------------------------------------------
Sales Distribution
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
data=df,
x="Sales",
kde=True
)

plt.title("Sales Distribution")

plt.tight_layout()
plt.show()

---------------------------------------------------------
Correlation
---------------------------------------------------------

print("Correlation:")
print(df[["Sales", "Customers"]].corr())

---------------------------------------------------------
Business Questions
---------------------------------------------------------

print("\nQuestions:")
print("1. Is there an upward sales trend?")
print("2. How does customer count change?")
print("3. Are sales and customer count associated?")

---------------------------------------------------------
Visualization Principle
---------------------------------------------------------

print("\nPrinciple:")
print("Choose a visualization based on the question you want to answer.")
