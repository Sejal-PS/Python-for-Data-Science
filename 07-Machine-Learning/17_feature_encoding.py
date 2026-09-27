# Feature Encoding

import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder
)


# ------------------------------------------
# Dataset
# ------------------------------------------

df = pd.DataFrame({
    "City": [
        "Pune",
        "Mumbai",
        "Delhi",
        "Pune"
    ],
    "Gender": [
        "Female",
        "Male",
        "Female",
        "Male"
    ]
})


print(
    "Original Data:"
)

print(
    df
)


# ------------------------------------------
# One-Hot Encoding
# ------------------------------------------

encoded_df = pd.get_dummies(
    df,
    columns=[
        "City",
        "Gender"
    ]
)

print(
    "\nOne-Hot Encoded Data:"
)

print(
    encoded_df
)


# ------------------------------------------
# Label Encoding
# ------------------------------------------

encoder = LabelEncoder()

gender_encoded = encoder.fit_transform(
    df["Gender"]
)

print(
    "\nLabel Encoded Gender:"
)

print(
    gender_encoded
)


# ------------------------------------------
# Important
# ------------------------------------------

# Encoding converts categorical
# values into numerical representation.
#
# One-hot encoding creates separate
# binary columns.
#
# Label encoding assigns numerical
# labels to categories.
