# NumPy Reshaping

import numpy as np


# -------------------------
# 1. Original Array
# -------------------------

arr = np.arange(1, 13)

print("Original Array:")
print(arr)


# -------------------------
# 2. Reshape 1D to 2D
# -------------------------

arr_2d = arr.reshape(3, 4)

print("\n3 x 4 Array:")
print(arr_2d)


# -------------------------
# 3. Reshape into 2 x 6
# -------------------------

arr_2x6 = arr.reshape(2, 6)

print("\n2 x 6 Array:")
print(arr_2x6)


# -------------------------
# 4. Reshape using -1
# -------------------------

arr_auto = arr.reshape(3, -1)

print("\nUsing -1:")
print(arr_auto)


# -------------------------
# 5. Check Shape
# -------------------------

print("\nOriginal Shape:", arr.shape)
print("New Shape:", arr_2d.shape)


# -------------------------
# 6. Flatten
# -------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix:")
print(matrix)

flat_array = matrix.flatten()

print("\nFlattened Array:")
print(flat_array)


# -------------------------
# 7. Ravel
# -------------------------

ravel_array = matrix.ravel()

print("\nRavel Array:")
print(ravel_array)


# -------------------------
# 8. Transpose
# -------------------------

print("\nOriginal Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)


# -------------------------
# 9. Resize
# -------------------------

arr = np.array([1, 2, 3, 4, 5, 6])

resized = np.resize(arr, (2, 3))

print("\nResized Array:")
print(resized)


# -------------------------
# 10. Reshape Error Example
# -------------------------

arr = np.arange(1, 7)

# 6 elements cannot be reshaped into 4 x 2
# because 4 * 2 = 8

# arr.reshape(4, 2)


# -------------------------
# 11. Data Science Example
# -------------------------

sales = np.array([
    1000, 1200, 1500,
    1800, 2000, 2200,
    2500, 2700, 3000,
    3200, 3500, 4000
])

monthly_sales = sales.reshape(4, 3)

print("\nMonthly Sales:")
print(monthly_sales)

print("\nMonthly Sales Shape:")
print(monthly_sales.shape)

print("\nTotal Sales:")
print(np.sum(monthly_sales))

print("\nAverage Sales:")
print(np.mean(monthly_sales))




