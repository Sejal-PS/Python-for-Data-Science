# Machine Learning Practice

import pandas as pd


# ==================================================
# Practice 1 - Features and Target
# ==================================================

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Attendance": [60, 65, 70, 80, 85, 90],
    "Marks": [35, 42, 50, 60, 70, 78]
}

df = pd.DataFrame(data)

# Tasks:
#
# 1. Identify features.
# 2. Identify target.
# 3. Create X.
# 4. Create y.


# ==================================================
# Practice 2 - Train Test Split
# ==================================================

# Tasks:
#
# 1. Split the dataset into training and testing.
# 2. Use 80% training data.
# 3. Use 20% testing data.
# 4. Print the shapes.


# ==================================================
# Practice 3 - Linear Regression
# ==================================================

# Use Study_Hours as X
# and Marks as y.
#
# Tasks:
#
# 1. Train LinearRegression.
# 2. Predict marks for 7 study hours.
# 3. Print the prediction.


# ==================================================
# Practice 4 - Multiple Linear Regression
# ==================================================

# Use:
#
# Study_Hours
# Attendance
#
# to predict:
#
# Marks
#
# Tasks:
#
# 1. Train model.
# 2. Predict marks for a new student.


# ==================================================
# Practice 5 - Classification
# ==================================================

from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data

y = iris.target

# Tasks:
#
# 1. Split the data.
# 2. Train Logistic Regression.
# 3. Predict test data.
# 4. Calculate accuracy.


# ==================================================
# Practice 6 - KNN
# ==================================================

# Use Iris dataset.
#
# Tasks:
#
# 1. Train KNN.
# 2. Try K values:
#    3
#    5
#    7
# 3. Compare accuracy.


# ==================================================
# Practice 7 - Decision Tree
# ==================================================

# Use Iris dataset.
#
# Tasks:
#
# 1. Train Decision Tree.
# 2. Predict test data.
# 3. Calculate accuracy.


# ==================================================
# Practice 8 - Random Forest
# ==================================================

# Use Iris dataset.
#
# Tasks:
#
# 1. Train Random Forest.
# 2. Calculate accuracy.
# 3. Display feature importance.


# ==================================================
# Practice 9 - Model Evaluation
# ==================================================

# Use a classification model.
#
# Calculate:
#
# 1. Accuracy
# 2. Precision
# 3. Recall
# 4. F1 Score
# 5. Confusion Matrix


# ==================================================
# Practice 10 - Feature Scaling
# ==================================================

# Create a dataset containing:
#
# Age
# Salary
# Experience
#
# Tasks:
#
# 1. Apply StandardScaler.
# 2. Apply MinMaxScaler.
# 3. Compare the results.


# ==================================================
# Practice 11 - Encoding
# ==================================================

data = pd.DataFrame({
    "City": [
        "Pune",
        "Mumbai",
        "Delhi",
        "Pune"
    ],
    "Gender": [
        "Female",
        "Male",
        "Female",
        "Male"
    ]
})

# Tasks:
#
# 1. Apply one-hot encoding.
# 2. Apply label encoding.
# 3. Compare the results.


# ==================================================
# Practice 12 - K-Means
# ==================================================

# Create customer data containing:
#
# Age
# Annual Income
# Spending Score
#
# Tasks:
#
# 1. Apply K-Means.
# 2. Try different values of K.
# 3. Observe the clusters.
# 4. Visualize the result.


# ==================================================
# Practice 13 - Cross Validation
# ==================================================

# Use Iris dataset.
#
# Tasks:
#
# 1. Apply 5-fold cross validation.
# 2. Calculate scores.
# 3. Calculate mean score.


# ==================================================
# Practice 14 - Pipeline
# ==================================================

# Create a pipeline containing:
#
# StandardScaler
# +
# LogisticRegression
#
# Train and evaluate the pipeline.


# ==================================================
# Practice 15 - Mini Machine Learning Project
# ==================================================

# Build a complete ML workflow:
#
# 1. Load dataset
# 2. Understand dataset
# 3. Separate features and target
# 4. Train-test split
# 5. Preprocess data
# 6. Train model
# 7. Make predictions
# 8. Evaluate model
# 9. Try another model
# 10. Compare results
#
# Document your observations.
