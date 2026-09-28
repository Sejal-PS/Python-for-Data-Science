import pandas as pd

data = {
    "Product": ["A", "B", "A", "C", "B", "C"],
    "Region": ["North", "South", "North", "West", "South", "West"],
    "Sales": [100, 150, 120, 200, 170, 180]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nBasic information:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nSales by product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop product:")
print(
    df.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)

# Next steps for learners:
# 1. Add visualizations.
# 2. Check data quality.
# 3. Find additional insights.
# 4. Write a short analysis report.



For prcatice follow the following 
"""
Real-World Dataset Practice

Choose any public dataset and complete the following:

1. Load the dataset.
2. Identify rows and columns.
3. Understand every important column.
4. Check data types.
5. Check missing values.
6. Check duplicate records.
7. Calculate descriptive statistics.
8. Analyze numerical variables.
9. Analyze categorical variables.
10. Create at least three visualizations.
11. Identify important patterns.
12. Write five observations.
13. Convert observations into business insights.
14. Document limitations of your analysis.
"""

print("Choose a real-world dataset and start your analysis.")

