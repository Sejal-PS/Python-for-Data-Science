# Python Dictionaries


# -------------------------
# 1. Creating a Dictionary
# -------------------------

student = {
    "name": "Pallavi",
    "age": 22,
    "marks": 85
}

print("Student:", student)


# -------------------------
# 2. Accessing Values
# -------------------------

print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])


# -------------------------
# 3. Using get()
# -------------------------

print("Name:", student.get("name"))
print("City:", student.get("city"))


# -------------------------
# 4. Adding a New Key-Value
# -------------------------

student["city"] = "Pune"

print("After adding city:", student)


# -------------------------
# 5. Updating a Value
# -------------------------

student["marks"] = 90

print("Updated marks:", student)


# -------------------------
# 6. Removing an Item
# -------------------------

student.pop("age")

print("After removing age:", student)


# -------------------------
# 7. Dictionary Keys and Values
# -------------------------

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# -------------------------
# 8. Loop through Dictionary
# -------------------------

for key, value in student.items():
    print(key, ":", value)


# -------------------------
# 9. Nested Dictionary
# -------------------------

students = {
    "student1": {
        "name": "Samar",
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "marks": 92
    }
}

print("\nNested Dictionary")
print(students["student1"]["name"])
print(students["student2"]["marks"])


# -------------------------
# 10. Data Science Example
# -------------------------

customer = {
    "customer_id": 101,
    "name": "Amit",
    "age": 28,
    "city": "Pune",
    "purchase_amount": 7500.50
}

print("\nCustomer Information")

for key, value in customer.items():
    print(key, ":", value)



## Topic Covered 
Dictionary
Key-Value Pair
Accessing Values
get()
Adding Data
Updating Data
Removing Data
keys()
values()
items()
Looping
Nested Dictionary

