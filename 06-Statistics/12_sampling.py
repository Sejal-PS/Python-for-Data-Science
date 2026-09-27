# Sampling

import numpy as np


# ------------------------------------------
# Population
# ------------------------------------------

population = np.arange(
    1,
    101
)

print(
    "Population:"
)

print(
    population
)


# ------------------------------------------
# Random Sample
# ------------------------------------------

sample = np.random.choice(
    population,
    size=10,
    replace=False
)

print(
    "\nRandom Sample:"
)

print(
    sample
)


# ------------------------------------------
# Sample Mean
# ------------------------------------------

print(
    "\nSample Mean:",
    np.mean(sample)
)


# ------------------------------------------
# Population Mean
# ------------------------------------------

print(
    "Population Mean:",
    np.mean(population)
)


# ------------------------------------------
# Sampling Concept
# ------------------------------------------

# Population:
# Complete group.
#
# Sample:
# Smaller group selected from population.
#
# Sampling helps us study large populations
# without collecting data from every member.


# ------------------------------------------
# Random Sampling
# ------------------------------------------

# Every observation can have a chance
# of being selected.
