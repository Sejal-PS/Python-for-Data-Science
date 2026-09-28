import pandas as pd

data = {
    "Channel": ["Email", "Social", "Email", "Search", "Social"],
    "Visitors": [1000, 1500, 1200, 1800, 1600],
    "Conversions": [80, 90, 100, 150, 110]
}

df = pd.DataFrame(data)

df["Conversion_Rate"] = (
    df["Conversions"] / df["Visitors"] * 100
)

print(df)

print("\nAverage conversion rate:")
print(df["Conversion_Rate"].mean())

print("\nBest channel:")
print(
    df.groupby("Channel")["Conversion_Rate"]
    .mean()
    .idxmax()
)
