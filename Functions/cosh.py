# Goal: Calculate the hyperbolic cosine of a given variable x
# Author: Wayne

from Functions.power_function import power_function
from Functions.constants import get_e
from Functions.auxiliary_functions import to_radians


# Goal: calculate cosh(x)
# Method: exponential, cosh(x) = (e^x + e^(-x))/2
# Instructions (example input = 5):
# Enter: "cosh(5)" default considers input as radians
# Enter: "cosh(5) radians" considers input as radians
# Enter: "cosh(5) degrees" considers input as degrees
def cosh(args):
    x = 0
    e = get_e()

    if len(args) == 1 or (len(args) == 2 and args[1] == 0):
        x = args[0]
        return (power_function([e, x]) + power_function([e, -x])) / 2
    elif len(args) == 2 and args[1] == 1:
        x = to_radians(args[0])
        return (power_function([e, x]) + power_function([e, -x])) / 2
    else:
        raise Exception("Invalid input: cosh takes 1 input which is the "
                        "number in radians, or 2 inputs which is the number "
                        "and whether the number is in \" radians\" or \" "
                        "degrees\".")
