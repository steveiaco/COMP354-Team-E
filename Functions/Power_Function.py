#Goal: Calculate the specified power of a specified base
#Handling: Does not compute complex numbers 

def power_function (args):
    base = 0
    power = 0

    #If the right number of arguments are passed, then continue
    if(len(args) == 2):
        base = args[0]
        power = args[1]
    else:
        raise Exception(f"Invalid number of arguments, power_function got {len(args)} but expected 2.")
  
    #Case 1: Power is equal to 0
    if (power == 0):
        return 1
        
    #Case 2: Power is equal to 1
    elif (power == 1):
        return base
        
    #Case 3: Power is an integer neither equal to 0 nor to 1
    elif (floor_function(power) == power):
        return power_integer(base, power)
    
    #Case 4: Power is a decimal
    else:
        return rounding_function(power_fractional(base, power))

def power_integer(base, power):
    #Case 1: Power is a negative integer
    if (power < 0):
        base = 1 / base
        power *= -1
    
    #Case 2: Power is a positive integer greater than 1
    result = 1
    while(power > 1):
        if(power % 2 == 0):
            base = (base * base)
            power = power/2
        else: 
            result = base * result
            base = base * base
            power = (power - 1) / 2
    
    return base * result
    
def power_fractional (base, power):
    #Case 1: Power is greater or equal to 0 and base is equal to 0
    if(power > 0 and base == 0):
        return 0
    #Case 2: Power is between 0 and 1 exclusively 
    elif (power > 0 and power < 1):
        integer_result = 1
        decimal_value = power
    #Case 3: Power is between -1 and 0 exclusively 
    elif (power > -1 and power < 0):
        try:
            return 1 / power_fractional(base, absolute_value(power))
        except Exception:
            if (base == 0):
                print("ERROR")
            return -0.0
    #Case 4: Power is less than -1 or greater than 1
    else: 
        integer_value = floor_function(power)
        integer_result = power_integer(base, integer_value)
        decimal_value = power - integer_value

    fraction = decimal_to_fraction(power)
    #Suppose we have a^(b/c), where "a" is negative...
    if (base < 0):
        #Case 1: "b" is even -> the result is a complex real number
        #Case 2: "b" is odd and "c" is odd -> the result is a real number
        if (fraction[0] % 2 == 0 or fraction[1] % 2 != 0):
            return -1 * power_fractional(base * -1, power)
        #Case 3: "b" is odd and "c" is even -> the result is a complex number
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
    
        #Uses binary search to find the closest value to the equation's result by continuously applying the square root
        while(absolute_value(mid - decimal_value) > precision):
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

def floor_function(power):
    power *= 1.0
    number = str(power)

    #Case 1: Power is a non-integer negative number
    if (number[0] == "-" and power != int(power)):
        number = int(power) - 1 
    #Case 2: Power is positive rational number
    else: 
        number = int(power)
    
    return number

def sqrt_function(base):
    precision = 0.0000000000001
    previous, mid = 0, float(base)

    #Uses binary search to find the closest approximation of the square root
    while absolute_value(mid - previous) > precision:
        previous, mid = mid, (mid + (base / mid)) / 2.0
    
    return mid

def rounding_function(number):
    #Rounds the result to 11 digits after the decimals
    precision = 0.00000000001
    result = str(number)
    first_half = result[ : result.find(".")]
    second_half = result[result.find(".") : ]

    if (len(second_half) < 13):
        return number

    precision_factor = second_half[1 : 13]
    second_half = second_half[ : 12]

    if (int(precision_factor[11]) < 5):
        full = float(first_half + second_half)
    else:
        value = float(second_half) + precision
        if (value == 1):
            full = floor_function(number)
        else:
            full = float(first_half) + (float(second_half) + precision)

    return full

def absolute_value(number):
    if (number < 0):
        number *= -1

    return number

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

    #Uses binary search to find the closest fraction to the decimal
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