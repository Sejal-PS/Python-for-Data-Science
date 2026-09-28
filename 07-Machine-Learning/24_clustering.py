"""
Clustering Evaluation

Clustering is an unsupervised learning technique.

This example demonstrates how to evaluate
K-Means clustering using the Silhouette Score.
"""

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data


# --------------------------------------------------
# Standardize Data
# --------------------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# --------------------------------------------------
# Test Different Numbers of Clusters
# --------------------------------------------------

for k in range(2, 7):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(
        X_scaled
    )

    score = silhouette_score(
        X_scaled,
        labels
    )

    print(
        f"K = {k}, "
        f"Silhouette Score = {score:.3f}"
    )


# --------------------------------------------------
# Train Final Model
# --------------------------------------------------

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

labels = model.fit_predict(
    X_scaled
)


# --------------------------------------------------
# Visualize First Two Features
# --------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=labels,
    cmap="viridis"
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Try different K values.
# 2. Compare silhouette scores.
# 3. Visualize different feature combinations.
# 4. Apply clustering to another dataset.
