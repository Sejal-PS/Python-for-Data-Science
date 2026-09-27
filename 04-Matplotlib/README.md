Matplotlib for Data Science

Matplotlib is a Python library used for creating graphs and visualizations.

In Data Science, visualization helps us understand patterns, trends, distributions and relationships in data.

Why Matplotlib?

Matplotlib can be used to:

Create charts and graphs

Understand data visually

Compare values

Identify trends

Understand distributions

Visualize relationships between variables

Create charts for Exploratory Data Analysis (EDA)

Customize plots

Save charts as image files

Topics Covered
1. Introduction to Matplotlib

What is Matplotlib?

Installation

Importing Matplotlib

pyplot

Basic plotting

2. Line Chart

plt.plot()

X-axis

Y-axis

Title

Labels

Legend

Grid

3. Bar Chart

plt.bar()

Vertical bar chart

Horizontal bar chart

Comparing categories

4. Scatter Plot

plt.scatter()

Relationship between two variables

Positive and negative relationships

5. Histogram

plt.hist()

Distribution of numerical data

Bins

6. Pie Chart

plt.pie()

Percentage distribution

Labels

Autopct

7. Plot Customization

Colors

Markers

Line styles

Line width

Figure size

Titles

Axis labels

Grid

Legend

8. Subplots

Multiple charts in one figure

plt.subplot()

plt.subplots()

9. Saving Charts

Saving plots as PNG

Saving plots as JPG

Saving plots as PDF

10. Matplotlib with Pandas

Plotting DataFrame columns

Visualizing grouped data

Basic Data Analysis charts

11. Data Science Visualization Examples

Sales analysis

Student marks

Employee salary

Product analysis

Monthly trends

12. Practice

Practice exercises based on different types of charts and Data Science datasets.

Learning Flow
Understand Data
      ↓
Choose Chart
      ↓
Create Plot
      ↓
Add Labels
      ↓
Customize Plot
      ↓
Understand Pattern
      ↓
Use for EDA

Basic Example
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 12000, 18000]

plt.plot(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

Matplotlib in Data Science

Matplotlib is commonly used after data cleaning and analysis.

A common workflow is:

NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
EDA
   ↓
Machine Learning

Official Documentation

Matplotlib documentation:

https://matplotlib.org/stable/
