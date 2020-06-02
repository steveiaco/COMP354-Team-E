# Done - Exponential: cosh(x) = (e^x + e^(-x))/2
# Taylor: cosh(x) = 1 + (x^2/2!) + (x^4/4!) + (x^6/6!) ...

from Power_Function import power_function


def cosh(args):
    e = 2.718281828459045 # replace from constant file once created
    x = 0
    if(len(args) == 1):
        x = args[0]
    else:
        raise Exception(f"Invalid number of arguments, power_function got {len(args)} but expected 1.")
    return (power_function([e, x]) + power_function([e, -x])) / 2
