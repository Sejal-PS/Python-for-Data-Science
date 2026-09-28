import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "AnnualIncome": [25, 30, 35, 80, 85, 90, 40, 45, 50],
    "SpendingScore": [80, 75, 85, 30, 25, 20, 60, 55, 65]
}

df = pd.DataFrame(data)

features = df[["AnnualIncome", "SpendingScore"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Segment"] = model.fit_predict(scaled_features)

print(df)
