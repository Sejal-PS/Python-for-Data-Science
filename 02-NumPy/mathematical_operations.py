# NumPy Mathematical Operations

import numpy as np


# -------------------------
# 1. Basic Arithmetic
# -------------------------

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)

print("\nPower:")
print(a ** 2)


# -------------------------
# 2. Scalar Operations
# -------------------------

arr = np.array([10, 20, 30, 40])

print("\nScalar Operations")

print("Add 5:", arr + 5)
print("Subtract 5:", arr - 5)
print("Multiply by 2:", arr * 2)
print("Divide by 2:", arr / 2)


# -------------------------
# 3. Mathematical Functions
# -------------------------

numbers = np.array([1, 4, 9, 16, 25])

print("\nMathematical Functions")

print("Square Root:", np.sqrt(numbers))
print("Absolute:", np.abs(numbers))
print("Exponential:", np.exp(numbers))
print("Log:", np.log(numbers))


# -------------------------
# 4. Aggregate Functions
# -------------------------

data = np.array([10, 20, 30, 40, 50])

print("\nAggregate Functions")

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))


# -------------------------
# 5. Rounding Functions
# -------------------------

values = np.array([1.234, 2.567, 3.891, 4.456])

print("\nRounding Functions")

print("Round:", np.round(values))
print("Floor:", np.floor(values))
print("Ceiling:", np.ceil(values))


# -------------------------
# 6. Absolute Values
# -------------------------

values = np.array([-10, -20, 30, -40])

print("\nAbsolute Values:")
print(np.abs(values))


# -------------------------
# 7. Data Science Example
# -------------------------

sales = np.array([1200, 2500, 1800, 4000, 3200])

total_sales = np.sum(sales)
average_sales = np.mean(sales)
maximum_sales = np.max(sales)
minimum_sales = np.min(sales)

print("\nSales Analysis")

print("Sales:", sales)
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)



## covered Basic Operation slike + ,- ,* ,/,** 

## NumPy mathematical functions
np.sqrt()
np.abs()
np.exp()
np.log()

## Statistical/aggregate functions
np.sum()
np.mean()
np.median()
np.min()
np.max()
np.std()
np.var()

## Rounding
np.round()
np.floor()
np.ceil()



