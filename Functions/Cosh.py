from Power_Function import power_function
from Constants import get_e()

# Goal: calculate cosh(x)
# Method: exponential, cosh(x) = (e^x + e^(-x))/2
def cosh(args):
    x = 0
    e = get_e()

    # if the correct number of arguments are passed, then continue
    if len(args) == 1:
        x == args[0]
    else:
        raise Exception(f"Invalid number of arguments, power_function got {len(args)} but expected 1.")

    return (power_function([e, x]) + power_function([e, -x])) / 2
