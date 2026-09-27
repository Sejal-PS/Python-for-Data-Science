# Seaborn - Practice Questions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==================================================
# Practice 1 - Scatter Plot
# ==================================================

df = sns.load_dataset("tips")

# Tasks:
#
# 1. Create a scatter plot.
# 2. Use total_bill on X-axis.
# 3. Use tip on Y-axis.
# 4. Add hue using sex.
# 5. Add a title.
# 6. Change marker size.


# ==================================================
# Practice 2 - Line Plot
# ==================================================

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],
    "Sales": [
        10000,
        12000,
        15000,
        13000,
        18000
    ]
}

sales_df = pd.DataFrame(data)

# Tasks:
#
# 1. Create a line plot.
# 2. Add markers.
# 3. Change the line color.
# 4. Add title.
# 5. Add axis labels.


# ==================================================
# Practice 3 - Bar Plot
# ==================================================

# Use the tips dataset.

# Tasks:
#
# 1. Create a bar plot.
# 2. Show average total_bill by day.
# 3. Add hue using sex.
# 4. Add title.


# ==================================================
# Practice 4 - Count Plot
# ==================================================

# Use the tips dataset.

# Tasks:
#
# 1. Create a count plot for day.
# 2. Create a count plot for sex.
# 3. Use hue=sex with day.
# 4. Add titles.


# ==================================================
# Practice 5 - Histogram
# ==================================================

# Use the tips dataset.

# Tasks:
#
# 1. Create histogram of total_bill.
# 2. Use 10 bins.
# 3. Add KDE.
# 4. Change color.
# 5. Add title.


# ==================================================
# Practice 6 - Box Plot
# ==================================================

# Use the tips dataset.

# Tasks:
#
# 1. Create a box plot of total_bill.
# 2. Compare total_bill by day.
# 3. Use hue=sex.
# 4. Identify possible outliers.


# ==================================================
# Practice 7 - Violin Plot
# ==================================================

# Use the tips dataset.

# Tasks:
#
# 1. Create violin plot.
# 2. Compare total_bill by day.
# 3. Add hue using sex.
# 4. Try split=True.


# ==================================================
# Practice 8 - Heatmap
# ==================================================

student_data = {
    "Math": [80, 85, 90, 75, 88],
    "Science": [75, 90, 85, 70, 92],
    "English": [70, 80, 88, 75, 85],
    "History": [65, 78, 82, 72, 90]
}

student_df = pd.DataFrame(student_data)

# Tasks:
#
# 1. Calculate correlation.
# 2. Create a heatmap.
# 3. Use annot=True.
# 4. Try different color maps.


# ==================================================
# Practice 9 - Pair Plot
# ==================================================

iris = sns.load_dataset("iris")

# Tasks:
#
# 1. Create a pairplot.
# 2. Use hue="species".
# 3. Observe relationships between variables.


# ==================================================
# Practice 10 - Regression Plot
# ==================================================

tips = sns.load_dataset("tips")

# Tasks:
#
# 1. Create regplot.
# 2. Use total_bill and tip.
# 3. Change scatter color.
# 4. Change regression line color.
# 5. Add title.


# ==================================================
# Practice 11 - Mini EDA
# ==================================================

# Use the tips dataset.

# Perform the following:
#
# 1. Display first 5 rows.
# 2. Create count plot for day.
# 3. Create histogram for total_bill.
# 4. Create box plot for total_bill.
# 5. Create scatter plot for total_bill vs tip.
# 6. Create heatmap for numerical columns.
# 7. Create pairplot.
#
# Try to understand what each
# visualization tells you about the data.
