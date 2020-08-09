from Functions.constants import get_pi


# Calculates the floor of a decimal
def floor_function(power):
    power *= 1.0
    number = str(power)

    # Case 1: Power is a non-integer negative number
    if (number[0] == "-" and power != int(power)):
        number = int(power) - 1
        # Case 2: Power is positive rational number
    else:
        number = int(power)

    return number


# Calculates the square root of a number
def sqrt_function(base):
    precision = 0.0000000000001
    previous, mid = 0, float(base)

    # Uses binary search to find the closest approximation of the square root
    while absolute_value(mid - previous) > precision:
        previous, mid = mid, (mid + (base / mid)) / 2.0

    return mid


# Calculates the absolute value
def absolute_value(number):
    if (number < 0):
        number *= -1

    return number


# Converts a decimal to a fraction using binary search
def decimal_to_fraction(decimal):
    precision = 0.0000000000001
    number = int(floor_function(decimal))
    decimal -= number
    if (decimal < precision):
        return (number, 1)
    elif (1 - precision < decimal):
        return (number + 1, 1)

    low_numerator = 0
    low_denominator = 1
    high_numerator = 1
    high_denominator = 1

    # Uses binary search to find the closest fraction to the decimal
    while True:
        middle_numerator = low_numerator + high_numerator
        middle_denominator = low_denominator + high_denominator

        if middle_denominator * (decimal + precision) < middle_numerator:
            high_numerator = middle_numerator
            high_denominator = middle_denominator
        elif middle_numerator < (decimal - precision) * middle_denominator:
            low_numerator = middle_numerator
            low_denominator = middle_denominator
        else:
            return (number * middle_denominator + middle_numerator, middle_denominator)


# Calculates the factorial using recursion
def factorial(number):
    # factorial by recursion
    if number < 0:
        print("factorial is undefined for negative numbers!")
        return None
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# Calculates the mean of an input
def calculate_mean(input):
    sum = 0
    for x in input:
        sum += x
    return (sum / len(input))


# Tallies up all values of elements in a list
def total_count(args):
    s = 0
    for i in range(len(args)):
        s = s + args[i]
    return s


# Converts degree to radians
def to_radians(degrees):
    return degrees * (get_pi() / 180)


# Converts radians to degrees
def to_degrees(radians):
    return radians * (180 / get_pi())
