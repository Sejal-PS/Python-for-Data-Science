# NumPy Indexing and Slicing

import numpy as np


# -------------------------
# 1. One-Dimensional Array
# -------------------------

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)


# -------------------------
# 2. Positive Indexing
# -------------------------

print("\nPositive Indexing")

print("First element:", arr[0])
print("Second element:", arr[1])
print("Third element:", arr[2])


# -------------------------
# 3. Negative Indexing
# -------------------------

print("\nNegative Indexing")

print("Last element:", arr[-1])
print("Second Last element:", arr[-2])


# -------------------------
# 4. Slicing
# -------------------------

print("\nSlicing")

print("First three elements:", arr[0:3])
print("Elements from index 2:", arr[2:])
print("Elements before index 4:", arr[:4])


# -------------------------
# 5. Slicing with Step
# -------------------------

print("\nSlicing with Step")

print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])


# -------------------------
# 6. Two-Dimensional Array
# -------------------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(matrix)


# -------------------------
# 7. Accessing Rows and Columns
# -------------------------

print("\nRows and Columns")

print("First row:", matrix[0])
print("Second row:", matrix[1])

print("First column:", matrix[:, 0])
print("Second column:", matrix[:, 1])


# -------------------------
# 8. Accessing Individual Elements
# -------------------------

print("\nIndividual Elements")

print("First element:", matrix[0, 0])
print("Element at row 2, column 3:", matrix[1, 2])


# -------------------------
# 9. 2D Array Slicing
# -------------------------

print("\n2D Slicing")

print(matrix[0:2, 0:2])

print("\nFirst two rows:")
print(matrix[:2, :])

print("\nLast two columns:")
print(matrix[:, 1:])


# -------------------------
# 10. Updating Array Elements
# -------------------------

arr = np.array([10, 20, 30, 40, 50])

arr[0] = 100

print("\nAfter Updating First Element:")
print(arr)


# -------------------------
# 11. Updating Multiple Elements
# -------------------------

arr[1:3] = 200

print("\nAfter Updating Multiple Elements:")
print(arr)


# -------------------------
# 12. Boolean Indexing
# -------------------------

marks = np.array([45, 67, 89, 32, 76, 90])

print("\nMarks:")
print(marks)

print("Marks greater than 60:")
print(marks[marks > 60])

print("Marks greater than or equal to 75:")
print(marks[marks >= 75])


# -------------------------
# 13. Data Science Example
# -------------------------

sales = np.array([1200, 4500, 2300, 6700, 3200, 8900])

print("\nSales Data:")
print(sales)

print("Sales above 5000:")
print(sales[sales > 5000])
