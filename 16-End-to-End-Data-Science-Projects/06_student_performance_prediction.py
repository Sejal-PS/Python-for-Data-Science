import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Score": [45, 50, 55, 62, 70, 78, 85, 92]
}

df = pd.DataFrame(data)

X = df[["StudyHours", "Attendance"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
