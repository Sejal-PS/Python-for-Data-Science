NumPy for Data Science

NumPy stands for Numerical Python.

It is a Python library mainly used for numerical computing and working with arrays.

NumPy is one of the important libraries used in Data Science, Machine Learning, Statistics and Scientific Computing.

1. Why NumPy?

Python lists can store multiple values, but NumPy arrays are designed for numerical operations and are generally more efficient for large numerical data.

Example using Python list:

numbers = [10, 20, 30, 40]

result = []

for number in numbers:
    result.append(number * 2)

print(result)


Using NumPy:

import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers * 2)


NumPy allows us to perform operations on the complete array without writing a loop for every element.

2. Installation

NumPy can be installed using pip.

pip install numpy


To check the installed version:

import numpy as np

print(np.__version__)

3. Import NumPy

The commonly used alias for NumPy is np.

import numpy as np


After importing:

np.array()
np.zeros()
np.ones()
np.arange()

4. NumPy Array

The main object in NumPy is the ndarray, which means N-dimensional array.

An array can contain numerical data in one or more dimensions.

Example:

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)

5. Difference Between List and NumPy Array

Python List:

numbers = [1, 2, 3, 4]

print(numbers * 2)


The result repeats the list.

NumPy Array:

import numpy as np

numbers = np.array([1, 2, 3, 4])

print(numbers * 2)


The result is:

[2 4 6 8]


NumPy performs element-wise numerical operations.

6. Creating NumPy Arrays
6.1 Array from List
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)

6.2 Array from Tuple
arr = np.array((10, 20, 30, 40))

print(arr)

6.3 Two-Dimensional Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)

6.4 Three-Dimensional Array
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr)

7. Important Array Properties

Consider:

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

ndim

Returns the number of dimensions.

print(arr.ndim)


Output:

2

shape

Returns the size of each dimension.

print(arr.shape)


Output:

(2, 3)


It means:

2 rows

3 columns

size

Returns the total number of elements.

print(arr.size)


Output:

6

dtype

Returns the data type of elements.

print(arr.dtype)


Example output:

int64

8. Special Array Creation Functions
zeros()

Creates an array filled with zeros.

arr = np.zeros(5)

print(arr)


Two-dimensional:

arr = np.zeros((2, 3))

print(arr)

ones()

Creates an array filled with ones.

arr = np.ones(5)

print(arr)

full()

Creates an array filled with a specific value.

arr = np.full((2, 3), 7)

print(arr)

arange()

Creates values within a given range.

arr = np.arange(1, 10)

print(arr)


With step:

arr = np.arange(1, 10, 2)

print(arr)

linspace()

Creates evenly spaced values between two numbers.

arr = np.linspace(0, 10, 5)

print(arr)

9. Indexing

Indexing is used to access individual elements.

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])


Output:

10
30
50

10. Two-Dimensional Indexing
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])
print(arr[0, 2])
print(arr[1, 1])


Here:

arr[row, column]

11. Slicing

Slicing is used to extract a portion of an array.

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])


Output:

[20 30 40]


Using step:

print(arr[::2])

12. Two-Dimensional Slicing
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[0:2, 0:2])


The general form is:

array[row_slice, column_slice]

13. Mathematical Operations

NumPy supports element-wise mathematical operations.

import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)

14. Scalar Operations

A single value can be applied to every element.

arr = np.array([10, 20, 30, 40])

print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 2)

15. Universal Functions

NumPy provides many mathematical functions.

arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))


Other examples:

print(np.abs(arr))
print(np.exp(arr))
print(np.log(arr))

16. Aggregate Functions

Aggregate functions are used to summarize numerical data.

data = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))


Important functions:

np.sum()
np.mean()
np.median()
np.min()
np.max()
np.std()
np.var()

17. Median

Median is the middle value of sorted data.

data = np.array([10, 20, 30, 40, 50])

print(np.median(data))

18. Axis

axis is very important when working with 2D arrays.

Consider:

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


Column-wise operation:

print(np.sum(arr, axis=0))


Row-wise operation:

print(np.sum(arr, axis=1))


Remember:

axis=0 → operate down the rows / column-wise result
axis=1 → operate across the columns / row-wise result

19. Reshaping

reshape() changes the shape of an array without changing its data.

arr = np.arange(1, 7)

print(arr)

new_arr = arr.reshape(2, 3)

print(new_arr)


Output:

[[1 2 3]
 [4 5 6]]


The total number of elements must remain the same.

20. Flatten

flatten() converts a multi-dimensional array into a one-dimensional array.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.flatten())

21. Transpose

Transpose changes rows into columns and columns into rows.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)

22. Concatenation

Arrays can be joined using concatenate().

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print(result)

23. Stack

Arrays can also be combined using stacking.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))
print(np.hstack((a, b)))

24. Boolean Indexing

Boolean indexing allows us to filter data based on a condition.

marks = np.array([45, 67, 89, 32, 76, 90])

result = marks[marks >= 60]

print(result)


Output:

[67 89 76 90]


This concept is very useful in Data Science.

25. Where()

np.where() can be used to find positions based on a condition.

marks = np.array([45, 67, 89, 32, 76])

result = np.where(marks >= 60)

print(result)


It can also be used for conditional values:

result = np.where(marks >= 60, "Pass", "Fail")

print(result)

26. Sorting
arr = np.array([50, 20, 40, 10, 30])

print(np.sort(arr))

27. Unique Values

np.unique() returns unique values.

data = np.array([10, 20, 10, 30, 20, 40])

print(np.unique(data))

28. Random Numbers

NumPy provides the random module for generating random data.

import numpy as np

print(np.random.randint(1, 10, 5))


Random decimal values:

print(np.random.rand(5))


Random normal distribution:

print(np.random.randn(5))

29. Random Seed

A seed can be used to generate reproducible random results.

np.random.seed(42)

print(np.random.randint(1, 100, 5))


Running the code again with the same seed produces the same sequence.

30. Copy and View

This is an important concept when working with NumPy arrays.

View

A view shares data with the original array.

arr = np.array([10, 20, 30, 40])

view_arr = arr[1:3]

view_arr[0] = 100

print(arr)


The original array can also be affected.

Copy

A copy creates a separate array.

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)
print(copy_arr)

31. Broadcasting

Broadcasting allows NumPy to perform operations between arrays of compatible shapes.

Example:

arr = np.array([10, 20, 30])

print(arr + 5)


A scalar 5 is applied to every element.

Another example:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

values = np.array([10, 20, 30])

print(arr + values)


Broadcasting is very useful in numerical and Data Science operations.

32. Handling Missing Values

NumPy commonly uses np.nan to represent missing numerical values.

data = np.array([10, 20, np.nan, 40])

print(np.isnan(data))


To calculate the mean while ignoring NaN:

print(np.nanmean(data))


Other useful functions:

np.nansum()
np.nanmin()
np.nanmax()
np.nanmean()

33. Linear Algebra

NumPy also provides functions for linear algebra.

Example:

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.dot(a, b))


Matrix multiplication can also be done using:

print(a @ b)

34. Commonly Used NumPy Functions

Some important functions to remember:

np.array()
np.zeros()
np.ones()
np.full()
np.arange()
np.linspace()

np.reshape()
np.flatten()
np.transpose()

np.sum()
np.mean()
np.median()
np.min()
np.max()
np.std()
np.var()

np.sort()
np.unique()
np.where()

np.concatenate()
np.vstack()
np.hstack()

np.sqrt()
np.abs()
np.exp()
np.log()

np.random.randint()
np.random.rand()
np.random.randn()

np.isnan()
np.nanmean()

np.dot()

35. NumPy in Data Science

NumPy is commonly used as a foundation for numerical work in Data Science.

Typical applications include:

Numerical calculations

Working with arrays and matrices

Statistical calculations

Data preprocessing

Mathematical operations

Linear algebra

Random data generation

Scientific computing

Supporting other Python Data Science libraries

Libraries such as Pandas, Matplotlib and many Machine Learning tools work with or build upon NumPy concepts.

36. Quick Revision
NumPy
  ↓
ndarray
  ↓
Array Creation
  ↓
Indexing & Slicing
  ↓
Mathematical Operations
  ↓
Aggregation
  ↓
Axis
  ↓
Reshaping
  ↓
Broadcasting
  ↓
Boolean Indexing
  ↓
Random
  ↓
Linear Algebra

Official Documentation

NumPy documentation:

https://numpy.org/doc/stable/
