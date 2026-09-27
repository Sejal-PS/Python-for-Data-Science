# Python Sets


# -------------------------
# 1. Creating a Set
# -------------------------

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# -------------------------
# 2. Duplicate Values
# -------------------------

numbers = {10, 20, 20, 30, 30, 40}

print("Set with duplicates:", numbers)


# -------------------------
# 3. Adding an Element
# -------------------------

numbers.add(50)

print("After add:", numbers)


# -------------------------
# 4. Adding Multiple Elements
# -------------------------

numbers.update([60, 70, 80])

print("After update:", numbers)


# -------------------------
# 5. Removing an Element
# -------------------------

numbers.remove(20)

print("After remove:", numbers)


# -------------------------
# 6. Discard
# -------------------------

numbers.discard(100)

print("After discard:", numbers)


# -------------------------
# 7. Membership Testing
# -------------------------

print(30 in numbers)
print(100 in numbers)


# -------------------------
# 8. Set Operations
# -------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


# Union
print("Union:", set_a | set_b)


# Intersection
print("Intersection:", set_a & set_b)


# Difference
print("Difference:", set_a - set_b)


# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)


# -------------------------
# 9. Data Science Example
# -------------------------

customer_ids = [101, 102, 103, 101, 104, 102, 105]

unique_customer_ids = set(customer_ids)

print("\nCustomer IDs:", customer_ids)
print("Unique Customer IDs:", unique_customer_ids)
print("Number of Unique Customers:", len(unique_customer_ids))






## concepts covered 
Set
Unique values
add()
update()
remove()
discard()
in
Union
Intersection
Difference
Symmetric Difference

