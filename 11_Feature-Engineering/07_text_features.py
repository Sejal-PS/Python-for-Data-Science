"""
Text Feature Engineering

Learn:
- Character count
- Word count
- Uppercase/lowercase conversion
- Keyword indicators
"""

import pandas as pd

data = {
    "review": [
        "Excellent product and very useful",
        "Good quality product",
        "Poor experience",
        "Excellent service"
    ]
}

df = pd.DataFrame(data)

# Character count
df["character_count"] = df["review"].str.len()

# Word count
df["word_count"] = df["review"].str.split().str.len()

# Lowercase text
df["lowercase_review"] = df["review"].str.lower()

# Keyword feature
df["contains_excellent"] = (
    df["review"].str.lower().str.contains("excellent")
)

print(df)

print("\nSimple text features can be useful for classification and sentiment tasks.")
