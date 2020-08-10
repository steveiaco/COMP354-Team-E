# Goal: Calculate the natural logarithm
# Author: Steven Iacobellis

from Functions.power_function import power_function
from Functions.constants import get_ln10

# Precalculated ln(10)
ln10 = 0


# Goal: Calculate the natural logarithm, log base e, of a given input x
# Method: we use a series based on the area hyperbolic tangent function
def ln(args):
    # If one argument is passed, then we can call ln
    if len(args) == 1:
        return ln_helper(args)
    else:
        raise Exception(f"Invalid number of arguments, ln got {len(args)} "
                        f"but expected 1.")


# Goal: Calculate the logarithm, log base 10, of a given input x. The
# base can be changed by specifying a second parameter
# Method: we use a series based on the area hyperbolic tangent function
def log(args):
    # If only one argument is passed, then we assume base 10
    if len(args) == 1:
        args.append(10.0)
        return ln_helper(args)
    # If two arguments are passed, then an operand and a base is defined
    elif len(args) == 2:
        return ln_helper(args)
    else:
        raise Exception(f"Invalid number of arguments, log got {len(args)} "
                        f"but expected 1 or 2.")


def ln_helper(args):
    x = 0
    base = 0
    use_base = False

    # If one argument is passed, then only an operand is passed, and
    # we assume a base of e.
    if len(args) == 1:
        x = args[0]
    # If two arguments are passed, then an operand and a base is
    # defined.
    elif len(args) == 2:
        x = args[0]
        base = args[1]
        use_base = True
        if base <= 0 or base == 1:
            raise Exception(f"Base of the logarithm must be b > 0 and b != 1, "
                            f"got {base}.")
    else:
        raise Exception(f"Invalid number of arguments, ln got {len(args)} but "
                        f"expected 1 or 2.")

    if x <= 0:
        raise Exception(f"Operand of the logarithm must be x > 0, got {x}.")

    # Use change of base calculation if the user specifies a base
    if use_base:
        return natural_log(x) / natural_log(base)
    # Otherwise default to the ln
    else:
        return natural_log(x)


# Calculates the natural logarithm ln
def natural_log(x):
    a = x
    b = 0

    # we will rewrite ln(x) where x = a * 10^b, with a < 1
    # we can then take the ln(x) = ln(a) + b * ln(10)
    while a > 1:
        a /= 10
        b += 1

    # Variable used to store the calculated sum
    s = 0

    # Number of iterations currently hardcoded at 100, but we can change
    # this to an accuracy based metric by calculating the accuracy of
    # e^s = x to a certain bound.
    for i in range(100):
        s += (1 / (2 * i + 1)) * power_function([(a - 1) / (a + 1), 2 * i + 1])

    return (2 * s) + b * get_ln10()
