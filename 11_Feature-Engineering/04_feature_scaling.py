### Feature Scaling

## Learn:
- StandardScaler
- MinMaxScaler
- RobustScaler
- Why scaling is useful


import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

data = {
    "age": [20, 25, 30, 35, 40],
    "income": [20000, 40000, 60000, 80000, 100000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

features = df[["age", "income"]]

# Standardization
standard_scaler = StandardScaler()
standardized = standard_scaler.fit_transform(features)

print("\nStandardScaler:")
print(standardized)

# Min-Max Scaling
minmax_scaler = MinMaxScaler()
minmax = minmax_scaler.fit_transform(features)

print("\nMinMaxScaler:")
print(minmax)

# Robust Scaling
robust_scaler = RobustScaler()
robust = robust_scaler.fit_transform(features)

print("\nRobustScaler:")
print(robust)

print("\nScaling is especially important for distance-based and gradient-based algorithms.")
