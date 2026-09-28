import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [21, 25, 30, 28],
    "Salary": [30000, 45000, 60000, 50000]
}

df = pd.DataFrame(data)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst records:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nSummary:")
print(df.describe())
