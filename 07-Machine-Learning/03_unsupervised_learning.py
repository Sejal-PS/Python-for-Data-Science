# Unsupervised Learning

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# ------------------------------------------
# Load Data
# ------------------------------------------

iris = load_iris()

X = iris.data


# ------------------------------------------
# K-Means Clustering
# ------------------------------------------

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X)


# ------------------------------------------
# Cluster Labels
# ------------------------------------------

labels = model.labels_

print("Cluster Labels:")
print(labels)


# ------------------------------------------
# Cluster Centers
# ------------------------------------------

print("\nCluster Centers:")

print(
    model.cluster_centers_
)


# ------------------------------------------
# Unsupervised Learning
# ------------------------------------------

# In unsupervised learning,
# target labels are not provided.
#
# The algorithm tries to find
# patterns or groups in the data.
#
# Examples:
#
# - Customer segmentation
# - Clustering
# - Dimensionality reduction
