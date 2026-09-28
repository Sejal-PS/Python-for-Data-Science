"""
10 - Principal Component Analysis
---------------------------------
PCA reduces the number of dimensions while preserving
as much variance as possible.
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# Load data
iris = load_iris()

X = iris.data
y = iris.target

# Standardize
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# Explained variance
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

print(
    "\nTotal Explained Variance:",
    pca.explained_variance_ratio_.sum()
)

# Visualization
plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y,
    cmap="viridis"
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Dataset - PCA")

plt.colorbar(scatter, label="Class")

plt.show()
