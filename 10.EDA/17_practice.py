"""
17 - EDA Practice

Complete these exercises independently.

Dataset:
A small sales dataset is provided below.

Try to solve each question using Pandas and visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Customer": ["A", "B", "C", "D", "E", "F", "G", "H"],
"Region": [
"West", "North", "West", "South",
"North", "West", "South", "North"
],
"Category": [
"Electronics", "Clothing", "Electronics", "Grocery",
"Clothing", "Grocery", "Electronics", "Clothing"
],
"Sales": [5000, 3000, 7000, 2500, 4000, 3500, 8000, 4500],
"Quantity": [2, 3, 4, 2, 3, 5, 4, 3]
}

df = pd.DataFrame(data)

=========================================================
LEVEL 1 - Dataset Understanding
=========================================================
1. Display the first five rows.
2. Find the number of rows and columns.
3. Display column names.
4. Display data types.
5. Generate descriptive statistics.
=========================================================
LEVEL 2 - Data Analysis
=========================================================
6. Find total sales.
7. Find average sales.
8. Find minimum and maximum sales.
9. Find total quantity sold.
10. Find the number of unique regions.
11. Find the number of customers in each region.
12. Find sales by category.
13. Find sales by region.
=========================================================
LEVEL 3 - Visualization
=========================================================
14. Create a bar chart of sales by region.
15. Create a bar chart of sales by category.
16. Create a histogram of sales.
17. Create a box plot of sales.
18. Create a count plot for categories.
=========================================================
LEVEL 4 - Business Questions
=========================================================
19. Which region generates the highest sales?
20. Which category generates the highest sales?
21. Which region has the highest quantity sold?
22. What percentage of total sales comes from each region?
=========================================================
LEVEL 5 - Interpretation
=========================================================
23. Write three observations from your analysis.
24. Convert at least two observations into business insights.
25. Write two questions that should be investigated next.
=========================================================
Optional Challenge
=========================================================
Create a one-page EDA summary containing:
- Dataset overview
- Key statistics
- Two visualizations
- Three observations
- Two business insights
- Two questions for further analysis

print("Practice dataset loaded successfully.")
print(df)
