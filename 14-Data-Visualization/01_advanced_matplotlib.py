import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 210, 195]

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    months,
    sales,
    marker="o",
    linewidth=2,
    color="steelblue",
    label="Sales"
)

ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.grid(alpha=0.3)
ax.legend()

for x, y in zip(months, sales):
    ax.annotate(str(y), (x, y), xytext=(0, 8),
                textcoords="offset points", ha="center")

plt.tight_layout()
plt.show()
