# K-Means Clustering

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# ------------------------------------------
# Load Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data


# ------------------------------------------
# Create Model
# ------------------------------------------

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)


# ------------------------------------------
# Train
# ------------------------------------------

model.fit(
    X
)


# ------------------------------------------
# Cluster Labels
# ------------------------------------------

labels = model.labels_

print(
    "Cluster Labels:"
)

print(
    labels
)


# ------------------------------------------
# Cluster Centers
# ------------------------------------------

print(
    "\nCluster Centers:"
)

print(
    model.cluster_centers_
)


# ------------------------------------------
# Visualization
# ------------------------------------------

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels,
    cmap="viridis"
)

plt.xlabel(
    "Feature 1"
)

plt.ylabel(
    "Feature 2"
)

plt.title(
    "K-Means Clustering"
)

plt.show()


# K-Means is an unsupervised
# clustering algorithm.
