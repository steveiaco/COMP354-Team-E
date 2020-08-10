# Goal: Calculate the sine of a variable x
# Author: Yongsu

from Functions.power_function import power_function
from Functions.constants import get_pi
from Functions.auxiliary_functions import factorial
from Functions.auxiliary_functions import to_radians


# Instructions (example input = 5):
# Enter: "sin(5)" default considers input as radians
# Enter: "sin(5) radians" considers input as radians
# Enter: "sin(5) degrees" considers input as degrees
def sine(args):
    if len(args) == 1 or (len(args) == 2 and args[1] == 0):
        num = args[0]
    elif len(args) == 2 and args[1] == 1:
        num = to_radians(args[0])
    else:
        raise Exception("Invalid input: sine takes 1 input which is the "
                        "number in degrees, or 2 inputs which is the number "
                        "and whether the number is in \" radians\" or \" "
                        "degrees\".")
    res = 0
    pi = get_pi()
    twopi = 2 * pi

    # program will crush if num too big, convert to interval 0 -> 2pi
    num = num % twopi

    # using for loop to create summation i=0 to i=79
    for i in range(80):
        res += (power_function([-1, i])) \
               * (power_function([num, (2 * i + 1)])) \
               / (factorial(2 * i + 1))
    return res
