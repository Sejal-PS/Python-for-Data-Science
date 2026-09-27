# NumPy Broadcasting
# Broadcasting is a feature in NumPy that allows arithmetic operations to be performed on arrays of different but compatible shapes.

""" For example:

import numpy as np
arr = np.array([10, 20, 30])
print(arr + 5)

Internally, NumPy applies the number 5 to every element:

10 + 520 + 530 + 5
Result: [15, 25, 35]

Data Science Example
Suppose we have a sales dataset and a flat tax rate:
sales = np.array([,
    [1500, 2500, 3500]
])

tax_rate = 0.18 """

# tax = sales * tax_rate


import numpy as np

# -------------------------
# 1. Scalar Broadcasting
# -------------------------

arr = np.array([10, 20, 30, 40])

print("Original Array:")
print(arr)

print("\nAdd 5:")
print(arr + 5)

print("\nMultiply by 2:")
print(arr * 2)


# -------------------------
# 2. Broadcasting with 2D Array
# -------------------------

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])

print("\n2D Array:")
print(arr)

print("\nValues:")
print(values)

print("\nAfter Broadcasting:")
print(arr + values)


# -------------------------
# 3. Row-wise Broadcasting
# -------------------------

prices = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = np.array([10, 20, 30])

print("\nPrices:")
print(prices)

print("\nDiscount:")
print(discount)

print("\nPrice after adding values:")
print(prices + discount)


# -------------------------
# 4. Broadcasting with Column
# -------------------------

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

column = np.array([
    [100],
    [200]
])

print("\nOriginal Array:")
print(arr)

print("\nColumn:")
print(column)

print("\nAfter Broadcasting:")
print(arr + column)


# -------------------------
# 5. Broadcasting with Different Shapes
# -------------------------

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30])

print("\nArray A:")
print(a)

print("\nArray B:")
print(b)

print("\nResult:")
print(a + b)


# -------------------------
# 6. Broadcasting in Calculation
# -------------------------

marks = np.array([
    [70, 80, 90],
    [60, 75, 85]
])

bonus = 5

final_marks = marks + bonus

print("\nMarks:")
print(marks)

print("\nBonus:", bonus)

print("\nFinal Marks:")
print(final_marks)


# -------------------------
# 7. Data Science Example
# -------------------------

sales = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 3500]
])

tax_rate = 0.18

tax = sales * tax_rate

final_amount = sales + tax

print("\nSales:")
print(sales)

print("\nTax:")
print(tax)

print("\nFinal Amount:")
print(final_amount)
