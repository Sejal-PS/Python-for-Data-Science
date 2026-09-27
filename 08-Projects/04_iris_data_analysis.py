import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris


iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = [
    iris.target_names[i]
    for i in iris.target
]


print("Dataset:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nStatistics:")
print(df.describe())

print("\nSpecies Count:")
print(
    df["species"].value_counts()
)


sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="sepal width (cm)",
    hue="species"
)

plt.title("Iris Species")
plt.show()
