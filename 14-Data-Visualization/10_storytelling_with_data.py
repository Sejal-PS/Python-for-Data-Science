import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West"]
sales = [320, 450, 280, 390]

highest_region = regions[sales.index(max(sales))]

plt.figure(figsize=(8, 5))

colors = [
    "steelblue" if region != highest_region else "orange"
    for region in regions
]

plt.bar(regions, sales, color=colors)

plt.title("Regional Sales Performance")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.annotate(
    f"Highest: {highest_region}",
    xy=(sales.index(max(sales)), max(sales)),
    xytext=(0, 20),
    textcoords="offset points",
    ha="center"
)

plt.tight_layout()
plt.show()

print(f"Observation: {highest_region} has the highest sales.")
