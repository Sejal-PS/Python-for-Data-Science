import pandas as pd

data = {
    "Customer": ["A", "B", "C", "D", "E"],
    "Age": [22, 35, 41, 29, 50],
    "Purchase": [1200, 3500, 4200, 1800, 5000]
}

df = pd.DataFrame(data)

print("Average purchase:", df["Purchase"].mean())

print("\nCustomers with purchase above average:")
print(df[df["Purchase"] > df["Purchase"].mean()])

print("\nHighest value customer:")
print(df.loc[df["Purchase"].idxmax()])
