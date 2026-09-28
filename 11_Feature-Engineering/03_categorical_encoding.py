### Categorical Encoding

## Learn:
- Label Encoding
- One-Hot Encoding
- Ordinal Encoding


import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

data = {
    "city": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"],
    "education": ["Graduate", "Postgraduate", "Graduate", "12th", "Graduate"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Label Encoding
label_encoder = LabelEncoder()

df["city_label"] = label_encoder.fit_transform(df["city"])

print("\nLabel Encoding:")
print(df)

# One-Hot Encoding
one_hot = pd.get_dummies(df["city"], prefix="city", dtype=int)

print("\nOne-Hot Encoding:")
print(one_hot)

# Ordinal Encoding
education_order = [["12th", "Graduate", "Postgraduate"]]

ordinal_encoder = OrdinalEncoder(categories=education_order)

df["education_encoded"] = ordinal_encoder.fit_transform(
    df[["education"]]
)

print("\nOrdinal Encoding:")
print(df)

print("\nEncoding choice depends on the meaning of the categorical variable.")
