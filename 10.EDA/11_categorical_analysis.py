"""
11 - Categorical Analysis

Analyze categorical variables using:

Frequencies

Proportions

Group comparisons
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Customer": ["A", "B", "C", "D", "E", "F", "G", "H"],
"City": [
"Pune", "Mumbai", "Pune", "Delhi",
"Mumbai", "Pune", "Delhi", "Mumbai"
],
"Category": [
"Electronics", "Clothing", "Electronics", "Grocery",
"Clothing", "Grocery", "Electronics", "Clothing"
],
"Revenue": [5000, 3000, 7000, 2500, 4000, 3500, 8000, 4500]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Frequency
---------------------------------------------------------

print("Category Frequency:")
print(df["Category"].value_counts())

---------------------------------------------------------
Proportion
---------------------------------------------------------

print("\nCategory Proportion:")
print(
df["Category"]
.value_counts(normalize=True)
.mul(100)
.round(2)
)

---------------------------------------------------------
Count Plot
---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
data=df,
x="Category"
)

plt.title("Customer Count by Category")
plt.xticks(rotation=20)

plt.show()

---------------------------------------------------------
Revenue by Category
---------------------------------------------------------

revenue_by_category = (
df.groupby("Category")["Revenue"]
.sum()
.sort_values(ascending=False)
)

print("\nRevenue by Category:")
print(revenue_by_category)

---------------------------------------------------------
Business Question
---------------------------------------------------------

print("\nBusiness Question:")
print("Which category has the highest total revenue?")
