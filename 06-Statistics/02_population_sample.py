# Population and Sample

import statistics


# ------------------------------------------
# Population
# ------------------------------------------

# Population means the complete group
# that we are interested in studying.

population = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

print("Population:")
print(population)


# ------------------------------------------
# Sample
# ------------------------------------------

# A sample is a smaller part selected
# from the population.

sample = [
    20,
    40,
    60,
    80
]

print("\nSample:")
print(sample)


# ------------------------------------------
# Population Mean
# ------------------------------------------

population_mean = statistics.mean(
    population
)

print(
    "\nPopulation Mean:",
    population_mean
)


# ------------------------------------------
# Sample Mean
# ------------------------------------------

sample_mean = statistics.mean(
    sample
)

print(
    "Sample Mean:",
    sample_mean
)


# ------------------------------------------
# Population vs Sample
# ------------------------------------------

print("\nPopulation:")
print("Complete group of data")

print("\nSample:")
print("Subset of the population")


# Example:
#
# Population:
# All students in a college
#
# Sample:
# 100 students selected from that college
