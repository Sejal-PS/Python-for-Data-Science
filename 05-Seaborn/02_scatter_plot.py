Log in
You said:

Explain topic Python for DS - NumPy detailed with defination,uses ,features,installation ,apllication,community document,array creation with numpy, with detaield,basic math opoerations,and all important term which i have naot given here with code and explanation

ChatGPT said:
NumPy for Data Science — Detailed Notes with Code
NumPy (Numerical Python) is one of the most important Python libraries for Data Science, Machine Learning, Scientific Computing, Statistics, and Data Analysis.

Below is a structured guide covering the concepts from basics to important NumPy operations, with explanations and code examples.

1. What is NumPy?
NumPy stands for Numerical Python.

It is an open-source Python library used for:

Numerical calculations

Working with arrays and matrices

Mathematical operations

Statistical calculations

Linear algebra

Random number generation

Scientific computing

Data preprocessing

Supporting other Data Science libraries

The central object in NumPy is the ndarray (N-dimensional array).

Simple example
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

Output:

[10 20 30 40 50]

Here:

np.array()

creates a NumPy array.

2. Why NumPy is Important for Data Science
Python lists can store numbers:

numbers = [10, 20, 30, 40, 50]

But NumPy arrays are designed specifically for efficient numerical computation.

For example:

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)

Output:

[11 22 33]

With normal Python lists:

a = [10, 20, 30]
b = [1, 2, 3]

print(a + b)

Output:

[10, 20, 30, 1, 2, 3]

Python lists concatenate, while NumPy performs element-wise numerical operations.

3. Main Features of NumPy
Important NumPy features include:

1. N-dimensional arrays
NumPy supports:

1D arrays

2D arrays

3D arrays

Higher-dimensional arrays

Example:

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a)

2. Fast numerical computation
NumPy operations are implemented using highly optimized compiled code, making array calculations much faster than many equivalent Python loops.

3. Vectorization
Instead of writing loops:

numbers = [1, 2, 3, 4, 5]

result = []

for x in numbers:
    result.append(x * 2)

print(result)

NumPy allows:

numbers = np.array([1, 2, 3, 4, 5])

print(numbers * 2)

Output:

[ 2  4  6  8 10]

This is called vectorized computation.

4. Broadcasting
NumPy can perform operations between arrays of compatible shapes.

a = np.array([1, 2, 3])

print(a + 10)

Output:

[11 12 13]

The scalar 10 is effectively applied to every element.

5. Mathematical functions
NumPy provides functions such as:

np.sqrt()
np.sin()
np.cos()
np.log()
np.exp()
np.power()

Example:

a = np.array([1, 4, 9])

print(np.sqrt(a))

Output:

[1. 2. 3.]

6. Statistical functions
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()

Example:

data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))
print(np.median(data))
print(np.std(data))

7. Linear algebra
NumPy supports:

Matrix multiplication

Dot product

Transpose

Inverse

Eigenvalues

Determinants

Example:

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a @ b)

4. Installation of NumPy
Using pip
Open Command Prompt / Terminal:

pip install numpy

If you have multiple Python versions:

python -m pip install numpy

or:

python3 -m pip install numpy

Check installation
import numpy as np

print(np.__version__)

Example output:

2.x.x

The exact version depends on what is currently installed.

5. Importing NumPy
The standard convention is:

import numpy as np

np is an alias.

Instead of:

numpy.array()

we write:

np.array()

Example:

import numpy as np

a = np.array([1, 2, 3])

print(a)

6. NumPy Array
An array is a collection of elements arranged in one or more dimensions.

The primary NumPy data structure is:

numpy.ndarray

Example:

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(type(arr))

Output:

[10 20 30 40]
<class 'numpy.ndarray'>

7. Python List vs NumPy Array
Python list
a = [1, 2, 3, 4]

NumPy array
a = np.array([1, 2, 3, 4])

Feature	Python List	NumPy Array
Numerical operations	Less convenient	Very convenient
Speed	Generally slower for numerical arrays	Generally faster
Memory efficiency	Generally higher overhead	More efficient for homogeneous numerical data
Multidimensional data	Possible but less convenient	Built-in
Vectorization	No	Yes
Broadcasting	No	Yes
Mathematical functions	Limited	Extensive

8. Array Creation
There are many ways to create NumPy arrays.

8.1 From a Python list
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)

8.2 From a tuple
a = np.array((10, 20, 30))

print(a)

8.3 2D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a)

Output:

[[1 2 3]
 [4 5 6]]

8.4 3D array
a = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(a)

A 3D array can be thought of as multiple 2D matrices stacked together.

9. Important Array Terms
You should know these terms very well for Data Science.

Dimension
The number of axes in an array.

a = np.array([1, 2, 3])
print(a.ndim)

Output:

1

For a matrix:

a = np.array([
    [1, 2],
    [3, 4]
])

print(a.ndim)

Output:

2

10. Shape
shape tells you the size of each dimension.

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.shape)

Output:

(2, 3)

Meaning:

2 rows
3 columns

11. Size
size gives the total number of elements.

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.size)

Output:

6

12. Data Type — dtype
dtype tells us the type of elements stored in the array.

a = np.array([1, 2, 3, 4])

print(a.dtype)

You might see:

int64

or another integer type depending on your platform.

Example:

a = np.array([1.5, 2.5, 3.5])

print(a.dtype)

13. Item Size
itemsize tells us how many bytes one element occupies.

a = np.array([1, 2, 3])

print(a.itemsize)

The exact result depends on the array's dtype.

14. zeros()
Creates an array filled with zeros.

a = np.zeros(5)

print(a)

Output:

[0. 0. 0. 0. 0.]

2D:

a = np.zeros((3, 4))

print(a)

This creates:

3 rows × 4 columns

15. ones()
Creates an array filled with ones.

a = np.ones(5)

print(a)

Output:

[1. 1. 1. 1. 1.]

2D:

a = np.ones((2, 3))

print(a)

16. full()
Creates an array filled with a specified value.

a = np.full((2, 3), 7)

print(a)

Output:

[[7 7 7]
 [7 7 7]]

17. arange()
Creates evenly spaced values using a step.

a = np.arange(1, 10)

print(a)

Output:

[1 2 3 4 5 6 7 8 9]

Syntax:

np.arange(start, stop, step)

Example:

a = np.arange(0, 20, 2)

print(a)

Output:

[ 0  2  4  6  8 10 12 14 16 18]

The stop value is normally excluded.

18. linspace()
Creates a specified number of evenly spaced values between two endpoints.

a = np.linspace(0, 10, 5)

print(a)

Output:

[ 0.   2.5  5.   7.5 10. ]

Difference:

arange()  → controls the step
linspace() → controls the number of values

19. Identity Matrix — eye()
a = np.eye(3)

print(a)

Output:

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

This is an identity matrix.

20. Random Arrays
NumPy provides random-number functionality through np.random.

Random values
a = np.random.rand(5)

print(a)

Generates five random floating-point values in the interval [0, 1).

Random integers
a = np.random.randint(1, 10, size=5)

print(a)

Possible output:

[4 8 2 9 1]

The exact output changes because the values are random.

21. Random Seed
For reproducible random results:

np.random.seed(42)

a = np.random.randint(1, 100, 5)

print(a)

Using the same seed and algorithm produces the same sequence in the same environment.

Modern NumPy code often uses a dedicated generator:

rng = np.random.default_rng(42)

a = rng.integers(1, 100, size=5)

print(a)

The second approach is generally preferred for new code.

22. Array Indexing
NumPy uses zero-based indexing.

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[2])

Output:

10
30

23. Negative Indexing
a = np.array([10, 20, 30, 40, 50])

print(a[-1])

Output:

50

-1 means the last element.

24. Array Slicing
Syntax:

array[start:stop:step]

Example:

a = np.array([10, 20, 30, 40, 50])

print(a[1:4])

Output:

[20 30 40]

Step
print(a[::2])

Output:

[10 30 50]

25. 2D Array Indexing
Consider:

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

Access row 1, column 2:

print(a[1, 2])

Output:

60

Remember:

a[row, column]

26. Selecting Rows
print(a[0])

Output:

[10 20 30]

27. Selecting Columns
print(a[:, 1])

Output:

[20 50 80]

Meaning:

:  → all rows
1  → column index 1

28. Changing Array Values
a = np.array([10, 20, 30, 40])

a[2] = 100

print(a)

Output:

[ 10  20 100  40]

29. Basic Mathematical Operations
NumPy supports element-wise arithmetic.

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

Addition
print(a + b)

Output:

[12 24 35]

Subtraction
print(a - b)

Multiplication
print(a * b)

Division
print(a / b)

Power
print(a ** 2)

30. Scalar Operations
a = np.array([1, 2, 3, 4])

print(a + 10)
print(a - 10)
print(a * 10)
print(a / 10)

The scalar is applied to every element.

31. Comparison Operations
a = np.array([10, 20, 30, 40])

print(a > 20)

Output:

[False False  True  True]

Other operators:

a < 30
a >= 20
a <= 30
a == 20
a != 20

These produce Boolean arrays.

32. Boolean Indexing
This is extremely important in Data Science.

a = np.array([10, 20, 30, 40, 50])

print(a[a > 25])

Output:

[30 40 50]

The expression:

a > 25

creates a Boolean mask.

That mask is then used to select values.

33. where()
np.where() can be used for conditional selection.

a = np.array([10, 20, 30, 40, 50])

result = np.where(a > 25, 1, 0)

print(result)

Output:

[0 0 1 1 1]

Meaning:

if value > 25 → 1
otherwise     → 0

34. Mathematical Functions
Square root
a = np.array([4, 9, 16])

print(np.sqrt(a))

Square
print(np.square(a))

Absolute value
a = np.array([-10, -5, 3, 8])

print(np.abs(a))

Output:

[10  5  3  8]

Exponential
print(np.exp([1, 2, 3]))

Logarithm
a = np.array([1, 10, 100])

print(np.log(a))

35. Trigonometric Functions
angles = np.array([0, np.pi / 2, np.pi])

print(np.sin(angles))
print(np.cos(angles))

NumPy trigonometric functions use radians.

36. Aggregation Functions
Aggregation reduces multiple values to a summary value.

Consider:

a = np.array([10, 20, 30, 40, 50])

Sum
print(np.sum(a))

Output:

150

Mean
print(np.mean(a))

Output:

30.0

Minimum
print(np.min(a))

Maximum
print(np.max(a))

Standard deviation
print(np.std(a))

Variance
print(np.var(a))

37. argmin() and argmax()
These return the index of the minimum or maximum.

a = np.array([10, 50, 20, 80, 30])

print(np.argmin(a))
print(np.argmax(a))

Output:

0
3

Because:

minimum = 10 → index 0
maximum = 80 → index 3

38. Sorting
a = np.array([50, 10, 40, 20, 30])

print(np.sort(a))

Output:

[10 20 30 40 50]

39. Unique Values
a = np.array([1, 2, 2, 3, 3, 3, 4])

print(np.unique(a))

Output:

[1 2 3 4]

You can also obtain counts:

values, counts = np.unique(a, return_counts=True)

print(values)
print(counts)

40. Reshaping Arrays
Suppose:

a = np.arange(1, 7)

print(a)

Output:

[1 2 3 4 5 6]

Convert it into a 2 × 3 array:

b = a.reshape(2, 3)

print(b)

Output:

[[1 2 3]
 [4 5 6]]

Important:

The number of elements must remain the same.

6 elements
2 × 3 = 6

41. Flattening
Convert a multidimensional array into 1D.

a = np.array([
    [1, 2],
    [3, 4]
])

print(a.flatten())

Output:

[1 2 3 4]

ravel() also returns a flattened array, and where possible it may return a view rather than a copy.

42. Transpose
Transpose changes rows into columns.

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.T)

Output:

[[1 4]
 [2 5]
 [3 6]]

43. Array Concatenation
Two arrays can be joined.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))

print(c)

Output:

[1 2 3 4 5 6]

44. vstack()
Vertical stacking:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))

Output:

[[1 2 3]
 [4 5 6]]

45. hstack()
Horizontal stacking:

print(np.hstack((a, b)))

Output:

[1 2 3 4 5 6]

For 2D arrays, horizontal stacking joins along columns.

46. Splitting Arrays
a = np.array([1, 2, 3, 4, 5, 6])

result = np.split(a, 3)

print(result)

Output:

[array([1, 2]), array([3, 4]), array([5, 6])]

47. Broadcasting
Broadcasting is one of the most important NumPy concepts.

Example:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a + 10)

Output:

[[11 12 13]
 [14 15 16]]

NumPy automatically broadcasts 10 across the array.

Broadcasting with arrays
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)

Output:

[[11 22 33]
 [14 25 36]]

The 1D array is applied across each row.

48. Axis
axis is a very important concept.

Consider:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

axis=0
Operations happen down the rows, producing one result per column.

print(np.sum(a, axis=0))

Output:

[5 7 9]

Because:

column 1: 1 + 4 = 5
column 2: 2 + 5 = 7
column 3: 3 + 6 = 9

axis=1
Operations happen across columns, producing one result per row.

print(np.sum(a, axis=1))

Output:

[ 6 15]

Because:

row 1: 1 + 2 + 3 = 6
row 2: 4 + 5 + 6 = 15

49. Matrix Multiplication
There is an important difference between:

*

and:

@

Element-wise multiplication
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a * b)

Output:

[[ 5 12]
 [21 32]]

Matrix multiplication
print(a @ b)

Output:

[[19 22]
 [43 50]]

50. Dot Product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))

Calculation:

1×4 + 2×5 + 3×6
= 4 + 10 + 18
= 32

51. Linear Algebra
NumPy has a linear algebra module:

np.linalg

Example:

a = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.det(a))

This calculates the determinant.

Matrix inverse
inverse = np.linalg.inv(a)

print(inverse)

Not every matrix has an inverse. Singular matrices do not.

Solving equations
For:

2x + y = 5
x + 3y = 6

we can write:

A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

x = np.linalg.solve(A, b)

print(x)

This is generally preferable to explicitly computing an inverse for solving a linear system.

52. Copy vs View
This is an important NumPy concept.

Copy
A copy creates independent data.

a = np.array([1, 2, 3])

b = a.copy()

b[0] = 100

print(a)
print(b)

Output:

[1 2 3]
[100   2   3]

View
A view can refer to the same underlying data.

a = np.array([1, 2, 3])

b = a.view()

b[0] = 100

print(a)

Depending on the operation, changes through the view can affect the original array because they may share memory.

53. Data Types in NumPy
Common dtypes include:

int8
int16
int32
int64
float32
float64
bool
complex64
complex128

Example:

a = np.array([1, 2, 3], dtype=np.float32)

print(a)
print(a.dtype)

54. Type Conversion
Use .astype():

a = np.array([1.2, 2.5, 3.8])

b = a.astype(int)

print(b)

Output may be:

[1 2 3]

The conversion truncates toward zero for these positive values; it does not perform mathematical rounding.

For rounding:

print(np.round(a))

55. Handling Missing Values
NumPy floating-point arrays can represent missing numeric values with NaN.

a = np.array([10, 20, np.nan, 40])

print(np.isnan(a))

Output:

[False False  True False]

To calculate a mean while ignoring NaN:

print(np.nanmean(a))

Similarly:

np.nansum()
np.nanmin()
np.nanmax()
np.nanstd()

56. Infinity
NumPy supports infinity:

a = np.array([10, np.inf, -np.inf])

print(a)

Check:

print(np.isinf(a))

57. Checking Conditions
any()
Returns True if at least one condition is true.

a = np.array([1, 2, 3, 4])

print(np.any(a > 3))

Output:

True

all()
Returns True if every condition is true.

print(np.all(a > 0))

Output:

True

58. Combining Conditions
Use:

&
|
~

rather than Python's and, or, and not for element-wise NumPy conditions.

Example:

a = np.array([10, 20, 30, 40, 50])

result = a[(a > 20) & (a < 50)]

print(result)

Output:

[30 40]

59. Rounding
a = np.array([1.234, 2.567, 3.891])

print(np.round(a, 2))

Output:

[1.23 2.57 3.89]

Other functions:

np.floor(a)
np.ceil(a)
np.trunc(a)

60. Saving NumPy Arrays
NumPy provides .npy format.

a = np.array([10, 20, 30])

np.save("data.npy", a)

Load:

b = np.load("data.npy")

print(b)

61. Saving Multiple Arrays
You can use .npz:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.savez("arrays.npz", first=a, second=b)

Load:

data = np.load("arrays.npz")

print(data["first"])
print(data["second"])

62. NumPy and Data Science
NumPy is the foundation for many Python Data Science tools.

A common ecosystem looks like:

              Python
                 |
              NumPy
          /      |      \
     pandas   SciPy   Matplotlib
        |
   Data Analysis
        |
   scikit-learn
        |
 Machine Learning

Libraries such as pandas and scikit-learn make extensive use of NumPy concepts and array-based computation.

63. Applications of NumPy
NumPy is used in:

Data Science
For:

Data manipulation

Numerical calculations

Feature preparation

Statistical computations

Machine Learning
For:

Feature matrices

Model calculations

Mathematical transformations

Numerical preprocessing

Scientific Computing
For:

Physics

Chemistry

Engineering

Biology

Research

Image Processing
Images can be represented as arrays.

For example, a grayscale image can conceptually be represented as:

height × width

A color image can commonly be represented as:

height × width × channels

Example:

image = np.zeros((100, 100, 3))

print(image.shape)

Output:

(100, 100, 3)

64. NumPy in Machine Learning
Suppose you have student data:

students = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [90, 95, 92]
])

Rows represent students.

Columns represent subjects.

You can calculate average marks:

average = np.mean(students, axis=1)

print(average)

Output:

[81.66666667 65.         92.33333333]

This is a typical Data Science operation.

65. Practical Data Science Example
Let's create a small dataset:

import numpy as np

sales = np.array([
    100,
    150,
    200,
    120,
    300,
    250
])

Total sales
print(np.sum(sales))

Average sales
print(np.mean(sales))

Highest sales
print(np.max(sales))

Lowest sales
print(np.min(sales))

Sales above 200
print(sales[sales > 200])

This illustrates how NumPy can be used for basic data analysis.

66. Important NumPy Functions Cheat Sheet
Function	Purpose
np.array()	Create array
np.zeros()	Create zeros
np.ones()	Create ones
np.full()	Fill with value
np.arange()	Range with step
np.linspace()	Evenly spaced values
np.eye()	Identity matrix
np.random	Random-number functionality
np.reshape()	Change shape
.flatten()	Flatten array
.ravel()	Flatten/view when possible
.T	Transpose
np.concatenate()	Join arrays
np.vstack()	Vertical stacking
np.hstack()	Horizontal stacking
np.split()	Split array
np.sum()	Sum
np.mean()	Mean
np.median()	Median
np.std()	Standard deviation
np.var()	Variance
np.min()	Minimum
np.max()	Maximum
np.argmin()	Index of minimum
np.argmax()	Index of maximum
np.sort()	Sort
np.unique()	Unique values
np.where()	Conditional selection
np.sqrt()	Square root
np.abs()	Absolute value
np.exp()	Exponential
np.log()	Natural logarithm
np.sin()	Sine
np.cos()	Cosine
np.isnan()	Check NaN
np.isinf()	Check infinity
np.round()	Round values
np.floor()	Floor
np.ceil()	Ceiling
np.dot()	Dot product
np.linalg.solve()	Solve linear system
np.linalg.det()	Determinant
np.linalg.inv()	Matrix inverse

67. Important NumPy Terms to Remember
For Data Science interviews and practical work, understand these terms:

Core concepts
ndarray

Dimension

Axis

Shape

Size

dtype

itemsize

Indexing

Slicing

Boolean indexing

Mask

Vectorization

Broadcasting

Aggregation

Reshaping

Transpose

Flattening

Copy

View

Data type conversion

Random number generation

Linear algebra

Mathematical concepts
Mean

Median

Variance

Standard deviation

Sum

Minimum

Maximum

Dot product

Matrix multiplication

Determinant

Inverse

Eigenvalues/eigenvectors

Data Science concepts
Missing values

NaN

Boolean masks

Feature matrices

Numerical preprocessing

Statistical calculations

68. One Complete Example
Here is a small program combining many concepts:

import numpy as np

# Create student marks
marks = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [90, 95, 92],
    [55, 60, 58]
])

# Basic information
print("Array:")
print(marks)

print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)

# Student averages
student_average = np.mean(marks, axis=1)

print("\nStudent averages:")
print(student_average)

# Subject averages
subject_average = np.mean(marks, axis=0)

print("\nSubject averages:")
print(subject_average)

# Highest mark
print("\nHighest mark:", np.max(marks))

# Lowest mark
print("Lowest mark:", np.min(marks))

# Students with average above 70
print("\nStudents with average above 70:")
print(student_average[student_average > 70])

# Add 5 grace marks
new_marks = marks + 5

print("\nMarks after adding 5:")
print(new_marks)

# Sort all marks
print("\nSorted marks:")
print(np.sort(marks, axis=None))

This single example demonstrates:

ndarray
↓
2D array
↓
shape
↓
axis
↓
mean
↓
max/min
↓
Boolean indexing
↓
broadcasting
↓
sorting

69. NumPy Documentation and Community
For learning NumPy, the official documentation is the most important reference.

NumPy Official Documentation

NumPy User Guide

NumPy Reference

NumPy GitHub Repository

The official documentation contains:

Installation information

Tutorials

User guides

API reference

Array concepts

Broadcasting

Mathematical functions

Random sampling

Linear algebra

Input/output

Developer information

The NumPy community also includes contributors, maintainers, scientific-computing users, researchers, educators, and developers.

70. Recommended Learning Order
If you're learning Python for Data Science, don't try to memorize every NumPy function. Learn the concepts in this order:

1. Python Lists & Tuples
        ↓
2. NumPy Installation
        ↓
3. ndarray
        ↓
4. Array Creation
        ↓
5. ndim / shape / size / dtype
        ↓
6. Indexing
        ↓
7. Slicing
        ↓
8. Boolean Indexing
        ↓
9. Mathematical Operations
        ↓
10. Aggregation
        ↓
11. axis
        ↓
12. Reshape
        ↓
13. Broadcasting
        ↓
14. Sorting & Searching
        ↓
15. Copy vs View
        ↓
16. Missing Values
        ↓
17. Random Numbers
        ↓
18. Linear Algebra
        ↓
19. NumPy + Pandas
        ↓
20. NumPy + Machine Learning

The 10 concepts you should especially master
If your goal is Data Science, concentrate particularly on:

70. Recommended Learning Order
ndarray

shape and ndim

Indexing and slicing

Boolean masking

Vectorization

Broadcasting

axis

Aggregation functions

Reshaping

Copy vs view

Once these are clear, NumPy becomes much easier, and moving into Pandas, Matplotlib, SciPy, and Scikit-learn will be considerably smoother.



You said:

how to add this in github

ChatGPT said:
Yes. If you want to put these NumPy notes + code examples into GitHub, the easiest approach is to create a repository and save the notes as a README.md or as a separate Markdown file.

1. Create a GitHub repository
Go to GitHub and log in.

Then:

Click + → New repository

Give it a name, for example:

python-for-data-science

Add a description:

My Python for Data Science learning notes and practice programs.

Select Public if you want others/recruiters to see it.

Check Add a README file

Click Create repository

2. Recommended GitHub folder structure
For learning Data Science, I recommend organizing your repository like this:

python-for-data-science/
│
├── README.md
│
├── 01-Python-Basics/
│   ├── variables.py
│   ├── data_types.py
│   ├── lists.py
│   └── functions.py
│
├── 02-NumPy/
│   ├── README.md
│   ├── array_creation.py
│   ├── indexing_slicing.py
│   ├── mathematical_operations.py
│   ├── statistics.py
│   ├── reshaping.py
│   ├── broadcasting.py
│   └── practice.py
│
├── 03-Pandas/
│   └── ...
│
├── 04-Matplotlib/
│   └── ...
│
└── 05-Projects/
    └── ...

This looks much better than putting everything into one huge file.

3. Put your NumPy notes in README.md
Inside your repository:

Add file → Create new file

Name it:

02-NumPy/README.md

Then paste your NumPy notes into it.

GitHub automatically renders Markdown.

For example, instead of plain text:

What is NumPy?
NumPy is Numerical Python...

use Markdown:

# NumPy for Data Science

## What is NumPy?

NumPy stands for Numerical Python.

It is a Python library used for numerical computing,
arrays, mathematical operations, statistics and linear algebra.

## Installation

```bash
pip install numpy

Import NumPy
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)

Array Properties
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)


GitHub will display the Python code with syntax highlighting.

---

# 4. Don't put all the code only in README

For a good learning repository, keep **notes and executable code separate**.

For example:

### `02-NumPy/README.md`

Contains explanations:

```markdown
# NumPy

## Array Creation

NumPy arrays can be created using `np.array()`.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)


### `02-NumPy/array_creation.py`

Contains the actual Python code:

```python
import numpy as np

# Array from list
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Array of zeros
arr2 = np.zeros(5)
print(arr2)

# Array of ones
arr3 = np.ones(5)
print(arr3)

# Range
arr4 = np.arange(1, 10)
print(arr4)

# Evenly spaced values
arr5 = np.linspace(0, 10, 5)
print(arr5)

This is much easier to maintain.

5. Add your NumPy topics as separate files
I'd organize the material you just learned like this:

array_creation.py
import numpy as np

a = np.array([1, 2, 3, 4])

b = np.zeros((2, 3))

c = np.ones((3, 3))

d = np.arange(1, 10, 2)

e = np.linspace(0, 10, 5)

print(a)
print(b)
print(c)
print(d)
print(e)

indexing_slicing.py
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[::2])

mathematical_operations.py
import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

statistics.py
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))

reshaping.py
import numpy as np

arr = np.arange(1, 7)

print("Original:")
print(arr)

matrix = arr.reshape(2, 3)

print("Reshaped:")
print(matrix)

print("Transpose:")
print(matrix.T)

print("Flatten:")
print(matrix.flatten())

broadcasting.py
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr + 10)

values = np.array([10, 20, 30])

print(arr + values)

6. Add a main README.md
Your main repository README should explain what the entire repository is about.

For example:

GitHub Repository README


Python for Data Science
My learning repository for Python, NumPy, Pandas, Data Visualization, Statistics, and Machine Learning.

📚 Topics
Python Basics

NumPy

Pandas

Matplotlib

Seaborn

Statistics

Machine Learning

Data Science Projects

📁 Repository Structure
python-for-data-science/
│
├── 01-Python-Basics/
├── 02-NumPy/
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Statistics/
├── 06-Machine-Learning/
└── 07-Projects/

🔢 NumPy
NumPy is a Python library for numerical computing and is an important foundation of the Python Data Science ecosystem.

Topics Covered
NumPy installation

NumPy arrays

Array creation

ndim

shape

size

dtype

Indexing

Slicing

Boolean indexing

Mathematical operations

Statistical operations

Broadcasting

Vectorization

Reshaping

Transpose

Concatenation

Splitting

Sorting

Random numbers

Missing values

Linear algebra

Copy vs View

🛠️ Installation
pip install numpy

🚀 Basic Example
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

📖 Official Documentation
NumPy Documentation

🎯 Goal
The goal of this repository is to document my Data Science learning journey through notes, examples, exercises, and projects.

7. Upload using GitHub website
If you're a beginner, you don't even need Git commands initially.

Inside your repository:

Add file → Upload files

Upload:

02-NumPy/
    README.md
    array_creation.py
    indexing_slicing.py
    mathematical_operations.py
    statistics.py
    reshaping.py
    broadcasting.py

Then enter a commit message:

Add NumPy notes and examples

Click:

Commit changes

Done. ✅

8. Better method: Git + VS Code
Once you start working with many files, I recommend using Git locally.

Install Git from Git official website.

Then clone your repository:

git clone YOUR_REPOSITORY_URL

Go inside it:

cd python-for-data-science

Create your NumPy folder:

mkdir 02-NumPy

Create your files using VS Code.

Then check what changed:

git status

Add the files:

git add .

Commit:

git commit -m "Add NumPy notes and examples"

Push to GitHub:

git push

9. Your GitHub workflow
Once you've learned this, your normal workflow will be:

Learn NumPy concept
       ↓
Write notes
       ↓
Write Python example
       ↓
Test the code
       ↓
Save in GitHub repository
       ↓
git add .
       ↓
git commit
       ↓
git push

For example:

git add .
git commit -m "Add NumPy array operations"
git push

10. One important recommendation
Since this is a Data Science learning repository, don't just copy the notes I gave you.

Use them as your reference, then add your own:

📖 Theory
💻 Code
📝 Your explanation
🧪 Practice questions
📊 Mini projects
❌ Mistakes/bugs you encountered
✅ What you learned

That will turn the GitHub repository into a genuine Data Science portfolio + learning journal, rather than just a collection of copied notes.



You said:

ek ek karatke batawo mai kar rahi hu

ChatGPT said:
Bilkul 👍 Hum ek-ek step karenge. Aap pehle step complete karo, phir mujhe “done” bolo. Uske baad main sirf next step bataungi.

Step 1️⃣ — GitHub open karo
GitHub par jao aur Login karo.

Login ho jaaye to mujhe “done” bolo.



You said:

github open kkiya but ias topic la separate repositiory craete kara ka konte folder create karun tyat karu

ChatGPT said:
Haan 👍 Agar tum Python for Data Science properly learn kar rahi ho, toh har topic ke liye separate repository banana zaroori nahi hai.

Main suggest karungi ki ek main repository banao aur uske andar folders rakho.

Example:

Python-for-Data-Science/
│
├── 01-Python-Basics/
├── 02-NumPy/
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Seaborn/
├── 06-Statistics/
└── 07-Machine-Learning/

Abhi hum sirf NumPy kar rahe hain, isliye:

Python-for-Data-Science/
└── 02-NumPy/

Abhi Step 2️⃣
GitHub par New repository button dabao.

Repository name mein likho:

Python-for-Data-Science

Aur Public select kar sakti ho agar portfolio ke liye rakhna hai.

Abhi repository create kar do.
Create ho jaaye toh mujhe “done” bolo. Phir main next step bataungi.



You said:

done

ChatGPT said:
Perfect! 👍 Ab next step.

Step 3️⃣ — 02-NumPy folder banao
Tum abhi apni Python-for-Data-Science repository ke main page par hogi.

Add file par click karo.

Create new file select karo.

File name ke box mein exactly likho:

02-NumPy/README.md

⚠️ Dhyan do: / lagane se GitHub 02-NumPy naam ka folder automatically bana dega, aur uske andar README.md file banegi.

Abhi kuch content likhne ki zarurat nahi hai.

Neeche Commit changes par click karo.

Commit message mein rehne do:

Create NumPy folder

Commit changes click karo.

Bas itna karo. Ho jaaye toh “done” bolo.



You said:

Python-for-Data-Science/
│
├── 01-Python-Basics/
├── 02-NumPy/
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Seaborn/
├── 06-Statistics/
└── 07-Machine-Learning/
he sarv karayache aahe ek ek karun sanga

ChatGPT said:
हो 👍 आपण सगळे 7 folders बनवू. पण एकावेळी एकच step करू.

आत्ता आपण 01-Python-Basics पासून सुरू करू.

Step 1 — 01-Python-Basics folder बनवा
तुमच्या Python-for-Data-Science repository मध्ये:

Add file वर click करा.

Create new file निवडा.

File name मध्ये हे exactly लिहा:

01-Python-Basics/README.md

खाली Commit changes वर click करा.

Commit message:

Add Python Basics folder

पुन्हा Commit changes click करा.

बस. ✅

हे झाल्यावर मला फक्त “done” म्हणा. मग आपण 02-NumPy folder बनवू.



You said:

tyat content kay lihayache code kay lihayache te purn tu sang ase samaj tu sejal mahun maze github ready karat aahe

ChatGPT said:
हो Sejal 👍 आता समजलं. आपण फक्त folders बनवणार नाही, तर मी तुझं complete GitHub Data Science learning repository step-by-step तयार करून देईन — कुठे काय लिहायचं, कोणता code ठेवायचा, README मध्ये काय content ठेवायचं, सगळं मी सांगते.

आपण एकदम सुरुवातीपासून professional structure ठेवू.

आपला Final GitHub Structure
Python-for-Data-Science/
│
├── README.md
│
├── 01-Python-Basics/
│   ├── README.md
│   ├── variables.py
│   ├── data_types.py
│   ├── operators.py
│   ├── conditional_statements.py
│   ├── loops.py
│   ├── functions.py
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   └── sets.py
│
├── 02-NumPy/
│   ├── README.md
│   ├── array_creation.py
│   ├── indexing_slicing.py
│   ├── mathematical_operations.py
│   ├── statistics.py
│   ├── reshaping.py
│   ├── broadcasting.py
│   └── practice.py
│
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Seaborn/
├── 06-Statistics/
└── 07-Machine-Learning/

पण आपण हे सगळं एकदम करणार नाही. एक folder complete → मग पुढचा.

आता Step 1: 01-Python-Basics
तुझ्या GitHub मध्ये Python-for-Data-Science repository उघड.

आपण आधी 01-Python-Basics folder तयार करू.

Create new file मध्ये हे लिही:
01-Python-Basics/README.md

आता README मध्ये हा पूर्ण content paste कर:

Python Basics README


Python Basics
This folder contains my Python fundamentals notes and practice programs as part of my Data Science learning journey.

Topics Covered
Variables

Data Types

Input and Output

Operators

Conditional Statements

Loops

Functions

Lists

Tuples

Dictionaries

Sets

1. Variables
A variable is a name used to store a value.

name = "Sejal"
age = 21
height = 5.4

print(name)
print(age)
print(height)

2. Data Types
Python provides different built-in data types.

name = "Sejal"       # String
age = 21             # Integer
marks = 85.5         # Float
is_student = True    # Boolean

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))

3. Input and Output
The input() function is used to take input from the user.

name = input("Enter your name: ")

print("Hello", name)

4. Operators
Arithmetic Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

Logical Operators
age = 21

print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not(age > 18))

5. Conditional Statements
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

6. For Loop
for i in range(1, 6):
    print(i)

7. While Loop
i = 1

while i <= 5:
    print(i)
    i += 1

8. Functions
A function is a reusable block of code.

def greet(name):
    return "Hello " + name

message = greet("Sejal")

print(message)

9. Lists
Lists are ordered and mutable collections.

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])

fruits.append("Orange")

print(fruits)

10. Tuples
Tuples are ordered and immutable collections.

numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[0])

11. Dictionaries
Dictionaries store data in key-value pairs.

student = {
    "name": "Sejal",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student["marks"])

12. Sets
Sets store unique values.

numbers = {1, 2, 2, 3, 4, 4}

print(numbers)

Goal
The goal of this section is to build a strong Python foundation before moving to NumPy, Pandas, Data Visualization, Statistics, and Machine Learning.

आता काय करायचं?
हा content README.md मध्ये paste कर → Commit changes कर.

फक्त हे एक काम कर. झालं की मला done सांग.

मग आपण त्याच 01-Python-Basics folder मध्ये पहिली actual Python file — variables.py — तयार करू आणि त्यात काय code टाकायचा ते मी तुला देईन.



You said:

sarv itake professionally nako lihu ,me ek data sciencet trainer aani humna aahe tyanusar lihi

ChatGPT said:
हो, समजलं. 👍
आपण beginner/student style मध्ये ठेवू — खूप corporate/professional portfolio सारखं नाही. तू Data Science शिकत आहेस आणि GitHub वर तुझे notes + practice code ठेवतेयस, असं दिसलं पाहिजे.

आणि एक correction: आपण आधी सांगितलेले सगळे folders लगेच बनवायचे नाहीत. एक topic पूर्ण करू, मग पुढचा.

आता 01-Python-Basics/README.md मध्ये हेच content ठेव:
Python Basics Notes


Python Basics
These are my Python notes and practice programs for Data Science.

Topics
Variables

Data Types

Input and Output

Operators

If-Else

Loops

Functions

List

Tuple

Dictionary

Set

Variables
A variable is used to store a value.

name = "Sejal"
age = 21
marks = 85.5

print(name)
print(age)
print(marks)

Data Types
Common Python data types:

String

Integer

Float

Boolean

List

Tuple

Dictionary

Set

Example:

name = "Sejal"
age = 21
marks = 85.5
is_student = True

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))

Input and Output
name = input("Enter your name: ")

print("Hello", name)

Operators
Arithmetic Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

Logical Operators
age = 21

print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not(age > 18))

If-Else
marks = 75

if marks >= 75:
    print("Good")
else:
    print("Need more practice")

For Loop
for i in range(1, 6):
    print(i)

While Loop
i = 1

while i <= 5:
    print(i)
    i += 1

Functions
A function is a reusable block of code.

def greet(name):
    print("Hello", name)

greet("Sejal")

List
A list is used to store multiple values.

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])

fruits.append("Orange")

print(fruits)

Tuple
A tuple is similar to a list but it cannot be changed after creation.

numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[0])

Dictionary
A dictionary stores data in key-value pairs.

student = {
    "name": "Sejal",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student["marks"])

Set
A set stores unique values.

numbers = {1, 2, 2, 3, 4, 4}

print(numbers)

Practice
I will add more Python practice programs and examples in this folder.

आत्ता फक्त हा README तयार करून Commit कर.

झाल्यावर done म्हण. मग आपण variables.py बनवू — त्यात काय code, comments आणि examples ठेवायचे ते मी एकदम सोप्या पद्धतीने देईन.



You said:

me dta science trauiner aahe student nahi

ChatGPT said:
हो, आता clear झालं. 👍 तू Data Science Trainer आहेस, त्यामुळे GitHub हे तुझ्या teaching material / trainer notes / examples म्हणून तयार करूया — student learning diary सारखं नाही.

आपण content simple + teaching-oriented ठेवू. खूप corporate किंवा portfolio language नको.

आपल्या repository ची दिशा
Python-for-Data-Science/
│
├── 01-Python-Basics/
├── 02-NumPy/
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Seaborn/
├── 06-Statistics/
└── 07-Machine-Learning/

प्रत्येक folder मध्ये:

README.md → Trainer notes + explanation + important concepts

.py files → Classroom demonstration/practical code

त्यामुळे 01-Python-Basics/README.md साठी heading अशी ठेवू:
# Python Basics for Data Science

This section covers the Python concepts required for Data Science.

## Topics Covered

- Variables and Data Types
- Input and Output
- Operators
- Conditional Statements
- Loops
- Functions
- Lists
- Tuples
- Dictionaries
- Sets

आत्ता आपण इथेच थांबूया.

जर 01-Python-Basics folder अजून तयार केला नसेल, तर आधी तो तयार कर.

तो folder तयार झाला आहे का?



You said:

basic foilder tayar zala aani var dilelei readme.md pan zale

ChatGPT said:
छान 👍 01-Python-Basics folder आणि त्याचा README.md तयार आहे.

आता एकच पुढचं काम करूया.

Step 2 — variables.py तयार करा
GitHub मध्ये:

01-Python-Basics folder उघडा.

Add file → Create new file वर click करा.

File name लिहा:

variables.py

खालील code जसाच्या तसा paste करा:

# Python Variables

# Variable stores a value
name = "Sejal"
age = 30
salary = 50000.50
is_trainer = True

print(name)
print(age)
print(salary)
print(is_trainer)

थोडं practical Data Science exampleही ठेवू:
# Student Data

student_name = "Rahul"
student_age = 22
student_marks = 85.5

print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)

हे दोन examples एकाच variables.py file मध्ये ठेवा.

खाली Commit changes करा.

Commit message:

Add Python variables examples

बस. ✅

हे झाल्यावर done म्हणा. मग आपण data_types.py तयार करू.



You said:

done

ChatGPT said:
Perfect 👍 आता पुढचा एकच file तयार करूया.

Step 3 — data_types.py
01-Python-Basics folder मध्ये जा → Add file → Create new file

File name:

data_types.py

यात हा code paste कर:

# Python Data Types

# 1. String
name = "Sejal"

# 2. Integer
age = 30

# 3. Float
salary = 50000.50

# 4. Boolean
is_trainer = True

# Check data types
print("Name:", name)
print("Type:", type(name))

print("Age:", age)
print("Type:", type(age))

print("Salary:", salary)
print("Type:", type(salary))

print("Is Trainer:", is_trainer)
print("Type:", type(is_trainer))

त्यानंतर एक छोटा Data Science related example add कर:
# Data Science Example

customer_name = "Amit"
customer_age = 28
purchase_amount = 1250.75
is_customer_active = True

print("\nCustomer Information")
print("Name:", customer_name)
print("Age:", customer_age)
print("Purchase Amount:", purchase_amount)
print("Active Customer:", is_customer_active)

Commit message:

Add Python data types examples

आणि Commit changes करा.

झालं की फक्त done म्हणा. मग आपण input_output.py घेऊ.



You said:

zale pn ,me he sarv python ofr data scinece repositiry mahde add karat aahe kahi change karu ka

ChatGPT said:
हो, पण मोठा change करण्याची गरज नाही. 👍 तू Python-for-Data-Science repository मध्येच हे करत आहेस, ते योग्य आहे.

फक्त एक गोष्ट आपण सुरुवातीपासून ठरवूया: हे trainer चं teaching repository आहे, त्यामुळे प्रत्येक topic मध्ये theory + classroom examples + practical code ठेवू.

आपला structure असा राहू दे:

Python-for-Data-Science/
│
├── README.md
│
├── 01-Python-Basics/
│   ├── README.md
│   ├── variables.py
│   ├── data_types.py
│   ├── input_output.py
│   ├── operators.py
│   ├── conditional_statements.py
│   ├── loops.py
│   ├── functions.py
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   └── sets.py
│
├── 02-NumPy/
│   ├── README.md
│   ├── array_creation.py
│   ├── indexing_slicing.py
│   ├── mathematical_operations.py
│   ├── statistics.py
│   ├── reshaping.py
│   ├── broadcasting.py
│   └── practice.py
│
├── 03-Pandas/
├── 04-Matplotlib/
├── 05-Seaborn/
├── 06-Statistics/
└── 07-Machine-Learning/

आत्तापर्यंत तुझं योग्य आहे:
01-Python-Basics/
│
├── README.md       ✅
├── variables.py    ✅
└── data_types.py   ✅

आता काही delete किंवा change करू नकोस.

आपण पुढे जाऊन प्रत्येक file मध्ये Data Science teaching perspective ठेवू. म्हणजे फक्त basic Python नाही, तर उदाहरणार्थ:

age = 25
salary = 45000
experience = 2

अशा examples मधून students ना पुढे Data Science मध्ये variables कसे उपयोगी पडतात हे समजेल.

आता पुढचा file input_output.py तयार करूया.



You said:

Skip to content
Sejal-PS
Python-for-Data-Science
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Security and quality
Sejal-PS
Python-for-Data-Science
Private
Sejal-PS
Sejal-PS
Add Python variables examples
85576ed
 · 
1 minute ago
Name		
01-Python-Basics
Add Python variables examples
1 minute ago
README.md
Initial commit
7 minutes ago
Repository files navigation
README
Python-for-Data-Science
About

No description, website, or topics provided.
Resources
Readme
Activity
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
 (1)
@Sejal-PS
Sejal-PSSejal Patil
Languages
Python
100%
Suggested workflows
Based on your tech stack

Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
By GitHub Actions
Python package logo
Python package
Create and test a Python package on multiple Python versions.
By GitHub Actions
Django logo
Django
Build and Test a Django Project
By GitHub Actions
More workflows
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
 itakezale .aata kay karu

ChatGPT said:
हो 👍 मी पाहिलं. सगळं बरोबर झालं आहे. तुमच्या repository मध्ये सध्या:

Python-for-Data-Science
│
├── 01-Python-Basics
│   ├── README.md
│   ├── variables.py
│   └── data_types.py
│
└── README.md

आता पुढचं एकच काम करूया.

Step 4 — input_output.py तयार करा
तुझ्या GitHub वर:

01-Python-Basics → Add file → Create new file

File name:

input_output.py

आणि हा code paste कर:

# Python Input and Output


# Output using print()

name = "Sejal"
age = 30

print("Name:", name)
print("Age:", age)


# Taking input from user

name = input("Enter your name: ")
print("Hello", name)


# Input is stored as a string by default

age = input("Enter your age: ")

print("Age:", age)
print("Data type:", type(age))


# Converting input into integer

age = int(input("Enter your age: "))

print("Age:", age)
print("Data type:", type(age))


# Data Science Example

name = input("Enter customer name: ")
age = int(input("Enter customer age: "))
salary = float(input("Enter customer salary: "))

print("\nCustomer Information")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)

Commit message
खाली:

Add input and output examples

आणि Commit changes करा.

बस, आत्ता एवढंच. झाल्यावर done म्हणा. मग आपण operators.py करू.



You said:

me ajun data types.py add nahi ke;e tyat kay add lakru te sang

ChatGPT said:
हो 👍 मग आधी data_types.py complete करूया. input_output.py नंतर करू.

तू 01-Python-Basics → Add file → Create new file कर आणि file name:

data_types.py

यात हा code ठेव:

# Python Data Types

# 1. String
name = "Sejal"
print("Name:", name)
print("Data Type:", type(name))


# 2. Integer
age = 30
print("Age:", age)
print("Data Type:", type(age))


# 3. Float
salary = 50000.50
print("Salary:", salary)
print("Data Type:", type(salary))


# 4. Boolean
is_trainer = True
print("Is Trainer:", is_trainer)
print("Data Type:", type(is_trainer))


# 5. List
skills = ["Python", "NumPy", "Pandas", "Machine Learning"]
print("Skills:", skills)
print("Data Type:", type(skills))


# 6. Tuple
coordinates = (18.52, 73.85)
print("Coordinates:", coordinates)
print("Data Type:", type(coordinates))


# 7. Dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "marks": 85
}

print("Student:", student)
print("Data Type:", type(student))


# 8. Set
numbers = {10, 20, 30, 20, 10}
print("Numbers:", numbers)
print("Data Type:", type(numbers))

यामध्ये आपण हे Data Types cover केले:
str        → String
int        → Integer
float      → Decimal numbers
bool       → True / False
list       → Collection of values
tuple      → Ordered, immutable collection
dict       → Key-value pairs
set        → Unique values

हे trainer म्हणून चांगलं आहे, कारण प्रत्येक type चा छोटा example आणि type() दोन्ही दाखवले आहेत.

आता Commit changes करा.

Commit message:

Add Python data types examples

झाल्यावर मला done सांग. मग पुढे input_output.py करू.



You said:

done

ChatGPT said:
छान 👍 आता 01-Python-Basics मध्ये आपल्याकडे:

README.md       ✅
variables.py    ✅
data_types.py   ✅

आता पुढचा file.

Step 5 — input_output.py
01-Python-Basics → Add file → Create new file

File name:

input_output.py

यात हा code paste कर:

# Python Input and Output


# -------------------------
# 1. Output using print()
# -------------------------

name = "Sejal"
age = 30

print("Name:", name)
print("Age:", age)


# -------------------------
# 2. Taking input from user
# -------------------------

name = input("Enter your name: ")

print("Hello", name)


# -------------------------
# 3. Input is string by default
# -------------------------

age = input("Enter your age: ")

print("Age:", age)
print("Data Type:", type(age))


# -------------------------
# 4. Converting input to integer
# -------------------------

age = int(input("Enter your age: "))

print("Age:", age)
print("Data Type:", type(age))


# -------------------------
# 5. Converting input to float
# -------------------------

salary = float(input("Enter your salary: "))

print("Salary:", salary)
print("Data Type:", type(salary))


# -------------------------
# 6. Data Science Example
# -------------------------

customer_name = input("Enter customer name: ")
customer_age = int(input("Enter customer age: "))
purchase_amount = float(input("Enter purchase amount: "))

print("\nCustomer Information")
print("Name:", customer_name)
print("Age:", customer_age)
print("Purchase Amount:", purchase_amount)

यात students ना काय शिकवता येईल?
print() → output दाखवण्यासाठी

input() → user कडून data घेण्यासाठी

input() चा default type → str

int() → integer conversion

float() → decimal number conversion

Real-world customer data example

Commit message:

Add input and output examples

आणि Commit changes करा.

झाल्यावर फक्त done म्हणा. मग आपण operators.py करू.



You said:

done

ChatGPT said:
छान 👍 आता पुढचा file करूया.

Step 6 — operators.py
01-Python-Basics → Add file → Create new file

File name:

operators.py

यात हा code paste कर:

# Python Operators


# -------------------------
# 1. Arithmetic Operators
# -------------------------

a = 10
b = 3

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

यात मुख्य operators cover झाले:
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

हे Data Science च्या आधीच्या Python foundation साठी पुरेसं आहे.

Commit message:
Add Python operators examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण conditional_statements.py करू.



You said:

done

ChatGPT said:
छान 👍 आता पुढचा topic.

Step 7 — conditional_statements.py
01-Python-Basics → Add file → Create new file

File name:

conditional_statements.py

यात हा code paste कर:

# Python Conditional Statements


# -------------------------
# 1. Simple if statement
# -------------------------

age = 25

if age >= 18:
    print("Eligible")


# -------------------------
# 2. if-else statement
# -------------------------

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# -------------------------
# 3. if-elif-else
# -------------------------

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
# -------------------------

age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Condition satisfied")
else:
    print("Condition not satisfied")


# -------------------------
# 5. Nested if
# -------------------------

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
# -------------------------

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

यामध्ये हे concepts cover झाले:
if
if-else
if-elif-else
multiple conditions
nested if
and

आणि शेवटी customer purchase + discount example आहे, त्यामुळे Data Science students ना real-world logic शी relate करता येईल.

Commit message:
Add conditional statements examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण loops.py करू.



You said:

done

ChatGPT said:
छान 👍 आता loops.py.

Step 8 — loops.py
01-Python-Basics → Add file → Create new file

File name:

loops.py

हा code paste कर:

# Python Loops


# -------------------------
# 1. For Loop
# -------------------------

for i in range(1, 6):
    print(i)


# -------------------------
# 2. Loop through a list
# -------------------------

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# -------------------------
# 3. range() with step
# -------------------------

for i in range(0, 11, 2):
    print(i)


# -------------------------
# 4. While Loop
# -------------------------

count = 1

while count <= 5:
    print(count)
    count += 1


# -------------------------
# 5. Break
# -------------------------

for i in range(1, 10):
    if i == 5:
        break

    print(i)


# -------------------------
# 6. Continue
# -------------------------

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# -------------------------
# 7. Nested Loop
# -------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# -------------------------
# 8. Data Science Example
# -------------------------

sales = [1000, 2500, 1800, 4000, 3200]

total_sales = 0

for sale in sales:
    total_sales += sale

print("Total Sales:", total_sales)

या file मध्ये students ना हे concepts समजतील:
for loop

while loop

range()

Loop through list

break

continue

Nested loop

Data Science related sales example

Commit message:

Add Python loops examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण functions.py करू.



You said:

done

ChatGPT said:
छान 👍 आता functions.py तयार करूया.

Step 9 — functions.py
01-Python-Basics → Add file → Create new file

File name:

functions.py

यात हा code paste कर:

# Python Functions


# -------------------------
# 1. Simple Function
# -------------------------

def greet():
    print("Hello, Welcome to Python!")


greet()


# -------------------------
# 2. Function with Parameter
# -------------------------

def greet_user(name):
    print("Hello", name)


greet_user("Sejal")
greet_user("Rahul")


# -------------------------
# 3. Function with Multiple Parameters
# -------------------------

def add_numbers(a, b):
    result = a + b
    print("Addition:", result)


add_numbers(10, 20)


# -------------------------
# 4. Function with Return
# -------------------------

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# -------------------------
# 5. Default Parameter
# -------------------------

def greet_person(name="Student"):
    print("Hello", name)


greet_person()
greet_person("Sejal")


# -------------------------
# 6. Keyword Arguments
# -------------------------

def student_info(name, age, marks):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)


student_info(
    name="Rahul",
    age=22,
    marks=85
)


# -------------------------
# 7. Data Science Example
# -------------------------

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)

    return average


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)

या file मध्ये मुख्य concepts:
Function
Parameter
Argument
Return value
Default parameter
Keyword argument
Function reuse

आणि शेवटी marks चा average calculate करणारा Data Science-related example आहे.

Commit message:
Add Python functions examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण lists.py करू.



You said:

done

ChatGPT said:
छान 👍 आता lists.py.

Step 10 — lists.py
01-Python-Basics → Add file → Create new file

File name:

lists.py

हा code paste कर:

# Python Lists


# -------------------------
# 1. Creating a List
# -------------------------

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


# -------------------------
# 2. Accessing List Elements
# -------------------------

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# -------------------------
# 3. List Slicing
# -------------------------

print("First two fruits:", fruits[0:2])


# -------------------------
# 4. Adding Elements
# -------------------------

fruits.append("Grapes")

print("After append:", fruits)


# -------------------------
# 5. Insert Element
# -------------------------

fruits.insert(1, "Pineapple")

print("After insert:", fruits)


# -------------------------
# 6. Remove Element
# -------------------------

fruits.remove("Banana")

print("After remove:", fruits)


# -------------------------
# 7. Pop Element
# -------------------------

removed_fruit = fruits.pop()

print("Removed:", removed_fruit)
print("After pop:", fruits)


# -------------------------
# 8. Change Element
# -------------------------

fruits[0] = "Watermelon"

print("After update:", fruits)


# -------------------------
# 9. List Length
# -------------------------

print("Number of fruits:", len(fruits))


# -------------------------
# 10. Loop through List
# -------------------------

for fruit in fruits:
    print(fruit)


# -------------------------
# 11. Sorting
# -------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Sorted numbers:", numbers)


# -------------------------
# 12. Data Science Example
# -------------------------

sales = [1000, 2500, 1800, 4000, 3200]

print("Sales:", sales)
print("Total Sales:", sum(sales))
print("Maximum Sales:", max(sales))
print("Minimum Sales:", min(sales))
print("Average Sales:", sum(sales) / len(sales))

यात हे concepts cover झाले:
List creation
Indexing
Negative indexing
Slicing
append()
insert()
remove()
pop()
Update
len()
Loop
sort()
sum()
max()
min()

शेवटचा sales example Data Science teaching साठी useful आहे.

Commit message:
Add Python list examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण tuples.py करू.



You said:

done

ChatGPT said:
छान 👍 आता tuples.py तयार करूया.

Step 11 — tuples.py
01-Python-Basics → Add file → Create new file

File name:

tuples.py

हा code paste कर:

# Python Tuples


# -------------------------
# 1. Creating a Tuple
# -------------------------

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)


# -------------------------
# 2. Accessing Elements
# -------------------------

print("First element:", numbers[0])
print("Last element:", numbers[-1])


# -------------------------
# 3. Tuple Slicing
# -------------------------

print("First three elements:", numbers[0:3])


# -------------------------
# 4. Length of Tuple
# -------------------------

print("Length:", len(numbers))


# -------------------------
# 5. Loop through Tuple
# -------------------------

for number in numbers:
    print(number)


# -------------------------
# 6. Tuple Methods
# -------------------------

values = (10, 20, 10, 30, 10, 40)

print("Count of 10:", values.count(10))
print("Index of 30:", values.index(30))


# -------------------------
# 7. Tuple Unpacking
# -------------------------

student = ("Rahul", 22, 85)

name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# -------------------------
# 8. Data Science Example
# -------------------------

coordinates = (18.5204, 73.8567)

latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)

Important concept
Tuple म्हणजे ordered collection, आणि tuple तयार केल्यानंतर त्यातील elements directly बदलता येत नाहीत.

उदाहरण:

numbers = (10, 20, 30)

# This will give an error:
# numbers[0] = 100

म्हणून list आणि tuple मधला basic difference students ना असा सांगू शकते:

List  → Mutable   → बदलता येते
Tuple → Immutable → बदलता येत नाही

Commit message:
Add Python tuple examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण dictionaries.py करू.



You said:

done

ChatGPT said:
छान 👍 आता dictionaries.py.

Step 12 — dictionaries.py
01-Python-Basics → Add file → Create new file

File name:

dictionaries.py

हा code paste कर:

# Python Dictionaries


# -------------------------
# 1. Creating a Dictionary
# -------------------------

student = {
    "name": "Rahul",
    "age": 22,
    "marks": 85
}

print("Student:", student)


# -------------------------
# 2. Accessing Values
# -------------------------

print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])


# -------------------------
# 3. Using get()
# -------------------------

print("Name:", student.get("name"))
print("City:", student.get("city"))


# -------------------------
# 4. Adding a New Key-Value
# -------------------------

student["city"] = "Pune"

print("After adding city:", student)


# -------------------------
# 5. Updating a Value
# -------------------------

student["marks"] = 90

print("Updated marks:", student)


# -------------------------
# 6. Removing an Item
# -------------------------

student.pop("age")

print("After removing age:", student)


# -------------------------
# 7. Dictionary Keys and Values
# -------------------------

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# -------------------------
# 8. Loop through Dictionary
# -------------------------

for key, value in student.items():
    print(key, ":", value)


# -------------------------
# 9. Nested Dictionary
# -------------------------

students = {
    "student1": {
        "name": "Rahul",
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "marks": 92
    }
}

print("\nNested Dictionary")
print(students["student1"]["name"])
print(students["student2"]["marks"])


# -------------------------
# 10. Data Science Example
# -------------------------

customer = {
    "customer_id": 101,
    "name": "Amit",
    "age": 28,
    "city": "Pune",
    "purchase_amount": 7500.50
}

print("\nCustomer Information")

for key, value in customer.items():
    print(key, ":", value)

या file मधून हे concepts cover होतील:
Dictionary
Key-Value Pair
Accessing Values
get()
Adding Data
Updating Data
Removing Data
keys()
values()
items()
Looping
Nested Dictionary

आणि शेवटी customer data चा example आहे, जो Data Science context मध्ये सहज explain करता येईल.

Commit message:
Add Python dictionary examples

Commit changes करा.

झाल्यावर done म्हणा. मग sets.py हा 01-Python-Basics मधला शेवटचा major file करू.



You said:

done

ChatGPT said:
छान 👍 आता 01-Python-Basics मधला शेवटचा collection topic — Sets.

Step 13 — sets.py
01-Python-Basics → Add file → Create new file

File name:

sets.py

हा code paste कर:

# Python Sets


# -------------------------
# 1. Creating a Set
# -------------------------

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# -------------------------
# 2. Duplicate Values
# -------------------------

numbers = {10, 20, 20, 30, 30, 40}

print("Set with duplicates:", numbers)


# -------------------------
# 3. Adding an Element
# -------------------------

numbers.add(50)

print("After add:", numbers)


# -------------------------
# 4. Adding Multiple Elements
# -------------------------

numbers.update([60, 70, 80])

print("After update:", numbers)


# -------------------------
# 5. Removing an Element
# -------------------------

numbers.remove(20)

print("After remove:", numbers)


# -------------------------
# 6. Discard
# -------------------------

numbers.discard(100)

print("After discard:", numbers)


# -------------------------
# 7. Membership Testing
# -------------------------

print(30 in numbers)
print(100 in numbers)


# -------------------------
# 8. Set Operations
# -------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


# Union
print("Union:", set_a | set_b)


# Intersection
print("Intersection:", set_a & set_b)


# Difference
print("Difference:", set_a - set_b)


# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)


# -------------------------
# 9. Data Science Example
# -------------------------

customer_ids = [101, 102, 103, 101, 104, 102, 105]

unique_customer_ids = set(customer_ids)

print("\nCustomer IDs:", customer_ids)
print("Unique Customer IDs:", unique_customer_ids)
print("Number of Unique Customers:", len(unique_customer_ids))

या file मध्ये important concepts:
Set
Unique values
add()
update()
remove()
discard()
in
Union
Intersection
Difference
Symmetric Difference

शेवटचा example duplicate customer IDs remove करण्यासाठी set चा वापर दाखवतो. Data Science मध्ये हा use-case समजावायला उपयोगी आहे.

Commit message:
Add Python set examples

Commit changes करा.

झाल्यावर done म्हणा.

यानंतर आपण 01-Python-Basics पूर्ण करून त्याचा README थोडा update करू, आणि मग पुढचा मोठा topic 02-NumPy सुरू करू.



You said:

done

ChatGPT said:
छान 👍 01-Python-Basics चे सगळे basic files आता तयार झाले आहेत.

आता एक छोटं काम बाकी आहे: README.md update करायचा, जेणेकरून GitHub वर folder उघडल्यावर trainer म्हणून कोणते concepts cover केले आहेत ते लगेच दिसतील.

Step 14 — README.md Update करा
01-Python-Basics → README.md उघडा → ✏️ Edit करा.

आतला जुना content पूर्ण replace करून हा content paste करा:

Python Basics README



Python Basics for Data Science
Python concepts required before starting Data Science libraries like NumPy and Pandas.

Topics Covered
1. Variables
Creating variables

Assigning values

Variable naming

Checking variable values

File: variables.py

2. Data Types
String

Integer

Float

Boolean

List

Tuple

Dictionary

Set

type()

File: data_types.py

3. Input and Output
print()

input()

Type conversion

int()

float()

File: input_output.py

4. Operators
Arithmetic operators

Comparison operators

Logical operators

Assignment operators

Membership operators

Identity operators

File: operators.py

5. Conditional Statements
if

if-else

if-elif-else

Nested if

Multiple conditions

File: conditional_statements.py

6. Loops
for loop

while loop

range()

break

continue

Nested loops

File: loops.py

7. Functions
Creating functions

Parameters

Arguments

Return values

Default parameters

Keyword arguments

File: functions.py

8. Lists
Creating lists

Indexing

Slicing

append()

insert()

remove()

pop()

sort()

len()

File: lists.py

9. Tuples
Creating tuples

Indexing

Slicing

Tuple methods

Tuple unpacking

Immutable nature of tuples

File: tuples.py

10. Dictionaries
Key-value pairs

Accessing values

get()

Adding and updating values

Removing values

keys()

values()

items()

Nested dictionaries

File: dictionaries.py

11. Sets
Unique values

Adding and removing elements

Membership testing

Union

Intersection

Difference

Symmetric difference

File: sets.py

Practice Focus
The examples include basic Python programs along with simple real-world examples such as:

Student data

Customer data

Sales data

Marks and average

Unique customer IDs

These concepts form the Python foundation required for Data Science.

Commit message
Update Python Basics README

आणि Commit changes करा.

हे झाल्यावर 01-Python-Basics section complete समजू. ✅

मग आपण 02-NumPy सुरू करू — आणि NumPy मध्ये यावेळी README.md मध्ये definition, uses, features, installation, array creation, indexing, math operations, broadcasting, statistics, axis, reshape, practical examples व्यवस्थित trainer notes म्हणून ठेवू.



You said:

ho

ChatGPT said:
छान 👍 आता आपण 02-NumPy सुरू करूया. एकदम step-by-step जाऊ.

Step 15 — 02-NumPy folder तयार करा
तुझ्या Python-for-Data-Science repository च्या main page वर जा.

Add file → Create new file

File name मध्ये लिहा:

02-NumPy/README.md

आत्ता README मध्ये content टाकू नको.

खाली Commit changes करा.

Commit message:

Create NumPy folder

आत्ता फक्त हेच कर.
02-NumPy folder तयार झाल्यावर done म्हण.

मग मी तुला NumPy चा पूर्ण trainer-level README content देईन — definition पासून arrays, installation, features, uses, mathematical operations, indexing, slicing, broadcasting, reshaping, statistics, random, linear algebra आणि important terms पर्यंत.



You said:

done

ChatGPT said:
छान 👍 02-NumPy folder तयार झाला.

आता Step 16 — NumPy README.md तयार करूया.
हा आपल्या NumPy section चा मुख्य trainer notes file असेल. खूप advanced language न ठेवता, class मध्ये explain करता येईल अशा पद्धतीने ठेवतो.

02-NumPy/README.md उघडून जुना content असेल तर replace करा आणि हा content paste करा:

NumPy Trainer Notes


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

आता README चा content paste करून Commit changes करा.

Commit message:

Add NumPy trainer notes

आत्ता फक्त README complete करा.
झाल्यावर done म्हणा. त्यानंतर आपण NumPy चा पहिला actual code file array_creation.py तयार करू.



You said:

done

ChatGPT said:
छान 👍 आता 02-NumPy मध्ये पहिली practical Python file तयार करूया.

Step 16 — array_creation.py
02-NumPy folder उघड → Add file → Create new file

File name:

array_creation.py

यात हा code paste कर:

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

हा file class मध्ये कशासाठी वापरायचा?
यातून तुम्ही students ना एकाच file मध्ये:

np.array()

1D array

2D array

3D array

np.zeros()

np.ones()

np.full()

np.arange()

np.linspace()

ndim

shape

size

dtype

हे demonstrate करू शकता.

Commit message
Add NumPy array creation examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण indexing_slicing.py करू.



You said:

done

ChatGPT said:
छान 👍 आता NumPy मधला खूप important topic:

Step 17 — indexing_slicing.py
02-NumPy → Add file → Create new file

File name:

indexing_slicing.py

हा पूर्ण code paste कर:

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

या file मधून काय cover होईल?
Indexing
Positive Indexing
Negative Indexing
Slicing
Step
Reverse
2D Indexing
Rows
Columns
2D Slicing
Updating Elements
Boolean Indexing
Filtering Data

विशेषतः हा भाग Data Science मध्ये खूप महत्त्वाचा आहे:

marks[marks >= 75]

यातून condition based filtering समजावता येते.

Commit message
Add NumPy indexing and slicing examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण mathematical_operations.py करू.



You said:

done

ChatGPT said:
छान 👍 आता NumPy मधला basic math + statistical calculations साठी foundation असलेला file तयार करूया.

Step 18 — mathematical_operations.py
02-NumPy → Add file → Create new file

File name:

mathematical_operations.py

हा code paste कर:

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

यात आपण काय cover केलं?
Basic operations
+
-
*
/
**

NumPy mathematical functions
np.sqrt()
np.abs()
np.exp()
np.log()

Statistical/aggregate functions
np.sum()
np.mean()
np.median()
np.min()
np.max()
np.std()
np.var()

Rounding
np.round()
np.floor()
np.ceil()

आणि शेवटी Sales Analysis example आहे, त्यामुळे class मध्ये numerical data वर operations कसे करतात ते दाखवता येईल.

Commit message
Add NumPy mathematical operations examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण statistics.py करू.



You said:

Done

ChatGPT said:
छान 👍 आता statistics.py तयार करूया. यात NumPy मधील statistics-related functions वेगळे आणि व्यवस्थित demonstrate करू.

Step 19 — statistics.py
02-NumPy → Add file → Create new file

File name:

statistics.py

हा code paste कर:

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

या file मध्ये important concepts cover झाले:
Mean
Median
Minimum
Maximum
Sum
Variance
Standard Deviation
Percentile
Axis
NaN
np.isnan()
np.nanmean()
Boolean filtering

विशेषतः axis=0 आणि axis=1 class मध्ये नीट explain करता येतील:

axis=0 → column-wise
axis=1 → row-wise

आणि शेवटचा student marks example practical आहे.

Commit message
Add NumPy statistics examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण reshaping.py करू.



You said:

done

ChatGPT said:
छान 👍 आता NumPy मधला एक महत्त्वाचा topic — Reshaping.

Step 20 — reshaping.py
02-NumPy → Add file → Create new file

File name:

reshaping.py

हा code paste कर:

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

या file मध्ये काय शिकवता येईल?
reshape()
shape
-1 in reshape
flatten()
ravel()
transpose()
resize()

सगळ्यात important concept:

arr.reshape(3, 4)

इथे original array मध्ये 12 elements आहेत आणि:

3 × 4 = 12

म्हणून reshape होतो.

पण:

arr.reshape(4, 2)

केल्यास:

4 × 2 = 8

म्हणून 12 elements असलेला array 8 positions मध्ये बसत नाही.

Commit message
Add NumPy reshaping examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण broadcasting.py करू.



You said:

done

ChatGPT said:
छान 👍 आता NumPy मधला Broadcasting topic करूया. हा Data Science मध्ये खूप useful आहे.

Step 21 — broadcasting.py
02-NumPy → Add file → Create new file

File name:

broadcasting.py

हा code paste कर:

# NumPy Broadcasting

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

Broadcasting म्हणजे काय?
सोप्या भाषेत:

Broadcasting म्हणजे वेगवेगळ्या shape च्या compatible arrays वर NumPy ला arithmetic operation करण्याची सुविधा.

उदाहरण:

arr = np.array([10, 20, 30])

print(arr + 5)

NumPy internally 5 प्रत्येक element सोबत वापरतो:

10 + 5
20 + 5
30 + 5

Result:

[15 25 35]

Data Science example
आपल्याकडे:

sales = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 3500]
])

tax_rate = 0.18

तर:

tax = sales * tax_rate

मध्ये 0.18 पूर्ण array वर apply होतो.

हेच Broadcasting चं practical use आहे.

Commit message
Add NumPy broadcasting examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण practice.py बनवू — त्यात NumPy चे एकत्रित practical exercises ठेवू.



You said:

done

ChatGPT said:
छान 👍 आता 02-NumPy मधला शेवटचा practical file करूया — practice.py.

यामध्ये वेगवेगळे concepts एकत्र वापरले जातील, त्यामुळे trainer म्हणून classroom practice आणि students ना assignment देण्यासाठीही उपयोगी पडेल.

Step 22 — practice.py
02-NumPy → Add file → Create new file

File name:

practice.py

हा code paste कर:

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

या file चा purpose
हा file revision + practice साठी आहे.

यात आपण एकत्र वापरले:

Array Creation
Array Properties
Arithmetic Operations
Statistics
Indexing
Boolean Filtering
2D Arrays
Axis
Reshape
Unique Values
Broadcasting
NaN
Random Numbers
Data Science Examples

विशेषतः शेवटचा Mini Data Science Practice class मध्ये students ना देऊ शकते.

Commit message
Add NumPy practice examples

Commit changes करा.

झाल्यावर done म्हणा.

मग आपण 02-NumPy चा final structure check + README मध्ये काही missing important topics आहेत का ते पाहू, आणि त्यानंतर 03-Pandas सुरू करू.



You said:

ho

ChatGPT said:
हो 👍 आता 02-NumPy चा final check करूया. आत्ता काही नवीन code add करू नकोस.

तुझा folder ideally असा दिसायला हवा:

Python-for-Data-Science/
│
├── 01-Python-Basics/
│   ├── README.md
│   ├── variables.py
│   ├── data_types.py
│   ├── input_output.py
│   ├── operators.py
│   ├── conditional_statements.py
│   ├── loops.py
│   ├── functions.py
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   └── sets.py
│
├── 02-NumPy/
│   ├── README.md
│   ├── array_creation.py
│   ├── indexing_slicing.py
│   ├── mathematical_operations.py
│   ├── statistics.py
│   ├── reshaping.py
│   ├── broadcasting.py
│   └── practice.py
│
└── README.md

NumPy मध्ये आपण काय cover केलं?
NumPy introduction

Installation

Importing NumPy

ndarray

1D, 2D, 3D arrays

Array creation

zeros(), ones(), full()

arange(), linspace()

ndim, shape, size, dtype

Indexing

Slicing

Boolean indexing

Mathematical operations

Aggregate/statistical functions

axis

Reshaping

flatten(), ravel()

Transpose

Concatenation

Stacking

Broadcasting

where()

Sorting

Unique values

Random numbers

Random seed

Copy vs View

Missing values / NaN

Linear algebra

Practical Data Science examples

Practice exercises

म्हणजे NumPy चा basic-to-intermediate teaching portion व्यवस्थित तयार झाला आहे. ✅

एक छोटासा important point
README.md मध्ये आपण official documentation ची raw URL लिहिली आहे. GitHub वर ते चालेल. पण पुढे repository अधिक clean ठेवायची असेल तर आपण शेवटी links section व्यवस्थित करू शकतो. आत्ता त्यासाठी काही करू नकोस.

आता 02-NumPy साठी सगळं झालं असं समज.

पुढचा मोठा section:

03-Pandas/

आणि Pandas मध्ये आपण DataFrame आणि Series पासून सुरू करून CSV/Excel reading, data inspection, filtering, sorting, missing values, groupby, merge, concat, apply, aggregation आणि mini data-analysis project घेऊ.

आत्ता फक्त NumPy चा folder GitHub वर एकदा पाहून वरचा structure match होतोय का ते check कर. मग done म्हणा.



You said:

done

ChatGPT said:
छान 👍 आता आपण 03-Pandas सुरू करूया. एकेक step नेच करू.

Step 23 — 03-Pandas folder तयार करा
तुझ्या Python-for-Data-Science repository च्या main page वर जा.

Add file → Create new file

File name मध्ये लिहा:

03-Pandas/README.md

आत्ता content टाकायचा नाही.

Commit changes करा.

Commit message:

Create Pandas folder

आत्ता फक्त folder तयार कर.

झाल्यावर done म्हणा. मग मी तुला Pandas चा trainer-friendly पूर्ण README देईन.



You said:

done

ChatGPT said:
छान 👍 आता 03-Pandas/README.md मध्ये आपले Pandas trainer notes ठेवूया.

यामध्ये NumPy पेक्षा एक step पुढे जाऊन real dataset handling वर focus ठेवू — कारण Data Science मध्ये Pandas चा मुख्य उपयोग data read, clean, filter, transform आणि analyze करण्यासाठी होतो.

Step 24 — Pandas README
03-Pandas/README.md उघड → ✏️ Edit → जुना content replace करून हा content paste कर:

Pandas Trainer Notes


Pandas for Data Science
Pandas is a Python library used for data manipulation, data cleaning, data analysis and working with tabular data.

It is one of the most commonly used libraries in Data Science.

Pandas mainly provides two important data structures:

Series

DataFrame

1. Why Pandas?
In Data Science, we usually work with data such as:

Customer data

Employee data

Sales data

Student data

Product data

Financial data

This data is often stored in rows and columns.

Pandas makes it easier to:

Read data

View data

Filter data

Clean data

Handle missing values

Sort data

Group data

Calculate statistics

Combine datasets

Prepare data for Machine Learning

2. Installation
Pandas can be installed using pip.

pip install pandas

To check the installed version:

import pandas as pd

print(pd.__version__)

3. Import Pandas
The commonly used alias for Pandas is pd.

import pandas as pd

4. Pandas Series
A Series is a one-dimensional labelled data structure.

Example:

import pandas as pd

marks = pd.Series([80, 75, 90, 85, 70])

print(marks)

Each value has an index.

5. Series with Custom Index
marks = pd.Series(
    [80, 75, 90],
    index=["Rahul", "Priya", "Amit"]
)

print(marks)

Access a value:

print(marks["Rahul"])

6. DataFrame
A DataFrame is a two-dimensional labelled data structure with rows and columns.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, 24, 23],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)

A DataFrame is similar to a table.

7. Important DataFrame Terms
A DataFrame contains:

Rows

Columns

Index

Values

Data Types

Example:

print(df.index)
print(df.columns)
print(df.values)
print(df.dtypes)

8. Creating DataFrame from Dictionary
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print(df)

9. Creating DataFrame from List
data = [
    ["Rahul", 22, 80],
    ["Priya", 24, 90],
    ["Amit", 23, 75]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Marks"]
)

print(df)

10. Reading CSV File
CSV files are very common in Data Science.

df = pd.read_csv("data.csv")

print(df)

11. Reading Excel File
df = pd.read_excel("data.xlsx")

print(df)

Excel support may require an additional package depending on the file format and environment.

12. Inspecting Data
head()
Shows the first rows.

print(df.head())

tail()
Shows the last rows.

print(df.tail())

shape
Returns number of rows and columns.

print(df.shape)

columns
Shows column names.

print(df.columns)

dtypes
Shows data types.

print(df.dtypes)

info()
Provides information about the DataFrame.

df.info()

describe()
Provides statistical summary for numerical columns.

print(df.describe())

13. Selecting a Column
print(df["Name"])

Another method:

print(df.Name)

The bracket method is generally preferred because it also works with column names containing spaces or special characters.

14. Selecting Multiple Columns
print(df[["Name", "Marks"]])

15. Selecting Rows with loc
loc is label-based selection.

print(df.loc[0])

Selecting multiple rows:

print(df.loc[0:2])

Selecting rows and columns:

print(df.loc[0:2, ["Name", "Marks"]])

16. Selecting Rows with iloc
iloc is position-based selection.

print(df.iloc[0])

Multiple rows:

print(df.iloc[0:3])

Rows and columns:

print(df.iloc[0:3, 0:2])

17. Filtering Data
Filtering is one of the most important Pandas concepts.

Example:

print(df[df["Marks"] > 80])

Multiple conditions:

print(
    df[
        (df["Age"] > 20) &
        (df["Marks"] > 80)
    ]
)

Using OR:

print(
    df[
        (df["Marks"] > 90) |
        (df["Age"] < 21)
    ]
)

18. Adding a New Column
df["Passed"] = df["Marks"] >= 40

print(df)

Another example:

df["Bonus"] = 5

print(df)

19. Updating a Column
df["Marks"] = df["Marks"] + 5

print(df)

20. Renaming Columns
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)

print(df)

21. Dropping Columns
df.drop(
    columns=["Age"],
    inplace=True
)

print(df)

22. Dropping Rows
df.drop(index=0, inplace=True)

print(df)

23. Sorting Data
Sort by one column:

df.sort_values("Marks")

Descending order:

df.sort_values(
    "Marks",
    ascending=False
)

24. Handling Missing Values
Missing values are common in real-world datasets.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, None, 24],
    "Marks": [80, 90, None]
}

df = pd.DataFrame(data)

print(df)

25. Detecting Missing Values
print(df.isnull())

Count missing values:

print(df.isnull().sum())

Another method:

print(df.isna().sum())

26. Removing Missing Values
df.dropna()

Remove rows containing missing values:

df.dropna(inplace=True)

27. Filling Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())

For a fixed value:

df["Marks"] = df["Marks"].fillna(0)

28. Duplicate Data
Check duplicates:

print(df.duplicated())

Count duplicates:

print(df.duplicated().sum())

Remove duplicates:

df.drop_duplicates(inplace=True)

29. Unique Values
print(df["Name"].unique())

Number of unique values:

print(df["Name"].nunique())

30. Value Counts
value_counts() counts how frequently each value occurs.

print(df["City"].value_counts())

This is useful for categorical data analysis.

31. Basic Statistics
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].sum())

32. GroupBy
groupby() is one of the most important Pandas concepts for Data Analysis.

Example:

data = {
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [1000, 2000, 1500, 2500]
}

df = pd.DataFrame(data)

print(
    df.groupby("City")["Sales"].sum()
)

Average sales:

print(
    df.groupby("City")["Sales"].mean()
)

33. GroupBy Multiple Columns
result = df.groupby(
    ["City"]
)["Sales"].agg(
    ["sum", "mean", "max", "min"]
)

print(result)

34. Aggregation
Pandas provides aggregation functions such as:

sum()
mean()
median()
min()
max()
count()

Example:

print(
    df["Sales"].agg(
        ["sum", "mean", "min", "max"]
    )
)

35. Apply Function
apply() can be used to apply a function to values.

Example:

def add_bonus(x):
    return x + 10

df["Updated_Sales"] = df["Sales"].apply(add_bonus)

print(df)

A lambda function can also be used:

df["Updated_Sales"] = df["Sales"].apply(
    lambda x: x + 10
)

36. String Operations
Pandas provides string methods for text columns.

Example:

df["Name"] = df["Name"].str.upper()

Other examples:

df["Name"].str.lower()
df["Name"].str.title()
df["Name"].str.len()

Checking text:

df["Name"].str.contains("A")

37. Date and Time
Pandas can work with dates.

dates = pd.to_datetime(
    ["2025-01-01", "2025-02-01", "2025-03-01"]
)

print(dates)

Create a date column:

df["Date"] = pd.to_datetime(df["Date"])

Extract year:

df["Year"] = df["Date"].dt.year

Extract month:

df["Month"] = df["Date"].dt.month

38. Concatenating DataFrames
Two DataFrames can be combined using concat().

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Marks": [75, 85]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

39. Merge
merge() is used to combine DataFrames using a common column.

Example:

students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Rahul", "Priya", "Amit"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [80, 90, 75]
})

result = pd.merge(
    students,
    marks,
    on="Student_ID"
)

print(result)

40. Merge Types
Important merge types:

inner
left
right
outer

Example:

pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

41. Exporting Data
Save DataFrame as CSV:

df.to_csv(
    "output.csv",
    index=False
)

Save as Excel:

df.to_excel(
    "output.xlsx",
    index=False
)

42. Index
Every Pandas DataFrame has an index.

print(df.index)

Set a column as index:

df.set_index("Student_ID", inplace=True)

Reset index:

df.reset_index(inplace=True)

43. Changing Data Type
Check data types:

print(df.dtypes)

Convert a column:

df["Age"] = df["Age"].astype(int)

For numeric conversion:

df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)

44. Pandas Data Cleaning Flow
A common Data Science workflow is:

Read Data
    ↓
Understand Data
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Clean Data
    ↓
Transform Data
    ↓
Filter Data
    ↓
Group / Aggregate
    ↓
Analyze Data
    ↓
Export / Use for ML

45. Simple Data Analysis Example
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [5000, 7000, 4500, 8000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nHighest Sales:")
print(df["Sales"].max())

print("\nPune Customers:")
print(df[df["City"] == "Pune"])

print("\nCity-wise Sales:")
print(
    df.groupby("City")["Sales"].sum()
)

46. Important Pandas Functions
pd.Series()
pd.DataFrame()

pd.read_csv()
pd.read_excel()

df.head()
df.tail()
df.info()
df.describe()

df.shape
df.columns
df.index
df.dtypes

df["column"]
df[["column1", "column2"]]

df.loc[]
df.iloc[]

df.isnull()
df.isna()
df.dropna()
df.fillna()

df.drop_duplicates()
df.duplicated()

df.sort_values()

df.groupby()
df.agg()
df.apply()

df.merge()
pd.concat()

df.rename()
df.drop()

df.unique()
df.nunique()
df.value_counts()

df.to_csv()
df.to_excel()

47. Pandas in Data Science
Pandas is mainly used for:

Data loading

Data cleaning

Data preprocessing

Data transformation

Exploratory Data Analysis (EDA)

Statistical analysis

Working with CSV and Excel files

Handling missing values

Filtering and sorting data

Grouping and aggregation

Preparing data for visualization

Preparing data for Machine Learning

48. Pandas and NumPy
NumPy is mainly focused on numerical arrays and mathematical operations.

Pandas provides higher-level data structures such as Series and DataFrame for working with structured and labelled data.

A common Data Science workflow is:

NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
Statistics / EDA
   ↓
Machine Learning

49. Quick Revision
Pandas
   ↓
Series
   ↓
DataFrame
   ↓
Read Data
   ↓
Inspect Data
   ↓
Select Data
   ↓
Filter Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
GroupBy
   ↓
Merge / Concat
   ↓
Analyze Data
   ↓
Export Data

Official Documentation
Pandas documentation:

https://pandas.pydata.org/docs/

आता हा पूर्ण README paste करून Commit changes कर.

Commit message:

Add Pandas trainer notes

आत्ता फक्त README कर. झाल्यावर done म्हण. मग आपण series_dataframe.py हा पहिला practical Pandas file तयार करू.



You said:

done

ChatGPT said:
छान 👍 आता Pandas चा पहिला practical file.

Step 25 — series_dataframe.py
03-Pandas → Add file → Create new file

File name:

series_dataframe.py

हा code paste कर:

# Pandas Series and DataFrame

import pandas as pd


# -------------------------
# 1. Creating a Series
# -------------------------

marks = pd.Series([80, 75, 90, 85, 70])

print("Marks Series:")
print(marks)


# -------------------------
# 2. Series with Custom Index
# -------------------------

marks = pd.Series(
    [80, 75, 90],
    index=["Rahul", "Priya", "Amit"]
)

print("\nSeries with Custom Index:")
print(marks)


# -------------------------
# 3. Accessing Series Values
# -------------------------

print("\nRahul's Marks:")
print(marks["Rahul"])

print("\nFirst Student:")
print(marks.iloc[0])


# -------------------------
# 4. Series Properties
# -------------------------

print("\nSeries Properties")

print("Values:")
print(marks.values)

print("Index:")
print(marks.index)

print("Data Type:")
print(marks.dtype)

print("Size:")
print(marks.size)


# -------------------------
# 5. Creating DataFrame
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# -------------------------
# 6. DataFrame Properties
# -------------------------

print("\nDataFrame Properties")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 7. Selecting a Column
# -------------------------

print("\nName Column:")
print(df["Name"])

print("\nMarks Column:")
print(df["Marks"])


# -------------------------
# 8. Selecting Multiple Columns
# -------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])


# -------------------------
# 9. Adding a New Column
# -------------------------

df["Passed"] = df["Marks"] >= 40

print("\nAfter Adding Passed Column:")
print(df)


# -------------------------
# 10. DataFrame Statistics
# -------------------------

print("\nMarks Statistics")

print("Mean:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())


# -------------------------
# 11. Data Science Example
# -------------------------

sales_data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Price": [55000, 25000, 18000, 15000],
    "Quantity": [2, 5, 3, 4]
}

sales_df = pd.DataFrame(sales_data)

sales_df["Total_Sales"] = (
    sales_df["Price"] * sales_df["Quantity"]
)

print("\nSales Data:")
print(sales_df)

print("\nTotal Revenue:")
print(sales_df["Total_Sales"].sum())

या file मध्ये काय cover होईल?
Series
DataFrame
Custom Index
Series indexing
iloc
values
index
dtype
size
DataFrame columns
shape
Selecting columns
Adding columns
Basic statistics
Real-world sales calculation

शेवटचा example:

sales_df["Total_Sales"] = (
    sales_df["Price"] * sales_df["Quantity"]
)

हा Pandas + basic business data analysis चा चांगला example आहे.

Commit message
Add Pandas Series and DataFrame examples

Commit changes करा.

झाल्यावर done म्हणा. मग आपण read_data.py करू — CSV, Excel आणि basic dataset loading.



You said:

done

ChatGPT said:
छान 👍 आता Pandas मधला real-world मध्ये खूप वापरला जाणारा भाग करूया — data files read करणे.

Step 26 — read_data.py
03-Pandas → Add file → Create new file

File name:

read_data.py

हा code paste कर:

# Pandas - Reading Data

import pandas as pd


# -------------------------
# 1. Reading a CSV File
# -------------------------

# Example:
# df = pd.read_csv("data.csv")

# print(df)


# -------------------------
# 2. Reading CSV with Different Separator
# -------------------------

# Some files use ; instead of ,

# df = pd.read_csv("data.csv", sep=";")

# print(df)


# -------------------------
# 3. Reading Excel File
# -------------------------

# df = pd.read_excel("data.xlsx")

# print(df)


# -------------------------
# 4. Reading a Specific Excel Sheet
# -------------------------

# df = pd.read_excel(
#     "data.xlsx",
#     sheet_name="Sheet1"
# )

# print(df)


# -------------------------
# 5. Reading JSON File
# -------------------------

# df = pd.read_json("data.json")

# print(df)


# -------------------------
# 6. Creating a Sample CSV File
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "City": ["Pune", "Mumbai", "Pune", "Nashik"],
    "Marks": [80, 90, 75, 88]
}

sample_df = pd.DataFrame(data)

print("Sample Data:")
print(sample_df)


# -------------------------
# 7. Saving DataFrame as CSV
# -------------------------

sample_df.to_csv(
    "students.csv",
    index=False
)

print("\nCSV file created successfully.")


# -------------------------
# 8. Reading the Created CSV
# -------------------------

df = pd.read_csv("students.csv")

print("\nData Read from CSV:")
print(df)


# -------------------------
# 9. Reading Selected Columns
# -------------------------

df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)

print("\nSelected Columns:")
print(df)


# -------------------------
# 10. Reading Limited Rows
# -------------------------

df = pd.read_csv(
    "students.csv",
    nrows=2
)

print("\nFirst Two Rows:")
print(df)


# -------------------------
# 11. Checking File Data
# -------------------------

df = pd.read_csv("students.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 12. Basic Data Analysis
# -------------------------

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

एक important गोष्ट
या code मध्ये:

sample_df.to_csv("students.csv", index=False)

केल्यामुळे file run केल्यावर students.csv तयार होईल.

नंतर:

df = pd.read_csv("students.csv")

ने आपण तीच file परत Pandas मध्ये read करतो.

यामुळे students ना DataFrame → CSV → DataFrame हा complete flow समजेल.

यात आपण काय cover केलं?
pd.read_csv()

pd.read_excel()

pd.read_json()

sep

sheet_name

usecols

nrows

to_csv()

head()

tail()

shape

columns

dtypes

Commit message:

Add Pandas data reading examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण data_inspection.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 27 — data_inspection.py करूया.

हा file students ना dataset मिळाल्यावर सगळ्यात आधी data कसा समजून घ्यायचा हे शिकवण्यासाठी आहे.

03-Pandas → Add file → Create new file

File name:

data_inspection.py

हा code paste कर:

# Pandas - Data Inspection

import pandas as pd


# -------------------------
# 1. Create Sample Dataset
# -------------------------

data = {
    "Name": [
        "Rahul", "Priya", "Amit",
        "Neha", "Sneha", "Rohit"
    ],
    "Age": [22, 24, 23, 21, 25, 22],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune"
    ],
    "Marks": [80, 90, 75, 88, 67, 95]
}

df = pd.DataFrame(data)


# -------------------------
# 2. Display Dataset
# -------------------------

print("Dataset:")
print(df)


# -------------------------
# 3. First 5 Rows
# -------------------------

print("\nFirst 5 Rows:")
print(df.head())


# -------------------------
# 4. First 3 Rows
# -------------------------

print("\nFirst 3 Rows:")
print(df.head(3))


# -------------------------
# 5. Last 5 Rows
# -------------------------

print("\nLast 5 Rows:")
print(df.tail())


# -------------------------
# 6. Last 2 Rows
# -------------------------

print("\nLast 2 Rows:")
print(df.tail(2))


# -------------------------
# 7. Shape
# -------------------------

print("\nShape:")
print(df.shape)


# -------------------------
# 8. Number of Rows
# -------------------------

print("\nNumber of Rows:")
print(df.shape[0])


# -------------------------
# 9. Number of Columns
# -------------------------

print("\nNumber of Columns:")
print(df.shape[1])


# -------------------------
# 10. Column Names
# -------------------------

print("\nColumn Names:")
print(df.columns)


# -------------------------
# 11. Index
# -------------------------

print("\nIndex:")
print(df.index)


# -------------------------
# 12. Data Types
# -------------------------

print("\nData Types:")
print(df.dtypes)


# -------------------------
# 13. Dataset Information
# -------------------------

print("\nDataset Information:")
df.info()


# -------------------------
# 14. Statistical Summary
# -------------------------

print("\nStatistical Summary:")
print(df.describe())


# -------------------------
# 15. Numerical Columns Only
# -------------------------

print("\nNumerical Columns:")
print(df.select_dtypes(include="number"))


# -------------------------
# 16. Object/String Columns
# -------------------------

print("\nString Columns:")
print(df.select_dtypes(include="object"))


# -------------------------
# 17. Unique Values
# -------------------------

print("\nUnique Cities:")
print(df["City"].unique())


# -------------------------
# 18. Number of Unique Values
# -------------------------

print("\nNumber of Unique Cities:")
print(df["City"].nunique())


# -------------------------
# 19. Value Counts
# -------------------------

print("\nCity Counts:")
print(df["City"].value_counts())


# -------------------------
# 20. Missing Values
# -------------------------

print("\nMissing Values:")
print(df.isnull())


# -------------------------
# 21. Missing Value Count
# -------------------------

print("\nMissing Values Count:")
print(df.isnull().sum())


# -------------------------
# 22. Duplicate Rows
# -------------------------

print("\nDuplicate Rows:")
print(df.duplicated())


# -------------------------
# 23. Number of Duplicate Rows
# -------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# -------------------------
# 24. Basic Statistics
# -------------------------

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())


# -------------------------
# 25. Data Inspection Summary
# -------------------------

print("\n--- Data Inspection Summary ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

या file मधून मुख्य workflow
जेव्हा एखादा नवीन dataset मिळतो, तेव्हा students ना असा approach शिकवता येईल:

Dataset
   ↓
head()
   ↓
tail()
   ↓
shape
   ↓
columns
   ↓
dtypes
   ↓
info()
   ↓
describe()
   ↓
missing values
   ↓
duplicates
   ↓
unique values
   ↓
value_counts()

विशेषतः हे commands Data Analysis मध्ये वारंवार वापरले जातात:

df.head()
df.shape
df.info()
df.describe()
df.dtypes
df.isnull().sum()
df.duplicated().sum()

Commit message
Add Pandas data inspection examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण select_filter_sort.py करू — Pandas मधला खूप important practical भाग.



You said:

done

ChatGPT said:
छान 👍 आता Step 28 — select_filter_sort.py.

हा Pandas मधला खूप important भाग आहे, कारण real dataset मध्ये आपल्याला specific rows/columns select, filter आणि sort करावे लागतात.

03-Pandas → Add file → Create new file

File name:

select_filter_sort.py

हा पूर्ण code paste कर:

# Pandas - Select, Filter and Sort

import pandas as pd


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul", "Priya", "Amit",
        "Neha", "Sneha", "Rohit"
    ],
    "Age": [22, 24, 23, 21, 25, 22],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune"
    ],
    "Marks": [80, 90, 75, 88, 67, 95]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# -------------------------
# 2. Select One Column
# -------------------------

print("\nName Column:")
print(df["Name"])


# -------------------------
# 3. Select Multiple Columns
# -------------------------

print("\nName and Marks:")
print(df[["Name", "Marks"]])


# -------------------------
# 4. Select First Row
# -------------------------

print("\nFirst Row:")
print(df.iloc[0])


# -------------------------
# 5. Select First Three Rows
# -------------------------

print("\nFirst Three Rows:")
print(df.iloc[0:3])


# -------------------------
# 6. Select Specific Rows
# -------------------------

print("\nFirst and Third Row:")
print(df.iloc[[0, 2]])


# -------------------------
# 7. Select Rows and Columns
# -------------------------

print("\nFirst Three Rows - Name and Marks:")
print(
    df.iloc[0:3, [0, 3]]
)


# -------------------------
# 8. loc - Label Based Selection
# -------------------------

print("\nUsing loc:")
print(df.loc[0:2, ["Name", "Marks"]])


# -------------------------
# 9. Filter by Marks
# -------------------------

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])


# -------------------------
# 10. Filter by Age
# -------------------------

print("\nStudents with Age > 22:")
print(df[df["Age"] > 22])


# -------------------------
# 11. Filter by City
# -------------------------

print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])


# -------------------------
# 12. Filter using >=
# -------------------------

print("\nStudents with Marks >= 80:")
print(df[df["Marks"] >= 80])


# -------------------------
# 13. Filter using <
# -------------------------

print("\nStudents with Marks < 80:")
print(df[df["Marks"] < 80])


# -------------------------
# 14. Multiple Conditions - AND
# -------------------------

print("\nAge > 22 AND Marks > 80:")

result = df[
    (df["Age"] > 22) &
    (df["Marks"] > 80)
]

print(result)


# -------------------------
# 15. Multiple Conditions - OR
# -------------------------

print("\nAge > 23 OR Marks > 90:")

result = df[
    (df["Age"] > 23) |
    (df["Marks"] > 90)
]

print(result)


# -------------------------
# 16. NOT Condition
# -------------------------

print("\nStudents NOT from Pune:")

result = df[df["City"] != "Pune"]

print(result)


# -------------------------
# 17. isin()
# -------------------------

print("\nStudents from Pune or Mumbai:")

result = df[
    df["City"].isin(["Pune", "Mumbai"])
]

print(result)


# -------------------------
# 18. between()
# -------------------------

print("\nStudents with Marks between 70 and 90:")

result = df[
    df["Marks"].between(70, 90)
]

print(result)


# -------------------------
# 19. Sort Ascending
# -------------------------

print("\nMarks - Ascending:")

result = df.sort_values("Marks")

print(result)


# -------------------------
# 20. Sort Descending
# -------------------------

print("\nMarks - Descending:")

result = df.sort_values(
    "Marks",
    ascending=False
)

print(result)


# -------------------------
# 21. Sort by Multiple Columns
# -------------------------

print("\nSort by City and Marks:")

result = df.sort_values(
    ["City", "Marks"]
)

print(result)


# -------------------------
# 22. Reset Index
# -------------------------

result = df.sort_values(
    "Marks",
    ascending=False
)

result = result.reset_index(drop=True)

print("\nAfter Resetting Index:")
print(result)


# -------------------------
# 23. Data Science Example
# -------------------------

print("\n--- Data Science Example ---")

sales_data = {
    "Product": [
        "Laptop", "Mobile", "Laptop",
        "Tablet", "Mobile", "Monitor"
    ],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune"
    ],
    "Sales": [
        55000, 25000, 65000,
        18000, 30000, 22000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Sales above 30000

print("\nSales above 30000:")
print(
    sales_df[
        sales_df["Sales"] > 30000
    ]
)


# Sales from Pune

print("\nSales from Pune:")
print(
    sales_df[
        sales_df["City"] == "Pune"
    ]
)


# Highest Sales

print("\nHighest Sales:")
print(
    sales_df.sort_values(
        "Sales",
        ascending=False
    ).head(1)
)

या file मध्ये important concepts
Selecting Columns
Selecting Rows
iloc
loc
Filtering
Comparison Operators
AND &
OR |
NOT !=
isin()
between()
sort_values()
reset_index()

दोन गोष्टी students ना नक्की explain कर
AND condition:

(df["Age"] > 22) & (df["Marks"] > 80)

OR condition:

(df["Age"] > 23) | (df["Marks"] > 90)

Pandas मध्ये multiple conditions वापरताना and / or ऐवजी & / | वापरतो आणि conditions parentheses मध्ये ठेवतो.

Commit message
Add Pandas selection filtering and sorting examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण missing_values.py करू — real-world data cleaning मधला खूप important भाग.



You said:

done

ChatGPT said:
छान 👍 आता Step 29 — missing_values.py.

Real-world datasets मध्ये missing data खूप common असतो. त्यामुळे हा topic Data Science training साठी महत्त्वाचा आहे.

03-Pandas → Add file → Create new file

File name:

missing_values.py

हा पूर्ण code paste कर:

# Pandas - Handling Missing Values

import pandas as pd
import numpy as np


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha",
        "Sneha"
    ],
    "Age": [22, 24, np.nan, 21, 25],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        np.nan,
        "Mumbai"
    ],
    "Marks": [80, np.nan, 75, 88, np.nan]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Check Missing Values
# -------------------------

print("\nIs Null:")
print(df.isnull())


# -------------------------
# 3. Check Missing Values using isna()
# -------------------------

print("\nIs NaN:")
print(df.isna())


# -------------------------
# 4. Count Missing Values
# -------------------------

print("\nMissing Values Count:")
print(df.isnull().sum())


# -------------------------
# 5. Total Missing Values
# -------------------------

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# -------------------------
# 6. Percentage of Missing Values
# -------------------------

print("\nMissing Value Percentage:")

missing_percentage = (
    df.isnull().mean() * 100
)

print(missing_percentage)


# -------------------------
# 7. Rows Having Missing Values
# -------------------------

print("\nRows with Missing Values:")
print(df[df.isnull().any(axis=1)])


# -------------------------
# 8. Rows Without Missing Values
# -------------------------

print("\nRows without Missing Values:")
print(df.dropna())


# -------------------------
# 9. Drop Rows with Missing Values
# -------------------------

clean_df = df.dropna()

print("\nAfter dropna():")
print(clean_df)


# -------------------------
# 10. Fill Missing Values with 0
# -------------------------

filled_zero = df.fillna(0)

print("\nMissing Values Filled with 0:")
print(filled_zero)


# -------------------------
# 11. Fill Missing Age with Mean
# -------------------------

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

print("\nAge after Filling with Mean:")
print(df)


# -------------------------
# 12. Fill Missing Marks with Mean
# -------------------------

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nMarks after Filling with Mean:")
print(df)


# -------------------------
# 13. Fill Missing City with Mode
# -------------------------

df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

print("\nCity after Filling with Mode:")
print(df)


# -------------------------
# 14. Forward Fill
# -------------------------

data = {
    "Sales": [
        1000,
        np.nan,
        1500,
        np.nan,
        2000
    ]
}

sales_df = pd.DataFrame(data)

print("\nSales Data:")
print(sales_df)

print("\nForward Fill:")
print(sales_df.ffill())


# -------------------------
# 15. Backward Fill
# -------------------------

print("\nBackward Fill:")
print(sales_df.bfill())


# -------------------------
# 16. Replace Specific Values
# -------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [80, -1, 90]
}

marks_df = pd.DataFrame(data)

print("\nOriginal Marks Data:")
print(marks_df)

marks_df["Marks"] = marks_df["Marks"].replace(
    -1,
    np.nan
)

print("\nAfter Replacing -1 with NaN:")
print(marks_df)


# -------------------------
# 17. Fill Replaced Value
# -------------------------

marks_df["Marks"] = marks_df["Marks"].fillna(
    marks_df["Marks"].mean()
)

print("\nAfter Filling Missing Marks:")
print(marks_df)


# -------------------------
# 18. Data Science Example
# -------------------------

employee_data = {
    "Employee": [
        "A", "B", "C", "D", "E"
    ],
    "Salary": [
        30000,
        40000,
        np.nan,
        50000,
        np.nan
    ],
    "Experience": [
        2,
        4,
        3,
        np.nan,
        5
    ]
}

employee_df = pd.DataFrame(employee_data)

print("\nEmployee Data:")
print(employee_df)

print("\nMissing Values:")
print(employee_df.isnull().sum())


# Fill Salary with Median

employee_df["Salary"] = employee_df["Salary"].fillna(
    employee_df["Salary"].median()
)


# Fill Experience with Mean

employee_df["Experience"] = employee_df["Experience"].fillna(
    employee_df["Experience"].mean()
)

print("\nCleaned Employee Data:")
print(employee_df)

या file मध्ये आपण काय cover केलं?
NaN
None
isnull()
isna()
sum()
dropna()
fillna()
mean()
median()
mode()
ffill()
bfill()
replace()
Missing Value Percentage

Trainer म्हणून एक important point
Missing value दिसला की नेहमी fillna(0) करायचा नसतो.

उदाहरण:

df["Age"].fillna(df["Age"].mean())

Numerical data मध्ये mean/median वापरला जाऊ शकतो, पण कोणती method वापरायची हे data आणि business context वर depend करते.

Categorical column साठी:

df["City"].fillna(df["City"].mode()[0])

असा approach वापरता येतो.

आणि काही cases मध्ये missing rows काढणे योग्य असू शकते:

df.dropna()

म्हणजे students ना missing value handling = one fixed rule नाही हेही समजेल.

Commit message
Add Pandas missing values examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण duplicates.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 30 — duplicates.py.

Real-world data मध्ये duplicate records खूप common असतात. हा file students ना duplicate rows identify आणि remove कसे करायचे ते शिकवेल.

03-Pandas → Add file → Create new file

File name:

duplicates.py

हा पूर्ण code paste कर:

# Pandas - Handling Duplicate Data

import pandas as pd


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Rahul",
        "Neha",
        "Priya"
    ],
    "Age": [
        22,
        24,
        23,
        22,
        21,
        24
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Pune",
        "Nashik",
        "Mumbai"
    ],
    "Marks": [
        80,
        90,
        75,
        80,
        88,
        90
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Check Duplicate Rows
# -------------------------

print("\nDuplicate Rows:")
print(df.duplicated())


# -------------------------
# 3. Count Duplicate Rows
# -------------------------

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# -------------------------
# 4. Display Only Duplicate Rows
# -------------------------

print("\nDuplicate Records:")

duplicates = df[
    df.duplicated()
]

print(duplicates)


# -------------------------
# 5. Keep First Occurrence
# -------------------------

print("\nKeep First Occurrence:")

print(
    df.duplicated(
        keep="first"
    )
)


# -------------------------
# 6. Keep Last Occurrence
# -------------------------

print("\nKeep Last Occurrence:")

print(
    df.duplicated(
        keep="last"
    )
)


# -------------------------
# 7. Remove Duplicate Rows
# -------------------------

clean_df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(clean_df)


# -------------------------
# 8. Remove Duplicates Permanently
# -------------------------

df = df.drop_duplicates()

print("\nClean Dataset:")
print(df)


# -------------------------
# 9. Duplicate Based on One Column
# -------------------------

data = {
    "Customer_ID": [
        101,
        102,
        103,
        101,
        104,
        102
    ],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Rahul",
        "Neha",
        "Priya"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Pune",
        "Nashik",
        "Mumbai"
    ]
}

customer_df = pd.DataFrame(data)

print("\nCustomer Data:")
print(customer_df)


# -------------------------
# 10. Check Duplicate Customer IDs
# -------------------------

print("\nDuplicate Customer IDs:")

print(
    customer_df[
        customer_df.duplicated(
            subset="Customer_ID"
        )
    ]
)


# -------------------------
# 11. Remove Duplicate Customer IDs
# -------------------------

unique_customers = customer_df.drop_duplicates(
    subset="Customer_ID"
)

print("\nUnique Customers:")
print(unique_customers)


# -------------------------
# 12. Keep Last Record
# -------------------------

unique_customers_last = customer_df.drop_duplicates(
    subset="Customer_ID",
    keep="last"
)

print("\nUnique Customers - Keep Last:")
print(unique_customers_last)


# -------------------------
# 13. Duplicate Check Before and After
# -------------------------

print("\nDuplicate Count Before Cleaning:")

print(
    customer_df.duplicated(
        subset="Customer_ID"
    ).sum()
)

clean_customer_df = customer_df.drop_duplicates(
    subset="Customer_ID"
)

print("\nDuplicate Count After Cleaning:")

print(
    clean_customer_df.duplicated(
        subset="Customer_ID"
    ).sum()
)


# -------------------------
# 14. Data Science Example
# -------------------------

sales_data = {
    "Order_ID": [
        1001,
        1002,
        1003,
        1001,
        1004,
        1002
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Monitor",
        "Mobile"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        55000,
        22000,
        25000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)

print("\nDuplicate Orders:")

print(
    sales_df[
        sales_df.duplicated(
            subset="Order_ID"
        )
    ]
)

clean_sales = sales_df.drop_duplicates(
    subset="Order_ID"
)

print("\nClean Sales Data:")
print(clean_sales)

या file मध्ये important concepts
duplicated()
duplicated().sum()
drop_duplicates()
keep="first"
keep="last"
subset=

एक important difference
पूर्ण row duplicate आहे का हे check करण्यासाठी:

df.duplicated()

पण specific column वर duplicate check करायचा असेल:

df.duplicated(
    subset="Customer_ID"
)

आणि duplicate records काढण्यासाठी:

df.drop_duplicates(
    subset="Customer_ID"
)

हा Customer ID / Order ID चा example real-world data cleaning मध्ये खूप useful आहे.

Commit message
Add Pandas duplicate data handling examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण data_transformation.py करू — columns create/update, apply(), map(), replace() वगैरे.



You said:

done

ChatGPT said:
छान 👍 आता Step 31 — data_transformation.py.

हा file Pandas मध्ये data ला modify/transform करण्यासाठी आहे. Data Science मध्ये हा भाग खूप वापरला जातो.

03-Pandas → Add file → Create new file

File name:

data_transformation.py

हा पूर्ण code paste कर:

# Pandas - Data Transformation

import pandas as pd


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha",
        "Sneha"
    ],
    "Age": [22, 24, 23, 21, 25],
    "Marks": [80, 90, 65, 88, 72],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Add New Column
# -------------------------

df["Passed"] = df["Marks"] >= 40

print("\nAfter Adding Passed Column:")
print(df)


# -------------------------
# 3. Add Column Using Calculation
# -------------------------

df["Bonus_Marks"] = df["Marks"] + 5

print("\nAfter Adding Bonus Marks:")
print(df)


# -------------------------
# 4. Create Percentage
# -------------------------

df["Percentage"] = (
    df["Marks"] / 100 * 100
)

print("\nPercentage:")
print(df)


# -------------------------
# 5. Create Grade
# -------------------------

def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Fail"


df["Grade"] = df["Marks"].apply(get_grade)

print("\nGrade:")
print(df)


# -------------------------
# 6. apply() with Lambda
# -------------------------

df["Marks_Double"] = df["Marks"].apply(
    lambda x: x * 2
)

print("\nMarks Doubled:")
print(df)


# -------------------------
# 7. map()
# -------------------------

city_mapping = {
    "Pune": "Maharashtra",
    "Mumbai": "Maharashtra",
    "Nashik": "Maharashtra"
}

df["State"] = df["City"].map(
    city_mapping
)

print("\nState Column:")
print(df)


# -------------------------
# 8. replace()
# -------------------------

df["City"] = df["City"].replace(
    "Mumbai",
    "Bombay"
)

print("\nAfter Replacing Mumbai:")
print(df)


# -------------------------
# 9. Rename Column
# -------------------------

df.rename(
    columns={
        "Marks": "Score"
    },
    inplace=True
)

print("\nAfter Renaming Marks:")
print(df)


# -------------------------
# 10. Update Values
# -------------------------

df["Score"] = df["Score"] + 2

print("\nAfter Increasing Score:")
print(df)


# -------------------------
# 11. Create Category
# -------------------------

df["Performance"] = df["Score"].apply(
    lambda x: (
        "Excellent" if x >= 90
        else "Good" if x >= 75
        else "Average" if x >= 60
        else "Needs Improvement"
    )
)

print("\nPerformance Category:")
print(df)


# -------------------------
# 12. Conditional Transformation
# -------------------------

df["Result"] = "Fail"

df.loc[
    df["Score"] >= 40,
    "Result"
] = "Pass"

print("\nResult:")
print(df)


# -------------------------
# 13. Create Salary Data
# -------------------------

employee_data = {
    "Employee": [
        "A", "B", "C", "D"
    ],
    "Salary": [
        30000,
        40000,
        50000,
        60000
    ]
}

employee_df = pd.DataFrame(employee_data)

print("\nEmployee Data:")
print(employee_df)


# -------------------------
# 14. Calculate Annual Salary
# -------------------------

employee_df["Annual_Salary"] = (
    employee_df["Salary"] * 12
)

print("\nAnnual Salary:")
print(employee_df)


# -------------------------
# 15. Salary Category
# -------------------------

employee_df["Salary_Category"] = employee_df[
    "Salary"
].apply(
    lambda x: (
        "High" if x >= 50000
        else "Medium" if x >= 40000
        else "Low"
    )
)

print("\nSalary Category:")
print(employee_df)


# -------------------------
# 16. Data Science Example
# -------------------------

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Price": [
        55000,
        25000,
        18000,
        22000
    ],
    "Quantity": [
        2,
        5,
        3,
        4
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Total Sales

sales_df["Total_Sales"] = (
    sales_df["Price"] *
    sales_df["Quantity"]
)

print("\nTotal Sales:")
print(sales_df)


# Discount

sales_df["Discount"] = (
    sales_df["Total_Sales"] * 0.10
)

print("\nDiscount:")
print(sales_df)


# Final Amount

sales_df["Final_Amount"] = (
    sales_df["Total_Sales"] -
    sales_df["Discount"]
)

print("\nFinal Amount:")
print(sales_df)

यात काय cover झालं?
Adding Columns
Updating Columns
Calculations
apply()
lambda
map()
replace()
rename()
loc
Conditional Transformation
Categories
Business Calculations

apply() समजण्यासाठी
df["Grade"] = df["Marks"].apply(get_grade)

प्रत्येक Marks value get_grade() function मध्ये जाते.

उदा.:

90 → A
80 → B
65 → C

map() समजण्यासाठी
city_mapping = {
    "Pune": "Maharashtra",
    "Mumbai": "Maharashtra"
}

आणि:

df["State"] = df["City"].map(city_mapping)

यामुळे existing values चे mapping करून नवीन column तयार करता येतो.

शेवटचा Sales example
हा Data Science/business analysis साठी useful आहे:

Price × Quantity
       ↓
Total Sales
       ↓
Discount
       ↓
Final Amount

Commit message
Add Pandas data transformation examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण groupby_aggregation.py करू — Pandas चा अत्यंत important Data Analysis topic.



You said:

done

ChatGPT said:
छान 👍 आता Step 32 — groupby_aggregation.py.

हा topic Data Analysis मध्ये खूप important आहे, कारण groupby() वापरून आपण category-wise analysis करू शकतो.

03-Pandas → Add file → Create new file

File name:

groupby_aggregation.py

हा code paste कर:

# Pandas - GroupBy and Aggregation

import pandas as pd


# -------------------------
# 1. Create Sales Dataset
# -------------------------

data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Tablet",
        "Mobile",
        "Monitor",
        "Tablet",
        "Laptop"
    ],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai",
        "Pune",
        "Nashik",
        "Mumbai"
    ],
    "Sales": [
        55000,
        25000,
        65000,
        18000,
        30000,
        22000,
        20000,
        60000
    ],
    "Quantity": [
        2,
        5,
        3,
        3,
        6,
        4,
        5,
        2
    ]
}

df = pd.DataFrame(data)

print("Sales Dataset:")
print(df)


# -------------------------
# 2. GroupBy - One Column
# -------------------------

print("\nSales by City:")

city_sales = df.groupby("City")["Sales"].sum()

print(city_sales)


# -------------------------
# 3. Average Sales by City
# -------------------------

print("\nAverage Sales by City:")

average_sales = df.groupby("City")["Sales"].mean()

print(average_sales)


# -------------------------
# 4. Maximum Sales by City
# -------------------------

print("\nMaximum Sales by City:")

max_sales = df.groupby("City")["Sales"].max()

print(max_sales)


# -------------------------
# 5. Minimum Sales by City
# -------------------------

print("\nMinimum Sales by City:")

min_sales = df.groupby("City")["Sales"].min()

print(min_sales)


# -------------------------
# 6. Total Quantity by City
# -------------------------

print("\nTotal Quantity by City:")

quantity_by_city = df.groupby("City")["Quantity"].sum()

print(quantity_by_city)


# -------------------------
# 7. GroupBy Product
# -------------------------

print("\nSales by Product:")

product_sales = df.groupby(
    "Product"
)["Sales"].sum()

print(product_sales)


# -------------------------
# 8. Multiple Aggregations
# -------------------------

print("\nMultiple Statistics:")

result = df.groupby("City")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)

print(result)


# -------------------------
# 9. Aggregation on Multiple Columns
# -------------------------

print("\nMultiple Column Aggregation:")

result = df.groupby("City").agg(
    {
        "Sales": ["sum", "mean"],
        "Quantity": ["sum", "mean"]
    }
)

print(result)


# -------------------------
# 10. GroupBy Multiple Columns
# -------------------------

print("\nCity and Product Wise Sales:")

result = df.groupby(
    ["City", "Product"]
)["Sales"].sum()

print(result)


# -------------------------
# 11. GroupBy with as_index=False
# -------------------------

print("\nGroupBy with Normal Columns:")

result = df.groupby(
    "City",
    as_index=False
)["Sales"].sum()

print(result)


# -------------------------
# 12. Sort Grouped Result
# -------------------------

print("\nCities Sorted by Sales:")

result = (
    df.groupby(
        "City",
        as_index=False
    )["Sales"]
    .sum()
    .sort_values(
        "Sales",
        ascending=False
    )
)

print(result)


# -------------------------
# 13. Product Performance
# -------------------------

print("\nProduct Performance:")

product_performance = (
    df.groupby(
        "Product",
        as_index=False
    )
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean"),
        Total_Quantity=("Quantity", "sum")
    )
)

print(product_performance)


# -------------------------
# 14. Highest Selling Product
# -------------------------

print("\nHighest Selling Product:")

highest_product = product_performance.sort_values(
    "Total_Sales",
    ascending=False
).head(1)

print(highest_product)


# -------------------------
# 15. City Performance
# -------------------------

print("\nCity Performance:")

city_performance = (
    df.groupby(
        "City",
        as_index=False
    )
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean"),
        Total_Quantity=("Quantity", "sum")
    )
)

print(city_performance)


# -------------------------
# 16. Count Records by City
# -------------------------

print("\nNumber of Records by City:")

print(
    df["City"].value_counts()
)


# -------------------------
# 17. Data Science Example
# -------------------------

student_data = {
    "Student": [
        "A", "B", "C", "D",
        "E", "F", "G", "H"
    ],
    "Subject": [
        "Python", "Python",
        "SQL", "SQL",
        "Python", "SQL",
        "Python", "SQL"
    ],
    "Marks": [
        80, 90, 75, 85,
        88, 92, 70, 78
    ]
}

student_df = pd.DataFrame(student_data)

print("\nStudent Data:")
print(student_df)


# Average marks by subject

print("\nAverage Marks by Subject:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].mean()
)


# Highest marks by subject

print("\nHighest Marks by Subject:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].max()
)


# Multiple statistics

print("\nSubject-wise Statistics:")

print(
    student_df.groupby(
        "Subject"
    )["Marks"].agg(
        ["count", "mean", "min", "max"]
    )
)

यामध्ये मुख्य concepts
groupby()
sum()
mean()
min()
max()
count()
agg()
as_index=False
GroupBy multiple columns
Sorting grouped data
Named aggregation

groupby() सोप्या भाषेत
समजा:

df.groupby("City")["Sales"].sum()

याचा अर्थ:

City नुसार data group करा
        ↓
प्रत्येक City ची Sales घ्या
        ↓
Sales ची total करा

Result साधारण:

Mumbai    115000
Pune      142000
Nashik     38000

असा येईल.

agg() का important आहे?
एकाच वेळी अनेक calculations:

df.groupby("City")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)

म्हणजे प्रत्येक city साठी:

Total Sales

Average Sales

Minimum Sales

Maximum Sales

Number of records

एकाच operation मध्ये मिळतात.

Commit message
Add Pandas groupby and aggregation examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण merge_concat.py करू — दोन किंवा अधिक datasets एकत्र कसे करायचे ते.



You said:

done

ChatGPT said:
छान 👍 आता Step 33 — merge_concat.py.

हा भाग real-world Data Science मध्ये खूप useful आहे. वेगवेगळ्या files/tables मधला data एकत्र करण्यासाठी merge() आणि concat() वापरतो.

03-Pandas → Add file → Create new file

File name:

merge_concat.py

हा पूर्ण code paste कर:

# Pandas - Merge and Concat

import pandas as pd


# ==================================================
# PART 1 - CONCAT
# ==================================================


# -------------------------
# 1. Create First DataFrame
# -------------------------

df1 = pd.DataFrame({
    "Name": ["Rahul", "Priya"],
    "Marks": [80, 90]
})

print("DataFrame 1:")
print(df1)


# -------------------------
# 2. Create Second DataFrame
# -------------------------

df2 = pd.DataFrame({
    "Name": ["Amit", "Neha"],
    "Marks": [75, 88]
})

print("\nDataFrame 2:")
print(df2)


# -------------------------
# 3. Concatenate Rows
# -------------------------

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("\nAfter Row-wise Concatenation:")
print(result)


# -------------------------
# 4. Concatenate Columns
# -------------------------

df3 = pd.DataFrame({
    "Age": [22, 24]
})

df4 = pd.DataFrame({
    "City": ["Pune", "Mumbai"]
})

result = pd.concat(
    [df3, df4],
    axis=1
)

print("\nColumn-wise Concatenation:")
print(result)


# ==================================================
# PART 2 - MERGE
# ==================================================


# -------------------------
# 5. Student Data
# -------------------------

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ]
})

print("\nStudents:")
print(students)


# -------------------------
# 6. Marks Data
# -------------------------

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Marks": [80, 90, 75, 88]
})

print("\nMarks:")
print(marks)


# -------------------------
# 7. Inner Merge
# -------------------------

inner_merge = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)

print("\nInner Merge:")
print(inner_merge)


# -------------------------
# 8. Left Merge
# -------------------------

left_merge = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)

print("\nLeft Merge:")
print(left_merge)


# -------------------------
# 9. Right Merge
# -------------------------

right_merge = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="right"
)

print("\nRight Merge:")
print(right_merge)


# -------------------------
# 10. Outer Merge
# -------------------------

outer_merge = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)

print("\nOuter Merge:")
print(outer_merge)


# ==================================================
# PART 3 - MERGE USING DIFFERENT COLUMN NAMES
# ==================================================


# -------------------------
# 11. Customer Data
# -------------------------

customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3],
    "Name": [
        "Rahul",
        "Priya",
        "Amit"
    ]
})

print("\nCustomers:")
print(customers)


# -------------------------
# 12. Orders Data
# -------------------------

orders = pd.DataFrame({
    "Cust_ID": [1, 2, 3],
    "Amount": [
        5000,
        7000,
        4500
    ]
})

print("\nOrders:")
print(orders)


# -------------------------
# 13. Merge Different Column Names
# -------------------------

result = pd.merge(
    customers,
    orders,
    left_on="Customer_ID",
    right_on="Cust_ID",
    how="inner"
)

print("\nMerge Using Different Column Names:")
print(result)


# ==================================================
# PART 4 - MULTIPLE DATASETS
# ==================================================


# -------------------------
# 14. Employee Data
# -------------------------

employee = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Name": [
        "A", "B", "C"
    ]
})


# -------------------------
# 15. Salary Data
# -------------------------

salary = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Salary": [
        30000,
        40000,
        50000
    ]
})


# -------------------------
# 16. Department Data
# -------------------------

department = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Department": [
        "IT",
        "HR",
        "Sales"
    ]
})


# -------------------------
# 17. Merge Employee + Salary
# -------------------------

employee_salary = pd.merge(
    employee,
    salary,
    on="Employee_ID"
)

print("\nEmployee + Salary:")
print(employee_salary)


# -------------------------
# 18. Merge Final Dataset
# -------------------------

final_employee_data = pd.merge(
    employee_salary,
    department,
    on="Employee_ID"
)

print("\nFinal Employee Dataset:")
print(final_employee_data)


# ==================================================
# PART 5 - PRACTICAL DATA SCIENCE EXAMPLE
# ==================================================


# -------------------------
# 19. Customer Information
# -------------------------

customer_data = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104],
    "Customer_Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ]
})


# -------------------------
# 20. Sales Information
# -------------------------

sales_data = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 105],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        22000
    ]
})


# -------------------------
# 21. Combine Customer and Sales
# -------------------------

customer_sales = pd.merge(
    customer_data,
    sales_data,
    on="Customer_ID",
    how="left"
)

print("\nCustomer Sales Data:")
print(customer_sales)


# -------------------------
# 22. Check Missing Sales
# -------------------------

print("\nMissing Sales:")
print(
    customer_sales["Sales"].isnull().sum()
)


# -------------------------
# 23. Fill Missing Sales
# -------------------------

customer_sales["Sales"] = customer_sales[
    "Sales"
].fillna(0)

print("\nFinal Customer Sales Data:")
print(customer_sales)


# -------------------------
# 24. Total Sales
# -------------------------

print("\nTotal Sales:")

print(
    customer_sales["Sales"].sum()
)

concat() आणि merge() मधला फरक
concat()
जेव्हा datasets चे rows किंवा columns जोडायचे असतात:

pd.concat([df1, df2])

उदा.:

Dataset 1
   ↓
Dataset 2
   ↓
एकाच table मध्ये

merge()
जेव्हा दोन datasets मध्ये common key/column असतो:

pd.merge(
    students,
    marks,
    on="Student_ID"
)

उदा.:

Students Table
Student_ID
    +
Marks Table
Student_ID
    ↓
Combined Dataset

Merge चे 4 important types
inner
left
right
outer

हे students ना Venn-diagram सारखं समजावून सांगता येतं.

Commit message
Add Pandas merge and concat examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण string_datetime.py करू — text आणि date columns सोबत काम करणे.



You said:

done

ChatGPT said:
छान 👍 आता Step 34 — string_datetime.py.

हा file Pandas मध्ये text/string data आणि date-time data handle करण्यासाठी आहे. Real datasets मध्ये customer names, cities, emails, dates, transactions अशा columns वर हे operations खूप वापरले जातात.

03-Pandas → Add file → Create new file

File name:

string_datetime.py

हा code paste कर:

# Pandas - String and DateTime Operations

import pandas as pd


# ==================================================
# PART 1 - STRING OPERATIONS
# ==================================================


# -------------------------
# 1. Create Dataset
# -------------------------

data = {
    "Name": [
        "Rahul Patil",
        "Priya Sharma",
        "Amit Joshi",
        "Neha Kulkarni"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik"
    ],
    "Email": [
        "rahul@gmail.com",
        "priya@gmail.com",
        "amit@gmail.com",
        "neha@gmail.com"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# -------------------------
# 2. Convert Text to Uppercase
# -------------------------

df["Name_Upper"] = df["Name"].str.upper()

print("\nUppercase Names:")
print(df["Name_Upper"])


# -------------------------
# 3. Convert Text to Lowercase
# -------------------------

df["Name_Lower"] = df["Name"].str.lower()

print("\nLowercase Names:")
print(df["Name_Lower"])


# -------------------------
# 4. Convert Text to Title Case
# -------------------------

df["Name_Title"] = df["Name"].str.title()

print("\nTitle Case Names:")
print(df["Name_Title"])


# -------------------------
# 5. String Length
# -------------------------

df["Name_Length"] = df["Name"].str.len()

print("\nName Length:")
print(df[["Name", "Name_Length"]])


# -------------------------
# 6. Check String Contains
# -------------------------

print("\nNames containing 'Rahul':")

print(
    df[df["Name"].str.contains(
        "Rahul",
        case=False,
        na=False
    )]
)


# -------------------------
# 7. City Contains 'Pune'
# -------------------------

print("\nCustomers from Pune:")

print(
    df[df["City"].str.contains(
        "Pune",
        case=False,
        na=False
    )]
)


# -------------------------
# 8. String Starts With
# -------------------------

print("\nNames starting with 'P':")

print(
    df[df["Name"].str.startswith(
        "P"
    )]
)


# -------------------------
# 9. String Ends With
# -------------------------

print("\nEmails ending with gmail.com:")

print(
    df[df["Email"].str.endswith(
        "gmail.com"
    )]
)


# -------------------------
# 10. Replace Text
# -------------------------

df["City"] = df["City"].str.replace(
    "Mumbai",
    "Bombay",
    regex=False
)

print("\nAfter Replacing Mumbai:")
print(df)


# -------------------------
# 11. Split String
# -------------------------

df["First_Name"] = df["Name"].str.split().str[0]

df["Last_Name"] = df["Name"].str.split().str[1]

print("\nFirst and Last Names:")
print(
    df[
        ["Name", "First_Name", "Last_Name"]
    ]
)


# -------------------------
# 12. Remove Extra Spaces
# -------------------------

data = {
    "Name": [
        " Rahul ",
        " Priya",
        "Amit ",
        " Neha "
    ]
}

space_df = pd.DataFrame(data)

print("\nData with Extra Spaces:")
print(space_df)

space_df["Name"] = space_df[
    "Name"
].str.strip()

print("\nAfter Removing Spaces:")
print(space_df)


# ==================================================
# PART 2 - DATETIME OPERATIONS
# ==================================================


# -------------------------
# 13. Create Date Data
# -------------------------

date_data = {
    "Customer": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ],
    "Order_Date": [
        "2025-01-15",
        "2025-02-20",
        "2025-03-10",
        "2025-04-25"
    ]
}

date_df = pd.DataFrame(date_data)

print("\nOriginal Date Data:")
print(date_df)


# -------------------------
# 14. Convert to Datetime
# -------------------------

date_df["Order_Date"] = pd.to_datetime(
    date_df["Order_Date"]
)

print("\nConverted Date:")
print(date_df)


# -------------------------
# 15. Extract Year
# -------------------------

date_df["Year"] = date_df[
    "Order_Date"
].dt.year

print("\nYear:")
print(date_df)


# -------------------------
# 16. Extract Month
# -------------------------

date_df["Month"] = date_df[
    "Order_Date"
].dt.month

print("\nMonth:")
print(date_df)


# -------------------------
# 17. Extract Day
# -------------------------

date_df["Day"] = date_df[
    "Order_Date"
].dt.day

print("\nDay:")
print(date_df)


# -------------------------
# 18. Extract Day Name
# -------------------------

date_df["Day_Name"] = date_df[
    "Order_Date"
].dt.day_name()

print("\nDay Name:")
print(date_df)


# -------------------------
# 19. Extract Month Name
# -------------------------

date_df["Month_Name"] = date_df[
    "Order_Date"
].dt.month_name()

print("\nMonth Name:")
print(date_df)


# -------------------------
# 20. Extract Quarter
# -------------------------

date_df["Quarter"] = date_df[
    "Order_Date"
].dt.quarter

print("\nQuarter:")
print(date_df)


# -------------------------
# 21. Filter by Year
# -------------------------

print("\nOrders from 2025:")

print(
    date_df[
        date_df["Year"] == 2025
    ]
)


# -------------------------
# 22. Sort by Date
# -------------------------

print("\nSorted by Date:")

print(
    date_df.sort_values(
        "Order_Date"
    )
)


# -------------------------
# 23. Date Difference
# -------------------------

today = pd.Timestamp("2025-05-01")

date_df["Days_From_Order"] = (
    today - date_df["Order_Date"]
).dt.days

print("\nDays From Order:")
print(date_df)


# -------------------------
# 24. Date Range
# -------------------------

dates = pd.date_range(
    start="2025-01-01",
    end="2025-01-10"
)

print("\nDate Range:")
print(dates)


# -------------------------
# 25. Monthly Date Range
# -------------------------

monthly_dates = pd.date_range(
    start="2025-01-01",
    periods=6,
    freq="ME"
)

print("\nMonthly Dates:")
print(monthly_dates)


# ==================================================
# PART 3 - PRACTICAL DATA SCIENCE EXAMPLE
# ==================================================


sales_data = {
    "Customer": [
        "Rahul Patil",
        "Priya Sharma",
        "Amit Joshi",
        "Neha Kulkarni"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Nashik"
    ],
    "Order_Date": [
        "2025-01-10",
        "2025-01-15",
        "2025-02-10",
        "2025-02-20"
    ],
    "Sales": [
        50000,
        30000,
        45000,
        25000
    ]
}

sales_df = pd.DataFrame(sales_data)


# Convert date

sales_df["Order_Date"] = pd.to_datetime(
    sales_df["Order_Date"]
)


# Extract Month

sales_df["Month"] = sales_df[
    "Order_Date"
].dt.month_name()


# Extract Year

sales_df["Year"] = sales_df[
    "Order_Date"
].dt.year


print("\nSales Data:")
print(sales_df)


# -------------------------
# Monthly Sales
# -------------------------

print("\nMonthly Sales:")

monthly_sales = sales_df.groupby(
    "Month"
)["Sales"].sum()

print(monthly_sales)


# -------------------------
# Sales by City
# -------------------------

print("\nSales by City:")

city_sales = sales_df.groupby(
    "City"
)["Sales"].sum()

print(city_sales)

यात important concepts
String operations
.str.upper()
.str.lower()
.str.title()
.str.len()
.str.contains()
.str.startswith()
.str.endswith()
.str.replace()
.str.split()
.str.strip()

Date-time operations
pd.to_datetime()
.dt.year
.dt.month
.dt.day
.dt.day_name()
.dt.month_name()
.dt.quarter
pd.date_range()

एक important pattern
Date column वर:

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)

केल्यानंतर आपण:

df["Order_Date"].dt.year

किंवा:

df["Order_Date"].dt.month

असे operations करू शकतो.

Commit message
Add Pandas string and datetime examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण index_columns.py करू — index, rename, reset index आणि column management.



You said:

done

ChatGPT said:
छान 👍 आता Step 35 — index_columns.py.

हा file Pandas मध्ये Index आणि Columns व्यवस्थित manage करण्यासाठी आहे. Data cleaning आणि analysis करताना हे concepts वारंवार लागतात.

03-Pandas → Add file → Create new file

File name:

index_columns.py

हा code paste कर:

# Pandas - Index and Column Management

import pandas as pd


# -------------------------
# 1. Create DataFrame
# -------------------------

data = {
    "Student_ID": [101, 102, 103, 104],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha"
    ],
    "Age": [22, 24, 23, 21],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# -------------------------
# 2. View Index
# -------------------------

print("\nIndex:")
print(df.index)


# -------------------------
# 3. View Columns
# -------------------------

print("\nColumns:")
print(df.columns)


# -------------------------
# 4. Set a Column as Index
# -------------------------

df_indexed = df.set_index(
    "Student_ID"
)

print("\nStudent_ID as Index:")
print(df_indexed)


# -------------------------
# 5. Access Data Using Index
# -------------------------

print("\nStudent 101:")
print(df_indexed.loc[101])


# -------------------------
# 6. Access Multiple Index Values
# -------------------------

print("\nStudents 101 and 103:")

print(
    df_indexed.loc[[101, 103]]
)


# -------------------------
# 7. Reset Index
# -------------------------

reset_df = df_indexed.reset_index()

print("\nAfter Resetting Index:")
print(reset_df)


# -------------------------
# 8. Set Index Permanently
# -------------------------

df.set_index(
    "Student_ID",
    inplace=True
)

print("\nPermanent Index:")
print(df)


# -------------------------
# 9. Reset Index Permanently
# -------------------------

df.reset_index(
    inplace=True
)

print("\nIndex Reset:")
print(df)


# -------------------------
# 10. Rename Columns
# -------------------------

df.rename(
    columns={
        "Student_ID": "ID",
        "Marks": "Score"
    },
    inplace=True
)

print("\nRenamed Columns:")
print(df)


# -------------------------
# 11. Rename All Columns
# -------------------------

df.columns = [
    "Student_ID",
    "Student_Name",
    "Student_Age",
    "Student_Score"
]

print("\nAll Columns Renamed:")
print(df)


# -------------------------
# 12. Add New Column
# -------------------------

df["Result"] = "Pass"

print("\nNew Column Added:")
print(df)


# -------------------------
# 13. Add Column at Specific Position
# -------------------------

df.insert(
    1,
    "Department",
    [
        "IT",
        "HR",
        "IT",
        "Sales"
    ]
)

print("\nColumn Inserted:")
print(df)


# -------------------------
# 14. Move Column
# -------------------------

result_column = df.pop("Result")

df["Result"] = result_column

print("\nResult Column Moved:")
print(df)


# -------------------------
# 15. Delete a Column
# -------------------------

df_without_department = df.drop(
    columns=["Department"]
)

print("\nAfter Removing Department:")
print(df_without_department)


# -------------------------
# 16. Drop Multiple Columns
# -------------------------

result = df.drop(
    columns=[
        "Department",
        "Result"
    ]
)

print("\nAfter Removing Multiple Columns:")
print(result)


# -------------------------
# 17. Reorder Columns
# -------------------------

result = df[
    [
        "Student_ID",
        "Student_Name",
        "Department",
        "Student_Age",
        "Student_Score",
        "Result"
    ]
]

print("\nReordered Columns:")
print(result)


# -------------------------
# 18. Check Column Names
# -------------------------

print("\nColumn Names:")
print(list(df.columns))


# -------------------------
# 19. Check Index Values
# -------------------------

print("\nIndex Values:")
print(df.index.tolist())


# -------------------------
# 20. Data Science Example
# -------------------------

sales_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        22000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(sales_df)


# Set Order_ID as index

sales_df.set_index(
    "Order_ID",
    inplace=True
)

print("\nOrder_ID as Index:")
print(sales_df)


# Access one order

print("\nOrder 1001:")
print(sales_df.loc[1001])


# Reset index

sales_df.reset_index(
    inplace=True
)

print("\nAfter Reset:")
print(sales_df)

या file मधून काय cover झालं?
df.index
df.columns
set_index()
reset_index()
loc[]
rename()
columns =
insert()
pop()
drop()
Column Reordering

set_index() समजून घे
Normal DataFrame:

Student_ID | Name  | Marks
101        | Rahul | 80
102        | Priya | 90

जेव्हा:

df.set_index("Student_ID")

करतो:

Student_ID
101 | Rahul | 80
102 | Priya | 90

म्हणजे Student_ID हा DataFrame चा index होतो.

reset_index()
पुन्हा normal structure मध्ये आणण्यासाठी:

df.reset_index()

Commit message
Add Pandas index and column management examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण practice.py तयार करू — आतापर्यंतच्या Pandas concepts वर practical exercises.



You said:

done

ChatGPT said:
छान 👍 आता Step 36 — practice.py.

हा आपल्या 03-Pandas folder मधला practice file असेल. यात direct answers न देता students ना स्वतः code लिहिता येईल असे exercises ठेवू.

03-Pandas → Add file → Create new file

File name:

practice.py

हा code paste कर:

# Pandas - Practice Exercises

import pandas as pd
import numpy as np


# ==================================================
# PRACTICE DATASET
# ==================================================

data = {
    "Employee_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110
    ],
    "Name": [
        "Rahul", "Priya", "Amit", "Neha", "Sneha",
        "Rohit", "Pooja", "Kiran", "Anjali", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Sales", "IT", "HR", "Sales"
    ],
    "City": [
        "Pune", "Mumbai", "Pune", "Nashik", "Mumbai",
        "Pune", "Nashik", "Pune", "Mumbai", "Pune"
    ],
    "Age": [
        25, 28, 24, 30, 27,
        26, 29, 23, 31, 28
    ],
    "Salary": [
        45000, 50000, 40000, 55000, 48000,
        52000, 46000, 42000, 60000, 58000
    ],
    "Experience": [
        2, 4, 1, 6, 3,
        4, 5, 1, 7, 5
    ]
}

df = pd.DataFrame(data)

print("Employee Dataset:")
print(df)


# ==================================================
# BASIC INSPECTION
# ==================================================

# Exercise 1
# Display the first 5 rows.


# Exercise 2
# Display the last 3 rows.


# Exercise 3
# Find the number of rows and columns.


# Exercise 4
# Display all column names.


# Exercise 5
# Display the data types.


# Exercise 6
# Display basic statistical information.


# ==================================================
# COLUMN SELECTION
# ==================================================

# Exercise 7
# Select only the Name column.


# Exercise 8
# Select Name, Department and Salary.


# Exercise 9
# Select Age and Experience.


# ==================================================
# FILTERING
# ==================================================

# Exercise 10
# Find employees whose salary is greater than 50000.


# Exercise 11
# Find employees whose age is greater than 27.


# Exercise 12
# Find employees from Pune.


# Exercise 13
# Find employees from the IT department.


# Exercise 14
# Find employees whose salary is between 40000 and 50000.


# Exercise 15
# Find employees from Pune AND salary greater than 45000.


# Exercise 16
# Find employees from IT OR Sales department.


# Exercise 17
# Find employees who are NOT from Mumbai.


# ==================================================
# SORTING
# ==================================================

# Exercise 18
# Sort employees by Salary in ascending order.


# Exercise 19
# Sort employees by Salary in descending order.


# Exercise 20
# Sort employees by Experience in descending order.


# Exercise 21
# Sort employees first by Department and then by Salary.


# ==================================================
# COLUMNS AND TRANSFORMATION
# ==================================================

# Exercise 22
# Create a new column:
# Annual_Salary = Salary * 12


# Exercise 23
# Create a new column:
# Experience_Level
#
# If Experience >= 5:
# "Senior"
#
# Otherwise:
# "Junior"


# Exercise 24
# Create a new column:
# Salary_Category
#
# Salary >= 55000 -> High
# Salary >= 45000 -> Medium
# Otherwise -> Low


# Exercise 25
# Increase Salary by 10% and store
# the result in a new column called
# Updated_Salary.


# ==================================================
# GROUPBY
# ==================================================

# Exercise 26
# Find total salary by Department.


# Exercise 27
# Find average salary by Department.


# Exercise 28
# Find maximum salary by Department.


# Exercise 29
# Find minimum salary by Department.


# Exercise 30
# Find employee count by Department.


# Exercise 31
# Find average salary by City.


# Exercise 32
# Find total salary by City.


# ==================================================
# AGGREGATION
# ==================================================

# Exercise 33
# For each Department calculate:
#
# total salary
# average salary
# minimum salary
# maximum salary


# Exercise 34
# For each Department calculate:
#
# employee count
# average age
# average experience


# ==================================================
# STRING OPERATIONS
# ==================================================

# Exercise 35
# Convert employee names to uppercase.


# Exercise 36
# Convert department names to lowercase.


# Exercise 37
# Find employees whose name starts with "P".


# Exercise 38
# Find employees whose city contains "Pune".


# ==================================================
# INDEX OPERATIONS
# ==================================================

# Exercise 39
# Set Employee_ID as the DataFrame index.


# Exercise 40
# Reset the index.


# ==================================================
# MISSING VALUES PRACTICE
# ==================================================

missing_data = {
    "Name": [
        "A", "B", "C", "D", "E"
    ],
    "Age": [
        25, np.nan, 30, 28, np.nan
    ],
    "Salary": [
        40000, 50000, np.nan, 60000, 55000
    ]
}

missing_df = pd.DataFrame(missing_data)

print("\nMissing Value Dataset:")
print(missing_df)


# Exercise 41
# Find the number of missing values
# in each column.


# Exercise 42
# Fill missing Age values
# using the mean.


# Exercise 43
# Fill missing Salary values
# using the median.


# Exercise 44
# Remove rows containing missing values.


# ==================================================
# DUPLICATE PRACTICE
# ==================================================

duplicate_data = {
    "Customer_ID": [
        101, 102, 103, 101, 104, 102
    ],
    "Name": [
        "Rahul", "Priya", "Amit",
        "Rahul", "Neha", "Priya"
    ]
}

duplicate_df = pd.DataFrame(duplicate_data)

print("\nDuplicate Dataset:")
print(duplicate_df)


# Exercise 45
# Find duplicate Customer_ID values.


# Exercise 46
# Remove duplicate Customer_ID records.


# ==================================================
# PRACTICAL DATA ANALYSIS
# ==================================================

sales_data = {
    "Product": [
        "Laptop", "Mobile", "Laptop",
        "Tablet", "Mobile", "Monitor",
        "Laptop", "Tablet"
    ],
    "City": [
        "Pune", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Pune",
        "Mumbai", "Nashik"
    ],
    "Sales": [
        55000, 25000, 65000,
        18000, 30000, 22000,
        60000, 20000
    ],
    "Quantity": [
        2, 5, 3, 3,
        6, 4, 2, 5
    ]
}

sales_df = pd.DataFrame(sales_data)

print("\nSales Dataset:")
print(sales_df)


# Exercise 47
# Calculate Total_Sales:
#
# Sales * Quantity


# Exercise 48
# Find total sales by City.


# Exercise 49
# Find total quantity sold by Product.


# Exercise 50
# Find the product with the highest
# total sales.


# Exercise 51
# Find the city with the highest
# total sales.


# Exercise 52
# Sort the sales data by
# Total_Sales in descending order.


# ==================================================
# FINAL CHALLENGE
# ==================================================

# Use the employee dataset and answer:
#
# 1. Which department has the highest
#    average salary?
#
# 2. What is the average salary of
#    employees from Pune?
#
# 3. How many employees have more
#    than 3 years of experience?
#
# 4. Which employee has the highest salary?
#
# 5. What is the average age of
#    IT employees?
#
# 6. Create a Salary_Category column.
#
# 7. Create an Experience_Level column.
#
# 8. Create Annual_Salary column.
#
# 9. Display employees with salary
#    greater than 50000.
#
# 10. Display the final cleaned and
#     transformed DataFrame.

हा file थोडा वेगळा का ठेवला?
आतापर्यंत आपण प्रत्येक concept चा code + explanation दिला.

आता practice.py मध्ये students स्वतः:

Think
  ↓
Write Code
  ↓
Run Code
  ↓
Check Output
  ↓
Understand

करू शकतात.

तू trainer असल्यामुळे हा format useful राहील — class मध्ये तू questions देऊ शकतेस आणि students कडून code करून घेऊ शकतेस.

Commit message
Add Pandas practice exercises

Commit changes कर.

झाल्यावर done म्हणा. त्यानंतर 03-Pandas मधले अजून 2 शेवटचे practical files करून आपण Pandas section complete करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 37 — read_write_files.py.

हा Pandas section मधला खूप practical topic आहे — CSV/Excel files read आणि write कशा करायच्या.

03-Pandas → Add file → Create new file

File name:

read_write_files.py

हा पूर्ण code paste कर:

# Pandas - Read and Write Files

import pandas as pd


# ==================================================
# 1. Create DataFrame
# ==================================================

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 24, 23, 21],
    "City": ["Pune", "Mumbai", "Pune", "Nashik"],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# ==================================================
# 2. Write DataFrame to CSV
# ==================================================

df.to_csv(
    "students.csv",
    index=False
)

print("\nCSV file created successfully.")


# ==================================================
# 3. Read CSV File
# ==================================================

df_csv = pd.read_csv(
    "students.csv"
)

print("\nData read from CSV:")
print(df_csv)


# ==================================================
# 4. Read Specific Columns from CSV
# ==================================================

df_selected = pd.read_csv(
    "students.csv",
    usecols=[
        "Name",
        "Marks"
    ]
)

print("\nSelected Columns:")
print(df_selected)


# ==================================================
# 5. Write to Excel
# ==================================================

df.to_excel(
    "students.xlsx",
    index=False
)

print("\nExcel file created successfully.")


# ==================================================
# 6. Read Excel File
# ==================================================

df_excel = pd.read_excel(
    "students.xlsx"
)

print("\nData read from Excel:")
print(df_excel)


# ==================================================
# 7. Write Only Selected Columns
# ==================================================

df[
    ["Name", "Marks"]
].to_csv(
    "student_marks.csv",
    index=False
)

print("\nSelected data saved to CSV.")


# ==================================================
# 8. Read Data with Specific Rows
# ==================================================

df_rows = pd.read_csv(
    "students.csv",
    nrows=2
)

print("\nFirst Two Rows:")
print(df_rows)


# ==================================================
# 9. Read CSV with Custom Missing Value
# ==================================================

data_with_missing = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit"
    ],
    "Marks": [
        80,
        "NA",
        75
    ]
}

missing_df = pd.DataFrame(
    data_with_missing
)

missing_df.to_csv(
    "marks_with_missing.csv",
    index=False
)

read_missing = pd.read_csv(
    "marks_with_missing.csv",
    na_values=["NA"]
)

print("\nCSV with Missing Values:")
print(read_missing)


# ==================================================
# 10. Append Data to CSV
# ==================================================

new_data = pd.DataFrame({
    "Name": ["Sneha"],
    "Age": [25],
    "City": ["Mumbai"],
    "Marks": [92]
})

new_data.to_csv(
    "students.csv",
    mode="a",
    header=False,
    index=False
)

print("\nNew data appended to CSV.")


# ==================================================
# 11. Read Final CSV
# ==================================================

final_df = pd.read_csv(
    "students.csv"
)

print("\nFinal CSV Data:")
print(final_df)


# ==================================================
# 12. Practical Data Science Example
# ==================================================

sales_data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Monitor"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Nashik",
        "Pune"
    ],
    "Sales": [
        55000,
        25000,
        18000,
        22000
    ]
}

sales_df = pd.DataFrame(
    sales_data
)

print("\nSales Data:")
print(sales_df)


# Save sales data

sales_df.to_csv(
    "sales_data.csv",
    index=False
)


# Read sales data

sales = pd.read_csv(
    "sales_data.csv"
)

print("\nSales Data Read from CSV:")
print(sales)


# Calculate total sales

total_sales = sales["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)

यात काय शिकवायचं?
मुख्य functions:

pd.read_csv()
pd.read_excel()

df.to_csv()
df.to_excel()

CSV save
df.to_csv(
    "students.csv",
    index=False
)

index=False म्हणजे Pandas चा index वेगळ्या column म्हणून save होणार नाही.

CSV read
df = pd.read_csv(
    "students.csv"
)

Excel
df.to_excel(
    "students.xlsx",
    index=False
)

आणि:

df = pd.read_excel(
    "students.xlsx"
)

Note: Excel code run करताना openpyxl missing असेल तर terminal मध्ये:

pip install openpyxl

करावे लागेल.

Commit message
Add Pandas file reading and writing examples

Commit changes कर.

झाल्यावर फक्त done म्हणा. मग 03-Pandas चा शेवटचा README.md update करू आणि त्यानंतर 04-Matplotlib ला जाऊ.



You said:

done

ChatGPT said:
छान 👍 आता 03-Pandas चा शेवटचा step — README.md update करू.

आत्ता 03-Pandas मध्ये आपण बरेच files तयार केले आहेत. README मध्ये फक्त काय काय शिकवलं आहे आणि कोणत्या file मध्ये आहे हे ठेवू. Trainer म्हणून simple आणि useful ठेवूया.

03-Pandas folder → README.md → Edit

आतला content replace करून हा paste कर:

03-Pandas README


Pandas for Data Science
Pandas is a Python library mainly used for working with data in table format.

It is useful for:

Data cleaning

Data analysis

Data manipulation

Working with CSV and Excel files

Preparing data for visualization and machine learning

Topics Covered
1. Pandas Basics
File: pandas_basics.py

What is Pandas

Series

DataFrame

Creating DataFrame

Basic DataFrame operations

head()

tail()

shape

columns

dtypes

info()

describe()

2. Selecting, Filtering and Sorting
File: select_filter_sort.py

Selecting columns

Selecting rows

loc

iloc

Filtering data

Multiple conditions

isin()

between()

Sorting data

sort_values()

3. Missing Values
File: missing_values.py

Missing values

isnull()

isna()

dropna()

fillna()

Mean

Median

Mode

Forward fill

Backward fill

4. Duplicate Data
File: duplicates.py

Finding duplicate records

duplicated()

Counting duplicates

drop_duplicates()

Duplicate values based on specific columns

5. Data Transformation
File: data_transformation.py

Creating new columns

Updating columns

apply()

lambda

map()

replace()

rename()

Conditional transformation

6. GroupBy and Aggregation
File: groupby_aggregation.py

groupby()

sum()

mean()

min()

max()

count()

agg()

Grouping by multiple columns

Data analysis using grouped data

7. Merge and Concat
File: merge_concat.py

concat()

merge()

Inner join

Left join

Right join

Outer join

Merging using different column names

8. String and DateTime Operations
File: string_datetime.py

String operations

upper()

lower()

title()

contains()

startswith()

endswith()

replace()

split()

strip()

DateTime conversion

Year

Month

Day

Quarter

Date difference

Date ranges

9. Index and Column Management
File: index_columns.py

Index

Columns

set_index()

reset_index()

rename()

insert()

drop()

Column reordering

10. Reading and Writing Files
File: read_write_files.py

Reading CSV files

Writing CSV files

Reading Excel files

Writing Excel files

Selecting columns while reading

Handling missing values while reading

Appending data

11. Practice
File: practice.py

Practice exercises covering:

DataFrame basics

Selection

Filtering

Sorting

Data transformation

GroupBy

Aggregation

Missing values

Duplicate data

String operations

Index operations

Sales data analysis

Basic Pandas Example
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)

print(df["Marks"].mean())

Learning Flow
Create DataFrame
       ↓
Understand Data
       ↓
Select / Filter
       ↓
Clean Data
       ↓
Transform Data
       ↓
Group and Aggregate
       ↓
Merge Data
       ↓
Analyze Data
       ↓
Save / Export Data

Practice
Try the exercises in:

practice.py

The goal is to understand the concepts by writing and running the code yourself.

आता Commit changes कर.

Commit message:

Update Pandas README with topics and learning flow

हे झालं की 03-Pandas section practically complete आहे. त्यानंतर आपण 04-Matplotlib folder सुरू करू.



You said:

Pandas for Data Science

Pandas is a Python library used for data manipulation, data cleaning, data analysis and working with tabular data.

It is one of the most commonly used libraries in Data Science.

Pandas mainly provides two important data structures:

Series

DataFrame

1. Why Pandas?

In Data Science, we usually work with data such as:

Customer data

Employee data

Sales data

Student data

Product data

Financial data

This data is often stored in rows and columns.

Pandas makes it easier to:

Read data

View data

Filter data

Clean data

Handle missing values

Sort data

Group data

Calculate statistics

Combine datasets

Prepare data for Machine Learning

2. Installation

Pandas can be installed using pip.

pip install pandas


To check the installed version:

import pandas as pd

print(pd.__version__)

3. Import Pandas

The commonly used alias for Pandas is pd.

import pandas as pd

4. Pandas Series

A Series is a one-dimensional labelled data structure.

Example:

import pandas as pd

marks = pd.Series([80, 75, 90, 85, 70])

print(marks)


Each value has an index.

5. Series with Custom Index
marks = pd.Series(
    [80, 75, 90],
    index=["Rahul", "Priya", "Amit"]
)

print(marks)


Access a value:

print(marks["Rahul"])

6. DataFrame

A DataFrame is a two-dimensional labelled data structure with rows and columns.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, 24, 23],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)


A DataFrame is similar to a table.

7. Important DataFrame Terms

A DataFrame contains:

Rows

Columns

Index

Values

Data Types

Example:

print(df.index)
print(df.columns)
print(df.values)
print(df.dtypes)

8. Creating DataFrame from Dictionary
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print(df)

9. Creating DataFrame from List
data = [
    ["Rahul", 22, 80],
    ["Priya", 24, 90],
    ["Amit", 23, 75]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Marks"]
)

print(df)

10. Reading CSV File

CSV files are very common in Data Science.

df = pd.read_csv("data.csv")

print(df)

11. Reading Excel File
df = pd.read_excel("data.xlsx")

print(df)


Excel support may require an additional package depending on the file format and environment.

12. Inspecting Data
head()

Shows the first rows.

print(df.head())

tail()

Shows the last rows.

print(df.tail())

shape

Returns number of rows and columns.

print(df.shape)

columns

Shows column names.

print(df.columns)

dtypes

Shows data types.

print(df.dtypes)

info()

Provides information about the DataFrame.

df.info()

describe()

Provides statistical summary for numerical columns.

print(df.describe())

13. Selecting a Column
print(df["Name"])


Another method:

print(df.Name)


The bracket method is generally preferred because it also works with column names containing spaces or special characters.

14. Selecting Multiple Columns
print(df[["Name", "Marks"]])

15. Selecting Rows with loc

loc is label-based selection.

print(df.loc[0])


Selecting multiple rows:

print(df.loc[0:2])


Selecting rows and columns:

print(df.loc[0:2, ["Name", "Marks"]])

16. Selecting Rows with iloc

iloc is position-based selection.

print(df.iloc[0])


Multiple rows:

print(df.iloc[0:3])


Rows and columns:

print(df.iloc[0:3, 0:2])

17. Filtering Data

Filtering is one of the most important Pandas concepts.

Example:

print(df[df["Marks"] > 80])


Multiple conditions:

print(
    df[
        (df["Age"] > 20) &
        (df["Marks"] > 80)
    ]
)


Using OR:

print(
    df[
        (df["Marks"] > 90) |
        (df["Age"] < 21)
    ]
)

18. Adding a New Column
df["Passed"] = df["Marks"] >= 40

print(df)


Another example:

df["Bonus"] = 5

print(df)

19. Updating a Column
df["Marks"] = df["Marks"] + 5

print(df)

20. Renaming Columns
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)

print(df)

21. Dropping Columns
df.drop(
    columns=["Age"],
    inplace=True
)

print(df)

22. Dropping Rows
df.drop(index=0, inplace=True)

print(df)

23. Sorting Data

Sort by one column:

df.sort_values("Marks")


Descending order:

df.sort_values(
    "Marks",
    ascending=False
)

24. Handling Missing Values

Missing values are common in real-world datasets.

Example:

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [22, None, 24],
    "Marks": [80, 90, None]
}

df = pd.DataFrame(data)

print(df)

25. Detecting Missing Values
print(df.isnull())


Count missing values:

print(df.isnull().sum())


Another method:

print(df.isna().sum())

26. Removing Missing Values
df.dropna()


Remove rows containing missing values:

df.dropna(inplace=True)

27. Filling Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())


For a fixed value:

df["Marks"] = df["Marks"].fillna(0)

28. Duplicate Data

Check duplicates:

print(df.duplicated())


Count duplicates:

print(df.duplicated().sum())


Remove duplicates:

df.drop_duplicates(inplace=True)

29. Unique Values
print(df["Name"].unique())


Number of unique values:

print(df["Name"].nunique())

30. Value Counts

value_counts() counts how frequently each value occurs.

print(df["City"].value_counts())


This is useful for categorical data analysis.

31. Basic Statistics
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].sum())

32. GroupBy

groupby() is one of the most important Pandas concepts for Data Analysis.

Example:

data = {
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [1000, 2000, 1500, 2500]
}

df = pd.DataFrame(data)

print(
    df.groupby("City")["Sales"].sum()
)


Average sales:

print(
    df.groupby("City")["Sales"].mean()
)

33. GroupBy Multiple Columns
result = df.groupby(
    ["City"]
)["Sales"].agg(
    ["sum", "mean", "max", "min"]
)

print(result)

34. Aggregation

Pandas provides aggregation functions such as:

sum()
mean()
median()
min()
max()
count()


Example:

print(
    df["Sales"].agg(
        ["sum", "mean", "min", "max"]
    )
)

35. Apply Function

apply() can be used to apply a function to values.

Example:

def add_bonus(x):
    return x + 10

df["Updated_Sales"] = df["Sales"].apply(add_bonus)

print(df)


A lambda function can also be used:

df["Updated_Sales"] = df["Sales"].apply(
    lambda x: x + 10
)

36. String Operations

Pandas provides string methods for text columns.

Example:

df["Name"] = df["Name"].str.upper()


Other examples:

df["Name"].str.lower()
df["Name"].str.title()
df["Name"].str.len()


Checking text:

df["Name"].str.contains("A")

37. Date and Time

Pandas can work with dates.

dates = pd.to_datetime(
    ["2025-01-01", "2025-02-01", "2025-03-01"]
)

print(dates)


Create a date column:

df["Date"] = pd.to_datetime(df["Date"])


Extract year:

df["Year"] = df["Date"].dt.year


Extract month:

df["Month"] = df["Date"].dt.month

38. Concatenating DataFrames

Two DataFrames can be combined using concat().

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Marks": [75, 85]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

39. Merge

merge() is used to combine DataFrames using a common column.

Example:

students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Rahul", "Priya", "Amit"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [80, 90, 75]
})

result = pd.merge(
    students,
    marks,
    on="Student_ID"
)

print(result)

40. Merge Types

Important merge types:

inner
left
right
outer


Example:

pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)

41. Exporting Data

Save DataFrame as CSV:

df.to_csv(
    "output.csv",
    index=False
)


Save as Excel:

df.to_excel(
    "output.xlsx",
    index=False
)

42. Index

Every Pandas DataFrame has an index.

print(df.index)


Set a column as index:

df.set_index("Student_ID", inplace=True)


Reset index:

df.reset_index(inplace=True)

43. Changing Data Type

Check data types:

print(df.dtypes)


Convert a column:

df["Age"] = df["Age"].astype(int)


For numeric conversion:

df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)

44. Pandas Data Cleaning Flow

A common Data Science workflow is:

Read Data
    ↓
Understand Data
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Clean Data
    ↓
Transform Data
    ↓
Filter Data
    ↓
Group / Aggregate
    ↓
Analyze Data
    ↓
Export / Use for ML

45. Simple Data Analysis Example
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Sales": [5000, 7000, 4500, 8000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nHighest Sales:")
print(df["Sales"].max())

print("\nPune Customers:")
print(df[df["City"] == "Pune"])

print("\nCity-wise Sales:")
print(
    df.groupby("City")["Sales"].sum()
)

46. Important Pandas Functions
pd.Series()
pd.DataFrame()

pd.read_csv()
pd.read_excel()

df.head()
df.tail()
df.info()
df.describe()

df.shape
df.columns
df.index
df.dtypes

df["column"]
df[["column1", "column2"]]

df.loc[]
df.iloc[]

df.isnull()
df.isna()
df.dropna()
df.fillna()

df.drop_duplicates()
df.duplicated()

df.sort_values()

df.groupby()
df.agg()
df.apply()

df.merge()
pd.concat()

df.rename()
df.drop()

df.unique()
df.nunique()
df.value_counts()

df.to_csv()
df.to_excel()

47. Pandas in Data Science

Pandas is mainly used for:

Data loading

Data cleaning

Data preprocessing

Data transformation

Exploratory Data Analysis (EDA)

Statistical analysis

Working with CSV and Excel files

Handling missing values

Filtering and sorting data

Grouping and aggregation

Preparing data for visualization

Preparing data for Machine Learning

48. Pandas and NumPy

NumPy is mainly focused on numerical arrays and mathematical operations.

Pandas provides higher-level data structures such as Series and DataFrame for working with structured and labelled data.

A common Data Science workflow is:

NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
Statistics / EDA
   ↓
Machine Learning

49. Quick Revision
Pandas
   ↓
Series
   ↓
DataFrame
   ↓
Read Data
   ↓
Inspect Data
   ↓
Select Data
   ↓
Filter Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
GroupBy
   ↓
Merge / Concat
   ↓
Analyze Data
   ↓
Export Data

Official Documentation

Pandas documentation:

https://pandas.pydata.org/docs/ he mazya readme file madhe aahe kay karu

ChatGPT said:
हो 👍 हे README खूप चांगलं आहे. आपण आत्ताच तयार केलेल्या 03-Pandas च्या README पेक्षा तुझं हे README जास्त detailed आणि trainer-friendly आहे.

म्हणून हे delete करू नकोस. आपण यालाच ठेवू.

फक्त एक गोष्ट करायची आहे: आत्तापर्यंत आपण जे .py files तयार केले आहेत, त्यांची file-wise list सुरुवातीला किंवा शेवटी add करू. त्यामुळे GitHub वर README पाहिल्यावर learner ला theory कुठे आहे आणि practical code कुठे आहे हे लगेच कळेल.

तुझ्या existing README च्या सगळ्यात वर, # Pandas for Data Science च्या खाली हे add कर:

Pandas README – File Structure Section


Files in This Folder
The concepts covered in this README are also available as separate Python practice files.

03-Pandas/
│
├── pandas_basics.py
├── select_filter_sort.py
├── missing_values.py
├── duplicates.py
├── data_transformation.py
├── groupby_aggregation.py
├── merge_concat.py
├── string_datetime.py
├── index_columns.py
├── read_write_files.py
└── practice.py

File-wise Practice
pandas_basics.py - Pandas basics, Series, DataFrame and basic operations

select_filter_sort.py - Selecting, filtering and sorting data

missing_values.py - Missing value handling

duplicates.py - Finding and removing duplicate data

data_transformation.py - Creating and transforming columns

groupby_aggregation.py - GroupBy and aggregation

merge_concat.py - Combining multiple DataFrames

string_datetime.py - String and date-time operations

index_columns.py - Index and column management

read_write_files.py - Reading and writing CSV/Excel files

practice.py - Practice exercises

एक correction मात्र
तुझ्या README मध्ये हे आहे:

print(df.info())

हे technically चालेल, पण info() स्वतः output print करते. त्यामुळे:

df.info()

हेच better आहे.

म्हणून Simple Data Analysis Example मध्ये:

print("\nDataset Information:")
print(df.info())

ऐवजी:

print("\nDataset Information:")
df.info()

कर.

बाकी README आत्ता rewrite करण्याची गरज नाही. आपण जो content तयार केला आहे तो यामध्ये already cover झालेला आहे.

आता काय करायचं?
वरचा Files in This Folder section add कर.

print(df.info()) → df.info() कर.

Commit changes.

Commit message:

Update Pandas README with file structure and examples

हे झाल्यावर 03-Pandas complete समज. मग आपण 04-Matplotlib सुरू करू — त्यातही ह्याच पद्धतीने README + एकेक Python file + trainer-friendly examples + practice file बनवू.



You said:

done

ChatGPT said:
छान 👍 आता 03-Pandas complete आहे.

आता पुढचा folder करूया:

Step 38 — 04-Matplotlib
तुझ्या main repository मध्ये:

Python-for-Data-Science/
│
├── 01-Python-Basics/
├── 02-NumPy/
├── 03-Pandas/
└── 04-Matplotlib/

आत्ता फक्त एकच काम कर
GitHub मध्ये Python-for-Data-Science उघड.

Add file → Create new file

File name मध्ये:

04-Matplotlib/README.md

टाक.

आणि हा content paste कर:

04-Matplotlib README


Matplotlib for Data Science
Matplotlib is a Python library used for creating graphs and visualizations.

In Data Science, visualization helps us understand patterns, trends, distributions and relationships in data.

Why Matplotlib?
Matplotlib can be used to:

Create charts and graphs

Understand data visually

Compare values

Identify trends

Understand distributions

Visualize relationships between variables

Create charts for Exploratory Data Analysis (EDA)

Customize plots

Save charts as image files

Topics Covered
1. Introduction to Matplotlib
What is Matplotlib?

Installation

Importing Matplotlib

pyplot

Basic plotting

2. Line Chart
plt.plot()

X-axis

Y-axis

Title

Labels

Legend

Grid

3. Bar Chart
plt.bar()

Vertical bar chart

Horizontal bar chart

Comparing categories

4. Scatter Plot
plt.scatter()

Relationship between two variables

Positive and negative relationships

5. Histogram
plt.hist()

Distribution of numerical data

Bins

6. Pie Chart
plt.pie()

Percentage distribution

Labels

Autopct

7. Plot Customization
Colors

Markers

Line styles

Line width

Figure size

Titles

Axis labels

Grid

Legend

8. Subplots
Multiple charts in one figure

plt.subplot()

plt.subplots()

9. Saving Charts
Saving plots as PNG

Saving plots as JPG

Saving plots as PDF

10. Matplotlib with Pandas
Plotting DataFrame columns

Visualizing grouped data

Basic Data Analysis charts

11. Data Science Visualization Examples
Sales analysis

Student marks

Employee salary

Product analysis

Monthly trends

12. Practice
Practice exercises based on different types of charts and Data Science datasets.

Learning Flow
Understand Data
      ↓
Choose Chart
      ↓
Create Plot
      ↓
Add Labels
      ↓
Customize Plot
      ↓
Understand Pattern
      ↓
Use for EDA

Basic Example
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 12000, 18000]

plt.plot(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

Matplotlib in Data Science
Matplotlib is commonly used after data cleaning and analysis.

A common workflow is:

NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
EDA
   ↓
Machine Learning

Official Documentation
Matplotlib documentation:

https://matplotlib.org/stable/

आता Commit changes कर.

Commit message:

Add Matplotlib README and topic structure

आत्ता फक्त हेच कर. झाल्यावर done म्हणा. मग आपण 01_basic_plot.py बनवू.



You said:

done

ChatGPT said:
छान 👍 आता Step 39 — 01_basic_plot.py.

हा Matplotlib चा पहिला practical file आहे. यात आपण अगदी basic पासून सुरुवात करू.

04-Matplotlib → Add file → Create new file

File name:

01_basic_plot.py

हा पूर्ण code paste कर:

# Matplotlib - Basic Plot

import matplotlib.pyplot as plt


# -------------------------
# 1. Simple Line Plot
# -------------------------

x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.show()


# -------------------------
# 2. Add Title
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()


# -------------------------
# 3. Add X and Y Labels
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# -------------------------
# 4. Add Grid
# -------------------------

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 5. Change Line Color
# -------------------------

plt.plot(
    x,
    y,
    color="blue"
)

plt.title("Blue Line")

plt.show()


# -------------------------
# 6. Change Line Style
# -------------------------

plt.plot(
    x,
    y,
    linestyle="--"
)

plt.title("Dashed Line")

plt.show()


# -------------------------
# 7. Change Line Width
# -------------------------

plt.plot(
    x,
    y,
    linewidth=3
)

plt.title("Thick Line")

plt.show()


# -------------------------
# 8. Add Markers
# -------------------------

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot with Markers")

plt.show()


# -------------------------
# 9. Marker + Color + Line
# -------------------------

plt.plot(
    x,
    y,
    color="green",
    linestyle="--",
    marker="o",
    linewidth=2
)

plt.title("Customized Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 10. Figure Size
# -------------------------

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot with Figure Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# -------------------------
# 11. Multiple Lines
# -------------------------

x = [1, 2, 3, 4, 5]

sales_2024 = [
    100,
    150,
    120,
    180,
    200
]

sales_2025 = [
    120,
    170,
    160,
    210,
    250
]

plt.plot(
    x,
    sales_2024,
    marker="o",
    label="2024"
)

plt.plot(
    x,
    sales_2025,
    marker="o",
    label="2025"
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# -------------------------
# 12. Real Data Science Example
# -------------------------

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    13000,
    18000,
    22000,
    25000
]

plt.figure(
    figsize=(9, 5)
)

plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()

या file मध्ये काय शिकायचं?
Basic Matplotlib structure:

import
  ↓
Data
  ↓
plt.plot()
  ↓
Title
  ↓
X Label
  ↓
Y Label
  ↓
Grid
  ↓
Legend
  ↓
plt.show()

सर्वात basic syntax
plt.plot(x, y)
plt.show()

Important functions
plt.plot()
plt.title()
plt.xlabel()
plt.ylabel()
plt.grid()
plt.legend()
plt.figure()
plt.show()

Plot customize करण्यासाठी
plt.plot(
    x,
    y,
    color="green",
    linestyle="--",
    marker="o",
    linewidth=2
)

इथे:

color      → line चा रंग
linestyle  → line चा प्रकार
marker     → प्रत्येक point वर marker
linewidth  → line ची thickness

Commit message
Add Matplotlib basic plot examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण Step 40 — 02_line_chart.py करू, ज्यात real Data Science examples घेऊन line charts व्यवस्थित शिकवू.



You said:

done

ChatGPT said:
छान 👍 आता Step 40 — 02_line_chart.py.

04-Matplotlib → Add file → Create new file

File name:

02_line_chart.py

हा code paste कर:

# Matplotlib - Line Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Line Chart
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [10000, 12000, 15000, 13000, 18000, 22000]

plt.plot(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 2. Line Chart with Markers
# ==================================================

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 3. Customized Line Chart
# ==================================================

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# ==================================================
# 4. Sales Comparison
# ==================================================

sales_2024 = [
    10000,
    12000,
    14000,
    16000,
    17000,
    19000
]

sales_2025 = [
    12000,
    15000,
    16000,
    18000,
    22000,
    25000
]

plt.plot(
    months,
    sales_2024,
    marker="o",
    label="2024"
)

plt.plot(
    months,
    sales_2025,
    marker="o",
    label="2025"
)

plt.title("Sales Comparison: 2024 vs 2025")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# ==================================================
# 5. Student Marks Trend
# ==================================================

subjects = [
    "Maths",
    "Science",
    "English",
    "Python",
    "Statistics"
]

marks = [
    75,
    82,
    78,
    90,
    85
]

plt.plot(
    subjects,
    marks,
    marker="o",
    color="blue"
)

plt.title("Student Marks")

plt.xlabel("Subject")

plt.ylabel("Marks")

plt.grid()

plt.show()


# ==================================================
# 6. Employee Salary Trend
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6
]

salary = [
    30000,
    35000,
    40000,
    47000,
    55000,
    65000
]

plt.plot(
    experience,
    salary,
    marker="o",
    color="purple"
)

plt.title("Salary vs Experience")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid()

plt.show()


# ==================================================
# 7. Multiple Line Charts
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

product_a = [
    100,
    120,
    150,
    130,
    170,
    200
]

product_b = [
    80,
    100,
    110,
    140,
    160,
    180
]

product_c = [
    60,
    90,
    100,
    120,
    150,
    170
]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A"
)

plt.plot(
    months,
    product_b,
    marker="s",
    label="Product B"
)

plt.plot(
    months,
    product_c,
    marker="^",
    label="Product C"
)

plt.title("Product Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()


# ==================================================
# 8. Add Data Points
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    14000,
    12000,
    18000,
    22000
]

plt.plot(
    months,
    sales,
    marker="o",
    color="red"
)

for month, sale in zip(months, sales):
    plt.text(
        month,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("Monthly Sales with Values")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()


# ==================================================
# 9. Real Data Science Example
# ==================================================

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

website_visitors = [
    120,
    150,
    140,
    180,
    220,
    300,
    250
]

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    days,
    website_visitors,
    marker="o",
    color="orange",
    linewidth=2
)

plt.title("Weekly Website Visitors")

plt.xlabel("Day")

plt.ylabel("Number of Visitors")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()

यात मुख्य concept
Line chart प्रामुख्याने trend किंवा change over time दाखवण्यासाठी उपयोगी आहे.

उदा.:

Monthly sales

Website visitors

Stock price trend

Temperature

Student performance

Salary vs experience

Important syntax
plt.plot(x, y)

इथे x → categories/time/independent values आणि y → measure/value.

Multiple lines साठी:

plt.plot(x, y1, label="2024")
plt.plot(x, y2, label="2025")

plt.legend()

Commit message
Add Matplotlib line chart examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण Step 41 — 03_bar_chart.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 41 — 03_bar_chart.py.

04-Matplotlib → Add file → Create new file

File name:

03_bar_chart.py

हा code paste कर:

# Matplotlib - Bar Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Bar Chart
# ==================================================

categories = [
    "Python",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "SQL"
]

students = [
    40,
    35,
    45,
    30,
    50
]

plt.bar(
    categories,
    students
)

plt.title("Students Enrolled")

plt.xlabel("Technology")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 2. Customized Bar Chart
# ==================================================

plt.bar(
    categories,
    students,
    color="skyblue"
)

plt.title("Students Enrolled")

plt.xlabel("Technology")

plt.ylabel("Number of Students")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 3. Horizontal Bar Chart
# ==================================================

plt.barh(
    categories,
    students,
    color="orange"
)

plt.title("Students Enrolled")

plt.xlabel("Number of Students")

plt.ylabel("Technology")

plt.show()


# ==================================================
# 4. Bar Chart with Different Colors
# ==================================================

colors = [
    "blue",
    "green",
    "orange",
    "purple",
    "red"
]

plt.bar(
    categories,
    students,
    color=colors
)

plt.title("Students Enrolled by Technology")

plt.xlabel("Technology")

plt.ylabel("Students")

plt.show()


# ==================================================
# 5. Sales by City
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur",
    "Thane"
]

sales = [
    50000,
    75000,
    40000,
    60000,
    85000
]

plt.bar(
    cities,
    sales,
    color="green"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 6. Bar Chart with Values
# ==================================================

plt.bar(
    cities,
    sales,
    color="teal"
)

for city, sale in zip(cities, sales):
    plt.text(
        city,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 7. Product Sales
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard"
]

product_sales = [
    120000,
    90000,
    60000,
    45000,
    25000
]

plt.bar(
    products,
    product_sales,
    color="steelblue"
)

plt.title("Product-wise Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.xticks(
    rotation=30
)

plt.show()


# ==================================================
# 8. Compare Two Categories
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales_2024 = [
    100,
    150,
    80,
    60
]

sales_2025 = [
    130,
    180,
    110,
    90
]

x = range(len(products))

width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    sales_2024,
    width=width,
    label="2024"
)

plt.bar(
    [i + width / 2 for i in x],
    sales_2025,
    width=width,
    label="2025"
)

plt.xticks(
    list(x),
    products
)

plt.title("Product Sales Comparison")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.legend()

plt.show()


# ==================================================
# 9. Employee Department Count
# ==================================================

departments = [
    "IT",
    "HR",
    "Sales",
    "Finance",
    "Marketing"
]

employees = [
    25,
    15,
    30,
    12,
    20
]

plt.barh(
    departments,
    employees,
    color="purple"
)

plt.title("Employees by Department")

plt.xlabel("Number of Employees")

plt.ylabel("Department")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

monthly_sales = [
    12000,
    15000,
    18000,
    14000,
    22000,
    25000
]

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    months,
    monthly_sales,
    color="cornflowerblue"
)

for month, sale in zip(
    months,
    monthly_sales
):
    plt.text(
        month,
        sale,
        str(sale),
        ha="center",
        va="bottom"
    )

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()

यात मुख्य concept
Bar chart categorical data compare करण्यासाठी वापरतो.

उदा.:

City-wise sales

Department-wise employees

Product-wise sales

Students per course

Monthly sales comparison

Vertical bar
plt.bar(
    categories,
    values
)

Horizontal bar
plt.barh(
    categories,
    values
)

दोन groups compare करणे
उदा. 2024 vs 2025:

plt.bar(...)
plt.bar(...)

plt.legend()

एक महत्त्वाचा फरक
Line chart → trend/change पाहण्यासाठी.

Bar chart → categories मधील values compare करण्यासाठी.

उदा.:

Month → Sales

यासाठी line chart उपयोगी.

पण:

City → Sales
Pune → 50000
Mumbai → 75000
Nashik → 40000

यासाठी bar chart natural choice आहे.

Commit message
Add Matplotlib bar chart examples

Commit changes कर.

झाल्यावर done म्हणा. मग 04_scatter_plot.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 42 — 04_scatter_plot.py.

04-Matplotlib → Add file → Create new file

File name:

04_scatter_plot.py

हा code paste कर:

# Matplotlib - Scatter Plot

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Scatter Plot
# ==================================================

x = [1, 2, 3, 4, 5]

y = [10, 15, 12, 20, 25]

plt.scatter(
    x,
    y
)

plt.title("Basic Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 2. Scatter Plot with Color
# ==================================================

plt.scatter(
    x,
    y,
    color="blue"
)

plt.title("Scatter Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 3. Scatter Plot with Size
# ==================================================

plt.scatter(
    x,
    y,
    color="green",
    s=100
)

plt.title("Scatter Plot with Marker Size")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 4. Scatter Plot with Transparency
# ==================================================

plt.scatter(
    x,
    y,
    color="red",
    alpha=0.5
)

plt.title("Scatter Plot with Transparency")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 5. Study Hours vs Marks
# ==================================================

study_hours = [
    1,
    2,
    2.5,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

marks = [
    40,
    45,
    50,
    55,
    60,
    68,
    72,
    78,
    85,
    92
]

plt.scatter(
    study_hours,
    marks,
    color="purple",
    s=80
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 6. Age vs Salary
# ==================================================

age = [
    22,
    24,
    25,
    27,
    29,
    30,
    32,
    35,
    38,
    40
]

salary = [
    28000,
    32000,
    35000,
    40000,
    45000,
    50000,
    55000,
    65000,
    75000,
    85000
]

plt.scatter(
    age,
    salary,
    color="orange",
    s=90
)

plt.title("Age vs Salary")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 7. Two Groups in One Scatter Plot
# ==================================================

study_hours_a = [
    1,
    2,
    3,
    4,
    5
]

marks_a = [
    45,
    50,
    60,
    65,
    72
]

study_hours_b = [
    4,
    5,
    6,
    7,
    8
]

marks_b = [
    60,
    70,
    78,
    85,
    92
]

plt.scatter(
    study_hours_a,
    marks_a,
    color="blue",
    label="Group A"
)

plt.scatter(
    study_hours_b,
    marks_b,
    color="red",
    label="Group B"
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.show()


# ==================================================
# 8. Scatter Plot with Different Sizes
# ==================================================

x = [
    10,
    20,
    30,
    40,
    50
]

y = [
    20,
    35,
    30,
    55,
    70
]

sizes = [
    50,
    100,
    150,
    250,
    350
]

plt.scatter(
    x,
    y,
    s=sizes,
    color="green",
    alpha=0.6
)

plt.title("Scatter Plot with Different Sizes")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.show()


# ==================================================
# 9. Sales vs Advertising Spend
# ==================================================

advertising = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

sales = [
    20,
    25,
    35,
    42,
    50,
    60,
    65,
    75
]

plt.scatter(
    advertising,
    sales,
    color="teal",
    s=100
)

plt.title("Advertising Spend vs Sales")

plt.xlabel("Advertising Spend")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

salary = [
    30000,
    34000,
    38000,
    42000,
    47000,
    52000,
    58000,
    65000,
    73000,
    82000
]

plt.figure(
    figsize=(9, 5)
)

plt.scatter(
    experience,
    salary,
    color="darkblue",
    s=100,
    alpha=0.7
)

plt.title("Experience vs Salary")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()

Scatter Plot म्हणजे काय?
Scatter plot मध्ये दोन numerical variables मधील relationship पाहतो.

उदा.:

Study Hours  →  Marks
Experience   →  Salary
Advertising  →  Sales
Age          →  Salary

Basic syntax:

plt.scatter(x, y)

Important parameters
plt.scatter(
    x,
    y,
    color="blue",
    s=100,
    alpha=0.5
)

color → points चा रंग

s → point size

alpha → transparency

Data Science मध्ये महत्त्व
Scatter plot वापरून data मध्ये काही pattern दिसतो का, variables एकमेकांशी कसे बदलतात, आणि unusual observations दिसतात का हे visually inspect करता येते. मात्र plot पाहून correlation किंवा causation आपोआप सिद्ध होत नाही.

Commit message
Add Matplotlib scatter plot examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण 05_histogram.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 43 — 05_histogram.py.

04-Matplotlib → Add file → Create new file

File name:

05_histogram.py

हा code paste कर:

# Matplotlib - Histogram

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Histogram
# ==================================================

marks = [
    45, 50, 55, 60, 62,
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

plt.hist(marks)

plt.title("Distribution of Marks")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 2. Histogram with Bins
# ==================================================

plt.hist(
    marks,
    bins=5
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 3. Customized Histogram
# ==================================================

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 4. Exam Marks Distribution
# ==================================================

marks = [
    35, 42, 48, 50, 55,
    58, 60, 62, 65, 68,
    70, 72, 75, 78, 80,
    82, 85, 88, 90, 92,
    95, 97
]

plt.hist(
    marks,
    bins=10,
    color="green",
    edgecolor="black"
)

plt.title("Student Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()


# ==================================================
# 5. Employee Age Distribution
# ==================================================

ages = [
    22, 24, 25, 26, 27,
    28, 29, 30, 31, 32,
    33, 34, 35, 36, 38,
    40, 42, 45
]

plt.hist(
    ages,
    bins=6,
    color="orange",
    edgecolor="black"
)

plt.title("Employee Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Employees")

plt.show()


# ==================================================
# 6. Salary Distribution
# ==================================================

salary = [
    25000, 28000, 30000, 32000,
    35000, 38000, 40000, 42000,
    45000, 48000, 50000, 52000,
    55000, 58000, 60000, 65000,
    70000, 75000, 80000
]

plt.hist(
    salary,
    bins=7,
    color="purple",
    edgecolor="black"
)

plt.title("Salary Distribution")

plt.xlabel("Salary")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 7. Histogram with Density
# ==================================================

plt.hist(
    marks,
    bins=10,
    density=True,
    color="teal",
    edgecolor="black"
)

plt.title("Marks Distribution - Density")

plt.xlabel("Marks")

plt.ylabel("Density")

plt.show()


# ==================================================
# 8. Compare Two Distributions
# ==================================================

class_a = [
    55, 60, 62, 65, 68,
    70, 72, 75, 78, 80
]

class_b = [
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 90
]

plt.hist(
    class_a,
    bins=5,
    alpha=0.5,
    label="Class A"
)

plt.hist(
    class_b,
    bins=5,
    alpha=0.5,
    label="Class B"
)

plt.title("Class Marks Comparison")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.legend()

plt.show()


# ==================================================
# 9. Horizontal Histogram
# ==================================================

plt.hist(
    marks,
    bins=10,
    orientation="horizontal",
    color="coral",
    edgecolor="black"
)

plt.title("Horizontal Histogram")

plt.xlabel("Frequency")

plt.ylabel("Marks")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

customer_age = [
    18, 20, 21, 22, 23,
    25, 26, 27, 28, 29,
    30, 31, 32, 34, 35,
    36, 38, 40, 42, 45,
    48, 50, 52, 55, 60
]

plt.figure(
    figsize=(9, 5)
)

plt.hist(
    customer_age,
    bins=8,
    color="steelblue",
    edgecolor="black"
)

plt.title("Customer Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Customers")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()

Histogram म्हणजे काय?
Histogram हा numerical data चा distribution समजण्यासाठी वापरला जातो.

उदा.:

Student marks distribution

Employee age distribution

Salary distribution

Customer age

Transaction amount

Basic syntax:

plt.hist(
    data,
    bins=10
)

bins म्हणजे काय?
समजा marks आहेत:

0–20
20–40
40–60
60–80
80–100

तर हे वेगवेगळे intervals म्हणजे bins.

bins बदलल्यावर data चा distribution वेगळ्या granularity ने दिसतो.

Histogram vs Bar Chart
हा difference लक्षात ठेव:

Histogram	Bar Chart
Numerical data distribution	Categories comparison
Bins वापरतो	Categories वापरतो
Bars generally adjacent असतात	Bars मध्ये gap असतो
Marks, Age, Salary	City, Product, Department

उदा.:

Histogram:

Marks → किती students कोणत्या range मध्ये आहेत?

Bar chart:

City → प्रत्येक city ची sales किती?

alpha
alpha=0.5

यामुळे bars transparent होतात. दोन distributions एकत्र compare करताना useful आहे.

Commit message
Add Matplotlib histogram examples

Commit changes कर.

झाल्यावर done म्हणा. मग 06_pie_chart.py करू.



You said:

done

ChatGPT said:
छान 👍 आता Step 44 — 06_pie_chart.py.

04-Matplotlib → Add file → Create new file

File name:

06_pie_chart.py

हा code paste कर:

# Matplotlib - Pie Chart

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Pie Chart
# ==================================================

labels = [
    "Python",
    "Pandas",
    "NumPy",
    "SQL"
]

students = [
    40,
    30,
    20,
    10
]

plt.pie(
    students,
    labels=labels
)

plt.title("Student Technology Preference")

plt.show()


# ==================================================
# 2. Show Percentage
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 3. Custom Colors
# ==================================================

colors = [
    "blue",
    "orange",
    "green",
    "purple"
]

plt.pie(
    students,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%"
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 4. Explode a Slice
# ==================================================

explode = [
    0.1,
    0,
    0,
    0
]

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 5. Shadow
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 6. Start Angle
# ==================================================

plt.pie(
    students,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Technology Preference")

plt.show()


# ==================================================
# 7. Employee Department Distribution
# ==================================================

departments = [
    "IT",
    "HR",
    "Sales",
    "Finance",
    "Marketing"
]

employees = [
    30,
    15,
    25,
    10,
    20
]

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Employee Distribution by Department")

plt.show()


# ==================================================
# 8. Sales Distribution by Product
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    400000,
    300000,
    150000,
    100000
]

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Product")

plt.show()


# ==================================================
# 9. Donut Chart
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor"
]

sales = [
    400,
    300,
    150,
    100
]

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={
        "width": 0.4
    }
)

plt.title("Product Sales Distribution")

plt.show()


# ==================================================
# 10. Real Data Science Example
# ==================================================

expense_categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Other"
]

expenses = [
    15000,
    8000,
    25000,
    10000,
    5000
]

colors = [
    "#ff9999",
    "#66b3ff",
    "#99ff99",
    "#ffcc99",
    "#c2c2f0"
]

plt.figure(
    figsize=(8, 6)
)

plt.pie(
    expenses,
    labels=expense_categories,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Monthly Expense Distribution")

plt.show()

Pie Chart म्हणजे काय?
Pie chart चा उपयोग whole data मधील प्रत्येक category चा proportion/share दाखवण्यासाठी होतो.

उदा.:

Total Employees
       ↓
IT       → 30%
HR       → 15%
Sales    → 25%
Finance  → 10%
Marketing→ 20%

Basic syntax:

plt.pie(
    values,
    labels=labels
)

Percentage दाखवण्यासाठी
autopct="%1.1f%%"

उदा. 25.0%.

Slice highlight करण्यासाठी
explode = [0.1, 0, 0, 0]

पहिला slice थोडा बाहेर येतो.

एक practical point
Pie chart खूप categories असतील तेव्हा cluttered होऊ शकतो. तसेच categories मधील values खूप जवळच्या असतील तर comparison कठीण होऊ शकतो. अशा वेळी bar chart अधिक स्पष्ट असू शकतो.

Commit message
Add Matplotlib pie chart examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण 07_subplots.py करू — एकाच figure मध्ये multiple charts.



You said:

Done

ChatGPT said:
छान 👍 आता Step 45 — 07_subplots.py.

हा important topic आहे कारण Data Science मध्ये एकाच analysis मध्ये multiple charts एकत्र दाखवावे लागतात.

04-Matplotlib → Add file → Create new file

File name:

07_subplots.py

हा पूर्ण code paste कर:

# Matplotlib - Subplots

import matplotlib.pyplot as plt


# ==================================================
# 1. Basic Subplot - 1 Row, 2 Columns
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    22000
]

profit = [
    2000,
    3000,
    2500,
    4000,
    5500
]


plt.subplot(1, 2, 1)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales")

plt.xlabel("Month")

plt.ylabel("Sales")


plt.subplot(1, 2, 2)

plt.plot(
    months,
    profit,
    marker="o",
    color="green"
)

plt.title("Profit")

plt.xlabel("Month")

plt.ylabel("Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 2. 2 Rows, 1 Column
# ==================================================

plt.subplot(2, 1, 1)

plt.bar(
    months,
    sales,
    color="skyblue"
)

plt.title("Monthly Sales")


plt.subplot(2, 1, 2)

plt.bar(
    months,
    profit,
    color="orange"
)

plt.title("Monthly Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 3. 2 Rows, 2 Columns
# ==================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


# First Plot

axes[0, 0].plot(
    months,
    sales,
    marker="o"
)

axes[0, 0].set_title("Sales")


# Second Plot

axes[0, 1].bar(
    months,
    profit,
    color="green"
)

axes[0, 1].set_title("Profit")


# Third Plot

axes[1, 0].scatter(
    sales,
    profit,
    color="red"
)

axes[1, 0].set_title("Sales vs Profit")

axes[1, 0].set_xlabel("Sales")

axes[1, 0].set_ylabel("Profit")


# Fourth Plot

axes[1, 1].hist(
    sales,
    bins=5,
    color="purple",
    edgecolor="black"
)

axes[1, 1].set_title("Sales Distribution")


plt.tight_layout()

plt.show()


# ==================================================
# 4. Different Charts in One Figure
# ==================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


# Line Chart

axes[0, 0].plot(
    months,
    sales,
    marker="o"
)

axes[0, 0].set_title("Line Chart")


# Bar Chart

axes[0, 1].bar(
    months,
    sales,
    color="orange"
)

axes[0, 1].set_title("Bar Chart")


# Scatter Plot

axes[1, 0].scatter(
    sales,
    profit,
    color="red"
)

axes[1, 0].set_title("Scatter Plot")


# Pie Chart

labels = [
    "Sales",
    "Profit"
]

values = [
    sum(sales),
    sum(profit)
]

axes[1, 1].pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

axes[1, 1].set_title("Sales vs Profit")


plt.tight_layout()

plt.show()


# ==================================================
# 5. Real Data Science Dashboard Example
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    18000,
    16000,
    22000,
    25000
]

customers = [
    100,
    120,
    150,
    140,
    180,
    210
]

profit = [
    2000,
    2500,
    3200,
    2800,
    4000,
    5000
]


fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)


# -------------------------
# Monthly Sales
# -------------------------

axes[0, 0].plot(
    months,
    sales,
    marker="o",
    color="blue"
)

axes[0, 0].set_title(
    "Monthly Sales"
)

axes[0, 0].set_xlabel(
    "Month"
)

axes[0, 0].set_ylabel(
    "Sales"
)


# -------------------------
# Customer Count
# -------------------------

axes[0, 1].bar(
    months,
    customers,
    color="green"
)

axes[0, 1].set_title(
    "Monthly Customers"
)

axes[0, 1].set_xlabel(
    "Month"
)

axes[0, 1].set_ylabel(
    "Customers"
)


# -------------------------
# Sales vs Profit
# -------------------------

axes[1, 0].scatter(
    sales,
    profit,
    color="red",
    s=80
)

axes[1, 0].set_title(
    "Sales vs Profit"
)

axes[1, 0].set_xlabel(
    "Sales"
)

axes[1, 0].set_ylabel(
    "Profit"
)


# -------------------------
# Sales Distribution
# -------------------------

axes[1, 1].hist(
    sales,
    bins=5,
    color="purple",
    edgecolor="black"
)

axes[1, 1].set_title(
    "Sales Distribution"
)

axes[1, 1].set_xlabel(
    "Sales"
)

axes[1, 1].set_ylabel(
    "Frequency"
)


plt.suptitle(
    "Sales Data Analysis Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.show()

Subplot म्हणजे काय?
एका figure मध्ये अनेक plots दाखवणे म्हणजे subplot.

उदा.:

┌───────────────┬───────────────┐
│    Sales      │   Customers   │
│   Line Chart  │   Bar Chart   │
├───────────────┼───────────────┤
│ Sales vs      │    Sales      │
│ Profit        │ Distribution  │
│   Scatter     │   Histogram   │
└───────────────┴───────────────┘

Basic subplot()
plt.subplot(
    2,
    2,
    1
)

याचा अर्थ:

2 → rows
2 → columns
1 → first plot

म्हणजे 2 × 2 grid मधला पहिला plot.

Modern approach — plt.subplots()
fig, axes = plt.subplots(
    2,
    2
)

मग:

axes[0, 0]
axes[0, 1]
axes[1, 0]
axes[1, 1]

प्रत्येक वेगळ्या plot साठी वापरता येतात.

tight_layout()
plt.tight_layout()

यामुळे plots मधील spacing व्यवस्थित होते आणि labels एकमेकांवर overlap होण्याची शक्यता कमी होते.

Commit message
Add Matplotlib subplot examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण 08_customization.py करू — colors, markers, legends, labels, styles आणि plot formatting एकाच file मध्ये.



You said:

next

ChatGPT said:
हो 👍 आता Step 46 — 08_customization.py.

हा file important आहे कारण आपण आतापर्यंत charts बनवले. आता ते readable आणि properly formatted कसे करायचे ते पाहू.

04-Matplotlib → Add file → Create new file

File name:

08_customization.py

हा पूर्ण code paste कर:

# Matplotlib - Plot Customization

import matplotlib.pyplot as plt


# ==================================================
# 1. Color
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [10000, 15000, 13000, 18000, 22000]

plt.plot(
    months,
    sales,
    color="blue"
)

plt.title("Sales")

plt.show()


# ==================================================
# 2. Line Style
# ==================================================

plt.plot(
    months,
    sales,
    linestyle="--"
)

plt.title("Dashed Line")

plt.show()


# ==================================================
# 3. Line Width
# ==================================================

plt.plot(
    months,
    sales,
    linewidth=4
)

plt.title("Thick Line")

plt.show()


# ==================================================
# 4. Markers
# ==================================================

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Line with Markers")

plt.show()


# ==================================================
# 5. Marker Size and Color
# ==================================================

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    markersize=8
)

plt.title("Customized Markers")

plt.show()


# ==================================================
# 6. Complete Line Customization
# ==================================================

plt.plot(
    months,
    sales,
    color="purple",
    linestyle="--",
    linewidth=2,
    marker="o",
    markersize=8
)

plt.title(
    "Monthly Sales",
    fontsize=16
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 7. Legend
# ==================================================

sales_2024 = [10000, 12000, 15000, 16000, 18000]

sales_2025 = [12000, 15000, 17000, 20000, 23000]

plt.plot(
    months,
    sales_2024,
    marker="o",
    label="2024"
)

plt.plot(
    months,
    sales_2025,
    marker="o",
    label="2025"
)

plt.title("Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 8. Legend Location
# ==================================================

plt.plot(
    months,
    sales_2024,
    label="2024"
)

plt.plot(
    months,
    sales_2025,
    label="2025"
)

plt.title("Sales Comparison")

plt.legend(
    loc="upper left"
)

plt.show()


# ==================================================
# 9. Rotate X-axis Labels
# ==================================================

products = [
    "Laptop",
    "Mobile Phone",
    "Tablet",
    "Monitor",
    "Keyboard"
]

product_sales = [
    120000,
    90000,
    60000,
    45000,
    25000
]

plt.bar(
    products,
    product_sales,
    color="skyblue"
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.xticks(
    rotation=30
)

plt.show()


# ==================================================
# 10. Figure Size
# ==================================================

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 11. Grid Customization
# ==================================================

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales with Grid")

plt.grid(
    color="gray",
    linestyle="--",
    linewidth=0.7,
    alpha=0.6
)

plt.show()


# ==================================================
# 12. Set Axis Limits
# ==================================================

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xlim(
    1,
    5
)

plt.ylim(
    0,
    60
)

plt.title("Axis Limits")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()


# ==================================================
# 13. Add Text / Annotation
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    25000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.annotate(
    "Highest Sales",
    xy=("May", 25000),
    xytext=("Mar", 22000),
    arrowprops={
        "arrowstyle": "->"
    }
)

plt.title("Monthly Sales")

plt.show()


# ==================================================
# 14. Bar Chart Customization
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur"
]

sales = [
    50000,
    75000,
    40000,
    60000
]

plt.bar(
    cities,
    sales,
    color=[
        "blue",
        "green",
        "orange",
        "purple"
    ],
    edgecolor="black"
)

plt.title(
    "City-wise Sales",
    fontsize=16
)

plt.xlabel("City")

plt.ylabel("Sales")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 15. Real Data Science Visualization
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    18000,
    16000,
    22000,
    25000
]

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    months,
    sales,
    color="#2563EB",
    linestyle="-",
    linewidth=2.5,
    marker="o",
    markersize=7,
    markerfacecolor="white",
    markeredgewidth=2
)

plt.title(
    "Monthly Sales Analysis",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Month",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.xticks(
    fontsize=10
)

plt.yticks(
    fontsize=10
)

plt.tight_layout()

plt.show()

यात आजचे important terms
color
linestyle
linewidth
marker
markersize
markerfacecolor
markeredgewidth
fontsize
fontweight
legend
grid
rotation
figsize
xlim
ylim
annotate
tight_layout

एक basic customized plot
plt.plot(
    months,
    sales,
    color="blue",
    linestyle="--",
    linewidth=2,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()

हे pattern तुला पुढे Pandas + Matplotlib + Seaborn EDA मध्ये खूप वापरायला मिळेल.

Commit message
Add Matplotlib plot customization examples

हे Commit changes कर.

झाल्यावर फक्त done म्हणा. मग पुढचा 09_save_plots.py करू.



You said:

next

ChatGPT said:
चला 👍 Step 47 — 09_save_plots.py

आता आपण तयार केलेले charts file म्हणून save करायला शिकू. Data Science projects मध्ये reports, presentations आणि notebooks साठी हे useful आहे.

04-Matplotlib → Add file → Create new file

File name:

09_save_plots.py

हा पूर्ण code paste कर:

# Matplotlib - Saving Plots

import matplotlib.pyplot as plt


# ==================================================
# 1. Save a Basic Line Chart
# ==================================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [10000, 15000, 13000, 18000, 22000]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.savefig(
    "monthly_sales.png"
)

plt.show()


# ==================================================
# 2. Save with Figure Size
# ==================================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    months,
    sales,
    color="skyblue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_large.png"
)

plt.show()


# ==================================================
# 3. Save as PNG with High Resolution
# ==================================================

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="green"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_high_resolution.png",
    dpi=300
)

plt.show()


# ==================================================
# 4. Save with Transparent Background
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="purple"
)

plt.title("Monthly Sales")

plt.savefig(
    "monthly_sales_transparent.png",
    transparent=True
)

plt.show()


# ==================================================
# 5. Save with Tight Bounding Box
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.savefig(
    "monthly_sales_tight.png",
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 6. Save Bar Chart
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur"
]

city_sales = [
    50000,
    75000,
    40000,
    60000
]

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    cities,
    city_sales,
    color="orange"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.savefig(
    "city_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 7. Save Scatter Plot
# ==================================================

experience = [
    1,
    2,
    3,
    4,
    5,
    6,
    7
]

salary = [
    30000,
    35000,
    40000,
    47000,
    55000,
    65000,
    75000
]

plt.figure(
    figsize=(8, 5)
)

plt.scatter(
    experience,
    salary,
    color="red",
    s=80
)

plt.title("Experience vs Salary")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.savefig(
    "experience_vs_salary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 8. Save Histogram
# ==================================================

marks = [
    45, 50, 55, 60, 62,
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92, 95
]

plt.figure(
    figsize=(8, 5)
)

plt.hist(
    marks,
    bins=6,
    color="steelblue",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.savefig(
    "marks_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 9. Save Pie Chart
# ==================================================

categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Other"
]

expenses = [
    15000,
    8000,
    25000,
    10000,
    5000
]

plt.figure(
    figsize=(7, 7)
)

plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Monthly Expense Distribution")

plt.savefig(
    "expense_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==================================================
# 10. Save Chart in Different Formats
# ==================================================

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    months,
    sales,
    marker="o",
    color="blue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

# PNG
plt.savefig(
    "sales_chart.png"
)

# PDF
plt.savefig(
    "sales_chart.pdf"
)

# SVG
plt.savefig(
    "sales_chart.svg"
)

plt.show()

Important concept
Chart save करण्यासाठी:

plt.savefig("filename.png")

हे plt.show() च्या आधी ठेवणे चांगले.

dpi
plt.savefig(
    "chart.png",
    dpi=300
)

dpi म्हणजे image resolution.

bbox_inches
bbox_inches="tight"

यामुळे chart च्या बाहेरची unnecessary जागा कमी करण्यास मदत होते.

वेगवेगळे formats
PNG → सामान्य image
JPG → image
PDF → document/report
SVG → scalable vector graphic

एक महत्त्वाची गोष्ट: हा Python file run केल्यावर तयार होणाऱ्या .png, .pdf, .svg files GitHub मध्ये लगेच upload करण्याची गरज नाही. आपण code शिकवण्यासाठी repository ठेवत आहोत; generated output files नंतर हवे असल्यास वेगळ्या outputs/ folder मध्ये ठेवू.

Commit message
Add Matplotlib plot saving examples

हे Commit changes कर.

झाल्यावर done म्हणा. मग पुढे 10_matplotlib_with_pandas.py करू — इथे आपला Pandas + Matplotlib connection सुरू होईल.



You said:

done

ChatGPT said:
छान 👍 आता Step 48 — 10_matplotlib_with_pandas.py.

हा आपल्या 04-Matplotlib folder मधला खूप important file आहे, कारण actual Data Science मध्ये आपण बर्‍याच वेळा Pandas DataFrame मधून directly visualization करतो.

04-Matplotlib → Add file → Create new file

File name:

10_matplotlib_with_pandas.py

हा पूर्ण code paste कर:

# Matplotlib with Pandas

import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# 1. Create DataFrame
# ==================================================

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 16000, 22000, 25000],
    "Profit": [2000, 2500, 3200, 2800, 4000, 5000]
}

df = pd.DataFrame(data)

print(df)


# ==================================================
# 2. Line Plot using Pandas DataFrame
# ==================================================

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 3. Plot DataFrame Column Directly
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o"
)

plt.title("Monthly Sales")

plt.show()


# ==================================================
# 4. Bar Chart using Pandas
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="bar",
    color="skyblue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()


# ==================================================
# 5. Multiple Columns
# ==================================================

df.plot(
    x="Month",
    y=["Sales", "Profit"],
    kind="line",
    marker="o"
)

plt.title("Sales and Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 6. Multiple Bar Charts
# ==================================================

df.plot(
    x="Month",
    y=["Sales", "Profit"],
    kind="bar"
)

plt.title("Sales vs Profit")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.show()


# ==================================================
# 7. Scatter Plot using DataFrame
# ==================================================

df.plot(
    x="Sales",
    y="Profit",
    kind="scatter",
    color="red"
)

plt.title("Sales vs Profit")

plt.xlabel("Sales")

plt.ylabel("Profit")

plt.show()


# ==================================================
# 8. Create City-wise Data
# ==================================================

city_data = {
    "City": [
        "Pune",
        "Mumbai",
        "Nashik",
        "Nagpur",
        "Thane"
    ],
    "Sales": [
        50000,
        75000,
        40000,
        60000,
        85000
    ]
}

city_df = pd.DataFrame(city_data)

print(city_df)


# ==================================================
# 9. City-wise Sales Bar Chart
# ==================================================

city_df.plot(
    x="City",
    y="Sales",
    kind="bar",
    color="green"
)

plt.title("City-wise Sales")

plt.xlabel("City")

plt.ylabel("Sales")

plt.xticks(
    rotation=0
)

plt.show()


# ==================================================
# 10. GroupBy + Matplotlib
# ==================================================

sales_data = {
    "City": [
        "Pune",
        "Mumbai",
        "Pune",
        "Mumbai",
        "Nashik",
        "Nashik"
    ],
    "Sales": [
        10000,
        15000,
        12000,
        18000,
        9000,
        11000
    ]
}

sales_df = pd.DataFrame(sales_data)

city_sales = (
    sales_df
    .groupby("City")["Sales"]
    .sum()
)

print(city_sales)


city_sales.plot(
    kind="bar",
    color="orange"
)

plt.title("Total Sales by City")

plt.xlabel("City")

plt.ylabel("Total Sales")

plt.xticks(
    rotation=0
)

plt.show()


# ==================================================
# 11. Histogram using Pandas
# ==================================================

marks_data = {
    "Marks": [
        45, 50, 55, 60,
        62, 65, 68, 70,
        72, 75, 78, 80,
        82, 85, 88, 90,
        92, 95
    ]
}

marks_df = pd.DataFrame(marks_data)

marks_df["Marks"].plot(
    kind="hist",
    bins=6,
    color="purple",
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()


# ==================================================
# 12. DataFrame Plot with Figure Size
# ==================================================

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o",
    figsize=(10, 5),
    color="blue"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.show()


# ==================================================
# 13. Real Data Science Example
# ==================================================

customer_data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Customers": [
        100,
        120,
        150,
        140,
        180,
        210
    ],
    "Sales": [
        12000,
        15000,
        18000,
        16000,
        22000,
        25000
    ]
}

customer_df = pd.DataFrame(
    customer_data
)

fig, axes = plt.subplots(
    1,
    2,
    figsize=(12, 5)
)


# Customer Trend

axes[0].plot(
    customer_df["Month"],
    customer_df["Customers"],
    marker="o",
    color="green"
)

axes[0].set_title(
    "Customer Trend"
)

axes[0].set_xlabel(
    "Month"
)

axes[0].set_ylabel(
    "Customers"
)


# Sales Trend

axes[1].bar(
    customer_df["Month"],
    customer_df["Sales"],
    color="steelblue"
)

axes[1].set_title(
    "Sales Trend"
)

axes[1].set_xlabel(
    "Month"
)

axes[1].set_ylabel(
    "Sales"
)


plt.tight_layout()

plt.show()

यात काय important आहे?
आता आपण दोन libraries जोडल्या:

Pandas
   ↓
DataFrame
   ↓
Data Analysis
   ↓
Matplotlib
   ↓
Visualization

दोन पद्धती लक्षात ठेव
Method 1 — Matplotlib directly:

plt.plot(
    df["Month"],
    df["Sales"]
)

Method 2 — Pandas plotting:

df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

दोन्ही valid आहेत.

Pandas मधून common plots
df.plot(kind="line")
df.plot(kind="bar")
df.plot(kind="scatter")
df.plot(kind="hist")
df.plot(kind="box")
df.plot(kind="pie")

यामुळे पुढे EDA करताना DataFrame मधून पटकन visualization करता येईल.

Commit message
Add Pandas and Matplotlib integration examples

Commit changes कर.

झाल्यावर done म्हणा. मग आपण 11_practice.py बनवू — आतापर्यंतच्या Matplotlib concepts वर trainer म्हणून students ना देता येतील असे practical exercises.



You said:

done

ChatGPT said:
छान 👍 आता Step 49 — 11_practice.py.

हा file आपण practice / exercises साठी ठेवू. यात answers देणार नाही, म्हणजे तुझ्या GitHub repository मध्ये students/learners साठी practice करता येईल.

04-Matplotlib → Add file → Create new file

File name:

11_practice.py

हा code paste कर:

# Matplotlib - Practice Questions

import matplotlib.pyplot as plt


# ==================================================
# Practice 1 - Basic Line Plot
# ==================================================

# Create a line chart using the following data.

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    10000,
    12000,
    15000,
    13000,
    18000,
    22000
]

# Tasks:
# 1. Create a line plot.
# 2. Add a title.
# 3. Add X-axis label.
# 4. Add Y-axis label.
# 5. Add grid.
# 6. Add markers.


# ==================================================
# Practice 2 - Bar Chart
# ==================================================

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard"
]

sales = [
    120000,
    90000,
    60000,
    45000,
    25000
]

# Tasks:
# 1. Create a bar chart.
# 2. Give the chart a title.
# 3. Add X-axis and Y-axis labels.
# 4. Change the bar color.
# 5. Display the values on top of each bar.


# ==================================================
# Practice 3 - Scatter Plot
# ==================================================

study_hours = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]

marks = [
    40,
    45,
    50,
    58,
    65,
    72,
    80,
    90
]

# Tasks:
# 1. Create a scatter plot.
# 2. Put Study Hours on X-axis.
# 3. Put Marks on Y-axis.
# 4. Change marker color.
# 5. Change marker size.
# 6. Add grid.


# ==================================================
# Practice 4 - Histogram
# ==================================================

student_marks = [
    35, 40, 45, 50, 52,
    55, 58, 60, 62, 65,
    68, 70, 72, 75, 78,
    80, 82, 85, 88, 90,
    92, 95
]

# Tasks:
# 1. Create a histogram.
# 2. Use 5 bins.
# 3. Add edgecolor.
# 4. Add title.
# 5. Add X-axis and Y-axis labels.


# ==================================================
# Practice 5 - Pie Chart
# ==================================================

expenses = [
    15000,
    8000,
    25000,
    10000,
    5000
]

categories = [
    "Food",
    "Travel",
    "Rent",
    "Shopping",
    "Other"
]

# Tasks:
# 1. Create a pie chart.
# 2. Add category labels.
# 3. Show percentages.
# 4. Change the colors.
# 5. Set startangle to 90.


# ==================================================
# Practice 6 - Multiple Lines
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales_2024 = [
    100,
    120,
    150,
    160,
    180
]

sales_2025 = [
    120,
    140,
    170,
    200,
    230
]

# Tasks:
# 1. Plot both years in one chart.
# 2. Use different colors.
# 3. Add markers.
# 4. Add legend.
# 5. Add title.
# 6. Add grid.


# ==================================================
# Practice 7 - Subplots
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    22000
]

profit = [
    2000,
    3000,
    2500,
    4000,
    5500
]

customers = [
    100,
    120,
    110,
    150,
    180
]

# Tasks:
# Create a 2x2 subplot layout.

# Plot 1:
# Monthly Sales - Line Chart

# Plot 2:
# Monthly Profit - Bar Chart

# Plot 3:
# Monthly Customers - Line Chart

# Plot 4:
# Sales vs Profit - Scatter Plot


# ==================================================
# Practice 8 - Plot Customization
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    14000,
    12000,
    18000,
    25000
]

# Tasks:
# Create a line chart and customize:
#
# 1. Line color
# 2. Line style
# 3. Line width
# 4. Marker
# 5. Marker size
# 6. Title font size
# 7. Axis labels
# 8. Grid
# 9. Figure size


# ==================================================
# Practice 9 - Sales Analysis
# ==================================================

cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur",
    "Thane"
]

sales = [
    50000,
    75000,
    40000,
    60000,
    85000
]

# Tasks:
# 1. Create a bar chart.
# 2. Find the city with the highest sales.
# 3. Display values on bars.
# 4. Add title.
# 5. Add axis labels.
# 6. Customize colors.


# ==================================================
# Practice 10 - DataFrame Visualization
# ==================================================

import pandas as pd


data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Sales": [
        12000,
        15000,
        18000,
        16000,
        22000,
        25000
    ],
    "Profit": [
        2000,
        2500,
        3200,
        2800,
        4000,
        5000
    ]
}

df = pd.DataFrame(data)

# Tasks:
# 1. Display the DataFrame.
# 2. Create a line chart for Sales.
# 3. Create a line chart for Profit.
# 4. Compare Sales and Profit.
# 5. Create a bar chart for Sales.
# 6. Create a scatter plot between Sales and Profit.


# ==================================================
# Practice 11 - Save Plot
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    10000,
    15000,
    13000,
    18000,
    22000
]

# Tasks:
# 1. Create a line chart.
# 2. Save it as "sales_chart.png".
# 3. Use dpi=300.
# 4. Use bbox_inches="tight".


# ==================================================
# Practice 12 - Mini Data Analysis
# ==================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

sales = [
    12000,
    15000,
    18000,
    16000,
    22000,
    25000
]

customers = [
    100,
    120,
    150,
    140,
    180,
    210
]

profit = [
    2000,
    2500,
    3200,
    2800,
    4000,
    5000
]

# Tasks:
#
# Create a simple visualization dashboard
# containing:
#
# 1. Sales trend
# 2. Customer trend
# 3. Sales vs Profit
# 4. Sales distribution
#
# Use subplots.
#
# Add:
# - Titles
# - Axis labels
# - Colors
# - Markers where required
# - Grid where useful
# - Proper spacing

हा file कशासाठी?
आत्तापर्यंत आपण:

01_basic_plot.py
02_line_chart.py
03_bar_chart.py
04_scatter_plot.py
05_histogram.py
06_pie_chart.py
07_subplots.py
08_customization.py
09_save_plots.py
10_matplotlib_with_pandas.py

हे concepts केले.

आता 11_practice.py मध्ये ते स्वतः करून पाहण्यासाठी questions आहेत.

म्हणजे तुझ्या GitHub मध्ये learner ला:

Concept
   ↓
Example
   ↓
Code
   ↓
Practice

असा flow मिळेल.

Commit message
Add Matplotlib practice exercises

Commit changes कर.

यानंतर 04-Matplotlib मध्ये आपले मुख्य files पूर्ण झाले आहेत. done म्हटल्यावर मी तुला Matplotlib folder ची final structure + README मध्ये कोणती छोटी update करायची ते एकदम सांगतो.



You said:

done

ChatGPT said:
छान 👍 04-Matplotlib चे files झाले.

आता पुढचा step README update आहे. नवीन file बनवायची गरज नाही.

Step 50 — 04-Matplotlib/README.md update
GitHub मध्ये:

04-Matplotlib → README.md → ✏️ Edit

तिथे सध्या जे आहे ते replace करून हे paste कर:

# Matplotlib for Data Science

Matplotlib is a Python library used for creating charts and visualizations.

It is commonly used in Data Science for understanding and presenting data.

## Topics Covered

- Basic plotting
- Line chart
- Bar chart
- Scatter plot
- Histogram
- Pie chart
- Subplots
- Plot customization
- Saving plots
- Matplotlib with Pandas
- Practice exercises

## Files

### 01_basic_plot.py
Basic Matplotlib plotting and figure concepts.

### 02_line_chart.py
Line charts with titles, labels, markers and grid.

### 03_bar_chart.py
Bar charts for comparing categories.

### 04_scatter_plot.py
Scatter plots for understanding relationships between two numerical variables.

### 05_histogram.py
Histograms for understanding numerical data distribution.

### 06_pie_chart.py
Pie charts for showing category proportions.

### 07_subplots.py
Creating multiple charts in one figure.

### 08_customization.py
Colors, markers, line styles, legends, grid, labels and other formatting.

### 09_save_plots.py
Saving charts as PNG, PDF and SVG files.

### 10_matplotlib_with_pandas.py
Using Matplotlib with Pandas DataFrames.

### 11_practice.py
Practice questions based on the topics covered.

## Common Matplotlib Functions

```python
import matplotlib.pyplot as plt

plt.plot()
plt.bar()
plt.scatter()
plt.hist()
plt.pie()

plt.title()
plt.xlabel()
plt.ylabel()

plt.legend()
plt.grid()

plt.show()
plt.savefig()

Basic Data Science Visualization Flow
Data
  ↓
Pandas
  ↓
Matplotlib
  ↓
Visualization
  ↓
Understand Data
  ↓
Analysis

Installation
pip install matplotlib

Official Documentation
https://matplotlib.org/stable/


### Commit message

```text
Update Matplotlib README

Commit changes कर.

बस. हे झाल्यावर 04-Matplotlib व्यवस्थित complete होईल. मग आपण 05-Seaborn ला सुरुवात करू.



You said:

readme.md madhe kay copy paste karu te ek celk adhe dya

ChatGPT said:
हो 👍 एकदम एकच complete README देतो. 04-Matplotlib/README.md मधलं सगळं delete करून खालील पूर्ण content copy-paste कर.

04-Matplotlib README


Matplotlib for Data Science
Matplotlib is a Python library used for creating charts and visualizations.

It is commonly used in Data Science for understanding and presenting data.

Topics Covered
Basic plotting

Line chart

Bar chart

Scatter plot

Histogram

Pie chart

Subplots

Plot customization

Saving plots

Matplotlib with Pandas

Practice exercises

Files
01_basic_plot.py
Basic Matplotlib plotting and figure concepts.

02_line_chart.py
Line charts with titles, labels, markers and grid.

03_bar_chart.py
Bar charts for comparing different categories.

04_scatter_plot.py
Scatter plots for understanding the relationship between two numerical variables.

05_histogram.py
Histograms for understanding the distribution of numerical data.

06_pie_chart.py
Pie charts for showing proportions of different categories.

07_subplots.py
Creating multiple charts in a single figure.

08_customization.py
Colors, markers, line styles, legends, grid, labels and other plot formatting.

09_save_plots.py
Saving charts as PNG, PDF and SVG files.

10_matplotlib_with_pandas.py
Using Matplotlib with Pandas DataFrames for data visualization.

11_practice.py
Practice questions based on the Matplotlib topics covered in this folder.

Common Matplotlib Functions
import matplotlib.pyplot as plt

plt.plot()
plt.bar()
plt.scatter()
plt.hist()
plt.pie()

plt.title()
plt.xlabel()
plt.ylabel()

plt.legend()
plt.grid()

plt.show()
plt.savefig()

Basic Example
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [10000, 15000, 13000, 18000]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.show()

Installation
Matplotlib can be installed using pip:

pip install matplotlib

Import Matplotlib:

import matplotlib.pyplot as plt

Important Concepts
Line Plot
Used to show trends over time.

plt.plot(x, y)

Bar Chart
Used to compare categories.

plt.bar(x, y)

Scatter Plot
Used to understand the relationship between two numerical variables.

plt.scatter(x, y)

Histogram
Used to understand the distribution of numerical data.

plt.hist(data)

Pie Chart
Used to show proportions or percentage share.

plt.pie(values, labels=labels)

Subplots
Used to display multiple charts in one figure.

fig, axes = plt.subplots(2, 2)

Plot Customization
Commonly used customization options:

color
linestyle
linewidth
marker
markersize
fontsize
figsize
legend
grid
xlim
ylim

Example:

plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    linewidth=2,
    marker="o"
)

Saving a Plot
plt.savefig(
    "chart.png",
    dpi=300,
    bbox_inches="tight"
)

Matplotlib supports formats such as:

PNG

PDF

SVG

Matplotlib with Pandas
Matplotlib is commonly used together with Pandas for Data Analysis and visualization.

Pandas
   ↓
DataFrame
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Matplotlib
   ↓
Visualization

Example:

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [10000, 15000, 13000, 18000]
}

df = pd.DataFrame(data)

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()

Data Science Use Cases
Matplotlib can be used for:

Sales analysis

Customer analysis

Student performance analysis

Salary analysis

Time-series visualization

Distribution analysis

Comparing categories

Understanding relationships between variables

Exploratory Data Analysis (EDA)

Presenting Data Science results

Learning Flow
Matplotlib
   ↓
Basic Plot
   ↓
Line Chart
   ↓
Bar Chart
   ↓
Scatter Plot
   ↓
Histogram
   ↓
Pie Chart
   ↓
Subplots
   ↓
Customization
   ↓
Save Plots
   ↓
Pandas + Matplotlib
   ↓
Practice

Official Documentation
Matplotlib Documentation:

https://matplotlib.org/stable/

हे paste करून Commit changes कर.

नंतर done म्हणा. आपण मग 05-Seaborn folder सुरू करू.



You said:

done

ChatGPT said:
छान 👍 आता 05-Seaborn सुरू करूया.

आपण आधीच्या pattern प्रमाणेच जाऊ — एक file → code → commit → done → next.

Step 51 — 05-Seaborn folder तयार करा
तुझ्या main repository:

Python-for-Data-Science

मध्ये जा.

Add file → Create new file

File name मध्ये:

05-Seaborn/README.md

लिहा.

आता खालील पूर्ण content paste करा:

05-Seaborn README


Seaborn for Data Science
Seaborn is a Python data visualization library built on top of Matplotlib.

It is mainly used for creating statistical and informative visualizations.

Seaborn works very well with Pandas DataFrames and is commonly used during Exploratory Data Analysis (EDA).

Why Seaborn?
Seaborn makes it easier to create attractive and meaningful statistical charts with less code.

It is useful for:

Data visualization

Exploratory Data Analysis (EDA)

Statistical analysis

Understanding data distributions

Finding relationships between variables

Comparing categories

Understanding correlations

Visualizing categorical data

Installation
Install Seaborn using pip:

pip install seaborn

Import Seaborn
The commonly used alias is sns.

import seaborn as sns

Matplotlib is also commonly imported:

import matplotlib.pyplot as plt

Seaborn and Matplotlib
Seaborn is built on top of Matplotlib.

A common workflow is:

Pandas
   ↓
Data Cleaning
   ↓
Seaborn
   ↓
Visualization
   ↓
EDA

Seaborn can also be combined with Matplotlib for additional customization.

Important Seaborn Plots
Some commonly used Seaborn plots are:

Scatter Plot

Line Plot

Bar Plot

Count Plot

Histogram

Box Plot

Violin Plot

Strip Plot

Swarm Plot

Heatmap

Pair Plot

Regression Plot

Basic Example
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.scatterplot(
    data=data,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()

Working with Pandas
Seaborn works directly with Pandas DataFrames.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, 90, 75, 85]
}

df = pd.DataFrame(data)

sns.barplot(
    data=df,
    x="Name",
    y="Marks"
)

plt.show()

Common Functions
sns.scatterplot()
sns.lineplot()
sns.barplot()
sns.countplot()
sns.histplot()
sns.boxplot()
sns.violinplot()
sns.stripplot()
sns.swarmplot()
sns.heatmap()
sns.pairplot()
sns.regplot()

Learning Flow
Seaborn
   ↓
Basic Visualization
   ↓
Categorical Data
   ↓
Numerical Data
   ↓
Distribution
   ↓
Relationships
   ↓
Correlation
   ↓
EDA

Data Science Use Cases
Seaborn is commonly used for:

Exploratory Data Analysis

Customer analysis

Sales analysis

Student performance analysis

Feature analysis

Distribution analysis

Correlation analysis

Outlier detection

Comparing categories

Understanding relationships between variables

Official Documentation
Seaborn Documentation:

https://seaborn.pydata.org/

Commit message
Add Seaborn README

Commit changes करा.

फक्त एवढंच करा आत्ता. झाल्यावर done म्हणा. मग आपण 01_basic_plots.py बनवू.



You said:

├── 06-Statistics/
└── 07-Machine-Learning/ ya saravnsathi ekach weli sarv craete karu  de .me te save karun eke ke nantr github la add kare .aata sarv ek zake ki ek as eakach weli de

ChatGPT said:
हो, नक्की 👍 आता आपण एक-एक folder तयार न करता, आधी पूर्ण structure तयार करू. तू हे सगळं save करून नंतर GitHub वर एक-एक folder/file add करू शकतेस.

तुझ्या Python-for-Data-Science repository साठी final structure असा ठेव:

Python-for-Data-Science/
│
├── README.md
│
├── 01-Python-Basics/
│   ├── README.md
│   ├── 01_variables.py
│   ├── 02_data_types.py
│   ├── 03_input_output.py
│   ├── 04_operators.py
│   ├── 05_conditional_statements.py
│   ├── 06_loops.py
│   ├── 07_strings.py
│   ├── 08_lists.py
│   ├── 09_tuples.py
│   ├── 10_sets.py
│   ├── 11_dictionaries.py
│   ├── 12_functions.py
│   ├── 13_lambda.py
│   ├── 14_list_comprehension.py
│   ├── 15_exception_handling.py
│   └── 16_practice.py
│
├── 02-NumPy/
│   ├── README.md
│   ├── 01_numpy_basics.py
│   ├── 02_array_creation.py
│   ├── 03_array_attributes.py
│   ├── 04_array_indexing.py
│   ├── 05_array_slicing.py
│   ├── 06_array_reshape.py
│   ├── 07_array_math_operations.py
│   ├── 08_statistical_operations.py
│   ├── 09_broadcasting.py
│   ├── 10_random_numbers.py
│   ├── 11_sorting_searching.py
│   ├── 12_numpy_with_pandas.py
│   └── 13_practice.py
│
├── 03-Pandas/
│   ├── README.md
│   ├── 01_series.py
│   ├── 02_dataframe.py
│   ├── 03_reading_data.py
│   ├── 04_inspecting_data.py
│   ├── 05_selecting_data.py
│   ├── 06_filtering_data.py
│   ├── 07_missing_values.py
│   ├── 08_duplicates.py
│   ├── 09_sorting.py
│   ├── 10_groupby.py
│   ├── 11_apply.py
│   ├── 12_string_operations.py
│   ├── 13_datetime.py
│   ├── 14_merge_concat.py
│   ├── 15_export_data.py
│   └── 16_practice.py
│
├── 04-Matplotlib/
│   ├── README.md
│   ├── 01_basic_plot.py
│   ├── 02_line_chart.py
│   ├── 03_bar_chart.py
│   ├── 04_scatter_plot.py
│   ├── 05_histogram.py
│   ├── 06_pie_chart.py
│   ├── 07_subplots.py
│   ├── 08_customization.py
│   ├── 09_save_plots.py
│   ├── 10_matplotlib_with_pandas.py
│   └── 11_practice.py
│
├── 05-Seaborn/
│   ├── README.md
│   ├── 01_basic_plots.py
│   ├── 02_scatter_plot.py
│   ├── 03_line_plot.py
│   ├── 04_bar_plot.py
│   ├── 05_count_plot.py
│   ├── 06_histogram.py
│   ├── 07_box_plot.py
│   ├── 08_violin_plot.py
│   ├── 09_categorical_plots.py
│   ├── 10_heatmap.py
│   ├── 11_pairplot.py
│   ├── 12_regression_plot.py
│   ├── 13_seaborn_with_pandas.py
│   └── 14_practice.py
│
├── 06-Statistics/
│   ├── README.md
│   ├── 01_statistics_basics.py
│   ├── 02_population_sample.py
│   ├── 03_mean_median_mode.py
│   ├── 04_range_variance_std.py
│   ├── 05_percentiles_quartiles.py
│   ├── 06_probability.py
│   ├── 07_distribution.py
│   ├── 08_normal_distribution.py
│   ├── 09_skewness.py
│   ├── 10_correlation.py
│   ├── 11_covariance.py
│   ├── 12_sampling.py
│   ├── 13_hypothesis_testing.py
│   ├── 14_confidence_interval.py
│   └── 15_practice.py
│
└── 07-Machine-Learning/
    ├── README.md
    ├── 01_machine_learning_basics.py
    ├── 02_supervised_learning.py
    ├── 03_unsupervised_learning.py
    ├── 04_train_test_split.py
    ├── 05_linear_regression.py
    ├── 06_multiple_linear_regression.py
    ├── 07_logistic_regression.py
    ├── 08_knn.py
    ├── 09_decision_tree.py
    ├── 10_random_forest.py
    ├── 11_kmeans.py
    ├── 12_preprocessing.py
    ├── 13_feature_scaling.py
    ├── 14_model_evaluation.py
    ├── 15_confusion_matrix.py
    ├── 16_cross_validation.py
    ├── 17_hyperparameter_tuning.py
    └── 18_practice.py

पण एक महत्त्वाची गोष्ट
सगळ्या .py files चा content आत्ता भरायचा नाही. आपण प्रत्येक folder साठी content व्यवस्थित तयार करू.

तुझ्यासाठी workflow असा ठेवू:

Structure तयार
      ↓
README तयार
      ↓
01 file
      ↓
Code + Explanation
      ↓
GitHub ला add
      ↓
done
      ↓
02 file
      ↓
...

आणि तू trainer असल्यामुळे code फक्त basic नसून प्रत्येक topic मध्ये:

Definition

Why it is used

Basic syntax

Simple examples

Data Science example

Important functions

Common mistakes

Practice questions

असा teaching-oriented content ठेवू.

आत्ता फक्त ही structure save करून ठेव. मग आपण 05-Seaborn पासून पुढे files भरायला सुरुवात करू.



You said:

│
├── 05-Seaborn/
│   ├── README.md
│   ├── 01_basic_plots.py
│   ├── 02_scatter_plot.py
│   ├── 03_line_plot.py
│   ├── 04_bar_plot.py
│   ├── 05_count_plot.py
│   ├── 06_histogram.py
│   ├── 07_box_plot.py
│   ├── 08_violin_plot.py
│   ├── 09_categorical_plots.py
│   ├── 10_heatmap.py
│   ├── 11_pairplot.py
│   ├── 12_regression_plot.py
│   ├── 13_seaborn_with_pandas.py
│   └── 14_practice.py
│he sarv de

ChatGPT said:
हो 👍 आता 05-Seaborn चे सगळे files एकाच वेळी देतो. तू हे प्रत्येक .py file मध्ये copy-paste करून save करू शकतेस. Content trainer म्हणून teaching-friendly ठेवला आहे — basic + explanation + Data Science examples.

01_basic_plots.py
# Seaborn - Basic Plots

import seaborn as sns
import matplotlib.pyplot as plt


# Seaborn comes with some built-in datasets.
# We will use the tips dataset for practice.

df = sns.load_dataset("tips")

print(df.head())


# ------------------------------------------
# 1. Basic Scatter Plot
# ------------------------------------------

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")

plt.show()


# ------------------------------------------
# 2. Basic Line Plot
# ------------------------------------------

sns.lineplot(
    data=df,
    x="size",
    y="total_bill"
)

plt.title("Size vs Total Bill")

plt.show()


# ------------------------------------------
# 3. Basic Bar Plot
# ------------------------------------------

sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Average Bill by Day")

plt.show()


# ------------------------------------------
# 4. Basic Count Plot
# ------------------------------------------

sns.countplot(
    data=df,
    x="day"
)

plt.title("Number of Records by Day")

plt.show()


# ------------------------------------------
# 5. Basic Histogram
# ------------------------------------------

sns.histplot(
    data=df,
    x="total_bill"
)

plt.title("Total Bill Distribution")

plt.show()


# ------------------------------------------
# 6. Basic Box Plot
# ------------------------------------------

sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("Bill Distribution by Day")

plt.show()

02_scatter_plot.py
