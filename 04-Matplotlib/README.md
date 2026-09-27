Matplotlib for Data Science

Matplotlib is a Python library used for creating charts and visualizations.

It is commonly used in Data Science for understanding and presenting data.

Topics Covered

Basic plotting

Line chart

Bar chart

Scatter plot

Histogram

Pie chart

Subplots

Plot customization

Saving plots

Matplotlib with Pandas

Practice exercises

Files
01_basic_plot.py

Basic Matplotlib plotting and figure concepts.

02_line_chart.py

Line charts with titles, labels, markers and grid.

03_bar_chart.py

Bar charts for comparing different categories.

04_scatter_plot.py

Scatter plots for understanding the relationship between two numerical variables.

05_histogram.py

Histograms for understanding the distribution of numerical data.

06_pie_chart.py

Pie charts for showing proportions of different categories.

07_subplots.py

Creating multiple charts in a single figure.

08_customization.py

Colors, markers, line styles, legends, grid, labels and other plot formatting.

09_save_plots.py

Saving charts as PNG, PDF and SVG files.

10_matplotlib_with_pandas.py

Using Matplotlib with Pandas DataFrames for data visualization.

11_practice.py

Practice questions based on the Matplotlib topics covered in this folder.

Common Matplotlib Functions
import matplotlib.pyplot as plt

plt.plot()
plt.bar()
plt.scatter()
plt.hist()
plt.pie()

plt.title()
plt.xlabel()
plt.ylabel()

plt.legend()
plt.grid()

plt.show()
plt.savefig()

Basic Example
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 13000, 18000]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()

Installation

Matplotlib can be installed using pip:

pip install matplotlib


Import Matplotlib:

import matplotlib.pyplot as plt

Important Concepts
Line Plot

Used to show trends over time.

plt.plot(x, y)

Bar Chart

Used to compare categories.

plt.bar(x, y)

Scatter Plot

Used to understand the relationship between two numerical variables.

plt.scatter(x, y)

Histogram

Used to understand the distribution of numerical data.

plt.hist(data)

Pie Chart

Used to show proportions or percentage share.

plt.pie(values, labels=labels)

Subplots

Used to display multiple charts in one figure.

fig, axes = plt.subplots(2, 2)

Plot Customization

Commonly used customization options:

color
linestyle
linewidth
marker
markersize
fontsize
figsize
legend
grid
xlim
ylim


Example:

plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    linewidth=2,
    marker="o"
)

Saving a Plot
plt.savefig(
    "chart.png",
    dpi=300,
    bbox_inches="tight"
)


Matplotlib supports formats such as:

PNG

PDF

SVG

Matplotlib with Pandas

Matplotlib is commonly used together with Pandas for Data Analysis and visualization.

Pandas
   ↓
DataFrame
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Matplotlib
   ↓
Visualization


Example:

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [10000, 15000, 13000, 18000]
}

df = pd.DataFrame(data)

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()

Data Science Use Cases

Matplotlib can be used for:

Sales analysis

Customer analysis

Student performance analysis

Salary analysis

Time-series visualization

Distribution analysis

Comparing categories

Understanding relationships between variables

Exploratory Data Analysis (EDA)

Presenting Data Science results

Learning Flow
Matplotlib
   ↓
Basic Plot
   ↓
Line Chart
   ↓
Bar Chart
   ↓
Scatter Plot
   ↓
Histogram
   ↓
Pie Chart
   ↓
Subplots
   ↓
Customization
   ↓
Save Plots
   ↓
Pandas + Matplotlib
   ↓
Practice

Official Documentation

Matplotlib Documentation:

https://matplotlib.org/stable/




---------------------------------------------------------------------


""" Matplotlib for Data Science

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

"""
