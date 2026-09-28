# Python Conditional Statements

# 1. Simple if statement
age = 25

if age >= 18:
    print("Eligible")
    
# -------------------------
# 2. if-else statement

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# -------------------------
# 3. if-elif-else


marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)


# -------------------------
# 4. Multiple conditions

age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Condition satisfied")
else:
    print("Condition not satisfied")


# -------------------------
# 5. Nested if


age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")


# -------------------------
# 6. Data Science Example


customer_age = 35
purchase_amount = 7500

if purchase_amount >= 10000:
    discount = 20
elif purchase_amount >= 5000:
    discount = 10
else:
    discount = 0

print("Customer Age:", customer_age)
print("Purchase Amount:", purchase_amount)
print("Discount:", discount, "%")

# -------------------------

## Concepts covered 
if
if-else
if-elif-else
multiple conditions
nested if
and
