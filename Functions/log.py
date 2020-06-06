# Goal: Calculate the natural logarithm
# Author: Steven Iacobellis

from power_function import power_function
from constants import get_ln10

# Precalculated ln(10)
ln10 = 0

#Goal: Calculate the natural logarithm, log base e, of a given input x
#Method: we use a series based on the area hyperbolic tangent function
def ln(args):

    x = 0

    # If the right number of arguments are passed, then continue
    if len(args) == 1:
        x = args[0]
    else:
        raise Exception(f"Invalid number of arguments, ln got {len(args)} but expected 1.")

    a = x
    b = 0

    # we will rewrite ln(x) where x = a * 10^b, with a < 1
    # we can then take the ln(x) = ln(a) + b * ln(10)
    while a > 1:
        a /= 10
        b += 1

    # Variable used to store the calculated sum
    s = 0

    # Number of iterations currently hardcoded at 100, but we can change this to an accuracy based metric by
    # calculating the accuracy of e^s = x to a certain bound.
    for i in range(100):
        s += (1 / (2 * i + 1)) * power_function([(a-1) / (a+1), 2 * i + 1])

    return (2 * s) + b * get_ln10()
