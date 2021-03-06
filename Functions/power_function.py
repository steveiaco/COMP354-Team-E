# Goal: Calculate the specified power of a specified base
# Handling: Does not compute complex numbers
# Instructions: Enter "0" as the third argument of the power function to
# obtain a fractional result
# Author: Amina

from Functions.auxiliary_functions import floor_function
from Functions.auxiliary_functions import sqrt_function
from Functions.auxiliary_functions import absolute_value
from Functions.auxiliary_functions import decimal_to_fraction


def power_function(args):
    base = 0
    power = 0

    # If two arguments are passed, the result will be an integer or a
    # decimal
    if (len(args) == 2):
        base = args[0]
        power = args[1]
        conversion = "decimal"
    # If three arguments are passed, where the third argument is a 0,
    # the result will be an integer or a fraction
    elif (len(args) == 3):
        if (args[2] == 0):
            base = args[0]
            power = args[1]
            conversion = "fraction"
        else:
            raise Exception(f"Invalid third argument, power_function got "
                            f"{str(args[2])} but expected 0.")
    else:
        raise Exception(f"Invalid number of arguments, power_function got "
                        f"{len(args)} but expected 2 or 3.")

    # Case 1: Power is equal to 0
    if (power == 0):
        return 1

    # Case 2: Power is equal to 1
    elif (power == 1):
        return base

    # Case 3: Power is an integer neither equal to 0 nor to 1
    elif (floor_function(power) == power):
        # Fractional result
        if (conversion == "fraction"):
            initial_result = power_integer(base, power)
            if (initial_result != floor_function(initial_result)):
                final_result = decimal_to_fraction(initial_result)
                return str(final_result[0]) + "/" + str(final_result[1])
            else:
                return initial_result
        # Decimal result
        else:
            return power_integer(base, power)

    # Case 4: Power is a decimal
    else:
        # Fractional result
        if (conversion == "fraction"):
            initial_result = power_fractional(base, power)
            final_result = decimal_to_fraction(initial_result)
            return str(final_result[0]) + "/" + str(final_result[1])
        # Decimal result
        else:
            return power_fractional(base, power)


def power_integer(base, power):
    # Case 1: Power is a negative integer
    if (power < 0):
        base = 1 / base
        power *= -1

    # Case 2: Power is a positive integer greater than 1
    result = 1
    while (power > 1):
        if (power % 2 == 0):
            base = (base * base)
            power = power / 2
        else:
            result = base * result
            base = base * base
            power = (power - 1) / 2

    return base * result


def power_fractional(base, power):
    # Case 1: Power is greater or equal to 0 and base is equal to 0
    if (power > 0 and base == 0):
        return 0
    # Case 2: Power is between 0 and 1 exclusively
    elif (power > 0 and power < 1):
        integer_result = 1
        decimal_value = power
    # Case 3: Power is between -1 and 0 exclusively
    elif (power > -1 and power < 0):
        try:
            return 1 / power_fractional(base, absolute_value(power))
        except Exception:
            if (base == 0):
                print("ERROR")
            return -0.0
    # Case 4: Power is less than -1 or greater than 1
    else:
        integer_value = floor_function(power)
        integer_result = power_integer(base, integer_value)
        decimal_value = power - integer_value

    fraction = decimal_to_fraction(power)
    # Suppose we have a^(b/c), where "a" is negative...
    if (base < 0):
        # Case 1: "b" is even -> the result is a real number
        # Case 2: "b" is odd and "c" is odd -> the result is a real
        # number
        if (fraction[0] % 2 == 0 or fraction[1] % 2 != 0):
            return -1 * power_fractional(base * -1, power)
        # Case 3: "b" is odd and "c" is even -> the result is a complex
        # number
        else:
            print("ERROR")
            return -0.0

    precision = 0.0000000000001
    low = 0.0
    high = 1.0

    try:
        root = sqrt_function(base)
        decimal_result = root
        mid = high / 2

        # Uses binary search to find the closest value to the equation's
        # result by continuously applying the square root
        while (absolute_value(mid - decimal_value) > precision):
            root = sqrt_function(root)

            if (mid <= decimal_value):
                low = mid
                decimal_result *= root
            else:
                high = mid
                decimal_result *= (1 / root)

            mid = (low + high) / 2
    except Exception:
        print("ERROR")
        return -0.0

    return decimal_result * integer_result
