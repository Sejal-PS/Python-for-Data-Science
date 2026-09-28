"""
15 - Business Insights

Learn how to convert analysis results into useful insights.

Observation = What the data shows.
Insight = What that observation may mean in context.
"""

import pandas as pd

data = {
"Region": ["West", "North", "South", "East"],
"Revenue": [150000, 120000, 95000, 80000],
"Customers": [300, 250, 220, 180],
"Average_Order_Value": [500, 480, 432, 444]
}

df = pd.DataFrame(data)

---------------------------------------------------------
Basic Analysis
---------------------------------------------------------

highest_revenue_region = df.loc[
df["Revenue"].idxmax(),
"Region"
]

highest_revenue = df["Revenue"].max()

highest_customer_region = df.loc[
df["Customers"].idxmax(),
"Region"
]

print("Highest Revenue Region:", highest_revenue_region)
print("Highest Revenue:", highest_revenue)

print(
"Highest Customer Count Region:",
highest_customer_region
)

---------------------------------------------------------
Revenue Share
---------------------------------------------------------

total_revenue = df["Revenue"].sum()

df["Revenue_Share_Percent"] = (
df["Revenue"] / total_revenue * 100
).round(2)

print("\nRevenue Share:")
print(df[["Region", "Revenue", "Revenue_Share_Percent"]])

---------------------------------------------------------
Observation vs Insight
---------------------------------------------------------

print("\nObservation:")
print(
f"{highest_revenue_region} has the highest observed revenue."
)

print("\nPotential Insight:")
print(
f"{highest_revenue_region} contributes the largest share "
"of the observed revenue in this dataset."
)

print("\nNext Question:")
print(
"Which products, customers, or other factors are driving "
"the regional performance?"
)

---------------------------------------------------------
Important
---------------------------------------------------------

print("\nImportant:")
print("Insights should be supported by data.")
print("Avoid claiming causation without appropriate evidence.")
