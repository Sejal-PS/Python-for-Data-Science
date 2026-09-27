
Pandas for Data Science

Pandas is a Python library used for data manipulation, data cleaning, data analysis and working with tabular data.

It is one of the most commonly used libraries in Data Science.

Pandas mainly provides two important data structures:

Series

DataFrame

1. Why Pandas?

In Data Science, we usually work with data such as:

Customer data

Employee data

Sales data

Student data

Product data

Financial data

This data is often stored in rows and columns.

Pandas makes it easier to:

Read data

View data

Filter data

Clean data

Handle missing values

Sort data

Group data

Calculate statistics

Combine datasets

Prepare data for Machine Learning

2. Installation

Pandas can be installed using pip.

pip install pandas


To check the installed version:

import pandas as pd

print(pd.__version__)

3. Import Pandas

The commonly used alias for Pandas is pd.

import pandas as pd

4. Pandas Series

A Series is a one-dimensional labelled data structure.

Example:

import pandas as pd

marks = pd.Series([80, 75, 90, 85, 70])

print(marks)


Each value has an index.

5. Series with Custom Index
marks = pd.Series(
    [80, 75, 90],
    index=["Rahul", "Priya", "Amit"]
)

print(marks)


Access a value:

print(marks["Rahul"])

6. DataFrame

A DataFrame is a two-dimensional labelled data structure with rows and columns.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, 24, 23],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)


A DataFrame is similar to a table.

7. Important DataFrame Terms

A DataFrame contains:

Rows

Columns

Index

Values

Data Types

Example:

print(df.index)
print(df.columns)
print(df.values)
print(df.dtypes)

8. Creating DataFrame from Dictionary
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print(df)

9. Creating DataFrame from List
data = [
    ["Rahul", 22, 80],
    ["Priya", 24, 90],
    ["Amit", 23, 75]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Marks"]
)

print(df)

10. Reading CSV File

CSV files are very common in Data Science.

df = pd.read_csv("data.csv")

print(df)

11. Reading Excel File
df = pd.read_excel("data.xlsx")

print(df)


Excel support may require an additional package depending on the file format and environment.

12. Inspecting Data
head()

Shows the first rows.

print(df.head())

tail()

Shows the last rows.

print(df.tail())

shape

Returns number of rows and columns.

print(df.shape)

columns

Shows column names.

print(df.columns)

dtypes

Shows data types.

print(df.dtypes)

info()

Provides information about the DataFrame.

df.info()

describe()

Provides statistical summary for numerical columns.

print(df.describe())

13. Selecting a Column
print(df["Name"])


Another method:

print(df.Name)


The bracket method is generally preferred because it also works with column names containing spaces or special characters.

14. Selecting Multiple Columns
print(df[["Name", "Marks"]])

15. Selecting Rows with loc

loc is label-based selection.

print(df.loc[0])


Selecting multiple rows:

print(df.loc[0:2])


Selecting rows and columns:

print(df.loc[0:2, ["Name", "Marks"]])

16. Selecting Rows with iloc

iloc is position-based selection.

print(df.iloc[0])


Multiple rows:

print(df.iloc[0:3])


Rows and columns:

print(df.iloc[0:3, 0:2])

17. Filtering Data

Filtering is one of the most important Pandas concepts.

Example:

print(df[df["Marks"] > 80])


Multiple conditions:

print(
    df[
        (df["Age"] > 20) &
        (df["Marks"] > 80)
    ]
)


Using OR:

print(
    df[
        (df["Marks"] > 90) |
        (df["Age"] < 21)
    ]
)

18. Adding a New Column
df["Passed"] = df["Marks"] >= 40

print(df)


Another example:

df["Bonus"] = 5

print(df)

19. Updating a Column
df["Marks"] = df["Marks"] + 5

print(df)

20. Renaming Columns
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)

print(df)

21. Dropping Columns
df.drop(
    columns=["Age"],
    inplace=True
)

print(df)

22. Dropping Rows
df.drop(index=0, inplace=True)

print(df)

23. Sorting Data

Sort by one column:

df.sort_values("Marks")


Descending order:

df.sort_values(
    "Marks",
    ascending=False
)

24. Handling Missing Values

Missing values are common in real-world datasets.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, None, 24],
    "Marks": [80, 90, None]
}

df = pd.DataFrame(data)

print(df)

25. Detecting Missing Values
print(df.isnull())


Count missing values:

print(df.isnull().sum())


Another method:

print(df.isna().sum())

26. Removing Missing Values
df.dropna()


Remove rows containing missing values:

df.dropna(inplace=True)

27. Filling Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())


For a fixed value:

df["Marks"] = df["Marks"].fillna(0)

28. Duplicate Data

Check duplicates:

print(df.duplicated())


Count duplicates:

print(df.duplicated().sum())


Remove duplicates:

df.drop_duplicates(inplace=True)

29. Unique Values
print(df["Name"].unique())


Number of unique values:

print(df["Name"].nunique())

30. Value Counts

value_counts() counts how frequently each value occurs.

print(df["City"].value_counts())


This is useful for categorical data analysis.

31. Basic Statistics
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].sum())

32. GroupBy

groupby() is one of the most important Pandas concepts for Data Analysis.

Example:

data = {
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [1000, 2000, 1500, 2500]
}

df = pd.DataFrame(data)

print(
    df.groupby("City")["Sales"].sum()
)


Average sales:

print(
    df.groupby("City")["Sales"].mean()
)

33. GroupBy Multiple Columns
result = df.groupby(
    ["City"]
)["Sales"].agg(
    ["sum", "mean", "max", "min"]
)

print(result)

34. Aggregation

Pandas provides aggregation functions such as:

sum()
mean()
median()
min()
max()
count()


Example:

print(
    df["Sales"].agg(
        ["sum", "mean", "min", "max"]
    )
)

35. Apply Function

apply() can be used to apply a function to values.

Example:

def add_bonus(x):
    return x + 10

df["Updated_Sales"] = df["Sales"].apply(add_bonus)

print(df)


A lambda function can also be used:

df["Updated_Sales"] = df["Sales"].apply(
    lambda x: x + 10
)

36. String Operations

Pandas provides string methods for text columns.

Example:

df["Name"] = df["Name"].str.upper()


Other examples:

df["Name"].str.lower()
df["Name"].str.title()
df["Name"].str.len()


Checking text:

df["Name"].str.contains("A")

37. Date and Time

Pandas can work with dates.

dates = pd.to_datetime(
    ["2025-01-01", "2025-02-01", "2025-03-01"]
)

print(dates)


Create a date column:

df["Date"] = pd.to_datetime(df["Date"])


Extract year:

df["Year"] = df["Date"].dt.year


Extract month:

df["Month"] = df["Date"].dt.month

38. Concatenating DataFrames

Two DataFrames can be combined using concat().

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Marks": [75, 85]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

39. Merge

merge() is used to combine DataFrames using a common column.

Example:

students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Rahul", "Priya", "Amit"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [80, 90, 75]
})

result = pd.merge(
    students,
    marks,
    on="Student_ID"
)

print(result)

40. Merge Types

Important merge types:

inner
left
right
outer


Example:

pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

41. Exporting Data

Save DataFrame as CSV:

df.to_csv(
    "output.csv",
    index=False
)


Save as Excel:

df.to_excel(
    "output.xlsx",
    index=False
)

42. Index

Every Pandas DataFrame has an index.

print(df.index)


Set a column as index:

df.set_index("Student_ID", inplace=True)


Reset index:

df.reset_index(inplace=True)

43. Changing Data Type

Check data types:

print(df.dtypes)


Convert a column:

df["Age"] = df["Age"].astype(int)


For numeric conversion:

df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)

44. Pandas Data Cleaning Flow

A common Data Science workflow is:

Read Data
    ↓
Understand Data
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Clean Data
    ↓
Transform Data
    ↓
Filter Data
    ↓
Group / Aggregate
    ↓
Analyze Data
    ↓
Export / Use for ML

45. Simple Data Analysis Example
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [5000, 7000, 4500, 8000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nHighest Sales:")
print(df["Sales"].max())

print("\nPune Customers:")
print(df[df["City"] == "Pune"])

print("\nCity-wise Sales:")
print(
    df.groupby("City")["Sales"].sum()
)

46. Important Pandas Functions
pd.Series()
pd.DataFrame()

pd.read_csv()
pd.read_excel()

df.head()
df.tail()
df.info()
df.describe()

df.shape
df.columns
df.index
df.dtypes

df["column"]
df[["column1", "column2"]]

df.loc[]
df.iloc[]

df.isnull()
df.isna()
df.dropna()
df.fillna()

df.drop_duplicates()
df.duplicated()

df.sort_values()

df.groupby()
df.agg()
df.apply()

df.merge()
pd.concat()

df.rename()
df.drop()

df.unique()
df.nunique()
df.value_counts()

df.to_csv()
df.to_excel()

47. Pandas in Data Science

Pandas is mainly used for:

Data loading

Data cleaning

Data preprocessing

Data transformation

Exploratory Data Analysis (EDA)

Statistical analysis

Working with CSV and Excel files

Handling missing values

Filtering and sorting data

Grouping and aggregation

Preparing data for visualization

Preparing data for Machine Learning

48. Pandas and NumPy

NumPy is mainly focused on numerical arrays and mathematical operations.

Pandas provides higher-level data structures such as Series and DataFrame for working with structured and labelled data.

A common Data Science workflow is:

NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
Statistics / EDA
   ↓
Machine Learning

49. Quick Revision
Pandas
   ↓
Series
   ↓
DataFrame
   ↓
Read Data
   ↓
Inspect Data
   ↓
Select Data
   ↓
Filter Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
GroupBy
   ↓
Merge / Concat
   ↓
Analyze Data
   ↓
Export Data

Official Documentation

Pandas documentation:

https://pandas.pydata.org/docs/
