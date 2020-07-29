# Goal: Calculate pi to the power of a given variable x
# Author: Ali

from Functions.constants import get_pi

# Pie Function
# Using Table Method
# I have basically created a global variable for PIE and its power
PIE = get_pi()

# the index (n) of the dictionary represent  PIE**(10**n)
PIE_Dictionary = {-5: 1.000011447364379, -4: 1.0001144795408674, -3: 1.001145385339187, -2: 1.0115130699114478,
                  -1: 1.1212823532318632, 0: 1, 1: PIE, 2: 93648.04747608298, 3: 5.187848314319592e+49}


def pi_function(args):

    x = 0
    # check if
    if len(args) == 1:
        x = args[0]
    else:
        raise Exception(f"Invalid number of arguments, pie expected 1 argument but got {len(args)} arguments.")

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
