# NumPy Array Creation

import numpy as np


# -------------------------
# 1. Array from a List
# -------------------------

arr1 = np.array([10, 20, 30, 40, 50])

print("Array from List:")
print(arr1)


# -------------------------
# 2. Array from a Tuple
# -------------------------

arr2 = np.array((10, 20, 30, 40))

print("\nArray from Tuple:")
print(arr2)


# -------------------------
# 3. Two-Dimensional Array
# -------------------------

arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr3)


# -------------------------
# 4. Three-Dimensional Array
# -------------------------

arr4 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array:")
print(arr4)


# -------------------------
# 5. Array of Zeros
# -------------------------

zeros = np.zeros(5)

print("\nZeros:")
print(zeros)


# -------------------------
# 6. 2D Array of Zeros
# -------------------------

zeros_2d = np.zeros((2, 3))

print("\n2D Zeros:")
print(zeros_2d)


# -------------------------
# 7. Array of Ones
# -------------------------

ones = np.ones(5)

print("\nOnes:")
print(ones)


# -------------------------
# 8. Array with a Specific Value
# -------------------------

full_array = np.full((2, 3), 7)

print("\nFull Array:")
print(full_array)


# -------------------------
# 9. arange()
# -------------------------

arr5 = np.arange(1, 10)

print("\narange:")
print(arr5)


# -------------------------
# 10. arange() with Step
# -------------------------

arr6 = np.arange(1, 11, 2)

print("\narange with Step:")
print(arr6)


# -------------------------
# 11. linspace()
# -------------------------

arr7 = np.linspace(0, 10, 5)

print("\nlinspace:")
print(arr7)


# -------------------------
# 12. Array Properties
# -------------------------

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nArray Properties")

print("Array:")
print(arr)

print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
