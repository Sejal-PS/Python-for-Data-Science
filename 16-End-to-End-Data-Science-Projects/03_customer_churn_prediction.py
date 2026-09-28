import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "Age": [22, 35, 40, 28, 50, 31, 45, 26],
    "MonthlySpend": [20, 50, 80, 30, 100, 45, 90, 25],
    "Churn": [0, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["Age", "MonthlySpend"]]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
