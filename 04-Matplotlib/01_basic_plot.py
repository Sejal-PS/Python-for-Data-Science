# Matplotlib - Basic Plot

import matplotlib.pyplot as plt


# -------------------------
# 1. Simple Line Plot
# -------------------------

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.show()


# -------------------------
# 2. Add Title
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()


# -------------------------
# 3. Add X and Y Labels
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# -------------------------
# 4. Add Grid
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 5. Change Line Color
# -------------------------

plt.plot(
    x,
    y,
    color="blue"
)

plt.title("Blue Line")

plt.show()


# -------------------------
# 6. Change Line Style
# -------------------------

plt.plot(
    x,
    y,
    linestyle="--"
)

plt.title("Dashed Line")

plt.show()


# -------------------------
# 7. Change Line Width
# -------------------------

plt.plot(
    x,
    y,
    linewidth=3
)

plt.title("Thick Line")

plt.show()


# -------------------------
# 8. Add Markers
# -------------------------

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot with Markers")

plt.show()


# -------------------------
# 9. Marker + Color + Line
# -------------------------

plt.plot(
    x,
    y,
    color="green",
    linestyle="--",
    marker="o",
    linewidth=2
)

plt.title("Customized Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 10. Figure Size
# -------------------------

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot with Figure Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 11. Multiple Lines
# -------------------------

x = [1, 2, 3, 4, 5]

sales_2024 = [
    100,
    150,
    120,
    180,
    200
]

sales_2025 = [
    120,
    170,
    160,
    210,
    250
]

plt.plot(
    x,
    sales_2024,
    marker="o",
    label="2024"
)

plt.plot(
    x,
    sales_2025,
    marker="o",
    label="2025"
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# -------------------------
# 12. Real Data Science Example
# -------------------------

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    13000,
    18000,
    22000,
    25000
]

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)



## here we can learn the flow or basic MAtplotlib Sturcuture like 

import
  ↓
Data
  ↓
plt.plot()
  ↓
Title
  ↓
X Label
  ↓
Y Label
  ↓
Grid
  ↓
Legend
  ↓
plt.show()


## Basic syntax
plt/.plot(x,y)]plt.show()

## important functions 
plt.plot()
plt.title()
plt.xlabel()
plt.ylabel()
plt.grid()
plt.legend()
plt.figure()
plt.show()


# for plot customize we use 
plt.plot(
    x,
    y,
    color="green",
    linestyle="--",
    marker="o",
    linewidth=2
)

here 
color  → color for line 
linestyle  → type of line
marker     → on every point we get marker symbol
linewidth  → line thickness


plt.show()
