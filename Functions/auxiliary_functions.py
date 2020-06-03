
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

# Rounds a number to 11 digits (We should revise whether we need this function)
def rounding_function(number):
    # Rounds the result to 11 digits after the decimals
    precision = 0.00000000001
    result = str(number)
    first_half = result[: result.find(".")]
    second_half = result[result.find("."):]

    if (len(second_half) < 13):
        return number

    precision_factor = second_half[1: 13]
    second_half = second_half[: 12]

    if (int(precision_factor[11]) < 5):
        full = float(first_half + second_half)
    else:
        value = float(second_half) + precision
        if (value == 1):
            full = floor_function(number)
        else:
            full = float(first_half) + (float(second_half) + precision)

    return full

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
        return number*factorial(number-1)

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