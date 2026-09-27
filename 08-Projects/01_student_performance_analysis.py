import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 70, 90, 60, 85, 75],
    "Science": [85, 75, 88, 65, 90, 78],
    "English": [78, 80, 92, 70, 88, 82]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

df["Average"] = df[
    ["Math", "Science", "English"]
].mean(axis=1)

print("\nStudent Average:")
print(df[["Name", "Average"]])

print("\nHighest Average:")
print(df["Average"].max())

print("\nOverall Subject Average:")
print(
    df[
        ["Math", "Science", "English"]
    ].mean()
)


# Visualization

sns.barplot(
    data=df,
    x="Name",
    y="Average"
)

plt.title("Student Average Marks")
plt.show()
