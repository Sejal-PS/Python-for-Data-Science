# NumPy Statistics

import numpy as np


# -------------------------
# 1. Sample Data
# -------------------------

data = np.array([10, 20, 30, 40, 50])

print("Data:")
print(data)


# -------------------------
# 2. Mean
# -------------------------

mean = np.mean(data)

print("\nMean:", mean)


# -------------------------
# 3. Median
# -------------------------

median = np.median(data)

print("Median:", median)


# -------------------------
# 4. Minimum and Maximum
# -------------------------

minimum = np.min(data)
maximum = np.max(data)

print("Minimum:", minimum)
print("Maximum:", maximum)


# -------------------------
# 5. Sum
# -------------------------

total = np.sum(data)

print("Sum:", total)


# -------------------------
# 6. Standard Deviation
# -------------------------

std = np.std(data)

print("Standard Deviation:", std)


# -------------------------
# 7. Variance
# -------------------------

variance = np.var(data)

print("Variance:", variance)


# -------------------------
# 8. Percentiles
# -------------------------

print("\nPercentiles")

print("25th Percentile:", np.percentile(data, 25))
print("50th Percentile:", np.percentile(data, 50))
print("75th Percentile:", np.percentile(data, 75))


# -------------------------
# 9. Statistics on 2D Array
# -------------------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(matrix)

print("\nMean of all values:", np.mean(matrix))

print("Mean column-wise:", np.mean(matrix, axis=0))

print("Mean row-wise:", np.mean(matrix, axis=1))


# -------------------------
# 10. Sum using Axis
# -------------------------

print("\nSum column-wise:")
print(np.sum(matrix, axis=0))

print("\nSum row-wise:")
print(np.sum(matrix, axis=1))


# -------------------------
# 11. Handling Missing Values
# -------------------------

data_with_nan = np.array([10, 20, np.nan, 40, 50])

print("\nData with NaN:")
print(data_with_nan)

print("Is NaN:")
print(np.isnan(data_with_nan))

print("Mean including NaN:")
print(np.mean(data_with_nan))

print("Mean ignoring NaN:")
print(np.nanmean(data_with_nan))


# -------------------------
# 12. Data Science Example
# -------------------------

marks = np.array([65, 78, 90, 55, 88, 72, 95, 60])

print("\nStudent Marks:")
print(marks)

print("Average Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))

print("Students scoring above 75:")
print(marks[marks > 75])



## 
axis=0 → column-wise
axis=1 → row-wise



