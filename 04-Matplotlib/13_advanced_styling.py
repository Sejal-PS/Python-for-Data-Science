"""
Advanced Styling in Matplotlib

Matplotlib provides many options for customizing
the appearance of charts.
"""

import matplotlib.pyplot as plt


# --------------------------------------------------
# Sample Data
# --------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 35, 30, 45, 50, 65]


# --------------------------------------------------
# Create Figure
# --------------------------------------------------

plt.figure(figsize=(10, 6))


# --------------------------------------------------
# Customized Line Plot
# --------------------------------------------------

plt.plot(
    months,
    sales,
    color="darkblue",
    linewidth=3,
    linestyle="-",
    marker="o",
    markersize=8,
    markerfacecolor="orange",
    markeredgecolor="black",
    label="Sales"
)


# --------------------------------------------------
# Title and Labels
# --------------------------------------------------

plt.title(
    "Monthly Sales Performance",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)


# --------------------------------------------------
# Grid
# --------------------------------------------------

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)


# --------------------------------------------------
# Legend
# --------------------------------------------------

plt.legend(
    loc="upper left",
    fontsize=10
)


# --------------------------------------------------
# Axis Limits
# --------------------------------------------------

plt.ylim(0, 80)


# --------------------------------------------------
# Layout
# --------------------------------------------------

plt.tight_layout()


# --------------------------------------------------
# Display Plot
# --------------------------------------------------

plt.show()


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Change the line color.
# 2. Change the marker style.
# 3. Add a different grid style.
# 4. Change the title font size.
# 5. Change the y-axis limits.
# 6. Add another line to the same chart.
