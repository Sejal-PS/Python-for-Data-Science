import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "IT", "Sales", "Sales"],
    "Salary": [60000, 45000, 75000, 50000, 65000]
}

df = pd.DataFrame(data)

print("Average salary:", df["Salary"].mean())

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nHighest salary:")
print(df.loc[df["Salary"].idxmax()])
