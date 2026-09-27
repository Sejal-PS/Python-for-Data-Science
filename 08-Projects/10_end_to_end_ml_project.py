# End-to-End Machine Learning Project

import pandas as pd

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ==================================================
# 1. Load Dataset
# ==================================================

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target


# ==================================================
# 2. Understand Data
# ==================================================

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nStatistics:")
print(df.describe())


# ==================================================
# 3. Check Missing Values
# ==================================================

print("\nMissing Values:")

print(
    df.isnull().sum()
)


# ==================================================
# 4. Features and Target
# ==================================================

X = df.drop(
    columns=["target"]
)

y = df["target"]


# ==================================================
# 5. Train-Test Split
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==================================================
# 6. Feature Scaling
# ==================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# ==================================================
# 7. Model Training
# ==================================================

model = LogisticRegression(
    max_iter=200
)

model.fit(
    X_train_scaled,
    y_train
)


# ==================================================
# 8. Prediction
# ==================================================

y_pred = model.predict(
    X_test_scaled
)


# ==================================================
# 9. Evaluation
# ==================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "\nAccuracy:",
    accuracy
)


print(
    "\nConfusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


print(
    "\nClassification Report:"
)

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==================================================
# 10. New Prediction
# ==================================================

new_flower = [[
    5.1,
    3.5,
    1.4,
    0.2
]]

new_flower_scaled = scaler.transform(
    new_flower
)

prediction = model.predict(
    new_flower_scaled
)

print(
    "\nPredicted Class:",
    prediction[0]
)

print(
    "Predicted Species:",
    iris.target_names[
        prediction[0]
    ]
)
