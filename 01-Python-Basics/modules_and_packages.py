# ============================================
# MODULES AND PACKAGES IN PYTHON
# ============================================

# A module is a Python file containing functions,
# variables, or classes that can be reused.


# ============================================
# IMPORTING BUILT-IN MODULES
# ============================================

import math

print(math.sqrt(25))
print(math.pi)


# ============================================
# RANDOM MODULE
# ============================================

import random

random_number = random.randint(1, 100)

print("Random number:", random_number)


# ============================================
# DATETIME MODULE
# ============================================

from datetime import datetime

current_time = datetime.now()

print("Current date and time:", current_time)


# ============================================
# IMPORT SPECIFIC FUNCTION
# ============================================

from math import sqrt

print(sqrt(64))


# ============================================
# MODULE ALIAS
# ============================================

import math as mathematical_operations

print(mathematical_operations.sqrt(100))


# ============================================
# DATA SCIENCE LIBRARIES
# ============================================

# Common Data Science libraries include:
#
# NumPy
# Pandas
# Matplotlib
# Seaborn
# Scikit-learn


# Example:
#
# import numpy as np
# import pandas as pd
#
# numbers = np.array([1, 2, 3, 4, 5])
# data = pd.DataFrame({"numbers": numbers})
#
# print(data)


# ============================================
# CREATING YOUR OWN MODULE
# ============================================

# Suppose we create a file named:
#
# calculator.py
#
# with:
#
# def add(a, b):
#     return a + b
#
# We can import it using:
#
# from calculator import add
#
# print(add(10, 20))


# ============================================
# __name__ == "__main__"
# ============================================

def greet():
    print("Welcome to Python for Data Science!")


if __name__ == "__main__":
    greet()


# ============================================
# PACKAGES
# ============================================

# A package is a collection of related Python modules.
#
# Example structure:
#
# data_analysis/
#     __init__.py
#     cleaning.py
#     visualization.py
#     statistics.py


# ============================================
# PRACTICE
# ============================================

# 1. Import the math module.
# 2. Generate a random number.
# 3. Display the current date and time.
# 4. Create your own calculator module.
# 5. Import a function from your custom module.
# 6. Explore commonly used Data Science libraries.
