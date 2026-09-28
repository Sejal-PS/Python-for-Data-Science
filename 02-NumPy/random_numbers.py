"""
NumPy Random Numbers

Random number generation is useful for simulations,
testing, sampling, and creating practice datasets.
"""

import numpy as np


# --------------------------------------------------
# 1. Random Integers
# --------------------------------------------------

random_numbers = np.random.randint(
    1,
    101,
    size=10
)

print("Random integers:")
print(random_numbers)


# --------------------------------------------------
# 2. Random Decimal Values
# --------------------------------------------------

random_values = np.random.random(5)

print("\nRandom decimal values:")
print(random_values)


# --------------------------------------------------
# 3. Random 2D Array
# --------------------------------------------------

random_matrix = np.random.randint(
    1,
    50,
    size=(3, 4)
)

print("\nRandom 2D array:")
print(random_matrix)


# --------------------------------------------------
# 4. Random Choice
# --------------------------------------------------

products = np.array([
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones"
])

selected_products = np.random.choice(
    products,
    size=5
)

print("\nRandomly selected products:")
print(selected_products)


# --------------------------------------------------
# 5. Sampling Without Replacement
# --------------------------------------------------

customer_ids = np.arange(1, 21)

sample = np.random.choice(
    customer_ids,
    size=5,
    replace=False
)

print("\nRandom customer sample:")
print(sample)


# --------------------------------------------------
# 6. Random Seed
# --------------------------------------------------

np.random.seed(42)

reproducible_data = np.random.randint(
    1,
    100,
    size=5
)

print("\nReproducible random data:")
print(reproducible_data)


# --------------------------------------------------
# 7. Normal Distribution
# --------------------------------------------------

normal_data = np.random.normal(
    loc=50,
    scale=10,
    size=10
)

print("\nNormally distributed data:")
print(normal_data)


# --------------------------------------------------
# 8. Practical Data Science Example
# --------------------------------------------------

np.random.seed(42)

ages = np.random.randint(
    18,
    65,
    size=20
)

print("\nSample customer ages:")
print(ages)

print("Average age:", np.mean(ages))
print("Minimum age:", np.min(ages))
print("Maximum age:", np.max(ages))


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Generate 20 random integers between 1 and 100.
# 2. Generate a 5x5 random matrix.
# 3. Select 10 random values without replacement.
# 4. Use a seed and generate reproducible data.
# 5. Generate 100 values from a normal distribution.
# 6. Create a sample customer dataset using random values.
