# Done - Exponential: cosh(x) = (e^x + e^(-x))/2
# Taylor: cosh(x) = 1 + (x^2/2!) + (x^4/4!) + (x^6/6!) ...

from Power_Function import power_function
from Constants import get_e()


def cosh(number):
    x = number
    e = get_e()

    return (power_function([e, x]) + power_function([e, -x])) / 2
