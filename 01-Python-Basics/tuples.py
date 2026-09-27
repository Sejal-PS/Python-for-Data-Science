# Python Tuples


# -------------------------
# 1. Creating a Tuple
# -------------------------

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)


# -------------------------
# 2. Accessing Elements
# -------------------------

print("First element:", numbers[0])
print("Last element:", numbers[-1])


# -------------------------
# 3. Tuple Slicing
# -------------------------

print("First three elements:", numbers[0:3])


# -------------------------
# 4. Length of Tuple
# -------------------------

print("Length:", len(numbers))


# -------------------------
# 5. Loop through Tuple
# -------------------------

for number in numbers:
    print(number)


# -------------------------
# 6. Tuple Methods
# -------------------------

values = (10, 20, 10, 30, 10, 40)

print("Count of 10:", values.count(10))
print("Index of 30:", values.index(30))


# -------------------------
# 7. Tuple Unpacking
# -------------------------

student = ("Rahul", 22, 85)

name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# -------------------------
# 8. Data Science Example
# -------------------------

coordinates = (18.5204, 73.8567)

latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)



## Important Note
## List  → Mutable   → can be change
## Tuple → Immutable   → cannot change

# ex 
numbers = (10, 20, 30)

# This will give an error:
# numbers[0] = 100

