import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Date": [
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05"
    ],
    "Temperature": [
        24,
        26,
        25,
        27,
        28
    ],
    "Rainfall": [
        0,
        2,
        5,
        0,
        1
    ]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(
    df["Date"]
)

print(df)

print(
    "\nAverage Temperature:",
    df["Temperature"].mean()
)

print(
    "\nMaximum Temperature:",
    df["Temperature"].max()
)

print(
    "\nMinimum Temperature:",
    df["Temperature"].min()
)

print(
    "\nTotal Rainfall:",
    df["Rainfall"].sum()
)


plt.plot(
    df["Date"],
    df["Temperature"],
    marker="o"
)

plt.xlabel("Date")
plt.ylabel("Temperature")

plt.title(
    "Temperature Trend"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
