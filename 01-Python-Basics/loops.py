# Python Loops


# -------------------------
# 1. For Loop
# -------------------------

for i in range(1, 6):
    print(i)


# -------------------------
# 2. Loop through a list
# -------------------------

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# -------------------------
# 3. range() with step
# -------------------------

for i in range(0, 11, 2):
    print(i)


# -------------------------
# 4. While Loop
# -------------------------

count = 1

while count <= 5:
    print(count)
    count += 1


# -------------------------
# 5. Break
# -------------------------

for i in range(1, 10):
    if i == 5:
        break

    print(i)


# -------------------------
# 6. Continue
# -------------------------

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# -------------------------
# 7. Nested Loop
# -------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# -------------------------
# 8. Data Science Example
# -------------------------

sales = [1000, 2500, 1800, 4000, 3200]

total_sales = 0

for sale in sales:
    total_sales += sale

print("Total Sales:", total_sales)
