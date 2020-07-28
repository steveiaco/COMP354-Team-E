#Goal: Calculate the sine of a variable x
# Author: Yongsu

from Functions.power_function import power_function
from Functions.constants import get_pi
from Functions.auxiliary_functions import factorial
"""
    Names of functions are "sine" and "factorial"
    Each only takes 1 input which is the number
"""

def sine(args):
    if len(args) == 1:
        num = args[0]
    else:
        raise Exception("Invalid number of input, sine take 1 input which is the number")
    res = 0
    pi = get_pi()
    twopi = 2 * pi

    # program will crush if num too big, convert to interval 0 -> 2pi
    num = num % twopi

    # using for loop to create summation i=0 to i=79
    for i in range(80):
        res += (power_function([-1, i])) * (power_function([num, (2*i+1)])) / (factorial(2*i+1))
    return res




