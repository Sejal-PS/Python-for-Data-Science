"""
### Feature Transformation

## Learn:
- Log transformation
- Square-root transformation
- Power transformation
- Handling skewed data
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import PowerTransformer

data = {
    "income": [10000, 12000, 15000, 20000, 50000, 150000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Log transformation
df["log_income"] = np.log1p(df["income"])

# Square-root transformation
df["sqrt_income"] = np.sqrt(df["income"])

print("\nTransformed Data:")
print(df)

# PowerTransformer
transformer = PowerTransformer(method="yeo-johnson")

df["power_income"] = transformer.fit_transform(
    df[["income"]]
)

print("\nPower Transformation:")
print(df)

print("\nTransformation can help represent highly skewed numerical features.")
