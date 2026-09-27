# Python Lists


# -------------------------
# 1. Creating a List
# -------------------------

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


# -------------------------
# 2. Accessing List Elements
# -------------------------

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# -------------------------
# 3. List Slicing
# -------------------------

print("First two fruits:", fruits[0:2])


# -------------------------
# 4. Adding Elements
# -------------------------

fruits.append("Grapes")

print("After append:", fruits)


# -------------------------
# 5. Insert Element
# -------------------------

fruits.insert(1, "Pineapple")

print("After insert:", fruits)


# -------------------------
# 6. Remove Element
# -------------------------

fruits.remove("Banana")

print("After remove:", fruits)


# -------------------------
# 7. Pop Element
# -------------------------

removed_fruit = fruits.pop()

print("Removed:", removed_fruit)
print("After pop:", fruits)


# -------------------------
# 8. Change Element
# -------------------------

fruits[0] = "Watermelon"

print("After update:", fruits)


# -------------------------
# 9. List Length
# -------------------------

print("Number of fruits:", len(fruits))


# -------------------------
# 10. Loop through List
# -------------------------

for fruit in fruits:
    print(fruit)


# -------------------------
# 11. Sorting
# -------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Sorted numbers:", numbers)


# -------------------------
# 12. Data Science Example
# -------------------------

sales = [1000, 2500, 1800, 4000, 3200]

print("Sales:", sales)
print("Total Sales:", sum(sales))
print("Maximum Sales:", max(sales))
print("Minimum Sales:", min(sales))
print("Average Sales:", sum(sales) / len(sales))



#3 concepts covered 
List creation
Indexing
Negative indexing
Slicing
append()
insert()
remove()
pop()
Update
len()
Loop
sort()
sum()
max()
min()

