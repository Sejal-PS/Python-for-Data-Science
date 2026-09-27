# Python Operators


# -------------------------
# 1. Arithmetic Operators
# -------------------------

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# -------------------------
# 2. Comparison Operators
# -------------------------

x = 10
y = 20

print("\nComparison Operators")

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


# -------------------------
# 3. Logical Operators
# -------------------------

age = 25
salary = 50000

print("\nLogical Operators")

print(age > 18 and salary > 30000)
print(age > 30 or salary > 30000)
print(not(age > 18))


# -------------------------
# 4. Assignment Operators
# -------------------------

number = 10

number += 5
print("\nAfter += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)


# -------------------------
# 5. Membership Operators
# -------------------------

skills = ["Python", "NumPy", "Pandas"]

print("\nMembership Operators")

print("Python" in skills)
print("Java" in skills)
print("Java" not in skills)


# -------------------------
# 6. Identity Operators
# -------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators")

print(a is b)
print(a is c)
print(a is not c)


## covered operators 
Arithmetic
+
-
*
/
//
%
**

Comparison
==
!=
>
<
>=
<=

Logical
and
or
not

Assignment
=
+=
-=
*=
/=

Membership
in
not in

Identity
is
is not

