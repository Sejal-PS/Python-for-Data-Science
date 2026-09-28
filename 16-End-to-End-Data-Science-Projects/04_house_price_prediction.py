import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "Area": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 5],
    "Price": [40, 50, 62, 70, 80, 95, 110, 125]
}

df = pd.DataFrame(data)

X = df[["Area", "Bedrooms"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
