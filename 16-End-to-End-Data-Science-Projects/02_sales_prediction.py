import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "Advertising": [10, 20, 30, 40, 50, 60, 70, 80],
    "Sales": [25, 35, 45, 52, 65, 72, 80, 92]
}

df = pd.DataFrame(data)

X = df[["Advertising"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
