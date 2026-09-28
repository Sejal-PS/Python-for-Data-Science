"""
Feature Engineering with Pandas

Learn:
- assign()
- apply()
- map()
- replace()
- astype()
- String operations
- Date operations
"""

import pandas as pd

data = {
    "name": ["Amit", "Priya", "Rahul", "Sneha"],
    "age": [22, 35, 28, 45],
    "city": ["Pune", "Mumbai", "Pune", "Nashik"],
    "salary": [30000, 55000, 42000, 80000]
}

df = pd.DataFrame(data)

# assign()
df = df.assign(
    salary_k=df["salary"] / 1000
)

# apply()
df["age_group"] = df["age"].apply(
    lambda age: "Young" if age < 30 else "Experienced"
)

# map()
city_code = {
    "Pune": "PN",
    "Mumbai": "MU",
    "Nashik": "NK"
}

df["city_code"] = df["city"].map(city_code)

# replace()
df["city"] = df["city"].replace(
    {"Mumbai": "Mumbai City"}
)

# astype()
df["age"] = df["age"].astype(int)

# String operation
df["name_upper"] = df["name"].str.upper()

print(df)

print("\nPandas provides flexible tools for practical feature engineering.")
