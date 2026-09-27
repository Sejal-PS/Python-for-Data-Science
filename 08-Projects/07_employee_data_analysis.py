import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
    ],
    "Department": [
        "IT",
        "HR",
        "IT",
        "Sales",
        "HR",
        "Sales"
    ],
    "Experience": [
        2,
        5,
        4,
        6,
        3,
        7
    ],
    "Salary": [
        40000,
        50000,
        60000,
        55000,
        45000,
        70000
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nDepartment-wise Salary:")
print(
    df.groupby(
        "Department"
    )["Salary"].mean()
)

print("\nHighest Salary:")
print(
    df.loc[
        df["Salary"].idxmax()
    ]
)


sns.barplot(
    data=df,
    x="Department",
    y="Salary"
)

plt.title("Department-wise Salary")

plt.show()
