#import math
import Power_Function as Pwr
from Constants import get_pi
"""
    Names of functions are "sine" and "factorial"
    Each only takes 1 input which is the number
"""


def factorial(number):
    # factorial by recursion
    if number < 0:
        print("factorial is undefined for negative numbers!")
        return None
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)


def sine(num):
    res = 0
    pi = get_pi()
    twopi = 2 * pi

    # program will crush if num too big, convert to interval 0 -> 2pi
    num = num % twopi
    # using for loop to create summation i=0 to i=39
    for i in range(80):
        res += (Pwr.power_function([-1, i])) * (Pwr.power_function([num, (2*i+1)])) / (factorial(2*i+1))
    return res


#x = -10

#print(math.sin(x))
#print(sine(x))
#print(Pwr.power_function([2, 2]))

