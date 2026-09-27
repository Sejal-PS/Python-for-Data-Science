Pandas for Data Science

Pandas is a Python library mainly used for working with data in table format.

It is useful for:

Data cleaning

Data analysis

Data manipulation

Working with CSV and Excel files

Preparing data for visualization and machine learning

Topics Covered
1. Pandas Basics

File: pandas_basics.py

What is Pandas

Series

DataFrame

Creating DataFrame

Basic DataFrame operations

head()

tail()

shape

columns

dtypes

info()

describe()

2. Selecting, Filtering and Sorting

File: select_filter_sort.py

Selecting columns

Selecting rows

loc

iloc

Filtering data

Multiple conditions

isin()

between()

Sorting data

sort_values()

3. Missing Values

File: missing_values.py

Missing values

isnull()

isna()

dropna()

fillna()

Mean

Median

Mode

Forward fill

Backward fill

4. Duplicate Data

File: duplicates.py

Finding duplicate records

duplicated()

Counting duplicates

drop_duplicates()

Duplicate values based on specific columns

5. Data Transformation

File: data_transformation.py

Creating new columns

Updating columns

apply()

lambda

map()

replace()

rename()

Conditional transformation

6. GroupBy and Aggregation

File: groupby_aggregation.py

groupby()

sum()

mean()

min()

max()

count()

agg()

Grouping by multiple columns

Data analysis using grouped data

7. Merge and Concat

File: merge_concat.py

concat()

merge()

Inner join

Left join

Right join

Outer join

Merging using different column names

8. String and DateTime Operations

File: string_datetime.py

String operations

upper()

lower()

title()

contains()

startswith()

endswith()

replace()

split()

strip()

DateTime conversion

Year

Month

Day

Quarter

Date difference

Date ranges

9. Index and Column Management

File: index_columns.py

Index

Columns

set_index()

reset_index()

rename()

insert()

drop()

Column reordering

10. Reading and Writing Files

File: read_write_files.py

Reading CSV files

Writing CSV files

Reading Excel files

Writing Excel files

Selecting columns while reading

Handling missing values while reading

Appending data

11. Practice

File: practice.py

Practice exercises covering:

DataFrame basics

Selection

Filtering

Sorting

Data transformation

GroupBy

Aggregation

Missing values

Duplicate data

String operations

Index operations

Sales data analysis

Basic Pandas Example
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)

print(df["Marks"].mean())

Learning Flow
Create DataFrame
       ↓
Understand Data
       ↓
Select / Filter
       ↓
Clean Data
       ↓
Transform Data
       ↓
Group and Aggregate
       ↓
Merge Data
       ↓
Analyze Data
       ↓
Save / Export Data

Practice

Try the exercises in:

practice.py

The goal is to understand the concepts by writing and running the code yourself.
