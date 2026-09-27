import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


data = {
    "Age": [
        20, 22, 25,
        35, 38, 40,
        50, 52, 55
    ],
    "Income": [
        25000,
        28000,
        30000,
        50000,
        55000,
        60000,
        80000,
        85000,
        90000
    ]
}

df = pd.DataFrame(data)

print(df)


features = [
    "Age",
    "Income"
]

X = df[features]


scaler = StandardScaler()

X_scaled = scaler.fit_transform(
    X
)


model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(
    X_scaled
)


print("\nCustomer Clusters:")
print(df)


plt.scatter(
    df["Age"],
    df["Income"],
    c=df["Cluster"],
    cmap="viridis"
)

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Customer Segmentation")

plt.show()
