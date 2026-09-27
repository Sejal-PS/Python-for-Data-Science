# NumPy Practice

import numpy as np


# ==================================================
# Exercise 1 - Create an Array
# ==================================================

numbers = np.array([10, 20, 30, 40, 50])

print("Exercise 1")
print(numbers)


# ==================================================
# Exercise 2 - Array Properties
# ==================================================

print("\nExercise 2")

print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)


# ==================================================
# Exercise 3 - Basic Mathematical Operations
# ==================================================

print("\nExercise 3")

print("Add 10:", numbers + 10)
print("Subtract 5:", numbers - 5)
print("Multiply by 2:", numbers * 2)
print("Divide by 2:", numbers / 2)


# ==================================================
# Exercise 4 - Statistics
# ==================================================

print("\nExercise 4")

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))


# ==================================================
# Exercise 5 - Filtering
# ==================================================

print("\nExercise 5")

print("Numbers greater than 25:")
print(numbers[numbers > 25])


# ==================================================
# Exercise 6 - Create 2D Array
# ==================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nExercise 6")
print(matrix)


# ==================================================
# Exercise 7 - Row and Column Operations
# ==================================================

print("\nExercise 7")

print("Row-wise Sum:")
print(np.sum(matrix, axis=1))

print("Column-wise Sum:")
print(np.sum(matrix, axis=0))

print("Row-wise Mean:")
print(np.mean(matrix, axis=1))

print("Column-wise Mean:")
print(np.mean(matrix, axis=0))


# ==================================================
# Exercise 8 - Reshape
# ==================================================

numbers = np.arange(1, 13)

print("\nExercise 8")

print("Original Array:")
print(numbers)

reshaped = numbers.reshape(3, 4)

print("Reshaped Array:")
print(reshaped)


# ==================================================
# Exercise 9 - Boolean Filtering
# ==================================================

marks = np.array([45, 67, 89, 32, 76, 90, 55, 82])

print("\nExercise 9")

print("All Marks:")
print(marks)

print("Marks >= 60:")
print(marks[marks >= 60])

print("Marks >= 75:")
print(marks[marks >= 75])


# ==================================================
# Exercise 10 - Unique Values
# ==================================================

customer_ids = np.array([
    101, 102, 103, 101, 104, 102, 105
])

print("\nExercise 10")

print("Customer IDs:")
print(customer_ids)

print("Unique Customer IDs:")
print(np.unique(customer_ids))


# ==================================================
# Exercise 11 - Sales Analysis
# ==================================================

sales = np.array([
    1200,
    2500,
    1800,
    4000,
    3200,
    5000
])

print("\nExercise 11")

print("Sales:", sales)

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

print("Sales above 3000:")
print(sales[sales > 3000])


# ==================================================
# Exercise 12 - Broadcasting
# ==================================================

prices = np.array([100, 200, 300, 400])

discount = 10

final_prices = prices - discount

print("\nExercise 12")

print("Original Prices:")
print(prices)

print("Discount:", discount)

print("Final Prices:")
print(final_prices)


# ==================================================
# Exercise 13 - Handling NaN
# ==================================================

data = np.array([10, 20, np.nan, 40, 50])

print("\nExercise 13")

print("Data:")
print(data)

print("NaN values:")
print(np.isnan(data))

print("Mean ignoring NaN:")
print(np.nanmean(data))


# ==================================================
# Exercise 14 - Random Data
# ==================================================

np.random.seed(42)

random_numbers = np.random.randint(1, 100, 10)

print("\nExercise 14")

print("Random Numbers:")
print(random_numbers)

print("Mean:", np.mean(random_numbers))
print("Maximum:", np.max(random_numbers))
print("Minimum:", np.min(random_numbers))


# ==================================================
# Mini Data Science Practice
# ==================================================

print("\nMini Data Science Practice")

student_marks = np.array([
    65, 78, 90, 55, 88,
    72, 95, 60, 84, 70
])

print("Marks:", student_marks)

average = np.mean(student_marks)
highest = np.max(student_marks)
lowest = np.min(student_marks)

passed_students = student_marks[student_marks >= 60]

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Students Marks:", passed_students)
print("Number of Passed Students:", len(passed_students))
