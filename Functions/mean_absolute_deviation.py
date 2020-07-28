# Algorithm
# 1. Calculate Mean
# 2. Sum the absolute values of all values minus the mean
# 3. Divide the sum by the number of values

# Author: Sean

from Functions.auxiliary_functions import absolute_value
from Functions.auxiliary_functions import calculate_mean


# Primary Algoirthm
def mean_absolute_deviation(args):
    
    # Local variables
    mean = calculate_mean(args)
    dividend = 0
    diviser = len(args)

    # Calculate the dividend
    for x in args:
        dividend += absolute_value(x - mean)

    # Return the Mean Absolute Deviation
    return (float(dividend) / diviser)
