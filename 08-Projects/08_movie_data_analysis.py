import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Movie": [
        "Movie A",
        "Movie B",
        "Movie C",
        "Movie D",
        "Movie E",
        "Movie F"
    ],
    "Genre": [
        "Action",
        "Drama",
        "Comedy",
        "Action",
        "Drama",
        "Comedy"
    ],
    "Rating": [
        8.2,
        7.5,
        8.0,
        9.0,
        7.8,
        8.5
    ],
    "Year": [
        2020,
        2021,
        2020,
        2022,
        2023,
        2022
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nGenre Count:")
print(
    df["Genre"].value_counts()
)

print("\nHighest Rated Movie:")
print(
    df.loc[
        df["Rating"].idxmax()
    ]
)


sns.boxplot(
    data=df,
    x="Genre",
    y="Rating"
)

plt.title("Ratings by Genre")

plt.show()
