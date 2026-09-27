# Confidence Interval

import numpy as np
from scipy import stats


data = np.array([
    45,
    50,
    52,
    48,
    55,
    60,
    58,
    49,
    53,
    51
])


# ------------------------------------------
# Sample Mean
# ------------------------------------------

mean = np.mean(data)

print(
    "Sample Mean:",
    mean
)


# ------------------------------------------
# Sample Standard Error
# ------------------------------------------

standard_error = stats.sem(
    data
)

print(
    "Standard Error:",
    standard_error
)


# ------------------------------------------
# 95% Confidence Interval
# ------------------------------------------

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(data) - 1,
    loc=mean,
    scale=standard_error
)

print(
    "\n95% Confidence Interval:"
)

print(
    confidence_interval
)


# ------------------------------------------
# Understanding
# ------------------------------------------

# A confidence interval gives a range of
# plausible values for a population parameter
# based on sample data.
#
# Confidence level:
# 90%
# 95%
# 99%
#
# 95% is commonly used in many applications.
