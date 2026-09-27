import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


data = {
    "Area": [
        800,
        1000,
        1200,
        1500,
        1800,
        2000
    ],
    "Bedrooms": [
        2,
        2,
        3,
        3,
        4,
        4
    ],
    "Price": [
        40,
        50,
        60,
        75,
        90,
        100
    ]
}

df = pd.DataFrame(data)

X = df[
    [
        "Area",
        "Bedrooms"
    ]
]

y = df["Price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()

model.fit(
    X_train,
    y_train
)


y_pred = model.predict(
    X_test
)


print("Predictions:")
print(y_pred)

print(
    "\nMAE:",
    mean_absolute_error(
        y_test,
        y_pred
    )
)

print(
    "R2 Score:",
    r2_score(
        y_test,
        y_pred
    )
)


new_house = pd.DataFrame({
    "Area": [1600],
    "Bedrooms": [3]
})

prediction = model.predict(
    new_house
)

print(
    "\nPredicted Price:",
    prediction[0]
)
