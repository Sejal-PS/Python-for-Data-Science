import pandas as pd

data = {
    "Name": ["A", "B", "B", "D"],
    "Age": [21, 25, None, 30],
    "Salary": [30000, 45000, 45000, -5000]
}

df = pd.DataFrame(data)

print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nInvalid salary values:")
print(df[df["Salary"] < 0])

print("\nData types:")
print(df.dtypes)
