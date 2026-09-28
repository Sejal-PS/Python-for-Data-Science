"""
Principal Component Analysis (PCA)

PCA is a dimensionality reduction technique.

It transforms a dataset with many features
into a smaller number of principal components.
"""

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# --------------------------------------------------
# Standardize Features
# --------------------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# --------------------------------------------------
# Apply PCA
# --------------------------------------------------

pca = PCA(
    n_components=2
)

X_pca = pca.fit_transform(
    X_scaled
)


# --------------------------------------------------
# Explained Variance
# --------------------------------------------------

print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Explained Variance:")
print(
    pca.explained_variance_ratio_.sum()
)


# --------------------------------------------------
# Visualize PCA Components
# --------------------------------------------------

plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y,
    cmap="viridis",
    edgecolor="black"
)

plt.title("Iris Dataset - PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.colorbar(scatter)

plt.tight_layout()
plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Try n_components=3.
# 2. Compare explained variance.
# 3. Plot different combinations of components.
# 4. Apply PCA to another dataset.
