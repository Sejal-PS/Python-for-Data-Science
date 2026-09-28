"""
Polynomial Features

Learn:
- Polynomial features
- Interaction features
- Feature expansion
"""

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

data = {
    "area": [500, 750, 1000, 1250, 1500],
    "bedrooms": [1, 2, 2, 3, 4]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms"]]

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)

feature_names = poly.get_feature_names_out(X.columns)

polynomial_df = pd.DataFrame(
    X_poly,
    columns=feature_names
)

print("Original Features:")
print(X)

print("\nPolynomial Features:")
print(polynomial_df)

print("\nPolynomial features can capture nonlinear relationships.")
