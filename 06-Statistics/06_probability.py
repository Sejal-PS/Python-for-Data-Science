# Probability Basics

import random


# ------------------------------------------
# What is Probability?
# ------------------------------------------

# Probability measures how likely
# an event is to happen.
#
# Probability ranges from 0 to 1.
#
# 0 -> Impossible
# 1 -> Certain


# ------------------------------------------
# Simple Probability
# ------------------------------------------

# Rolling a fair dice

total_outcomes = 6

favorable_outcomes = 1

probability = (
    favorable_outcomes /
    total_outcomes
)

print(
    "Probability of getting 6:",
    probability
)


# ------------------------------------------
# Probability of Even Number
# ------------------------------------------

even_outcomes = 3

probability_even = (
    even_outcomes /
    total_outcomes
)

print(
    "Probability of even number:",
    probability_even
)


# ------------------------------------------
# Random Experiment
# ------------------------------------------

result = random.randint(
    1,
    6
)

print(
    "Dice Result:",
    result
)


# ------------------------------------------
# Coin Toss
# ------------------------------------------

coin = random.choice(
    ["Heads", "Tails"]
)

print(
    "Coin Result:",
    coin
)


# ------------------------------------------
# Basic Formula
# ------------------------------------------

# Probability =
#
# Favorable Outcomes
# ------------------
# Total Outcomes
