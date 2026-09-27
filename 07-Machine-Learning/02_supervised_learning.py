# Supervised Learning

from sklearn.datasets import load_iris


# ------------------------------------------
# Load Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


print("Features shape:")
print(X.shape)

print("\nTarget shape:")
print(y.shape)


# ------------------------------------------
# Supervised Learning
# ------------------------------------------

# In supervised learning:
#
# Input data (X)
# +
# Known target (y)
# =
# Model learns relationship


print("\nFeature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)


# ------------------------------------------
# Examples
# ------------------------------------------

# Regression:
# Predict house price
#
# Classification:
# Predict whether email is spam
#
# Classification:
# Predict flower species


# ------------------------------------------
# Common Algorithms
# ------------------------------------------

# Linear Regression
# Logistic Regression
# KNN
# Decision Tree
# Random Forest
# Naive Bayes
# SVM
