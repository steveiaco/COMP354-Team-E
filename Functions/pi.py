# Goal: Calculate pi to the power of a given variable x
# Author: Ali

from constants import get_pi
from power_function import power_function
# Pie Function
# Using Table Method
# I have basically created a global variable for PIE and its power
PIE = get_pi()

# the index (n) of the dictionary represent  PIE**(10**n)
PIE_Dictionary = {-5: power_function([PIE, 0.00001]), -4: power_function([PIE, 0.0001]), -3: power_function([PIE, 0.001]), -2: power_function([PIE, 0.01]),
                  -1: power_function([PIE, 0.1]), 0: 1, 1: PIE, 2: power_function([PIE, 10]), 3: power_function([PIE,100])}


def pi_function(args):

    x = 0
    # check if
    if len(args) == 1:
        x = args[0]
    else:
        raise Exception(f"Invalid number of arguments, pie got expected 1 arguments but got {len(args)} arguments.")

    negative_exponent = False
    if float(x) < 0:
        negative_exponent = True
        x = float(x)*-1

    exponent = list(str(float(x))) 
    decimal = list(str(float(x))).index('.')
    n = 1.0

    for i in range(len(exponent)):
        power_level = decimal-int(i)  # power_level give us the index of PIE_Dictionary

        if power_level != 0:
            j = int(exponent[i])

            for k in range(j):
                n = n*PIE_Dictionary[power_level]

    if negative_exponent:
        return 1/n

    return n
