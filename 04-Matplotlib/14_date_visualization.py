"""
Date and Time Visualization with Matplotlib

Matplotlib can be used to visualize data
that contains dates and time.
"""

import matplotlib.pyplot as plt
from datetime import datetime


# --------------------------------------------------
# Date Data
# --------------------------------------------------

dates = [
    datetime(2025, 1, 1),
    datetime(2025, 2, 1),
    datetime(2025, 3, 1),
    datetime(2025, 4, 1),
    datetime(2025, 5, 1),
    datetime(2025, 6, 1)
]

sales = [20, 30, 25, 40, 50, 60]


# --------------------------------------------------
# Create Date Plot
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    dates,
    sales,
    marker="o",
    color="green",
    linewidth=2
)


# --------------------------------------------------
# Title and Labels
# --------------------------------------------------

plt.title(
    "Monthly Sales Over Time",
    fontsize=16
)

plt.xlabel("Date")
plt.ylabel("Sales")


# --------------------------------------------------
# Grid
# --------------------------------------------------

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)


# --------------------------------------------------
# Automatic Layout
# --------------------------------------------------

plt.gcf().autofmt_xdate()

plt.tight_layout()


# --------------------------------------------------
# Display
# --------------------------------------------------

plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Create daily temperature data.
# 2. Plot temperature against dates.
# 3. Customize the date labels.
# 4. Add markers and grid.
