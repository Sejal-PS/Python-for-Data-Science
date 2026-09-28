import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range("2025-01-01", periods=12, freq="ME")
sales = [100, 120, 115, 140, 150, 160, 155, 180, 190, 185, 210, 225]

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Sales"], marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
